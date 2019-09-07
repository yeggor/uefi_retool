import os
import glob
import re
import argparse
import shutil
import click

DATA_PATH = "..{sep}conf".format(sep=os.sep)
IDA_GUIDS = "..{sep}ida_plugin{sep}uefi_analyser{sep}guids".format(sep=os.sep)
R2_GUIDS = "..{sep}r2_uefi_re{sep}guids".format(sep=os.sep)

def get_py(string):
    new_string = "edk2_guids = {\n"
    replace_table = {
        "{"     : "[",
        "}"     : "]",
        "#"     : "\t#",
        "="     : ":",
        "]\n"   : "],\n",
    }

    re_table = {
        r"\ng"     : "\n\t'g",
        r" +:"     : ":",
        r":"       : "' :",
        r"\]\]"    : "]",
        r"\] +\]"  : "]",
        r", +\["   : ",",
        r",\["     : ","
    }

    for key in replace_table:
        string = string.replace(key, replace_table[key])
    new_string += string + "}"
    for regexp in re_table:
        new_string = re.sub(re.compile(regexp), re_table[regexp], new_string)
    return new_string

def get_guids_list(edk2_path, data_path):
    if os.path.isdir(edk2_path) == 0:
        print("[-] Error, check edk2 path")
        return False
    dec_files = glob.glob(edk2_path + "{sep}*{sep}*.dec".format(sep=os.sep))
    if len(dec_files) == 0:
        print("[-] Error, *.dec files list is empty")
        return False
    if os.path.isdir(DATA_PATH) == False:
        os.mkdir(DATA_PATH)
    regexp = re.compile(r"g.+=.+{.+}")
    conf_content = ""
    for dec_file in dec_files:
        with open(dec_file, "rb") as dec:
            guids_list = re.findall(regexp, dec.read())
            conf_content += "# Guids from {dec_file} file \n".format(dec_file=dec_file)
            for guid in guids_list:
                conf_content += guid + "\n"
    with open(DATA_PATH + os.sep + "edk2_guids.conf", "wb") as conf:
        conf.write("# This file was automatically generated with update_edk2_guids.py script\n")
        conf.write(conf_content)
    py_content = get_py(conf_content)
    with open(DATA_PATH + os.sep + "edk2_guids.py", "wb") as conf:
        conf.write("# This file was automatically generated with update_edk2_guids.py script\n")
        conf.write(py_content)
    return True

def update(edk2_path, data_path, guids_path):
    if get_guids_list(edk2_path, data_path):
        shutil.copy(data_path + os.sep + "edk2_guids.py", guids_path + os.sep + "edk2_guids.py")
        print("[*] Files {0}, {1} was successfully updated"
        .format(data_path + os.sep + "edk2_guids.conf", data_path + os.sep + "edk2_guids.py"))
        return True
    else:
        return False

def main():
    program = "python " + os.path.basename(__file__)
    parser = argparse.ArgumentParser(
        description="Get all UEFI PE-images",
		prog=program)
    parser.add_argument("edk2_path", 
        type=str, 
        help="the path to EDK2 directory")
    
    args = parser.parse_args()
    if get_guids_list(args.edk2_path, DATA_PATH):
        shutil.copyfile(DATA_PATH + os.sep + "edk2_guids.py", IDA_GUIDS + os.sep + "edk2_guids.py")
        shutil.copyfile(DATA_PATH + os.sep + "edk2_guids.py", R2_GUIDS + os.sep + "edk2_guids.py")
        print("[*] Files {0}, {1} was successfully updated"
        .format(DATA_PATH + os.sep + "edk2_guids.conf", DATA_PATH + os.sep + "edk2_guids.py"))

if __name__=="__main__":
    main()