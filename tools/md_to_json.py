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

import argparse
import json
import os


def get_module_json(module_chunk):
    module_json = {}
    mn_end_index = module_chunk.find('\n')
    module_name = module_chunk[:mn_end_index]
    module_json['module_name'] = module_name
    module_chunk = module_chunk[mn_end_index + 2:]
    bs_chunk_end_index = module_chunk.find('### Protocols:')
    bs_chunk = module_chunk[:bs_chunk_end_index]
    prot_chunk = module_chunk[len(bs_chunk):]
    bs_lines = bs_chunk.split('\n')
    prot_lines = prot_chunk.split('\n')
    bs_lines = bs_lines[1:len(bs_lines) - 1]
    prot_lines = prot_lines[1:len(prot_lines) - 1]
    module_json['boot_services'] = []
    for bs_line in bs_lines:
        # get boot service address
        address = bs_line[3:bs_line.find('] ')]
        # get boot service name
        bs_name = bs_line[bs_line.find('EFI'):]
        if address[:2] != '0x':
            continue
        module_json['boot_services'].append({
            'address': address,
            'bs_name': bs_name
        })

    module_json['protocols'] = []
    for i in range(0, len(prot_lines) - 1, 5):
        # get protocol address
        address = prot_lines[i][3:prot_lines[i].find(']')]
        # get service name
        # yapf: disable
        service_index = prot_lines[i + 1].find('[service]') + len('[service]') + 1
        service = prot_lines[i + 1][service_index:]
        # get protocol name
        protocol_name_index = prot_lines[i + 2].find('[protocol_name]') + len(
            '[protocol_name]') + 1
        protocol_name = prot_lines[i + 2][protocol_name_index:]
        # get protocol place
        protocol_place_index = prot_lines[i + 3].find(
            '[protocol_place]') + len('[protocol_place]') + 1
        protocol_place = prot_lines[i + 3][protocol_place_index:]
        # get protocol guid
        guid_index = prot_lines[i + 4].find('[guid]') + len('[guid]') + 1
        guid = prot_lines[i + 4][guid_index:]
        # add element
        module_json['protocols'].append({
            'address': address,
            'service': service,
            'protocol_name': protocol_name,
            'protocol_place': protocol_place,
            'guid': guid
        })
    return module_json


def md_to_json(md_file, json_file):
    with open(md_file, 'r') as f:
        data = f.read()
    res_json = []
    modules = data.split('## Module: ')[1:]
    for module_chunk in modules:
        module_json = get_module_json(module_chunk)
        res_json.append(module_json)
    with open(json_file, 'w') as f:
        json.dump(res_json, f, indent=4)


def get_json(md_file):
    json_file = md_file.replace('.md', '.json')
    md_to_json(md_file, json_file)


def main():
    program = 'python ' + os.path.basename(__file__)
    parser = argparse.ArgumentParser(
        description='Convert log from MarkDown to JSON', prog=program)
    parser.add_argument(
        'md_log_file',
        type=str,
        help='path to your MarkDown log file (for example, ida_log_all.md)')

    args = parser.parse_args()

    if os.path.isfile(args.md_log_file):
        try:
            get_json(args.md_log_file)
        except Exception as e:
            print('[error] {}'.format(repr(e)))
    else:
        print('[error] check file name')


if __name__ == '__main__':
    main()
