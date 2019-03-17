import idautils
import idaapi
import idc
import json
from terminaltables import SingleTable

import utils
from guids import edk_guids, ami_guids, edk2_guids

OFFSET = {
    "InstallProtocolInterface": 0x80,
    "ReinstallProtocolInterface": 0x88,
    "UninstallProtocolInterface": 0x90,
    "HandleProtocol": 0x98,
    "RegisterProtocolNotify": 0xA8,
    "OpenProtocol": 0x118,
    "CloseProtocol": 0x120,
    "OpenProtocolInformation": 0x128,
    "ProtocolsPerHandle": 0x130,
    "LocateHandleBuffer": 0x138,
    "LocateProtocol": 0x140,
    "InstallMultipleProtocolInterfaces": 0x148,
    "UninstallMultipleProtocolInterfaces": 0x150,
}

LEA_NUM = {
    "InstallProtocolInterface": 2,
    "ReinstallProtocolInterface": 1,
    "UninstallProtocolInterface": 1,
    "HandleProtocol": 1,
    "RegisterProtocolNotify": 1,
    "OpenProtocol": 1,
    "CloseProtocol": 1,
    "OpenProtocolInformation": 1,
    "LocateHandleBuffer": 2,
    "LocateProtocol": 1,
#   "InstallMultipleProtocolInterfaces": 2,
#   "UninstallMultipleProtocolInterfaces": x,
}

