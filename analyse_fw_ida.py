#!/usr/bin/env python3.7

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
import platform
import sys
from glob import glob

import click
import uefi_firmware

from tools import md_to_json, utils
from tools.get_efi_images import get_efi_images
from tools.update_edk2_guids import update

if platform.system() == 'Windows':
    CONFIG_FILE = 'config-win.json'

if platform.system() == 'Linux':
    CONFIG_FILE = 'config-nix.json'

# reads configuration data
with open(CONFIG_FILE, 'rb') as cfile:
    config = json.load(cfile)

dump_dir = config['DUMP_DIR']
pe_dir = config['PE_DIR']
ida_path = '"{}"'.format(config['IDA_PATH'])
ida64_path = '"{}"'.format(config['IDA64_PATH'])


def show_item(item):
    return 'current module: {}'.format(item)


def analyse_all(scr_name):
    log_path = os.path.join('log',
                            'ida_{}'.format(scr_name.replace('.py', '.md')))
    if os.path.isfile(log_path):
        os.remove(log_path)
    files = os.listdir(pe_dir)
    bar_template = click.style('%(label)s  %(bar)s | %(info)s', fg='cyan')
    label = 'Modules analysis'
    with click.progressbar(files,
                           length=len(files),
                           bar_template=bar_template,
                           label=label,
                           item_show_func=show_item) as bar:
        for module in bar:
            if module[-4:] in ['.idb', '.i64', '.id1', '.id2', '.nam', '.til']:
                continue
            module_path = os.path.join(pe_dir, module)
            machine_type = utils.get_machine_type(module_path)
            ida_exe = ida64_path
            if machine_type == utils.IMAGE_FILE_MACHINE_I386:
                ida_exe = ida_path
            cmd_line = ' '.join([
                ida_exe, '-c -A -S' +
                os.path.join('plugins', 'uefi_analyser', scr_name), module_path
            ])
            if not os.system(cmd_line):
                msg = '[-] Error during {module} module processing\n\t{hint}'.format(
                    module=module_path,
                    hint=
                    'check your config.json file or move ida_plugin/uefi_analyser directory to IDA plugins directory'
                )
                exit(msg)
    if scr_name == 'log_all.py':
        md_name = os.path.join('log', 'ida_log_all.md')
        md_to_json.get_json(md_name)


def clear(dirname):
    for root, dirs, files in os.walk(dirname, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def clear_all():
    clear(config['DUMP_DIR'])
    clear(config['PE_DIR'])


def main():
    click.echo(click.style('UEFI_RETool', fg='cyan'))
    click.echo(
        click.style('A tool for UEFI firmware analysis with IDA Pro',
                    fg='cyan'))
    program = 'python ' + os.path.basename(__file__)
    parser = argparse.ArgumentParser(prog=program)
    parser.add_argument('firmware_path',
                        type=str,
                        help='path to UEFI firmware for analysis')
    parser.add_argument('--all',
                        action='store_true',
                        help='''analyse of all UEFI firmware modules
		and output of information to .{sep}log{sep}ida_log_all.md file
		(example: python analyse_fw_ida.py --all <firmware_path>)'''.format(
                            sep=os.sep))
    parser.add_argument('--pp_guids',
                        action='store_true',
                        help='''analyse all UEFI firmware modules
		and save a table with proprietry protocols
		to .{sep}log{sep}ida_pp_guids.md file
		(example: python analyse_fw_ida.py --pp_guids <firmware_path>)'''.format(
                            sep=os.sep))
    parser.add_argument('--get_efi_images',
                        action='store_true',
                        help='''get all executable images from UEFI firmware
		(images are stored in .{sep}modules directory, 
		example: python analyse_fw_ida.py --get_efi_images <firmware_path>)'''.
                        format(sep=os.sep))

    args = parser.parse_args()

    if (args.all and os.path.isfile(args.firmware_path)):
        clear_all()
        get_efi_images(args.firmware_path)
        analyse_all('log_all.py')
        print('Check .{sep}log{sep}ida_log_all.md file'.format(sep=os.sep))
        clear_all()

    if (args.pp_guids and os.path.isfile(args.firmware_path)):
        clear_all()
        get_efi_images(args.firmware_path)
        analyse_all('log_pp_guids.py')
        print('Check .{sep}log{sep}ida_pp_guids.md file'.format(sep=os.sep))
        clear_all()

    if (args.get_efi_images and os.path.isfile(args.firmware_path)):
        clear_all()
        get_efi_images(args.firmware_path)
        print('Check .{sep}modules directory'.format(sep=os.sep))


if __name__ == '__main__':
    main()
