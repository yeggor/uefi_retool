# SPDX-License-Identifier: MIT

import binascii
import json
import os
import tempfile

import ida_nalt
import idaapi
import idc

from uefi_analyser.analyser import Analyser
from uefi_analyser.utils import get_guid_str


def get_boot_services(analyser):
    boot_services = list()
    for service in analyser.gBServices:
        for address in analyser.gBServices[service]:
            boot_services.append(
                {"address": f"{address:#x}", "bs_name": f"EFI_BOOT_SERVICES->{service}"}
            )
    return boot_services


def get_protocols(analyser):
    protocols = list()
    analyser.get_protocols()
    analyser.get_prot_names()
    data = analyser.Protocols["all"]
    for element in data:
        guid = get_guid_str(element["guid"])
        addr = element["address"]
        address = f"{addr:#x}"
        protocols.append(
            {
                "address": address,
                "service": element["service"],
                "protocol_name": element["protocol_name"],
                "protocol_place": element["protocol_place"],
                "guid": guid,
            }
        )
    return protocols


def log_all():
    data = dict()
    idc.auto_wait()
    analyser = Analyser()
    if not analyser.valid:
        idc.qexit(-1)
    analyser.get_boot_services()
    module = idaapi.get_root_filename()
    boot_services = get_boot_services(analyser)
    protocols = get_protocols(analyser)
    data["module_name"] = module
    data["boot_services"] = boot_services
    data["protocols"] = protocols
    logs_dir = os.path.join(tempfile.gettempdir(), "uefi-retool-all-info")
    if not os.path.isdir(logs_dir):
        os.mkdir(logs_dir)
    log_fname = f"{binascii.hexlify(ida_nalt.retrieve_input_file_md5()).decode()}.json"
    log_fpath = os.path.join(logs_dir, log_fname)
    with open(log_fpath, "w") as f:
        json.dump(data, f, indent=2)
    idc.qexit(0)


if __name__ == "__main__":
    log_all()
