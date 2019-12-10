import os

import idaapi
import idc

import utils
from analyser import Analyser

LOG_FILE = os.path.join('..', 'log', 'ida_log_pp_guids.md')

'''
output format:
| Guid | Module | Service | Address |
| ---  | ---    | ---     | ---     |
| ...  | ...    | ...     | ...     |
'''

def print_log(data):
    with open(LOG_FILE, 'ab') as log:
        log.write(data + '\r\n')

def get_table_line(guid, module, service, address):
    line =  '| ' + guid + ' '
    line += '| ' + module + ' '
    line += '| ' + service + ' '
    line += '| ' + address + ' '
    line += '|'
    return line

def log_pp_guids():
    if not os.path.isfile(LOG_FILE) or not os.path.getsize(LOG_FILE):
        print_log(get_table_line('Guid', 'Module', 'Service', 'Address'))
        print_log(get_table_line('---', '---', '---', '---'))
    idc.auto_wait()
    analyser = Analyser()
    if not analyser.valid:
        idc.qexit(0)
    analyser.get_boot_services()
    analyser.get_protocols()
    analyser.get_prot_names()
    for protocol_record in analyser.Protocols['All']:
        if (protocol_record['protocol_name'] == 'ProprietaryProtocol'):
            guid = utils.get_guid_str(protocol_record['guid'])
            module = idaapi.get_root_filename()
            service = protocol_record['service']
            address = '{addr:#x}'.format(addr=protocol_record['address'])
            print_log(get_table_line(guid, module, service, address))
    idc.qexit(0)

if __name__=='__main__':
    log_pp_guids()
