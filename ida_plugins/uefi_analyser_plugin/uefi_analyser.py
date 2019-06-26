import idaapi
import uefi_analyser.analyser as analyser
from uefi_analyser.analyser import Analyser

def analyse_all():
    analyser.main()

class ActionHandler(idaapi.action_handler_t):
    def __init__(self, callback):
        idaapi.action_handler_t.__init__(self)
        self.callback = callback

    def activate(self, ctx):
        self.callback()
        return 1

    def update(self, ctx):
        return idaapi.AST_ENABLE_ALWAYS

def register_actions():
    actions = [
        {
            "id": "analyser:all",
            "name": "Analyse all",
            "hotkey": "Ctrl+Alt+U",
            "comment": "Automatic analysis of the input UEFI module",
            "callback": analyse_all,
            "menu_location": "Edit/Plugins/UEFI analyser/Analyse all"
        }
    ]

    for action in actions:
        if not idaapi.register_action(idaapi.action_desc_t(
            action["id"],
            action["name"],
            ActionHandler(action["callback"]),
            action["hotkey"],
            action["comment"]
        )):
            print("Failed to register " + action["id"])
        if not idaapi.attach_action_to_menu(
            action["menu_location"],
            action["id"],
            0
        ):
            print("Failed to attach to menu "+ action["id"])

class UefiAnalyserPlugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_HIDE
    comment = "This plugin performs automatic analysis of the input UEFI module"
    help = "Hotkey: Ctrl+Alt+U"
    wanted_name = "UEFI analyser"
    wanted_hotkey = "Ctrl+Alt+U"

    def init(self):
        print("UEFI analyser plugin initialization")
        register_actions()
        return idaapi.PLUGIN_KEEP

def PLUGIN_ENTRY():
    try:
        return UefiAnalyserPlugin()
    except Exception, err:
        import traceback
        print("Error: %s\n%s" % str((err), traceback.format_exc()))
        raise
