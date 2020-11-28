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
import tempfile
from concurrent.futures import ProcessPoolExecutor, as_completed

import click
import uefi_firmware
from tools import utils
from tools.get_efi_images import get_efi_images
from tqdm import tqdm

CONFIG_FILE = 'config.json'
DONE = click.style('DONE', fg='green')
ERROR = click.style('ERROR', fg='red')

# read configuration data
with open(CONFIG_FILE, 'rb') as cfile:
    CONFIG = json.load(cfile)

# ida and ida64 executables
IDA_PATH = '"{}"'.format(CONFIG['IDA_PATH'])
IDA64_PATH = '"{}"'.format(CONFIG['IDA64_PATH'])

# directories with logs
PP_GUIDS_LOGS = os.path.join(tempfile.gettempdir(), 'uefi-retool-pp-guids')
ALL_INFO_LOGS = os.path.join(tempfile.gettempdir(), 'uefi-retool-all-info')


def analyse_module(module, scr_name):
    module_path = os.path.join(CONFIG['PE_DIR'], module)
    machine_type = utils.get_machine_type(module_path)
    ida_exe = IDA64_PATH
    if machine_type == utils.IMAGE_FILE_MACHINE_I386:
        ida_exe = IDA_PATH
    analyser = os.path.join('plugins', 'uefi_analyser', scr_name)
    cmd = ' '.join([ida_exe, f'-c -A -S{analyser}', module_path])
    # analyse module in batch mode
    os.system(cmd)
    if not (os.path.isfile(f'{module_path}.i64')
            or os.path.isfile(f'{module_path}.idb')):
        print(
            '{ERROR} check your config.json file or move ida_plugin/uefi_analyser directory to IDA plugins directory'
        )
        exit()
    return True


def analyse_all(scr_name, max_workers):
    files = os.listdir(CONFIG['PE_DIR'])
    # check first module
    analyse_module(files[0], scr_name)
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(analyse_module, module, scr_name)
            for module in files[1:]
        ]
        params = {
            'total': len(futures),
            'unit': 'module',
            'unit_scale': True,
            'leave': True
        }
        for f in tqdm(as_completed(futures), **params):
            pass


def clear(dirname):
    for root, dirs, files in os.walk(dirname, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def clear_all():
    clear(CONFIG['DUMP_DIR'])
    clear(CONFIG['PE_DIR'])
    clear(PP_GUIDS_LOGS)
    clear(ALL_INFO_LOGS)


def get_log(command, firmware_path):
    suf = 'all-info.json'
    tmp_dir = ALL_INFO_LOGS
    if command == 'get-pp':
        suf = 'pp-guids.json'
        tmp_dir = PP_GUIDS_LOGS
    # collect all in one log
    if not os.path.isdir(CONFIG['LOGS_DIR']):
        os.mkdir(CONFIG['LOGS_DIR'])
    _, fw_name = os.path.split(firmware_path)
    log_fname = os.path.join(CONFIG['LOGS_DIR'], f'{fw_name}-{suf}')
    info = list()
    logs = os.listdir(tmp_dir)
    for log in logs:
        with open(os.path.join(tmp_dir, log), 'r') as f:
            info.append(json.load(f))
    with open(log_fname, 'w') as f:
        json.dump(info, f, indent=4)
    print(f'{DONE} check {log_fname} file')


@click.group()
def cli():
    pass


@click.command()
@click.argument('firmware_path')
@click.option('-w',
              '--workers',
              help='Number of workers (8 by default).',
              type=int)
def get_info(firmware_path, workers):
    """Analyze the entire UEFI firmware. The analysis result is saved to .json file."""
    if not workers:
        workers = 8
    clear_all()
    get_efi_images(firmware_path)
    analyse_all('log_all.py', workers)
    get_log('get-info', firmware_path)


@click.command()
@click.argument('firmware_path')
@click.option('-w',
              '--workers',
              help='Number of workers (8 by default).',
              type=int)
def get_pp(firmware_path, workers):
    """Get a list of proprietary protocols in the UEFI firmware. The result is saved to .json file."""
    if not workers:
        workers = 8
    clear_all()
    get_efi_images(firmware_path)
    analyse_all('log_pp_guids.py', workers)
    get_log('get-pp', firmware_path)


@click.command()
@click.argument('firmware_path')
def get_images(firmware_path):
    """Get executable images from UEFI firmware. Images are stored in "modules" directory."""
    clear_all()
    get_efi_images(firmware_path)
    print(f'{DONE} check .{os.sep}modules directory')


cli.add_command(get_info)
cli.add_command(get_pp)
cli.add_command(get_images)

if __name__ == '__main__':
    cli()
