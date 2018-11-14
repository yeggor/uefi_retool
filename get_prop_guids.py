import uefi_firmware
from glob import glob
from os import path
import os
import sys

from tools.parse_firmware import Dumper

fw_path = "fw.bin"
dump_dir = "all"

pe_dir = "modules"
ida_path = '"C:\\Program Files\\IDA 7.0\\ida.exe"'
ida64_path = '"C:\\Program Files\\IDA 7.0\\ida64.exe"'

LOG = False

def analyse_all():
	if LOG and path.isfile("result.log"):
		os.system("DEL result.log")
	files = os.listdir(pe_dir)
	for module in files:
		if module.find(".i64") >= 0 | module.find(".idb") >= 0:
			continue
		module_path = pe_dir + "\\" + module
		print("[*] current module: " + module)
		if LOG:
			with open("result.log", "ab") as log:
				log.write(b"\r\n" + b"=" * 60)
				log.write(b"\r\n" + module_path)
				log.write(b"\r\n" + b"=" * 60)
		os.system(ida64_path + ' -c -A -Sprop_guids\\prop_guids.py ' + module_path)


def get_efi_images(fw_path, dump_dir, pe_dir):
	pe_dump = Dumper(fw_path, dump_dir, pe_dir)
	pe_dump.get_pe_files()
	return True

def main():
	get_efi_images(fw_path, dump_dir, pe_dir)
	analyse_all()

if __name__=="__main__":
	main()