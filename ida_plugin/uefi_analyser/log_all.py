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
import idc
from uefi_analyser.analyser import Analyser
from uefi_analyser.utils import get_guid_str

LOG_FILE = os.path.join('..', 'log', 'ida_log_all.md')


def print_log(data):
    with open(LOG_FILE, 'a') as log:
        log.write(data + '\n')


def list_boot_services(analyser):
    empty = True
    for service in analyser.gBServices:
        for address in analyser.gBServices[service]:
            empty = False
            print_log('* [{0}] EFI_BOOT_SERVICES->{1}'.format(
                '{addr:#x}'.format(addr=address), service))
    if empty:
        print_log('* empty')


def log_all():
    idc.auto_wait()
    analyser = Analyser()
    if not analyser.valid:
        idc.qexit(-1)
    analyser.get_boot_services()
    print_log('## Module: ' + idaapi.get_root_filename())
    print_log('### Boot services:')
    list_boot_services(analyser)
    analyser.get_protocols()
    analyser.get_prot_names()
    data = analyser.Protocols['all']
    print_log('### Protocols:')
    if not len(data):
        print_log('* empty')
    for element in data:
        guid_str = '[guid] ' + get_guid_str(element['guid'])
        print_log('* [{0}]'.format(
            '{addr:#x}'.format(addr=element['address'])))
        print_log('\t - [service] ' + element['service'])
        print_log('\t - [protocol_name] ' + element['protocol_name'])
        print_log('\t - [protocol_place] ' + element['protocol_place'])
        print_log('\t - ' + guid_str)
    idc.qexit(0)


if __name__ == '__main__':
    log_all()
