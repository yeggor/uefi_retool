import idc
import idaapi
import os

from analyser import Analyser

LOG_FILE = "..{sep}log{sep}ida_log_all.md".format(sep=os.sep)

def print_log(data):
    with open(LOG_FILE, "ab") as log:
        log.write(data + "\r\n")

def list_boot_services(analyser):
    empty = False
    for service in analyser.gBServices:
        for address in analyser.gBServices[service]:
            empty = True
            print_log("* [{0}] EFI_BOOT_SERVICES->{1}".format(hex(address).replace("L", ""), service))
    if (empty == False):
        print_log("* empty")
    
def log_all():
    idc.auto_wait()
    analyser = Analyser()
    analyser.get_boot_services()
    print_log("## Module: " + idaapi.get_root_filename())
    print_log("### Boot services:")
    list_boot_services(analyser)
    analyser.get_protocols()
    analyser.get_prot_names()
    data = analyser.Protocols["All"]
    print_log("### Protocols:")
    if (len(data) == 0):
        print_log("* empty")
    for element in data:
        guid_str = "[guid] " + str(map(hex, element["guid"])).replace("L", "").replace("'", "")
        print_log("* [{0}]".format(hex(element["address"]).replace("L", "")))
        print_log("\t - [service] " + element["service"])
        print_log("\t - [protocol_name] " + element["protocol_name"])
        print_log("\t - [protocol_place] " + element["protocol_place"])
        print_log("\t - " + guid_str)
    idc.qexit(0)

if __name__=="__main__":
    log_all()