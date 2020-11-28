################################################################################
# MIT License
#
# Copyright (c) 2018-2020 yeggor
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
################################################################################

import os

import ida_bytes
import idaapi
import idautils
import idc

# definitions from PE file structure
IMAGE_FILE_MACHINE_IA64 = 0x8664
IMAGE_FILE_MACHINE_I386 = 0x014c
PE_OFFSET = 0x3c
IMAGE_SUBSYSTEM_EFI_APPLICATION = 0xa
IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER = 0xb
IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER = 0xc


class Table():
    """build table from array"""
    def __init__(self, table_data):
        self.table_data = table_data
        self.max_sizes = self._get_max_sizes()
        self.angle = '+'
        self.gl = '-'
        self.vl = '|'

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
        cls = Table(table_data)
        table = cls.angle + f'{cls.angle}'.join([((cls.gl * (size + 2)))
                                                 for size in cls.max_sizes])
        table += f'{cls.angle}\n{cls.vl} '
        table += f'{cls.vl} '.join([
            ((cls.table_data[0][i] + ' ' *
              (cls.max_sizes[i] - len(cls.table_data[0][i]) + 1)))
            for i in range(len(cls.table_data[0]))
        ])
        table += f'{cls.vl}\n{cls.angle}'
        table += f'{cls.angle}'.join([((cls.gl * (size + 2)))
                                      for size in cls.max_sizes])
        table += f'{cls.angle}\n'
        for j in range(1, len(cls.table_data)):
            table += f'{cls.vl} '
            table += f'{cls.vl} '.join([
                ((cls.table_data[j][i] + ' ' *
                  (cls.max_sizes[i] - len(cls.table_data[j][i]) + 1)))
                for i in range(len(cls.table_data[j]))
            ])
            table += f'{cls.vl}\n'
        table += cls.angle
        table += f'{cls.angle}'.join([((cls.gl * (size + 2)))
                                      for size in cls.max_sizes])
        table += f'{cls.angle}'
        return table


def set_hexrays_comment(address, text):
    """set comment in decompiled code"""
    cfunc = idaapi.decompile(address)
    tl = idaapi.treeloc_t()
    tl.ea = address
    tl.itp = idaapi.ITP_SEMI
    cfunc.set_user_cmt(tl, text)
    cfunc.save_user_cmts()


def check_guid(address):
    """correctness is determined based on the number of unique bytes"""
    return (len(set(ida_bytes.get_bytes(address, 16))) > 8)


def get_guid(address):
    """get GUID located by address"""
    guid = []
    guid.append(idc.get_wide_dword(address))
    guid.append(idc.get_wide_word(address + 4))
    guid.append(idc.get_wide_word(address + 6))
    for addr in range(address + 8, address + 16, 1):
        guid.append(idc.get_wide_byte(addr))
    return guid


def get_guid_str(guid_struct):
    guid = f'{guid_struct[0]:08X}-'
    guid += f'{guid_struct[1]:04X}-'
    guid += f'{guid_struct[2]:04X}-'
    guid += ''.join([f'{guid_struct[i]:02X}' for i in range(3, 11)])
    return guid


def get_num_le(bytearr):
    """translate a set of bytes into a number in the little endian format"""
    num_le = 0
    for i in range(len(bytearr)):
        num_le += bytearr[i] * pow(256, i)
    return num_le


def rev_endian(num):
    """reorders bytes in number"""
    num_str = f'{num:x}'
    # yapf: disable
    num_ba = ([int('0x' + num_str[i:i + 2], 16) for i in range(0, len(num_str) - 1, 2)])
    # yapf: enable
    return get_num_le(num_ba)


def get_machine_type(header):
    """get the architecture of the investigated file"""
    if len(header) < PE_OFFSET + 1:
        return 'unknown'
    PE_POINTER = header[PE_OFFSET]
    FH_POINTER = PE_POINTER + 4
    if len(header) < FH_POINTER + 3:
        return 'unknown'
    machine_type = header[FH_POINTER:FH_POINTER + 2:]
    type_value = get_num_le(machine_type)
    if type_value == IMAGE_FILE_MACHINE_I386:
        return 'x86'
    if type_value == IMAGE_FILE_MACHINE_IA64:
        return 'x64'
    return 'unknown'


def check_subsystem(header):
    """get the subsystem of the investigated file"""
    if len(header) < PE_OFFSET + 1:
        return False
    PE_POINTER = header[PE_OFFSET]
    if len(header) < PE_POINTER + 0x5d:
        return False
    subsystem = header[PE_POINTER + 0x5c]
    return (subsystem == IMAGE_SUBSYSTEM_EFI_APPLICATION
            or subsystem == IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER
            or subsystem == IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER)


def get_header_idb():
    """get file header from idb"""
    if idc.get_segm_name(0) == 'HEADER':
        header = bytearray(
            [idc.get_wide_byte(ea) for ea in range(0, idc.get_segm_end(0))])
        return header
    return bytearray(b'')


def get_header_file():
    """get file header from analysing file"""
    if os.path.isfile(idaapi.get_input_file_path()):
        with open(idaapi.get_input_file_path(), 'rb') as f:
            buf = f.read(512)
    else:
        buf = b'\x00'
    return bytearray(buf)


def get_dep_json(res_json):
    """get json for dependency browser and dependency graph"""
    CLIENT_PROTOCOL_SERVICES = ('LocateProtocol', 'OpenProtocol')

    dep_json = []
    for module_info in res_json:
        for protocol in module_info['protocols']:
            if (protocol['service'] == 'InstallProtocolInterface'
                    or protocol['service']
                    == 'InstallMultipleProtocolInterfaces'):
                dep_json_item = {
                    'module_name': module_info['module_name'],
                    'protocol_name': protocol['protocol_name'],
                    'guid': protocol['guid'],
                    'service': protocol['service']
                }
                dep_json_item['used_by'] = []
                for module_info in res_json:
                    for protocol in module_info['protocols']:
                        if (protocol['service'] in CLIENT_PROTOCOL_SERVICES
                                and protocol['guid'] == dep_json_item['guid']):
                            dep_json_item['used_by'].append(
                                module_info['module_name'])
                dep_json.append(dep_json_item)
    return dep_json
