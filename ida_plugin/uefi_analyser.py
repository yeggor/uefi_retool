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

import idaapi
import idautils
import idc

import uefi_analyser.analyser as analyser
import uefi_analyser.prot_wind as pw

AUTHOR = 'yeggor'
VERSION = 'v1.0.0'

class UefiAnalyserPlugin(idaapi.plugin_t):
    flags = (idaapi.PLUGIN_MOD | idaapi.PLUGIN_PROC | idaapi.PLUGIN_FIX)
    comment = 'This plugin performs automatic analysis of the input UEFI module'
    help  = 'This plugin performs automatic analysis of the input UEFI module.\n'
    help += 'Based on the https://github.com/yeggor/UEFI_RETool/blob/master/ida_plugin/uefi_analyser/analyser.py script.'
    wanted_name = 'UEFI analyser'
    wanted_hotkey = 'Ctrl+Alt+U'

    def init(self):
        self.input_file_path = idaapi.get_input_file_path()
        self._welcome()
        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        self._analyse_all()

    def term(self):
        pass

    @staticmethod
    def _welcome():
        main_line = ' UEFI analyser plugin {version} by {author} '.format(
            version=VERSION, 
            author=AUTHOR
        )
        message =  '[{line}]\n'.format(line='='*len(main_line))
        message += '|{line}|\n'.format(line=' '*len(main_line))
        message += '|{main_line}|\n'.format(main_line=main_line)
        message += '|{line}|\n'.format(line=' '*len(main_line))
        message += '[{line}]\n'.format(line='='*len(main_line))
        print(message)

    @staticmethod
    def _analyse_all():
        pw.run()

def PLUGIN_ENTRY():
    try:
        return UefiAnalyserPlugin()
    except Exception as err:
        import traceback
        print('[Error] %s\n%s' % str((err), traceback.format_exc()))
        raise
