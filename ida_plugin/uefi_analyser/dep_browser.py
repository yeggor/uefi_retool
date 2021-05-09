# SPDX-License-Identifier: MIT

import json

import ida_kernwin
import idaapi
import idautils
import idc
from idaapi import Choose

from .utils import get_dep_json

NAME = "UEFI_RETool"


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
    """class to display protocols information output window"""

    def __init__(self, title, dep_json, nb=5):
        sizes = self._get_sizes(dep_json)
        Choose.__init__(
            self,
            title,
            [
                ["GUID", sizes["GUID"]],
                ["Name", sizes["Name"]],
                ["Module", sizes["Module"]],
                ["Service", sizes["Service"]],
            ],
            flags=0,
            width=None,
            height=None,
            embedded=False,
        )
        self.n = 0
        self.items = self._get_lines(dep_json)
        self.selcount = 0
        self.modal = False
        self.popup_names = list()
        self.dep_json = dep_json

    def _get_sizes(self, data):
        """get maximum field sizes"""
        sizes = {"GUID": 0, "Name": 0, "Module": 0, "Service": 0}
        for element in data:
            if len(element["guid"]) > sizes["GUID"]:
                sizes["GUID"] = len(element["guid"])
            if len(element["protocol_name"]) > sizes["Name"]:
                sizes["Name"] = len(element["protocol_name"])
            if len(element["module_name"]) > sizes["Module"]:
                sizes["Module"] = len(element["module_name"])
            if len(element["service"]) > sizes["Service"]:
                sizes["Service"] = len(element["service"])
        return sizes

    def _get_lines(self, dep_json):
        """to fill line in the table"""
        lines = list()
        for elem in dep_json:
            item = [
                elem["guid"],
                elem["protocol_name"],
                elem["module_name"],
                elem["service"],
            ]
            if not lines.count(item):
                lines.append(item)
        return lines

    def _make_item(self):
        """make custom element"""
        item = [
            idaapi.ask_str(str(), 0, "GUID"),
            idaapi.ask_str(str(), 0, "Name"),
            idaapi.ask_str(str(), 0, "Module"),
            idaapi.ask_str(str(), 0, "Service"),
        ]
        self.n += 1
        return item

    def OnGetLine(self, n):
        return self.items[n]

    def OnGetSize(self):
        n = len(self.items)
        return n

    def OnClose(self):
        print(f"[{NAME}] dependency browser window was closed")

    def OnEditLine(self, n):
        print(f"[{NAME}] editing is not supported")
        return n

    def OnInsertLine(self, n):
        print(f"[{NAME}] inserting is not supported")
        return n

    def OnSelectLine(self, n):
        self.selcount += 1
        guid = self.items[n][0]
        print(f"[{NAME}] {self.items[n][1]} protocol information")
        for protocol in self.dep_json:
            if protocol["guid"] == guid:
                print(json.dumps(protocol, indent=4))
                break
        return n

    def OnDeleteLine(self, n):
        print(f"[{NAME}] deleting is not supported")
        return n

    def OnRefresh(self, n):
        print(f"[{NAME}] refreshing is not supported")
        return n

    def OnGetLineAttr(self, n):
        return n

    def show(self):
        return self.Show(self.modal) >= 0


def handle_json(res_json):
    dep_json = get_dep_json(res_json)
    wind = ProtsWindow(f"{NAME} dependency browser", dep_json, nb=10)
    wind.show()


def run(log_file):
    try:
        with open(log_file, "rb") as f:
            res_json = json.load(f)
        handle_json(res_json)
    except Exception as e:
        print(f"[{NAME} error] {repr(e)}")
        return False
    return True
