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

import argparse
import json
import os
import sys

import click
import r2pipe
from terminaltables import SingleTable

from .guids import (ami_guids, asrock_guids, dell_guids, edk2_guids, edk_guids,
                    lenovo_guids)

MIN_SET_LEN = 5

OFFSET_x64 = {
    'InstallProtocolInterface': 0x80,
    'ReinstallProtocolInterface': 0x88,
    'UninstallProtocolInterface': 0x90,
    'HandleProtocol': 0x98,
    'RegisterProtocolNotify': 0xA8,
    'OpenProtocol': 0x118,
    'CloseProtocol': 0x120,
    'OpenProtocolInformation': 0x128,
    'ProtocolsPerHandle': 0x130,
    'LocateHandleBuffer': 0x138,
    'LocateProtocol': 0x140,
    'InstallMultipleProtocolInterfaces': 0x148,
    'UninstallMultipleProtocolInterfaces': 0x150
}

LEA_NUM = {
    'InstallProtocolInterface': 2,
    'ReinstallProtocolInterface': 1,
    'UninstallProtocolInterface': 1,
    'HandleProtocol': 1,
    'RegisterProtocolNotify': 1,
    'OpenProtocol': 1,
    'CloseProtocol': 1,
    'OpenProtocolInformation': 1,
    'LocateHandleBuffer': 2,
    'LocateProtocol': 1
}


