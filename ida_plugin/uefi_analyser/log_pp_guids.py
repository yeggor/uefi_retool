################################################################################
# MIT License
#
# Copyright (c) 2018-2020 yeggor
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

import binascii
import json
import os
import tempfile

import ida_nalt
import idaapi
import idc
from uefi_analyser.analyser import Analyser
from uefi_analyser.utils import get_guid_str


def log_pp_guids():
    idc.auto_wait()
    analyser = Analyser()
    if not analyser.valid:
        idc.qexit(-1)
    analyser.get_boot_services()
    analyser.get_protocols()
    analyser.get_prot_names()
    data = dict()
    data['module_name'] = idaapi.get_root_filename()
    data['protocols'] = []
    for protocol_record in analyser.Protocols['all']:
        if (protocol_record['protocol_name'] == 'ProprietaryProtocol'):
            guid = get_guid_str(protocol_record['guid'])
            service = protocol_record['service']
            addr = protocol_record['address']
            address = f'{addr:#x}'
            data['protocols'].append({
                'guid': guid,
                'service': service,
                'address': address
            })
    logs_dir = os.path.join(tempfile.gettempdir(), 'uefi-retool-pp-guids')
    if not os.path.isdir(logs_dir):
        os.mkdir(logs_dir)
    log_fname = f'{binascii.hexlify(ida_nalt.retrieve_input_file_md5()).decode()}.json'
    log_fpath = os.path.join(logs_dir, log_fname)
    with open(log_fpath, 'w') as f:
        json.dump(data, f, indent=2)
    idc.qexit(0)


if __name__ == '__main__':
    log_pp_guids()
