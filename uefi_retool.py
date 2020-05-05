#!/usr/bin/env python3.7

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

import json
import os
import platform

import click
import uefi_firmware
from tools import md_to_json, utils
from tools.get_efi_images import get_efi_images
from tools.update_edk2_guids import update

# get a platform
if platform.system() == 'Windows':
    CONFIG_FILE = 'config-win.json'

if platform.system() == 'Linux':
    CONFIG_FILE = 'config-nix.json'

# read configuration data
with open(CONFIG_FILE, 'rb') as cfile:
    config = json.load(cfile)

IDA_PATH = '"{}"'.format(config['IDA_PATH'])
IDA64_PATH = '"{}"'.format(config['IDA64_PATH'])

DONE = click.style('DONE', fg='green')
ERROR = click.style('ERROR', fg='red')


def show_item(item):
    return 'current module: {}'.format(item)


def analyse_all(scr_name):
    log_path = os.path.join('log',
                            'ida_{}'.format(scr_name.replace('.py', '.md')))
    if os.path.isfile(log_path):
        os.remove(log_path)
    files = os.listdir(config['PE_DIR'])
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
            module_path = os.path.join(config['PE_DIR'], module)
            machine_type = utils.get_machine_type(module_path)
            ida_exe = IDA64_PATH
            if machine_type == utils.IMAGE_FILE_MACHINE_I386:
                ida_exe = IDA_PATH
            analyser = os.path.join('plugins', 'uefi_analyser', scr_name)
            cmd = ' '.join(
                [ida_exe, '-c -A -S{}'.format(analyser), module_path])
            # analyse module in batch mode
            os.system(cmd)
            if not (os.path.isfile('{}.i64'.format(module_path))
                    or os.path.isfile('{}.idb'.format(module_path))):
                print(
                    '{res} check your config.json file or move ida_plugin/uefi_analyser directory to IDA plugins directory'
                    .format(res=ERROR))
                exit()
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


@click.group()
def cli():
    pass


@click.command()
@click.argument('firmware_path')
def get_info(firmware_path):
    """Analyze the entire UEFI firmware. The analysis result is saved to .md and .json files."""
    clear_all()
    get_efi_images(firmware_path)
    analyse_all('log_all.py')
    print(
        '{res} check .{sep}log{sep}ida_log_all.md and .{sep}log{sep}ida_log_all.json files'
        .format(res=DONE, sep=os.sep))
    clear_all()


@click.command()
@click.argument('firmware_path')
def get_pp(firmware_path):
    """Get a list of proprietary protocols in the UEFI firmware. The result is saved to .md file."""
    clear_all()
    get_efi_images(firmware_path)
    analyse_all('log_pp_guids.py')
    print('{res} check .{sep}log{sep}ida_pp_guids.md file'.format(res=DONE,
                                                                  sep=os.sep))
    clear_all()


@click.command()
@click.argument('firmware_path')
def get_images(firmware_path):
    """Get executable images from UEFI firmware. Images are stored in "modules" directory."""
    clear_all()
    get_efi_images(firmware_path)
    print('{res} check .{sep}modules directory'.format(res=DONE, sep=os.sep))


cli.add_command(get_info)
cli.add_command(get_pp)
cli.add_command(get_images)

if __name__ == '__main__':
    cli()
