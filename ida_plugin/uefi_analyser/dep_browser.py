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

# pylint: disable=import-error
import ida_kernwin
import idaapi
import idautils
import idc
from idaapi import Choose

from .utils import get_dep_json

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
    '''
    class to display protocols information output window
    '''
    def __init__(self, title, dep_json, nb=5):
        sizes = self._get_sizes(dep_json)
        # yapf: disable
        Choose.__init__(
            self,
            title,
            [
                ['GUID', sizes['GUID']],
                ['Name', sizes['Name']],
                ['Module', sizes['Module']],
                ['Service', sizes['Service']]
            ],
            flags=0,
            width=None,
            height=None,
            embedded=False
        )
        self.n = 0
        self.items = self._get_lines(dep_json)
        self.selcount = 0
        self.modal = False
        self.popup_names = []
        self.dep_json = dep_json

    def _get_sizes(self, data):
        '''
        get maximum field sizes
        '''
        sizes = {
            'GUID': 0,
            'Name': 0,
            'Module': 0,
            'Service': 0
        }
        for element in data:
            if len(element['guid']) > sizes['GUID']:
                sizes['GUID'] = len(element['guid'])
            if len(element['protocol_name']) > sizes['Name']:
                sizes['Name'] = len(element['protocol_name'])
            if len(element['module_name']) > sizes['Module']:
                sizes['Module'] = len(element['module_name'])
            if len(element['service']) > sizes['Service']:
                sizes['Service'] = len(element['service'])
        return sizes

    def _get_lines(self, dep_json):
        '''
        to fill line in the table
        '''
        lines = []
        for elem in dep_json:
            item = [
                elem['guid'],
                elem['protocol_name'],
                elem['module_name'],
                elem['service']
            ]
            if not lines.count(item):
                lines.append(item)
        return lines

    def _make_item(self):
        '''
        make custom element
        '''
        item = [
            idaapi.ask_str('', 0, 'GUID'),
            idaapi.ask_str('', 0, 'Name'),
            idaapi.ask_str('', 0, 'Module'),
            idaapi.ask_str('', 0, 'Service')
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
            print('[{}] dependency browser window was closed'.format(NAME))

    def OnEditLine(self, n):
        if DEBUG:
            print('[{}] editing is not supported'.format(NAME))
        return n

    def OnInsertLine(self, n):
        if DEBUG:
            print('[{}] inserting is not supported'.format(NAME))
        return n

    def OnSelectLine(self, n):
        self.selcount += 1
        guid = self.items[n][0]
        print('[{}] {} protocol information'.format(NAME, self.items[n][1]))
        for protocol in self.dep_json:
            if protocol['guid'] == guid:
                print(json.dumps(protocol, indent=4))
                break
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


def handle_json(res_json):
    dep_json = get_dep_json(res_json)
    wind = ProtsWindow('{} dependency browser'.format(NAME), dep_json, nb=10)
    wind.show()


def run(log_file):
    try:
        with open(log_file, 'rb') as f:
            res_json = json.load(f)
        handle_json(res_json)
    except Exception as e:
        print('[{} error] {}'.format(NAME, repr(e)))
        return False
    return True
