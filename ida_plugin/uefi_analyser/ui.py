# SPDX-License-Identifier: MIT

import idaapi

NAME = "UEFI_RETool"


def init_menu(action_handler):
    action = f"{NAME}:loadfile"
    action_desc = idaapi.action_desc_t(
        action,
        f"{NAME}...",
        action_handler,
        "Ctrl+Alt+J",
        f"{NAME} dependency browser",
    )
    idaapi.register_action(action_desc)
    idaapi.attach_action_to_menu("File", action, idaapi.SETMENU_APP)
