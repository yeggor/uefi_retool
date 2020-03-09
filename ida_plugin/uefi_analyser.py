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

# pylint: disable=import-error
import idaapi
import idautils
import idc
from PyQt5 import QtWidgets
from uefi_analyser import dep_browser, dep_graph, prot_explorer, ui

AUTHOR = 'yeggor'
VERSION = '1.1.0'

NAME = 'UEFI_RETool'
HELP_MSG = 'This plugin performs automatic analysis of the input UEFI module'
COMMENT_MSG = 'This plugin performs automatic analysis of the input UEFI module'


class UefiAnalyserPlugin(idaapi.plugin_t):
    flags = (idaapi.PLUGIN_MOD | idaapi.PLUGIN_PROC | idaapi.PLUGIN_FIX)
    comment = COMMENT_MSG
    help = HELP_MSG
    wanted_name = NAME
    wanted_hotkey = 'Ctrl+Alt+U'

    def init(self):
        self._last_directory = idautils.GetIdbDir()
        ui.init_menu(MenuHandler(self))
        self._welcome()
        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        try:
            self._analyse_all()
        except Exception as err:
            import traceback
            print('[{} error] {}\n{}'.format(NAME, str(err),
                                             traceback.format_exc()))

    def term(self):
        pass

    def load_json_log(self):
        print('[{}] try to parse JSON log file'.format(NAME))
        log_name = self._select_log()
        print('[{}] log name: {}'.format(NAME, log_name))
        dep_browser.run(log_name)
        dep_graph.run(log_name)

    def _select_log(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        filename = None
        try:
            filename, _ = file_dialog.getOpenFileName(
                file_dialog, 'Select the {} log file'.format(NAME),
                self._last_directory, 'Results files (*.json)')
        except Exception as e:
            print('[{} error] {}'.format(NAME, str(e)))
        if filename:
            self._last_directory = os.path.dirname(filename)
        return filename

    @staticmethod
    def _welcome():
        main_line = ' {} plugin {} by {} '.format(NAME, VERSION, AUTHOR)
        message = '[{}]\n'.format('=' * len(main_line))
        message += '|{}|\n'.format(' ' * len(main_line))
        message += '|{}|\n'.format(main_line)
        message += '|{}|\n'.format(' ' * len(main_line))
        message += '[{}]\n'.format('=' * len(main_line))
        print(message)

    @staticmethod
    def _analyse_all():
        prot_explorer.run()


class MenuHandler(idaapi.action_handler_t):
    def __init__(self, plugin):
        idaapi.action_handler_t.__init__(self)
        self.plugin = plugin

    def activate(self, ctx):
        try:
            self.plugin.load_json_log()
        except Exception as err:
            import traceback
            print('[{} error] {}\n{}'.format(NAME, str(err),
                                             traceback.format_exc()))

        return True

    def update(self, ctx):
        return idaapi.AST_ENABLE_ALWAYS


def PLUGIN_ENTRY():
    try:
        return UefiAnalyserPlugin()
    except Exception as err:
        import traceback
        print('[{} error] {}\n{}'.format(NAME, str(err),
                                         traceback.format_exc()))
