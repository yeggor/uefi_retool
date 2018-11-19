import uefi_firmware
from glob import glob
from os import path
import os
import sys
import json

from tools.get_efi_images import get_efi_images

IMAGE_FILE_MACHINE_IA64 = 0x8664
IMAGE_FILE_MACHINE_I386 = 0x014c
PE_OFFSET = 0x3c

with open("config.json", "rb") as cfile:
	config = json.load(cfile)

fw_path = config["FW_PATH"]
dump_dir = config["DUMP_DIR"]
pe_dir = config["PE_DIR"]
ida_path = '"%s"' % config["IDA_PATH"]  
ida64_path = '"%s"' % config["IDA64_PATH"]

def get_num_le(bytearr):
	num_le = 0
	for i in range(len(bytearr)):
		num_le += ord(bytearr[i]) * pow(256, i)
	return num_le

def get_machine_type(module_path):
	with open(module_path, "rb") as module:
		data = module.read()
	PE_POINTER = get_num_le(data[PE_OFFSET:PE_OFFSET+1:])
	FH_POINTER = PE_POINTER + 4
	machine_type = data[FH_POINTER:FH_POINTER+2:]
	type_value = get_num_le(machine_type)
	return type_value

def analyse_all(scr_name):
	log_path = "log\\result_" + scr_name.replace(".py", ".log")
	if path.isfile(log_path):
		os.system("DEL " + log_path)
	files = os.listdir(pe_dir)
	for module in files:
		if module.find(".i64") == -1 and module.find(".idb") == -1:
			module_path = pe_dir + "\\" + module
			if get_machine_type(module_path) == IMAGE_FILE_MACHINE_IA64:
				print("[*] current module: " + module)
				os.system(ida64_path + ' -c -A -Sida_uefi_re\\' + scr_name + " " + module_path)
			if get_machine_type(module_path) == IMAGE_FILE_MACHINE_I386:
				print("[*] current module: " + module)
				os.system(ida_path + ' -c -A -Sida_uefi_re\\' + scr_name + " " + module_path)

def main():
	get_efi_images(fw_path)
	analyse_all("log_all.py")

if __name__=="__main__":
	main()