class Analyser():
    def __init__(self, module_path):
        self.module_path = module_path
        # '-2' for disabling warnings
        self.r2 = r2pipe.open(module_path, ['-2'])
        self.r2.cmd('aaa')

        self.gBServices = {}
        self.gBServices['InstallProtocolInterface'] = []
        self.gBServices['ReinstallProtocolInterface'] = []
        self.gBServices['UninstallProtocolInterface'] = []
        self.gBServices['HandleProtocol'] = []
        self.gBServices['RegisterProtocolNotify'] = []
        self.gBServices['OpenProtocol'] = []
        self.gBServices['CloseProtocol'] = []
        self.gBServices['OpenProtocolInformation'] = []
        self.gBServices['ProtocolsPerHandle'] = []
        self.gBServices['LocateHandleBuffer'] = []
        self.gBServices['LocateProtocol'] = []
        self.gBServices['InstallMultipleProtocolInterfaces'] = []
        self.gBServices['UninstallMultipleProtocolInterfaces'] = []

        self.Protocols = {}
        self.Protocols['ami_guids'] = ami_guids.ami_guids
        self.Protocols['asrock_guids'] = asrock_guids.asrock_guids
        self.Protocols['dell_guids'] = dell_guids.dell_guids
        self.Protocols['edk_guids'] = edk_guids.edk_guids
        self.Protocols['edk2_guids'] = edk2_guids.edk2_guids
        self.Protocols['lenovo_guids'] = lenovo_guids.lenovo_guids
        self.Protocols['all'] = []
        self.Protocols['prop_guids'] = []
        self.info = self.get_info()

    @staticmethod
    def _get_word(bytes):
        '''
        get le-word from bytes
        '''
        word = (bytes[1] << 8) & 0xff00
        word |= (bytes[0] << 0) & 0x00ff
        return word

    @staticmethod
    def _get_dword(bytes):
        '''
        get le-dword from bytes
        '''
        dword = (bytes[3] << 24) & 0xff000000
        dword |= (bytes[2] << 16) & 0x00ff0000
        dword |= (bytes[1] << 8) & 0x0000ff00
        dword |= (bytes[0] << 0) & 0x000000ff
        return dword

    @staticmethod
    def get_guid_str(guid_struct):
        '''
        get GUID output string
        '''
        guid = '{dw:08X}-'.format(dw=guid_struct[0])
        guid += '{w:04X}-'.format(w=guid_struct[1])
        guid += '{w:04X}-'.format(w=guid_struct[2])
        guid += ''.join(
            ['{b:02X}'.format(b=guid_struct[i]) for i in range(3, 11)])
        return guid

    def get_info(self):
        '''
        get common info about UEFI module
        '''
        info = json.loads(self.r2.cmd('ij'))
        return info

    def get_funcs(self):
        '''
        get all recognized functions
        '''
        funcs = {}
        json_funcs = json.loads(self.r2.cmd('aflj'))
        if not len(json_funcs):
            return {}
        for func_info in json_funcs:
            funcs[func_info['name']] = func_info['offset']
        return funcs

    def get_boot_services(self):
        '''
        find boot services from OFFSET_x64
        '''
        funcs = self.get_funcs()
        pdfs = []
        for name in funcs:
            func_info = self.r2.cmd('pdfj @ {name}'.format(name=funcs[name]))
            pdfs.append(json.loads(func_info))
        for func_info in pdfs:
            if ('ops' in func_info):
                fcode = func_info['ops']
                for line in fcode:
                    if ('ptr' in line and 'type' in line and 'offset' in line
                            and 'disasm' in line):
                        if (line['type'].find('call') > -1
                                and line['disasm'].find('call qword [') > -1):
                            for service_name in OFFSET_x64:
                                ea = line['offset']
                                if (line['ptr'] == OFFSET_x64[service_name]
                                        and not self.gBServices[service_name].
                                        count(ea)):
                                    self.gBServices[service_name].append(ea)
        return True

    def prev_head(self, ea):
        '''
        return 0 if ea is start of block
        '''
        addresses = []
        i = 0
        self.r2.cmd('s {addr:#x}'.format(addr=ea))
        block = json.loads(self.r2.cmd('pdfj'))
        for instr in block['ops']:
            addresses.append(instr['offset'])
        i = addresses.index(ea)
        if i > 0:
            return addresses[i - 1]
        else:
            return 0

    def get_guid(self, address):
        '''
        get GUID structure from data by address
        '''
        self.r2.cmd('s {addr:#x}'.format(addr=address))
        guid_bytes = json.loads(self.r2.cmd('pcj 16'))
        current_guid = []
        current_guid.append(self._get_dword(bytearray(guid_bytes[:4:])))
        current_guid.append(self._get_word(bytearray(guid_bytes[4:6:])))
        current_guid.append(self._get_word(bytearray(guid_bytes[6:8:])))
        current_guid += guid_bytes[8:16:]
        return current_guid

    def get_protocols(self):
        '''
        find protocols
        '''
        baddr = 0
        if 'baddr' in self.info['bin']:
            baddr = self.get_info()['bin']['baddr']
        for service_name in self.gBServices:
            if not (service_name in LEA_NUM.keys()):
                continue
            for address in self.gBServices[service_name]:
                ea = address
                lea_counter = 0
                while (True):
                    ea = self.prev_head(ea)
                    if not ea:
                        break
                    instr = json.loads(
                        self.r2.cmd('pdj 1 @ {addr}'.format(addr=ea)))[0]
                    if (instr['type'] == 'lea'):
                        lea_counter += 1
                        if (lea_counter == LEA_NUM[service_name]):
                            break
                if not ea:
                    continue
                guid_addr = instr.get('ptr')
                if (guid_addr is None) or guid_addr <= baddr:
                    continue
                current_guid = self.get_guid(guid_addr)
                if len(set(current_guid)) >= MIN_SET_LEN:
                    protocol_record = {}
                    protocol_record['address'] = guid_addr
                    protocol_record['service'] = service_name
                    protocol_record['guid'] = current_guid
                    if not self.Protocols['all'].count(protocol_record):
                        self.Protocols['all'].append(protocol_record)

    def get_prot_names(self):
        '''
        identify known protocols
        '''
        for index in range(len(self.Protocols['all'])):
            fin = False
            for guid_place in [
                    'ami_guids', 'asrock_guids', 'dell_guids', 'edk_guids',
                    'edk2_guids', 'lenovo_guids'
            ]:
                for prot_name in self.Protocols[guid_place].keys():
                    guid_r2 = self.Protocols['all'][index]['guid']
                    guid_conf = self.Protocols[guid_place][prot_name]
                    if (guid_r2 == guid_conf):
                        self.Protocols['all'][index][
                            'protocol_name'] = prot_name
                        self.Protocols['all'][index][
                            'protocol_place'] = guid_place
                        fin = True
                        break
                if fin:
                    break
            if fin:
                continue
            if not 'protocol_name' in self.Protocols['all'][index]:
                self.Protocols['all'][index][
                    'protocol_name'] = 'ProprietaryProtocol'
                self.Protocols['all'][index]['protocol_place'] = 'unknown'
                self.Protocols['prop_guids'].append(guid_r2)

    def list_boot_services(self):
        '''
        print information about recognized boot services
        '''
        self.get_boot_services()
        empty = True
        table_data = []
        table_instance = SingleTable(table_data)
        table_data.append(['Address', 'Service'])
        print('Boot services:')
        for service in self.gBServices:
            for address in self.gBServices[service]:
                table_data.append(['{addr:#x}'.format(addr=address), service])
                empty = False
        if empty:
            print(' * list is empty')
        else:
            print(table_instance.table)

    def list_protocols(self):
        '''
        print information about recognized protocols
        '''
        self.get_boot_services()
        self.get_protocols()
        self.get_prot_names()
        data = self.Protocols['all']
        print('Protocols:')
        if not len(data):
            print(' * list is empty')
        else:
            table_data = []
            table_instance = SingleTable(table_data)
            table_data.append([
                'GUID', 'Protocol name', 'Address', 'Service', 'Protocol place'
            ])
            for element in data:
                guid = self.get_guid_str(element['guid'])
                table_data.append([
                    guid, element['protocol_name'],
                    '{addr:#x}'.format(addr=element['address']),
                    element['service'], element['protocol_place']
                ])
            print(table_instance.table)

    def print_all(self):
        self.list_boot_services()
        self.list_protocols()


if __name__ == '__main__':
    click.echo(click.style('UEFI_RETool', fg='cyan'))
    click.echo(
        click.style('A tool for UEFI module analysis with radare2', fg='cyan'))
    program = 'python ' + os.path.basename(__file__)
    parser = argparse.ArgumentParser(description='UEFI module analyser',
                                     prog=program)
    parser.add_argument('module', type=str, help='path to UEFI module')
    args = parser.parse_args()
    if os.path.isfile(args.module):
        analyser = Analyser(args.module)
        analyser.print_all()
    else:
        print('Invalid argument')
