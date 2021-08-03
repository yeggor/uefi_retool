# SPDX-License-Identifier: MIT

import os

import idaapi
import idautils
import idc
from PyQt5 import QtWidgets

from uefi_analyser import dep_browser, dep_graph, prot_explorer, ui

AUTHOR = "yeggor"
VERSION = "1.2.0"

NAME = "UEFI_RETool"
WANTED_KEY = "Ctrl+Alt+U"


HELP_MSG = "This plugin performs automatic analysis of the input UEFI module"
COMMENT_MSG = "This plugin performs automatic analysis of the input UEFI module"


class UefiAnalyserPlugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_MOD | idaapi.PLUGIN_PROC | idaapi.PLUGIN_FIX
    comment = COMMENT_MSG
    help = HELP_MSG
    wanted_name = NAME
    wanted_hotkey = WANTED_KEY

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

            print(f"[{NAME} error] {str(err)}\n{traceback.format_exc()}")

    def term(self):
        pass

    def load_json_log(self):
        print(f"[{NAME}] try to parse JSON log file")
        log_name = self._select_log()
        print(f"[{NAME}] log name: {log_name}")
        dep_browser.run(log_name)
        dep_graph.run(log_name)

    def _select_log(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        filename = None
        try:
            filename, _ = file_dialog.getOpenFileName(
                file_dialog,
                f"Select the {NAME} log file",
                self._last_directory,
                "Results files (*.json)",
            )
        except Exception as e:
            print(f"[{NAME} error] {str(e)}")
        if filename:
            self._last_directory = os.path.dirname(filename)
        return filename

    @staticmethod
    def _welcome():
        print(f"\n{NAME} plugin by {AUTHOR} ({VERSION})")
        print(f"{NAME} shortcut key is {WANTED_KEY}\n")

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

            print(f"[{NAME} error] {str(err)}\n{traceback.format_exc()}")

        return True

    def update(self, ctx):
        return idaapi.AST_ENABLE_ALWAYS


def PLUGIN_ENTRY():
    try:
        return UefiAnalyserPlugin()
    except Exception as err:
        import traceback

        print(f"[{NAME} error] {str(err)}\n{traceback.format_exc()}")
