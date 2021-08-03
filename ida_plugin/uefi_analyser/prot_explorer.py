# SPDX-License-Identifier: MIT

import idaapi
import idc
from idaapi import Choose

from .analyser import Analyser
from .tables import BOOT_SERVICES_OFFSET_x64, BOOT_SERVICES_OFFSET_x86
from .utils import get_guid_str

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
    """display protocols information output window"""

    def __init__(self, title, analyser, nb=5):
        sizes = self._get_sizes(analyser)
        head = [
            ["Address", sizes["Address"]],
            ["Name", sizes["Name"]],
            ["Service", sizes["Service"]],
            ["Place", sizes["Place"]],
            ["GUID", sizes["GUID"]],
        ]
        Choose.__init__(
            self, title, head, flags=0, width=None, height=None, embedded=False
        )
        self.n = 0
        self.items = self._get_lines(analyser)
        self.selcount = 0
        self.modal = False
        self.popup_names = list()

    def _get_sizes(self, analyser):
        """get maximum field sizes"""
        sizes = {"Address": 0, "Name": 0, "Service": 0, "Place": 0, "GUID": 0}
        for prot in analyser.Protocols["all"] + analyser.Protocols["data"]:
            addr = prot["address"]
            if len(f"{addr:016X}") > sizes["Address"]:
                sizes["Address"] = len(f"{addr:016X}")
            if len(prot["protocol_name"]) > sizes["Name"]:
                sizes["Name"] = len(prot["protocol_name"])
            if len(prot["service"]) > sizes["Service"]:
                sizes["Service"] = len(prot["service"])
            if len(prot["protocol_place"]) > sizes["Place"]:
                sizes["Place"] = len(prot["protocol_place"])
            if len(get_guid_str(prot["guid"])) > sizes["GUID"]:
                sizes["GUID"] = len(get_guid_str(prot["guid"]))
        return sizes

    def _get_lines(self, analyser):
        """fill line in the table"""
        lines = list()
        for prot in analyser.Protocols["all"] + analyser.Protocols["data"]:
            addr = prot["address"]
            item = [
                f"{addr:016X}",
                prot["protocol_name"],
                prot["service"],
                prot["protocol_place"],
                get_guid_str(prot["guid"]),
            ]
            if not lines.count(item):
                lines.append(item)
        return lines

    def _make_item(self):
        """make custom element"""
        item = [
            idaapi.ask_str(str(), 0, "Address"),
            idaapi.ask_str(str(), 0, "Name"),
            idaapi.ask_str(str(), 0, "Service"),
            idaapi.ask_str(str(), 0, "Place"),
            idaapi.ask_str(str(), 0, "GUID"),
        ]
        self.n += 1
        return item

    def OnGetLine(self, n):
        return self.items[n]

    def OnGetSize(self):
        n = len(self.items)
        return n

    def OnClose(self):
        print(f"[{NAME}] protocol explorer window was closed")

    def OnInsertLine(self, n):
        print(f"[{NAME}] inserting is not supported")
        return n

    def OnSelectLine(self, n):
        self.selcount += 1
        ea = int(self.items[n][0], 16)
        idc.jumpto(ea)
        print(f"[{NAME}] jump to {ea:016X}")
        return n

    def OnEditLine(self, n):
        print(f"[{NAME}] editing is not supported")
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


def run():
    idc.auto_wait()
    analyser = Analyser()
    if analyser.valid:
        analyser.print_all()
        analyser.analyse_all()
    if not analyser.valid:
        analyser.arch = idaapi.ask_str(
            "x86 / x64", 0, "Set architecture manually (x86 or x64)"
        )
        if analyser.arch == "x86":
            analyser.BOOT_SERVICES_OFFSET = BOOT_SERVICES_OFFSET_x86
        elif analyser.arch == "x64":
            analyser.BOOT_SERVICES_OFFSET = BOOT_SERVICES_OFFSET_x64
        else:
            return False
        analyser.print_all()
        analyser.analyse_all()
    if analyser.Protocols["all"]:
        wind = ProtsWindow(f"{NAME} protocol explorer", analyser, nb=10)
        wind.show()
    return True


if __name__ == "__main__":
    run()
