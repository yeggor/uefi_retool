import idc
import idaapi
import os

from analyser import Analyser

LOG_FILE = "..{sep}log{sep}ida_log_pp_guids.md".format(sep=os.sep)

"""
output format:
| Guid | Module | Service | Address |
| ---  | ---    | ---     | ---     |
| ...  | ...    | ...     | ...     |
"""

def print_log(data):
    with open(LOG_FILE, "ab") as log:
        log.write(data + "\r\n")

def get_table_line(guid, module, service, address):
    line =  "| " + guid + " "
    line += "| " + module + " "
    line += "| " + service + " "
    line += "| " + address + " "
    line += "|"
    return line

def log_pp_guids():
    if os.path.isfile(LOG_FILE) == 0 or os.path.getsize(LOG_FILE) == 0:
        print_log(get_table_line("Guid", "Module", "Service", "Address"))
        print_log(get_table_line("---", "---", "---", "---"))

    idc.auto_wait()
    analyser = Analyser()
    analyser.get_boot_services()
    analyser.get_protocols()
    analyser.get_prot_names()

    for protocol_record in analyser.Protocols["All"]:
        if (protocol_record["protocol_name"] == "ProprietaryProtocol"):
            guid = str(map(hex, protocol_record["guid"]))
            guid = guid.replace("L", "").replace("'", "")
            module = idaapi.get_root_filename()
            service = protocol_record["service"]
            address = hex(protocol_record["address"])
            address = address.replace("L", "")
            print_log(get_table_line(guid, module, service, address))
    idc.qexit(0)

if __name__=="__main__":
    log_pp_guids()