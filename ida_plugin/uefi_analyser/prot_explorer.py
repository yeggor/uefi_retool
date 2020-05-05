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

# pylint: disable=import-error
import ida_kernwin
import idaapi
import idautils
import idc
from idaapi import Choose

from .analyser import Analyser
from .tables import BOOT_SERVICES_OFFSET_x64, BOOT_SERVICES_OFFSET_x86
from .utils import get_guid_str

NAME = 'UEFI_RETool'
DEBUG = True


class chooser_handler_t(idaapi.action_handler_t):
    def __init__(self, thing):
        idaapi.action_handler_t.__init__(self)
        self.thing = thing

    def activate(self, ctx):
        pass

    def update(self, ctx):
        if idaapi.is_chooser_tform(ctx.form_type):
            return idaapi.AST_ENABLE_FOR_FORM
        return idaapi.AST_DISABLE_FOR_FORM


class ProtsWindow(Choose):
    """display protocols information output window"""
    def __init__(self, title, analyser, nb=5):
        sizes = self._get_sizes(analyser)
        # yapf: disable
        Choose.__init__(
            self,
            title,
            [
                ['Address', sizes['Address']],
                ['Name', sizes['Name']],
                ['Service', sizes['Service']],
                ['Place', sizes['Place']],
                ['GUID', sizes['GUID']],
            ],
            flags=0,
            width=None,
            height=None,
            embedded=False
        )
        self.n = 0
        self.items = self._get_lines(analyser)
        self.selcount = 0
        self.modal = False
        self.popup_names = []

    def _get_sizes(self, analyser):
        """get maximum field sizes"""
        sizes = {
            'Address': 0,
            'Name': 0,
            'Service': 0,
            'Place': 0,
            'GUID': 0
        }
        for prot in analyser.Protocols['all'] + analyser.Protocols['data']:
            if len('{addr:#010x}'.format(addr=prot['address'])) > sizes['Address']:
                sizes['Address'] = len(
                    '{addr:#010x}'.format(addr=prot['address']))
            if len(prot['protocol_name']) > sizes['Name']:
                sizes['Name'] = len(prot['protocol_name'])
            if len(prot['service']) > sizes['Service']:
                sizes['Service'] = len(prot['service'])
            if len(prot['protocol_place']) > sizes['Place']:
                sizes['Place'] = len(prot['protocol_place'])
            if len(get_guid_str(prot['guid'])) > sizes['GUID']:
                sizes['GUID'] = len(get_guid_str(prot['guid']))
        return sizes

    def _get_lines(self, analyser):
        """fill line in the table"""
        lines = []
        for prot in analyser.Protocols['all'] + analyser.Protocols['data']:
            item = [
                '{addr:#010x}'.format(addr=prot['address']),
                prot['protocol_name'],
                prot['service'],
                prot['protocol_place'],
                get_guid_str(prot['guid'])
            ]
            if not lines.count(item):
                lines.append(item)
        return lines

    def _make_item(self):
        """make custom element"""
        item = [
            idaapi.ask_str('', 0, 'Address'),
            idaapi.ask_str('', 0, 'Name'),
            idaapi.ask_str('', 0, 'Service'),
            idaapi.ask_str('', 0, 'Place'),
            idaapi.ask_str('', 0, 'GUID')
        ]
        self.n += 1
        return item

    def OnGetLine(self, n):
        return self.items[n]

    def OnGetSize(self):
        n = len(self.items)
        return n

    def OnClose(self):
        if DEBUG:
            print('[{}] protocol explorer window was closed'.format(NAME))

    def OnInsertLine(self, n):
        if DEBUG:
            print('[{}] inserting is not supported'.format(NAME))
        return n

    def OnSelectLine(self, n):
        self.selcount += 1
        ea = int(self.items[n][0], 16)
        idc.jumpto(ea)
        if DEBUG:
            print('[{}] jump to {addr:#010x}'.format(NAME, addr=ea))
        return n

    def OnEditLine(self, n):
        if DEBUG:
            print('[{}] editing is not supported'.format(NAME))
        return n

    def OnDeleteLine(self, n):
        if DEBUG:
            print('[{}] deleting is not supported'.format(NAME))
        return n

    def OnRefresh(self, n):
        if DEBUG:
            print('[{}] refreshing is not supported'.format(NAME))
        return n

    def OnGetLineAttr(self, n):
        return n

    def show(self):
        return self.Show(self.modal) >= 0


def run():
    idc.auto_wait()
    analyser = Analyser()
    if analyser.valid:
        analyser.print_all()
        analyser.analyse_all()
    if not analyser.valid:
        analyser.arch = idaapi.ask_str(
            'x86 / x64', 0, 'Set architecture manually (x86 or x64)')
        if not (analyser.arch == 'x86' or analyser.arch == 'x64'):
            return False
        if (analyser.arch == 'x86'):
            analyser.BOOT_SERVICES_OFFSET = BOOT_SERVICES_OFFSET_x86
        if (analyser.arch == 'x64'):
            analyser.BOOT_SERVICES_OFFSET = BOOT_SERVICES_OFFSET_x64
        analyser.print_all()
        analyser.analyse_all()
    if len(analyser.Protocols['all']):
        wind = ProtsWindow(
            '{} protocol explorer'.format(NAME), analyser, nb=10)
        wind.show()
    return True


if __name__ == '__main__':
    run()
