import idc
import idaapi

from analyser import Analyser

LOG_FILE = "..\\log\\result_log_all.log"

def print_log(data):
    with open(LOG_FILE, "ab") as log:
        log.write("\r\n" + data)

def list_boot_services(analyser):
    for service in analyser.gBServices:
        for address in analyser.gBServices[service]:
            print_log("\t [{0}] EFI_BOOT_SERVICES->{1}".format(hex(address), service))
    
def log_all():
    idc.auto_wait()
    analyser = Analyser()
    analyser.get_boot_services()
    print_log("=" * 100)
    print_log("\r\nModue name: " + idaapi.get_root_filename())
    print_log("\r\nBoot services:")
    list_boot_services(analyser)
    analyser.get_protocols()
    analyser.get_prot_names()
    data = analyser.Protocols["All"]
    print_log("\r\nProtocols:")
    for element in data:
        guid_str = "[guid] " + str(map(hex, element["guid"]))
        print_log("\t [address] " + hex(element["address"]))
        print_log("\t [service] " + element["service"])
        print_log("\t [protocol_name] " + element["protocol_name"])
        print_log("\t [protocol_place] " + element["protocol_place"])
        print_log("\t " + guid_str)
        print_log("\t " + "*" * len(guid_str))
    print_log("\r\n" + "=" * 100 + "\r\n\r\n")
    idc.qexit(0)

if __name__=="__main__":
    log_all()