class Analyser(object):
    def __init__(self):
        idc.Til2Idb(-1, "EFI_GUID")
        idc.Til2Idb(-1, "EFI_SYSTEM_TABLE")
        idc.Til2Idb(-1, "EFI_RUNTIME_SERVICES")
        idc.Til2Idb(-1, "EFI_BOOT_SERVICES")

        self.gBServices = {}
        self.gBServices["InstallProtocolInterface"] = []
        self.gBServices["ReinstallProtocolInterface"] = []
        self.gBServices["UninstallProtocolInterface"] = []
        self.gBServices["HandleProtocol"] = []
        self.gBServices["RegisterProtocolNotify"] = []
        self.gBServices["OpenProtocol"] = []
        self.gBServices["CloseProtocol"] = []
        self.gBServices["OpenProtocolInformation"] = []
        self.gBServices["ProtocolsPerHandle"] = []
        self.gBServices["LocateHandleBuffer"] = []
        self.gBServices["LocateProtocol"] = []
        self.gBServices["InstallMultipleProtocolInterfaces"] = []
        self.gBServices["UninstallMultipleProtocolInterfaces"] = []

        self.Protocols = {}
        self.Protocols["AmiGuids"] = ami_guids.ami_guids
        self.Protocols["EdkGuids"] = edk_guids.edk_guids
        self.Protocols["Edk2Guids"] = edk2_guids.edk2_guids
        self.Protocols["All"] = [
            # {
            #   address: ...
            #   service: ...
            #   guid: ...
            # }, 
            # ...
        ]
        self.Protocols["PropGuids"] = []

    @staticmethod
    def help():
        print("Methods:")
        print(" * analyser.get_boot_services()")
        print("   - check: analyser.gBServices[<service_name>]")
        print(" * analyser.get_protocols()")
        print("   - check: analyser.Protocols['All']")
        print(" * analyser.get_prot_names()")
        print("   - check: analyser.Protocols['All']")
        print("Commands:")
        print(" * analyser.list_boot_services()")
        print(" * analyser.list_protocols()")
        print(" * analyser.make_comments()")
        print(" * analyser.make_names()")
        print(" * analyser.set_types()")
        print(" * analyser.print_all()")

    def get_boot_services(self):
        for ea_start in idautils.Functions():
            for ea in idautils.FuncItems(ea_start):
                for service_name in OFFSET:
                    if (idc.GetMnem(ea) == "call" and \
                        idc.get_operand_value(ea, 0) == OFFSET[service_name]
                        ):
                        if self.gBServices[service_name].count(ea) == 0:
                            self.gBServices[service_name].append(ea)

    def list_boot_services(self):
        self.get_boot_services()
        empty = True
        table_data = []
        table_instance = SingleTable(table_data)
        table_data.append(["Address", "Service"])
        print("Boot services:")
        for service in self.gBServices:
            for address in self.gBServices[service]:
                table_data.append([hex(address), service])
                empty = False
        if empty:
            print(" * list is empty")
        else:
            print(table_instance.table)
    
    def list_protocols(self):
        self.get_boot_services()
        self.get_protocols()
        self.get_prot_names()
        data = self.Protocols["All"]
        print("Protocols:")
        if len(data) == 0:
            print(" * list is empty")
        else:
            table_data = []
            table_instance = SingleTable(table_data)
            table_data.append(["GUID", "Protocol name", "Address", "Service", "Protocol place"])
            for element in data:
                table_data.append([
                    str(map(hex, element["guid"])), 
                    element["protocol_name"],
                    hex(element["address"]),
                    element["service"],
                    element["protocol_place"]
                    ])
            print(table_instance.table)

    def get_protocols(self):
        for service_name in self.gBServices:
            if service_name in LEA_NUM.keys():
                for address in self.gBServices[service_name]:
                    ea = address
                    lea_counter = 0
                    while (True):
                        ea = idc.prev_head(ea)
                        if (idc.GetMnem(ea) == "lea"):
                            lea_counter += 1
                            if (lea_counter == LEA_NUM[service_name]):
                                break
                    for xref in idautils.DataRefsFrom(ea):
                        if (idc.GetMnem(xref) == ""):
                            CurrentGUID = utils.get_guid(xref)
                            protocol_record = {}
                            protocol_record["address"] = xref
                            protocol_record["service"] = service_name
                            protocol_record["guid"] = CurrentGUID
                            if self.Protocols["All"].count(protocol_record) == 0:
                                self.Protocols["All"].append(protocol_record)

    def get_prot_names(self):
        for index in range(len(self.Protocols["All"])):
            fin = False
            for prot_name in self.Protocols["Edk2Guids"].keys():
                guid_idb = self.Protocols["All"][index]["guid"]
                guid_conf = self.Protocols["Edk2Guids"][prot_name]
                if (guid_idb == guid_conf):
                    self.Protocols["All"][index]["protocol_name"] = prot_name
                    self.Protocols["All"][index]["protocol_place"] = "edk2_guids"
                    fin = True
                    break
            if fin: continue
            for prot_name in self.Protocols["EdkGuids"].keys():
                guid_idb = self.Protocols["All"][index]["guid"]
                guid_conf = self.Protocols["EdkGuids"][prot_name]
                if (guid_idb == guid_conf):
                    self.Protocols["All"][index]["protocol_name"] = prot_name
                    self.Protocols["All"][index]["protocol_place"] = "edk_guids"
                    fin = True
                    break
            if fin: continue
            for prot_name in self.Protocols["Edk2Guids"].keys():
                guid_idb = self.Protocols["All"][index]["guid"]
                guid_conf = self.Protocols["Edk2Guids"][prot_name]
                if (guid_idb == guid_conf):
                    self.Protocols["All"][index]["protocol_name"] = prot_name
                    self.Protocols["All"][index]["protocol_place"] = "ami_guids"
                    fin = True
                    break
            if fin: continue
            if not "protocol_name" in self.Protocols["All"][index]:
                self.Protocols["All"][index]["protocol_name"] = "ProprietaryProtocol"
                self.Protocols["All"][index]["protocol_place"] = "unknown"

    def make_comments(self):
        self.get_boot_services()
        for service in self.gBServices:
            for address in self.gBServices[service]:
                """ utils.set_hexrays_comment(address, "EFI_BOOT_SERVICES->{0}".format(service)) """
                message = "EFI_BOOT_SERVICES->{0}".format(service)
                idc.MakeComm(address, message)
                print("[{ea}] {message}".format(ea=hex(address), message=message))
    
    def make_names(self):
        EFI_GUID = "EFI_GUID *"
        self.get_boot_services()
        self.get_protocols()
        self.get_prot_names()
        data = self.Protocols["All"]
        for element in data:
            try:
                idc.SetType(element["address"], EFI_GUID)
                idc.MakeName(element["address"], element["protocol_name"])
                print("[{ea}] {name}".format(ea=hex(element["address"]), name=element["protocol_name"]))
            except:
                continue

    def set_types(self):
        """ handle (EFI_BOOT_SERVICES *) type """
        RAX = 0
        O_REG = 1
        O_MEM = 2
        EFI_BOOT_SERVICES = "EFI_BOOT_SERVICES *"
        for service in self.gBServices:
            for address in self.gBServices[service]:
                ea = address
                num_of_attempts = 10
                for _ in range(num_of_attempts):
                    ea = idc.prev_head(ea)
                    if (idc.GetMnem(ea) == "mov" and idc.get_operand_type(ea, 1) == O_MEM):
                        if (idc.get_operand_type(ea, 0) == O_REG and idc.get_operand_value(ea, 0) == RAX):
                            gBs_var = idc.get_operand_value(ea, 1)
                            gBs_var_type = idc.get_type(gBs_var)
                            if (gBs_var_type == "EFI_BOOT_SERVICES *"):
                                print("[{0}] EFI_BOOT_SERVICES->{1}".format(hex(address).replace("L", ""), service))
                                print("\t [address] {0}".format(hex(gBs_var).replace("L", "")))
                                print("\t [message] type already applied")
                                break
                            if idc.SetType(gBs_var, EFI_BOOT_SERVICES):
                                old_name = idc.Name(gBs_var)
                                idc.MakeName(gBs_var, "gBs_" + old_name)
                                print("[{0}] EFI_BOOT_SERVICES->{1}".format(hex(address).replace("L", ""), service))
                                print("\t [address] {0}".format(hex(gBs_var).replace("L", "")))
                                print("\t [message] type successfully applied")
                            else:
                                print("[{0}] EFI_BOOT_SERVICES->{1}".format(hex(address).replace("L", ""), service))
                                print("\t [address] {0}".format(hex(gBs_var).replace("L", "")))
                                print("\t [message] type not applied")
                            break

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

def main():
    print("Usage:")
    print("analyser = Analyser()")
    print("analyser.help()")
    analyser = Analyser()
    analyser.print_all()
    analyser.analyse_all()

if __name__=="__main__":
    main()