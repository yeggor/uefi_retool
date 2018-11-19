import sys
import os
from os import path
import glob
import re

DATA_PATH = "..\\conf"
GUIDS = "..\\ida\\guids"

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


def get_guids_list(edk2_path):
    if path.isdir(edk2_path) == 0:
        print("[-] Error, check edk2 path")
        return False
    dec_files = glob.glob(edk2_path + "\\*\\*.dec")
    if len(dec_files) == 0:
        print("[-] Error, *.dec files list is empty")
        return False
    if path.isdir(DATA_PATH) == False:
        os.system("MKDIR " + DATA_PATH)
    regexp = re.compile(r"g.+=.+{.+}")
    conf_content = ""
    for dec_file in dec_files:
        with open(dec_file, "rb") as dec:
            guids_list = re.findall(regexp, dec.read())
            conf_content += "# Guids from {0} file \n".format(dec_file)
            for guid in guids_list:
                conf_content += guid + "\n"
    with open(DATA_PATH + "\\edk2_guids.conf", "wb") as conf:
        conf.write("# This file was automatically generated with update_edk2_guids.py script\n")
        conf.write(conf_content)
    py_content = get_py(conf_content)
    with open(DATA_PATH + "\\edk2_guids.py", "wb") as conf:
        conf.write("# This file was automatically generated with update_edk2_guids.py script\n")
        conf.write(py_content)
    return True

def update(edk2_path):    
    if get_guids_list(edk2_path):
        return True
    else:
        return False

def main():
    if len(sys.argv) != 2:
        print("[*] Usage: $python {0} <EDK2_PATH>".format(sys.argv[0]))
        return False
    if get_guids_list(sys.argv[1]):
        os.system("COPY " + DATA_PATH + "\\edk2_guids.py " + GUIDS + "\\edk2_guids.py")
        print("[*] Files {0}, {1} was successfully updated".format(DATA_PATH + "\\edk2_guids.conf", DATA_PATH + "\\edk2_guids.py"))
        return True
    else:
        return False
    

if __name__=="__main__":
    main()