# SPDX-License-Identifier: MIT

import glob
import os
import pathlib
import re
import shutil

import colorama
import uefi_firmware

from .guid_db import UEFI_GUIDS

DIR_NAME = "all"
PE_DIR = "modules"

g_re_guid = re.compile(
    r"file-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
)


class Dumper:
    def __init__(self, fw_name, dir_name, pe_dir):
        self.fw_name = fw_name
        self.dir_name = dir_name
        self.pe_dir = pe_dir
        self.modules = list()
        if not os.path.isdir(self.dir_name):
            os.mkdir(self.dir_name)
        if not os.path.isdir(self.pe_dir):
            os.mkdir(self.pe_dir)

    @staticmethod
    def _unsupported() -> bool:
        print("[-] This type of binary is not supported")
        return False

    def get_unique_name(self, module_name: str) -> str:
        # Get unique name, see https://github.com/binarly-io/efiXplorer/issues/11
        index = 1
        unique_name = module_name
        while True:
            if unique_name in self.modules:
                unique_name = f"{module_name}_{index:#d}"
                index += 1
                continue
            return unique_name

    def get_module_name(self, module_path: str) -> str:
        module_name = str()
        dir_name, _ = os.path.split(module_path)
        template = os.path.join(dir_name, "*.ui")
        if len(glob.glob(template)) == 1:
            # try to get a friendly name from the *.ui file
            ui_path = glob.glob(template)[0]
            with open(ui_path, "rb") as f:
                module_name = f.read()
            module_name = module_name.decode("utf-16le")
            module_name = self.get_unique_name(module_name[:-1])
            self.modules.append(module_name)
            return module_name
        # no UI section, try to get a friendly name from the GUID database
        file_guids = g_re_guid.findall(dir_name)
        if not file_guids:
            return str()
        module_guid = file_guids[-1].replace("file-", "")
        module_name = UEFI_GUIDS.get(module_guid.upper())
        if not module_name:
            module_name = module_guid
        module_name = self.get_unique_name(module_name)
        self.modules.append(module_name)
        return module_name

    @staticmethod
    def search_pe(d: str) -> list:
        return list(map(str, pathlib.Path(d).rglob("*.pe")))

    @staticmethod
    def search_te(d: str) -> list:
        return list(map(str, pathlib.Path(d).rglob("*.te")))

    def get_pe_files(self):
        pe_files = self.search_pe(self.dir_name)
        te_files = self.search_te(self.dir_name)
        for module_path in te_files + pe_files:
            module_name = self.get_module_name(module_path)
            if not module_name:
                print(f"Current module: unknown")
                continue
            print(f"Current module: {module_name}")
            dst = os.path.join(self.pe_dir, module_name)
            shutil.copy(module_path, dst)

    def dump_all(self) -> bool:
        if not os.path.isfile(self.fw_name):
            print(f"[-] Check {self.fw_name} file")
            return False
        with open(self.fw_name, "rb") as fw:
            file_content = fw.read()
        parser = uefi_firmware.AutoParser(file_content)
        if parser.type() is "unknown":
            fvh_index = file_content.find(b"_FVH")
            if fvh_index < 0:
                return self._unsupported()
            parser = uefi_firmware.AutoParser(file_content[fvh_index - 40 :])
            if parser.type() is "unknown":
                return self._unsupported()
        firmware = parser.parse()
        firmware.dump(self.dir_name)
        return True


def get_efi_images(fw_name) -> bool:
    """get images from firmware"""
    colorama.init(autoreset=True)  # for correct color display in uefi_firmware module
    dumper = Dumper(fw_name, DIR_NAME, PE_DIR)
    if not dumper.dump_all():
        exit()
    dumper.get_pe_files()
    return True
