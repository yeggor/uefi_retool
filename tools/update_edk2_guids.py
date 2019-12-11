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
import glob
import os
import re
import shutil

import click

DATA_PATH = os.path.join('..', 'conf')
IDA_GUIDS = os.path.join('..', 'ida_plugin', 'uefi_analyser', 'guids')
R2_GUIDS = os.path.join('..', 'r2_uefi_re', 'guids')

def get_py(string):
    new_string = 'edk2_guids = {\n'

    replace_table = {
        '{'     : '[',
        '}'     : ']',
        '#'     : '\t#',
        '='     : ':',
        ']\n'   : '],\n',
    }

    re_table = {
        r'\ng'     : "\n\t'g",
        r' +:'     : ':',
        r':'       : ' :',
        r'\]\]'    : ']',
        r'\] +\]'  : ']',
        r', +\['   : ',',
        r',\['     : ','
    }

    for key in replace_table:
        string = string.replace(key, replace_table[key])
    new_string += string + '}'
    for regexp in re_table:
        new_string = re.sub(re.compile(regexp), re_table[regexp], new_string)
    return new_string

def get_guids_list(edk2_path, data_path):
    if not os.path.isdir(edk2_path):
        print('[-] Error, check edk2 path')
        return False
    dec_files = glob.glob(edk2_path + '{sep}*{sep}*.dec'.format(sep=os.sep))
    if not len(dec_files):
        print('[-] Error, *.dec files list is empty')
        return False
    if not os.path.isdir(DATA_PATH):
        os.mkdir(DATA_PATH)
    regexp = re.compile(r'g.+=.+{.+}')
    conf_content = ''
    for dec_file in dec_files:
        with open(dec_file, 'rb') as dec:
            guids_list = re.findall(regexp, dec.read())
            conf_content += '# Guids from {dec_file} file \n'.format(dec_file=dec_file)
            for guid in guids_list:
                conf_content += guid + '\n'
    with open(os.path.join(DATA_PATH, 'edk2_guids.conf'), 'wb') as conf:
        conf.write('# This file was automatically generated with update_edk2_guids.py script\n')
        conf.write(conf_content)
    py_content = get_py(conf_content)
    with open(DATA_PATH + os.sep + 'edk2_guids.py', 'wb') as conf:
        conf.write('# This file was automatically generated with update_edk2_guids.py script\n')
        conf.write(py_content)
    return True

def update(edk2_path, data_path, guids_path):
    if get_guids_list(edk2_path, data_path):
        shutil.copy(os.path.join(data_path, 'edk2_guids.py'), os.path.join(guids_path, 'edk2_guids.py'))
        print('[*] Files {0}, {1} was successfully updated'.format(
            os.path.join(data_path, 'edk2_guids.conf'),
            os.path.join(data_path, 'edk2_guids.py'))
        )
        return True
    return False

def main():
    program = 'python ' + os.path.basename(__file__)
    parser = argparse.ArgumentParser(
        description='Get all UEFI PE-images',
		prog=program
    )
    parser.add_argument(
        'edk2_path', 
        type=str, 
        help='the path to EDK2 directory'
    )

    args = parser.parse_args()
    if get_guids_list(args.edk2_path, DATA_PATH):
        shutil.copyfile(
            os.path.join(DATA_PATH, 'edk2_guids.py'),
            os.path.join(IDA_GUIDS, 'edk2_guids.py')
        )
        shutil.copyfile(
            os.path.join(DATA_PATH, 'edk2_guids.py'),
            os.path.join(R2_GUIDS, 'edk2_guids.py')
        )
        print('[*] Files {0}, {1} was successfully updated'.format(
            os.path.join(DATA_PATH, 'edk2_guids.conf'),
            os.path.join(DATA_PATH, 'edk2_guids.py')
        ))

if __name__ == '__main__':
    main()
