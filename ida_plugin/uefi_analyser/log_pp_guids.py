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


def log_pp_guids():
    idc.auto_wait()
    analyser = Analyser()
    if not analyser.valid:
        idc.qexit(-1)
    analyser.get_boot_services()
    analyser.get_protocols()
    analyser.get_prot_names()
    data = dict()
    data["module_name"] = idaapi.get_root_filename()
    data["protocols"] = list()
    for protocol_record in analyser.Protocols["all"]:
        if protocol_record["protocol_name"] == "ProprietaryProtocol":
            guid = get_guid_str(protocol_record["guid"])
            service = protocol_record["service"]
            addr = protocol_record["address"]
            address = f"{addr:#x}"
            data["protocols"].append(
                {"guid": guid, "service": service, "address": address}
            )
    logs_dir = os.path.join(tempfile.gettempdir(), "uefi-retool-pp-guids")
    if not os.path.isdir(logs_dir):
        os.mkdir(logs_dir)
    log_fname = f"{binascii.hexlify(ida_nalt.retrieve_input_file_md5()).decode()}.json"
    log_fpath = os.path.join(logs_dir, log_fname)
    with open(log_fpath, "w") as f:
        json.dump(data, f, indent=2)
    idc.qexit(0)


if __name__ == "__main__":
    log_pp_guids()
