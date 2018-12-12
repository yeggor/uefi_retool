import os
import json
import argparse
import r2pipe

from tools import utils

""" reads configuration data """
with open("config.json", "rb") as cfile:
	config = json.load(cfile)

pe_dir = config["PE_DIR"]

def print_info(module_path):
    r2 = r2pipe.open(module_path)
    r2.cmd("aaa")
    name = json.loads(r2.cmd("ij"))["core"]["file"]
    info = json.loads(r2.cmd("ij"))
    print("[*] " + name)
    print(json.dumps(info, indent=2))

def analyse_all():
	files = os.listdir(pe_dir)
	for module in files:
		if (module[len(module)-4:len(module):] == ".efi"):
			module_path = pe_dir + os.sep + module
			""" x64 only """
			if utils.get_machine_type(module_path) == utils.IMAGE_FILE_MACHINE_IA64:
				print_info(module_path)
			if utils.get_machine_type(module_path) == utils.IMAGE_FILE_MACHINE_I386:
				continue

if __name__=="__main__":
	analyse_all()