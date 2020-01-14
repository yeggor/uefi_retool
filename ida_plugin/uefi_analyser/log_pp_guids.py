# MIT License
# 
# Copyright (c) 2018-2019 yeggor
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
        log.write(data.encode('utf-8') + b'\r\n')

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
