# SPDX-License-Identifier: MIT

import ida_bytes
import ida_name
import idaapi
import idautils
import idc

from .guids import (
    ami_guids,
    asrock_guids,
    dell_guids,
    edk2_guids,
    edk_guids,
    lenovo_guids,
)
from .tables import BOOT_SERVICES_OFFSET_x64, BOOT_SERVICES_OFFSET_x86
from .utils import (
    Table,
    check_guid,
    check_subsystem,
    get_guid,
    get_guid_str,
    get_header_file,
    get_header_idb,
    get_machine_type,
)


class Analyser:
    def __init__(self):
        header = get_header_idb()
        if not header:
            header = get_header_file()
        self.arch = get_machine_type(header)
        self.subsystem = check_subsystem(header)
        self.valid = True
        if not self.subsystem:
            print("[ERROR] Wrong subsystem")
            self.valid = False
        if not (self.arch == "x86" or self.arch == "x64"):
            print("[ERROR] Wrong architecture")
            self.valid = False
        if self.arch == "x86":
            self.BOOT_SERVICES_OFFSET = BOOT_SERVICES_OFFSET_x86
        if self.arch == "x64":
            self.BOOT_SERVICES_OFFSET = BOOT_SERVICES_OFFSET_x64
        self.base = idaapi.get_imagebase()
        idc.import_type(-1, "EFI_GUID")
        idc.import_type(-1, "EFI_SYSTEM_TABLE")
        idc.import_type(-1, "EFI_RUNTIME_SERVICES")
        idc.import_type(-1, "EFI_BOOT_SERVICES")

        self.gBServices = dict()
        self.gBServices["InstallProtocolInterface"] = list()
        self.gBServices["ReinstallProtocolInterface"] = list()
        self.gBServices["UninstallProtocolInterface"] = list()
        self.gBServices["HandleProtocol"] = list()
        self.gBServices["RegisterProtocolNotify"] = list()
        self.gBServices["OpenProtocol"] = list()
        self.gBServices["CloseProtocol"] = list()
        self.gBServices["OpenProtocolInformation"] = list()
        self.gBServices["ProtocolsPerHandle"] = list()
        self.gBServices["LocateHandleBuffer"] = list()
        self.gBServices["LocateProtocol"] = list()
        self.gBServices["InstallMultipleProtocolInterfaces"] = list()
        self.gBServices["UninstallMultipleProtocolInterfaces"] = list()

        self.Protocols = dict()
        self.Protocols["ami_guids"] = ami_guids.ami_guids
        self.Protocols["asrock_guids"] = asrock_guids.asrock_guids
        self.Protocols["dell_guids"] = dell_guids.dell_guids
        self.Protocols["edk_guids"] = edk_guids.edk_guids
        self.Protocols["edk2_guids"] = edk2_guids.edk2_guids
        self.Protocols["lenovo_guids"] = lenovo_guids.lenovo_guids
        self.Protocols["all"] = list()
        self.Protocols["prop_guids"] = list()
        self.Protocols["data"] = list()

    def _find_est(self, gvar, start, end):
        REG_RAX = 0
        BS_OFFSET = 0x60
        EFI_SYSTEM_TABLE = "EFI_SYSTEM_TABLE *"
        if self.arch == "x86":
            BS_OFFSET = 0x3C
        ea = start
        while ea < end:
            if (
                (idc.print_insn_mnem(ea) == "mov")
                and (idc.get_operand_value(ea, 0) == REG_RAX)
                and (idc.get_operand_value(ea, 1) == BS_OFFSET)
            ):
                if idc.SetType(gvar, EFI_SYSTEM_TABLE):
                    idc.set_name(gvar, f"gST_{gvar:X}")
                    return True
            ea = idc.next_head(ea)
        return False

    def get_boot_services(self):
        """found boot services in idb"""
        code = list(idautils.Functions())[0]
        start = idc.get_segm_start(code)
        end = idc.get_segm_end(code)
        ea = start
        while ea <= end:
            if idc.print_insn_mnem(ea) != "call":
                ea = idc.next_head(ea)
                continue
            for service_name in self.BOOT_SERVICES_OFFSET:
                if (
                    idc.get_operand_value(ea, 0)
                    == self.BOOT_SERVICES_OFFSET[service_name]
                ):
                    if not self.gBServices[service_name].count(ea):
                        self.gBServices[service_name].append(ea)
            ea = idc.next_head(ea)

    def get_protocols(self):
        """found UEFI protocols information in idb"""
        for service_name in self.gBServices:
            for address in self.gBServices[service_name]:
                ea, found = address, False
                if self.arch == "x86":
                    for _ in range(1, 25):
                        ea = idc.prev_head(ea)
                        if (
                            idc.get_operand_value(ea, 0) > self.base
                            and idc.print_insn_mnem(ea) == "push"
                        ):
                            found = True
                            break
                if self.arch == "x64":
                    for _ in range(1, 16):
                        ea = idc.prev_head(ea)
                        if (
                            idc.get_operand_value(ea, 1) > self.base
                            and idc.print_insn_mnem(ea) == "lea"
                        ):
                            found = True
                            break
                if not found:
                    continue
                for xref in idautils.DataRefsFrom(ea):
                    if idc.print_insn_mnem(xref):
                        continue
                    if not check_guid(xref):
                        continue
                    cur_guid = get_guid(xref)
                    record = {
                        "address": xref,
                        "service": service_name,
                        "guid": cur_guid,
                    }
                    if not self.Protocols["all"].count(record):
                        self.Protocols["all"].append(record)

    def get_prot_names(self):
        """
        match UEFI protocols GUIDs with known GUIDs
        if protocol GUID is not found in a lists of known GUIDs, the protocol is considered proprietary
        """
        for index in range(len(self.Protocols["all"])):
            fin = False
            for guid_place in [
                "ami_guids",
                "asrock_guids",
                "dell_guids",
                "edk_guids",
                "edk2_guids",
                "lenovo_guids",
            ]:
                for prot_name in self.Protocols[guid_place].keys():
                    guid_idb = self.Protocols["all"][index]["guid"]
                    guid_conf = self.Protocols[guid_place][prot_name]
                    if guid_idb == guid_conf:
                        self.Protocols["all"][index]["protocol_name"] = prot_name
                        self.Protocols["all"][index]["protocol_place"] = guid_place
                        fin = True
                        break
                if fin:
                    break
            if fin:
                continue
            if not "protocol_name" in self.Protocols["all"][index]:
                self.Protocols["all"][index]["protocol_name"] = "ProprietaryProtocol"
                self.Protocols["all"][index]["protocol_place"] = "unknown"

    def get_data_guids(self):
        """rename GUIDs in idb"""
        EFI_GUID = "EFI_GUID"
        EFI_GUID_ID = idc.get_struc_id("EFI_GUID")
        segments = [".text", ".data"]
        for segment in segments:
            seg_start, seg_end = 0, 0
            for seg in idautils.Segments():
                if idc.get_segm_name(seg) == segment:
                    seg_start = idc.get_segm_start(seg)
                    seg_end = idc.get_segm_end(seg)
                    break
            ea = seg_start
            while ea <= seg_end - 15:
                prot_name = str()
                if "unk" in idc.get_name(ea, ida_name.GN_VISIBLE):
                    find = False
                    cur_guid = list()
                    cur_guid.append(idc.get_wide_dword(ea))
                    cur_guid.append(idc.get_wide_word(ea + 4))
                    cur_guid.append(idc.get_wide_word(ea + 6))
                    for addr in range(ea + 8, ea + 16, 1):
                        cur_guid.append(idc.get_wide_byte(addr))
                    if cur_guid == [0] * 11:
                        ea += 1
                        continue
                    for guid_place in [
                        "ami_guids",
                        "asrock_guids",
                        "dell_guids",
                        "edk_guids",
                        "edk2_guids",
                        "lenovo_guids",
                    ]:
                        for name in self.Protocols[guid_place]:
                            if self.Protocols[guid_place][name] == cur_guid:
                                prot_name = f"{name}_{ea:016X}"
                                record = {
                                    "address": ea,
                                    "service": "unknown",
                                    "guid": cur_guid,
                                    "protocol_name": name,
                                    "protocol_place": guid_place,
                                }
                                find = True
                                break
                            if find:
                                break
                    if find and (idc.get_name(ea, ida_name.GN_VISIBLE) != prot_name):
                        idc.SetType(ea, EFI_GUID)
                        self.apply_struct(ea, 16, EFI_GUID_ID)
                        idc.set_name(ea, prot_name)
                        self.Protocols["data"].append(record)
                ea += 1

    def make_comments(self):
        """make comments in idb"""
        EFI_BOOT_SERVICES_ID = idc.get_struc_id("EFI_BOOT_SERVICES")
        self.get_boot_services()
        empty = True
        for service in self.gBServices:
            for address in self.gBServices[service]:
                message = f"EFI_BOOT_SERVICES->{service}"
                idc.set_cmt(address, message, 0)
                idc.op_stroff(address, 0, EFI_BOOT_SERVICES_ID, 0)
                empty = False
                print(f"[ {address:016X} ] {message}")
        if empty:
            print(" * list is empty")

    def make_names(self):
        """make names in idb"""
        EFI_GUID = "EFI_GUID"
        EFI_GUID_ID = idc.get_struc_id("EFI_GUID")
        self.get_boot_services()
        self.get_protocols()
        self.get_prot_names()
        data = self.Protocols["all"]
        empty = True
        for element in data:
            try:
                idc.SetType(element["address"], EFI_GUID)
                self.apply_struct(element["address"], 16, EFI_GUID_ID)
                prot_name = element["protocol_name"]
                addr = element["address"]
                name = f"{prot_name}_{addr:X}"
                idc.set_name(element["address"], name)
                empty = False
                print(f"[ {addr:016X} ] {name}")
            except:
                continue
        if empty:
            print(" * list is empty")

    def set_types(self):
        """
        handle (EFI_BOOT_SERVICES *) type
        and (EFI_SYSTEM_TABLE *) for x64 images
        """
        REG_RAX = 0
        EFI_BOOT_SERVICES = "EFI_BOOT_SERVICES *"
        EFI_SYSTEM_TABLE = "EFI_SYSTEM_TABLE *"
        empty = True
        for service in self.gBServices:
            for address in self.gBServices[service]:
                ea = address
                num_of_attempts = 10
                for _ in range(num_of_attempts):
                    ea = idc.prev_head(ea)
                    if (
                        idc.print_insn_mnem(ea) == "mov"
                        and idc.get_operand_type(ea, 1) == idc.o_mem
                    ):
                        if (
                            idc.get_operand_type(ea, 0) == idc.o_reg
                            and idc.get_operand_value(ea, 0) == REG_RAX
                        ):
                            gvar = idc.get_operand_value(ea, 1)
                            gvar_type = idc.get_type(gvar)
                            # if (EFI_SYSTEM_TABLE *)
                            if (gvar_type != "EFI_SYSTEM_TABLE *") and (
                                idc.print_operand(address, 0).find("rax") == 1
                            ):
                                if self._find_est(gvar, ea, address):
                                    print(
                                        f"[ {gvar:016X} ] Type ({EFI_SYSTEM_TABLE}) successfully applied"
                                    )
                                    empty = False
                                    break
                            # otherwise it (EFI_BOOT_SERVICES *)
                            if (
                                gvar_type != "EFI_BOOT_SERVICES *"
                                and gvar_type != "EFI_SYSTEM_TABLE *"
                            ):
                                if idc.SetType(gvar, EFI_BOOT_SERVICES):
                                    empty = False
                                    idc.set_name(gvar, f"gBS_{gvar:X}")
                                    print(
                                        f"[ {gvar:016X} ] Type ({EFI_BOOT_SERVICES}) successfully applied"
                                    )
                            break
        if empty:
            print(" * list is empty")

    def list_boot_services(self):
        """display boot services information"""
        self.get_boot_services()
        empty = True
        table_data = list()
        table_data.append(["Address", "Service"])
        print("Boot services:")
        for service in self.gBServices:
            for address in self.gBServices[service]:
                table_data.append([f"{address:016X}", service])
                empty = False
        if empty:
            print(" * list is empty")
        else:
            print(Table.display(table_data))

    def list_protocols(self):
        """display protocols information"""
        self.get_boot_services()
        self.get_protocols()
        self.get_prot_names()
        data = self.Protocols["all"] + self.Protocols["data"]
        print("Protocols:")
        if len(data) == 0:
            print(" * list is empty")
        else:
            table_data = list()
            table_data.append(
                ["GUID", "Protocol name", "Address", "Service", "Protocol place"]
            )
            for element in data:
                guid = get_guid_str(element["guid"])
                addr = element["address"]
                table_data.append(
                    [
                        guid,
                        element["protocol_name"],
                        f"{addr:016X}",
                        element["service"],
                        element["protocol_place"],
                    ]
                )
            print(Table.display(table_data))

    def print_all(self):
        self.list_boot_services()
        self.list_protocols()

    def analyse_all(self):
        print("Comments:")
        self.make_comments()
        print("Names:")
        self.make_names()
        print("Types:")
        self.set_types()
        self.get_data_guids()

    @staticmethod
    def apply_struct(ea, size, sid):
        ida_bytes.del_items(ea, size, idc.DELIT_DELNAMES)
        ida_bytes.create_struct(ea, size, sid)
        return size


def main():
    idc.auto_wait()
    analyser = Analyser()
    if analyser.valid:
        analyser.print_all()
        analyser.analyse_all()
    if not analyser.valid:
        analyser.arch = idaapi.askstr(
            0, "x86 / x64", "Set architecture manually (x86 or x64)"
        )
        if analyser.arch == "x86":
            analyser.BOOT_SERVICES_OFFSET = BOOT_SERVICES_OFFSET_x86
        elif analyser.arch == "x64":
            analyser.BOOT_SERVICES_OFFSET = BOOT_SERVICES_OFFSET_x64
        else:
            return False
        analyser.print_all()
        analyser.analyse_all()
        return True


if __name__ == "__main__":
    main()
