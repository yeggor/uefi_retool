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

import ida_bytes  # pylint: disable=import-error
import idaapi  # pylint: disable=import-error
import idautils  # pylint: disable=import-error
import idc  # pylint: disable=import-error

'''
definitions from PE file structure
'''
IMAGE_FILE_MACHINE_IA64 = 0x8664
IMAGE_FILE_MACHINE_I386 = 0x014c
PE_OFFSET = 0x3c
IMAGE_SUBSYSTEM_EFI_APPLICATION = 0xa
IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER = 0xb
IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER = 0xc

class Table():
    '''
    class to build table from array
    '''
    def __init__(self, table_data):
        self.table_data = table_data
        self.max_sizes = self._get_max_sizes()

    def _get_max_sizes(self):
        num = len(self.table_data[0])
        sizes = [0 for _ in range(num)]
        for i in range(len(self.table_data[0])):
            for j in range(len(self.table_data)):
              if len(self.table_data[j][i]) > sizes[i]:
                  sizes[i] = len(self.table_data[j][i])
        return sizes

    @classmethod
    def display(cls, table_data):
        cl = Table(table_data)
        gl = '-'
        vl = '|'
        angle = '+'
        table = angle + '{angle}'.join([((gl * (size + 2))) for size in cl.max_sizes]).format(angle=angle) + '{angle}\n'.format(angle=angle)
        table += '{vl} '.format(vl=vl) + \
            '{vl} '.join([((cl.table_data[0][i] + ' ' * (cl.max_sizes[i] - len(cl.table_data[0][i]) + 1))) for i in range(len(cl.table_data[0]))]).format(vl=vl) + \
            '{vl}\n'.format(vl=vl)
        table += angle + '{angle}'.join([((gl * (size + 2))) for size in cl.max_sizes]).format(angle=angle) + '{angle}\n'.format(angle=angle)
        for j in range(1, len(cl.table_data)):
            table += '{vl} '.format(vl=vl) + \
            '{vl} '.join([((cl.table_data[j][i] + ' ' * (cl.max_sizes[i] - len(cl.table_data[j][i]) + 1))) for i in range(len(cl.table_data[j]))]).format(vl=vl) + \
            '{vl}\n'.format(vl=vl)
        table += angle + '{angle}'.join([((gl * (size + 2))) for size in cl.max_sizes]).format(angle=angle) + '{angle}'.format(angle=angle)
        return table

def set_hexrays_comment(address, text):
    '''
    set comment in decompiled code
    '''
    cfunc = idaapi.decompile(address)
    tl = idaapi.treeloc_t()
    tl.ea = address
    tl.itp = idaapi.ITP_SEMI
    cfunc.set_user_cmt(tl, text)
    cfunc.save_user_cmts()

def check_guid(address):
    '''
    correctness is determined based on the number of unique bytes
    '''
    return (len(set(ida_bytes.get_bytes(address, 16))) > 8)

def get_guid(address):
    '''
    get GUID located by address
    '''
    guid = []
    guid.append(idc.get_wide_dword(address))
    guid.append(idc.get_wide_word(address + 4))
    guid.append(idc.get_wide_word(address + 6))
    for addr in range(address + 8, address + 16, 1):
        guid.append(idc.get_wide_byte(addr))
    return guid

def get_guid_str(guid_struct):
    guid = '{dw:08X}-'.format(dw=guid_struct[0])
    guid += '{w:04X}-'.format(w=guid_struct[1])
    guid += '{w:04X}-'.format(w=guid_struct[2])
    guid += ''.join(['{b:02X}'.format(b=guid_struct[i]) for i in range(3, 11)])
    return guid

def get_num_le(bytearr):
    '''
    translate a set of bytes into a number in the little endian format
    '''
    num_le = 0
    for i in range(len(bytearr)):
        num_le += bytearr[i] * pow(256, i)
    return num_le

def rev_endian(num):
    '''
    reorders bytes in number
    '''
    num_str = hex(num).replace('0x', '').replace('L', '')
    num_ba = ([int('0x' + num_str[i:i+2], 16) for i in range(0, len(num_str)-1, 2)])
    return get_num_le(num_ba)

def get_machine_type(header):
    '''
    get the architecture of the investigated file
    '''
    if len(header) < PE_OFFSET + 1:
        return 'unknown'
    PE_POINTER = header[PE_OFFSET]
    FH_POINTER = PE_POINTER + 4
    if len(header) < FH_POINTER + 3:
        return 'unknown'
    machine_type = header[FH_POINTER:FH_POINTER+2:]
    type_value = get_num_le(machine_type)
    if type_value == IMAGE_FILE_MACHINE_I386:
        return 'x86'
    if type_value == IMAGE_FILE_MACHINE_IA64:
        return 'x64'
    return 'unknown'

def check_subsystem(header):
    '''
    get the subsystem of the investigated file
    '''
    if len(header) < PE_OFFSET + 1:
        return False
    PE_POINTER = header[PE_OFFSET]
    if len(header) < PE_POINTER + 0x5d:
        return False
    subsystem = header[PE_POINTER + 0x5c]
    return (subsystem == IMAGE_SUBSYSTEM_EFI_APPLICATION or \
            subsystem == IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER or \
            subsystem == IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER)

def get_header_idb():
    '''
    get file header from idb
    '''
    if idc.get_segm_name(0) == 'HEADER':
        header = bytearray([idc.get_wide_byte(ea) for ea in range(0, idc.get_segm_end(0))])
        return header
    return bytearray(b'')

def get_header_file():
    '''
    get file header from analysing file
    '''
    if os.path.isfile(idaapi.get_input_file_path()):
        with open(idaapi.get_input_file_path(), 'rb') as f:
            buf = f.read(512)
    else:
        buf = b'\x00'
    return bytearray(buf)


def get_dep_json(res_json):
    '''
    get json for dependency browser and dependency graph
    '''
    dep_json = []
    for module_info in res_json:
        for protocol in module_info['protocols']:
            if (protocol['service'] == 'InstallProtocolInterface' or
                protocol['service'] == 'InstallMultipleProtocolInterfaces'
            ):
                dep_json_item = {
                    'module_name': module_info['module_name'],
                    'protocol_name': protocol['protocol_name'],
                    'guid': protocol['guid'],
                    'service': protocol['service']
                }
                dep_json_item['used_by'] = []
                for module_info in res_json:
                    for protocol in module_info['protocols']:
                        if (protocol['service'] == 'LocateProtocol' and
                            protocol['guid'] == dep_json_item['guid']
                        ):
                            dep_json_item['used_by'].append(module_info['module_name'])        
                dep_json.append(dep_json_item)
    return dep_json

