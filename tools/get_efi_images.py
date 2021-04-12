################################################################################
# MIT License
#
# Copyright (c) 2018-2021 yeggor
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

import glob
import os
import pathlib
import re
import shutil

import colorama
import uefi_firmware

from .guid_db import UEFI_GUIDS

DIR_NAME = 'all'
PE_DIR = 'modules'

g_re_guid = re.compile(
    r'file-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')


class Dumper():
    def __init__(self, fw_name, dir_name, pe_dir):
        self.fw_name = fw_name
        self.dir_name = dir_name
        self.pe_dir = pe_dir
        if not os.path.isdir(self.dir_name):
            os.mkdir(self.dir_name)
        if not os.path.isdir(self.pe_dir):
            os.mkdir(self.pe_dir)

    @staticmethod
    def _unsupported() -> bool:
        print('[-] This type of binary is not supported')
        return False

    @staticmethod
    def get_module_name(module_path: str) -> str:
        module_name = str()
        dir_name, _ = os.path.split(module_path)
        template = os.path.join(dir_name, '*.ui')
        if len(glob.glob(template)) == 1:
            # try to get a friendly name from the *.ui file
            ui_path = glob.glob(template)[0]
            with open(ui_path, 'rb') as f:
                module_name = f.read()
            module_name = module_name.decode('utf-16le')
            return module_name[:-1]
        # no UI section, try to get a friendly name from the GUID database
        file_guids = g_re_guid.findall(dir_name)
        if not file_guids:
            return str()
        module_guid = file_guids[-1].replace('file-', '')
        module_name = UEFI_GUIDS.get(module_guid.upper())
        if not module_name:
            module_name = module_guid
        return module_name

    @staticmethod
    def search_pe(d: str) -> list:
        return list(map(str, pathlib.Path(d).rglob('*.pe')))

    @staticmethod
    def search_te(d: str) -> list:
        return list(map(str, pathlib.Path(d).rglob('*.te')))

    def get_pe_files(self):
        pe_files = self.search_pe(self.dir_name)
        te_files = self.search_te(self.dir_name)
        for module_path in (te_files + pe_files):
            module_name = self.get_module_name(module_path)
            if not module_name:
                print(f'Current module: unknown')
                continue
            print(f'Current module: {module_name}')
            dst = os.path.join(self.pe_dir, module_name)
            shutil.copy(module_path, dst)

    def dump_all(self) -> bool:
        if not os.path.isfile(self.fw_name):
            print(f'[-] Check {self.fw_name} file')
            return False
        with open(self.fw_name, 'rb') as fw:
            file_content = fw.read()
        parser = uefi_firmware.AutoParser(file_content)
        if parser.type() is 'unknown':
            fvh_index = file_content.find(b'_FVH')
            if fvh_index < 0:
                return self._unsupported()
            parser = uefi_firmware.AutoParser(file_content[fvh_index - 40:])
            if parser.type() is 'unknown':
                return self._unsupported()
        firmware = parser.parse()
        firmware.dump(self.dir_name)
        return True


def get_efi_images(fw_name) -> bool:
    """get images from firmware"""
    colorama.init()  # for correct color display in uefi_firmware module
    dumper = Dumper(fw_name, DIR_NAME, PE_DIR)
    if not dumper.dump_all():
        exit()
    dumper.get_pe_files()
    return True
