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

import json

import ida_bytes
import ida_name
import idaapi
import idautils
import idc
import utils
from guids import ami_guids, edk2_guids, edk_guids
from tables import BOOT_SERVICES_OFFSET_x64, BOOT_SERVICES_OFFSET_x86
from utils import Table


class Analyser():
    def __init__(self):
        header = utils.get_header_idb()
        if not len(header):
            header = utils.get_header_file()
        self.arch = utils.get_machine_type(header)
        self.subsystem = utils.check_subsystem(header)
        self.valid = True
        if not self.subsystem:
            print('[ERROR] Wrong subsystem')
            self.valid = False
        if not (self.arch == 'x86' or self.arch == 'x64'):
            print('[ERROR] Wrong architecture')
            self.valid = False
        if self.arch == 'x86':
            self.BOOT_SERVICES_OFFSET = BOOT_SERVICES_OFFSET_x86
        if self.arch == 'x64':
            self.BOOT_SERVICES_OFFSET = BOOT_SERVICES_OFFSET_x64
        self.base = idaapi.get_imagebase()
        idc.import_type(-1, 'EFI_GUID')
        idc.import_type(-1, 'EFI_SYSTEM_TABLE')
        idc.import_type(-1, 'EFI_RUNTIME_SERVICES')
        idc.import_type(-1, 'EFI_BOOT_SERVICES')

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
        self.Protocols['AmiGuids'] = ami_guids.ami_guids
        self.Protocols['EdkGuids'] = edk_guids.edk_guids
        self.Protocols['Edk2Guids'] = edk2_guids.edk2_guids
        self.Protocols['All'] = [
            # {
            #   address: ...
            #   service: ...
            #   guid: ...
            #   protocol_name: ...
            #   protocol_place: ...
            # }, 
            # ...
        ]
        self.Protocols['PropGuids'] = []
        self.Protocols['Data'] = []

    @staticmethod
    def help():
        print('Methods:')
        print(' * analyser.get_boot_services()')
        print('   - check: analyser.gBServices[<service_name>]')
        print(' * analyser.get_protocols()')
        print('   - check: analyser.Protocols["All"]')
        print(' * analyser.get_prot_names()')
        print('   - check: analyser.Protocols["All"]')
        print('Commands:')
        print(' * analyser.list_boot_services()')
        print(' * analyser.list_protocols()')
        print(' * analyser.make_comments()')
        print(' * analyser.make_names()')
        print(' * analyser.set_types()')
        print(' * analyser.print_all()')
        print(' * analyser.analyse_all()')

    def get_boot_services(self):
        '''
        found boot services in idb
        '''
        code = list(idautils.Functions())[0]
        start = idc.get_segm_start(code)
        end = idc.get_segm_end(code)
        for ea in range(start, end):
            for service_name in self.BOOT_SERVICES_OFFSET:
                if (idc.print_insn_mnem(ea) == 'call' and \
                    idc.get_operand_value(ea, 0) == self.BOOT_SERVICES_OFFSET[service_name]
                ):
                    if not self.gBServices[service_name].count(ea):
                        self.gBServices[service_name].append(ea)

    def get_protocols(self):
        '''
        found UEFI protocols information in idb
        '''
        for service_name in self.gBServices:
            for address in self.gBServices[service_name]:
                ea, found = address, False
                if self.arch == 'x86':
                    for _ in range(1, 25):
                        ea = idc.prev_head(ea)
                        if (idc.get_operand_value(ea, 0) > self.base and idc.print_insn_mnem(ea) == 'push'):
                            found = True
                            break
                if self.arch == 'x64':
                    for _ in range(1, 16):
                        ea = idc.prev_head(ea)
                        if (idc.get_operand_value(ea, 1) > self.base and idc.print_insn_mnem(ea) == 'lea'):
                            found = True
                            break
                if not found:
                    continue
                for xref in idautils.DataRefsFrom(ea):
                    if (idc.print_insn_mnem(xref) == ''):
                        cur_guid = utils.get_guid(xref)
                        if cur_guid != [0] * 11:
                            record = {
                                'address': xref,
                                'service': service_name,
                                'guid': cur_guid,
                            }
                            record['address'] = xref
                            record['service'] = service_name
                            record['guid'] = cur_guid
                            if not self.Protocols['All'].count(record):
                                self.Protocols['All'].append(record)

    def get_prot_names(self):
        '''
        match UEFI protocols GUIDs with known GUIDs
        if protocol GUID is not found in a lists of known GUIDs, the protocol is considered proprietary
        '''
        for index in range(len(self.Protocols['All'])):
            fin = False
            for prot_name in self.Protocols['Edk2Guids'].keys():
                guid_idb = self.Protocols['All'][index]['guid']
                guid_conf = self.Protocols['Edk2Guids'][prot_name]
                if (guid_idb == guid_conf):
                    self.Protocols['All'][index]['protocol_name'] = prot_name
                    self.Protocols['All'][index]['protocol_place'] = 'edk2_guids'
                    fin = True
                    break
            if fin: continue
            for prot_name in self.Protocols['EdkGuids'].keys():
                guid_idb = self.Protocols['All'][index]['guid']
                guid_conf = self.Protocols['EdkGuids'][prot_name]
                if (guid_idb == guid_conf):
                    self.Protocols['All'][index]['protocol_name'] = prot_name
                    self.Protocols['All'][index]['protocol_place'] = 'edk_guids'
                    fin = True
                    break
            if fin: continue
            for prot_name in self.Protocols['AmiGuids'].keys():
                guid_idb = self.Protocols['All'][index]['guid']
                guid_conf = self.Protocols['AmiGuids'][prot_name]
                if (guid_idb == guid_conf):
                    self.Protocols['All'][index]['protocol_name'] = prot_name
                    self.Protocols['All'][index]['protocol_place'] = 'ami_guids'
                    fin = True
                    break
            if fin: continue
            if not 'protocol_name' in self.Protocols['All'][index]:
                self.Protocols['All'][index]['protocol_name'] = 'ProprietaryProtocol'
                self.Protocols['All'][index]['protocol_place'] = 'unknown'

    @staticmethod
    def apply_struct(ea, size, sid):
	    ida_bytes.del_items(ea, size, idc.DELIT_DELNAMES)
	    ida_bytes.create_struct(ea, size, sid)
	    return size

    def get_data_guids(self):
        '''
        rename GUIDs in idb
        '''
        EFI_GUID = 'EFI_GUID *'
        EFI_GUID_ID = idc.get_struc_id('EFI_GUID')
        segments = [
            '.text', 
            '.data'
        ]
        for segment in segments:
            seg_start, seg_end = 0, 0
            for seg in idautils.Segments():
                if idc.get_segm_name(seg) == segment:
                    seg_start = idc.get_segm_start(seg)
                    seg_end = idc.get_segm_end(seg)
                    break
            ea = seg_start
            while (ea <= seg_end - 15):
                prot_name = ''
                if idc.get_name(ea, ida_name.GN_VISIBLE).find('unk_') != -1:
                    find = False
                    cur_guid = []
                    cur_guid.append(idc.get_wide_dword(ea))
                    cur_guid.append(idc.get_wide_word(ea + 4))
                    cur_guid.append(idc.get_wide_word(ea + 6))
                    for addr in range(ea + 8, ea + 16, 1):
                        cur_guid.append(idc.get_wide_byte(addr))
                    if cur_guid == [0] * 11:
                        ea += 1
                        continue
                    for name in self.Protocols['Edk2Guids']:
                        if self.Protocols['Edk2Guids'][name] == cur_guid:
                            prot_name = name + '_' + '{addr:#x}'.format(addr=ea)
                            record = {
                                'address': ea, 
                                'service': 'unknown', 
                                'guid': cur_guid, 
                                'protocol_name': name, 
                                'protocol_place': 'edk2_guids'
                            }
                            find = True
                            break
                    for name in self.Protocols['EdkGuids']:
                        if self.Protocols['EdkGuids'][name] == cur_guid:
                            prot_name = name + '_' + '{addr:#x}'.format(addr=ea)
                            prot_name = name + '_' + '{addr:#x}'.format(addr=ea)
                            record = {
                                'address': ea, 
                                'service': 'unknown', 
                                'guid': cur_guid, 
                                'protocol_name': name, 
                                'protocol_place': 'edk_guids'
                            }
                            find = True
                            break
                    for name in self.Protocols['AmiGuids']:
                        if self.Protocols['AmiGuids'][name] == cur_guid:
                            prot_name = name + '_' + '{addr:#x}'.format(addr=ea)
                            prot_name = name + '_' + '{addr:#x}'.format(addr=ea)
                            record = {
                                'address': ea, 
                                'service': 'unknown', 
                                'guid': cur_guid, 
                                'protocol_name': name, 
                                'protocol_place': 'ami_guids'
                            }
                            find = True
                            break
                    if find and (idc.get_name(ea, ida_name.GN_VISIBLE) != prot_name):
                        idc.SetType(ea, EFI_GUID)
                        self.apply_struct(ea, 16, EFI_GUID_ID)
                        idc.set_name(ea, prot_name)
                        self.Protocols['Data'].append(record)
                ea += 1

    def make_comments(self):
        '''
        make comments in idb
        '''
        EFI_BOOT_SERVICES_ID = idc.get_struc_id('EFI_BOOT_SERVICES')
        self.get_boot_services()
        empty = True
        for service in self.gBServices:
            for address in self.gBServices[service]:
                message = 'EFI_BOOT_SERVICES->{0}'.format(service)
                idc.set_cmt(address, message, 0)
                idc.op_stroff(address, 0, EFI_BOOT_SERVICES_ID, 0)
                empty = False
                print('[ {ea} ] {message}'.format(ea='{addr:#010x}'.format(addr=address), message=message))
        if empty:
            print(' * list is empty')

    def make_names(self):
        '''
        make names in idb
        '''
        EFI_GUID = 'EFI_GUID *'
        EFI_GUID_ID = idc.get_struc_id('EFI_GUID')
        self.get_boot_services()
        self.get_protocols()
        self.get_prot_names()
        data = self.Protocols['All']
        empty = True
        for element in data:
            try:
                idc.SetType(element['address'], EFI_GUID)
                self.apply_struct(element['address'], 16, EFI_GUID_ID)
                name = element['protocol_name'] + '_' + '{addr:#x}'.format(addr=element['address'])
                idc.set_name(element['address'], name)
                empty = False
                print('[ {ea} ] {name}'.format(
                    ea='{addr:#010x}'.format(addr=element['address']),
                    name=name
                ))
            except:
                continue
        if empty:
            print(' * list is empty')

    def _find_est(self, gvar, start, end):
        RAX = 0
        BS_OFFSET = 0x60
        EFI_SYSTEM_TABLE = 'EFI_SYSTEM_TABLE *'
        if self.arch == 'x86':
            BS_OFFSET = 0x3c
        ea = start
        while (ea < end):
            if ((idc.print_insn_mnem(ea) == 'mov') and (idc.get_operand_value(ea, 0) == RAX) and \
                (idc.get_operand_value(ea, 1) == BS_OFFSET)
            ):
                if idc.SetType(gvar, EFI_SYSTEM_TABLE):
                    idc.set_name(gvar, 'gSt_{addr:#x}'.format(addr=gvar))
                    return True
            ea = idc.next_head(ea)
        return False

    def set_types(self):
        '''
        handle (EFI_BOOT_SERVICES *) type
        and (EFI_SYSTEM_TABLE *) for x64 images
        '''
        RAX = 0
        O_REG = 1
        O_MEM = 2
        EFI_BOOT_SERVICES = 'EFI_BOOT_SERVICES *'
        EFI_SYSTEM_TABLE = 'EFI_SYSTEM_TABLE *'
        empty = True
        for service in self.gBServices:
            for address in self.gBServices[service]:
                ea = address
                num_of_attempts = 10
                for _ in range(num_of_attempts):
                    ea = idc.prev_head(ea)
                    if (idc.print_insn_mnem(ea) == 'mov' and idc.get_operand_type(ea, 1) == O_MEM):
                        if (idc.get_operand_type(ea, 0) == O_REG and idc.get_operand_value(ea, 0) == RAX):
                            gvar = idc.get_operand_value(ea, 1)
                            gvar_type = idc.get_type(gvar)
                            '''
                            if (EFI_SYSTEM_TABLE *)
                            '''
                            if ((gvar_type != 'EFI_SYSTEM_TABLE *') and \
                                (idc.print_operand(address, 0).find('rax') == 1)
                            ):
                                if self._find_est(gvar, ea, address):
                                    print('[ {0} ] Type ({type}) successfully applied'.format(
                                        '{addr:#010x}'.format(addr=gvar), 
                                        type=EFI_SYSTEM_TABLE)
                                    )
                                    empty = False
                                    break
                            '''
                            otherwise it (EFI_BOOT_SERVICES *)
                            '''
                            if (gvar_type != 'EFI_BOOT_SERVICES *' and gvar_type != 'EFI_SYSTEM_TABLE *'):
                                if idc.SetType(gvar, EFI_BOOT_SERVICES):
                                    empty = False
                                    idc.set_name(gvar, 'gBs_{addr:#x}'.format(addr=gvar))
                                    print('[ {0} ] Type ({type}) successfully applied'.format(
                                        '{addr:#010x}'.format(addr=gvar), 
                                        type=EFI_BOOT_SERVICES)
                                    )
                            break
        if empty:
            print(' * list is empty')

    def list_boot_services(self):
        '''
        display boot services information to the IDAPython output window
        '''
        self.get_boot_services()
        empty = True
        table_data = []
        table_data.append(['Address', 'Service'])
        print('Boot services:')
        for service in self.gBServices:
            for address in self.gBServices[service]:
                table_data.append(['{addr:#010x}'.format(addr=address), service])
                empty = False
        if empty:
            print(' * list is empty')
        else:
            print(Table.display(table_data))

    def list_protocols(self):
        '''
        display protocols information to the IDAPython output window
        '''
        self.get_boot_services()
        self.get_protocols()
        self.get_prot_names()
        data = self.Protocols['All'] + self.Protocols['Data']
        print('Protocols:')
        if len(data) == 0:
            print(' * list is empty')
        else:
            table_data = []
            table_data.append(['GUID', 'Protocol name', 'Address', 'Service', 'Protocol place'])
            for element in data:
                guid = utils.get_guid_str(element['guid'])
                table_data.append([
                    guid,
                    element['protocol_name'],
                    '{addr:#010x}'.format(addr=element['address']),
                    element['service'],
                    element['protocol_place']
                ])
            print(Table.display(table_data))

    def print_all(self):
        self.list_boot_services()
        self.list_protocols()

    def analyse_all(self):
        print('Comments:')
        self.make_comments()
        print('Names:')
        self.make_names()
        print('Types:')
        self.set_types()
        self.get_data_guids()

def main():
    idc.auto_wait()
    analyser = Analyser()
    if analyser.valid:
        analyser.print_all()
        analyser.analyse_all()
    if not analyser.valid:
        analyser.arch = idaapi.askstr(0, 'x86 / x64', 'Set architecture manually (x86 or x64)')
        if not (analyser.arch == 'x86' or analyser.arch == 'x64'):
            return False 
        if (analyser.arch == 'x86'):
            analyser.BOOT_SERVICES_OFFSET = BOOT_SERVICES_OFFSET_x86
        if (analyser.arch == 'x64'):
            analyser.BOOT_SERVICES_OFFSET = BOOT_SERVICES_OFFSET_x64
        analyser.print_all()
        analyser.analyse_all()
        return True

if __name__=='__main__':
    main()
