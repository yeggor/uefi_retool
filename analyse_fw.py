import uefi_firmware
from glob import glob
from os import path
import os
import sys

from tools.get_efi_images import get_efi_images

fw_path = "fw.bin"
dump_dir = "all"

pe_dir = "modules"
ida_path = '"C:\\Program Files\\IDA 7.0\\ida.exe"'
ida64_path = '"C:\\Program Files\\IDA 7.0\\ida64.exe"'

LOG = True

def analyse_all(scr_name):
	log_path = "log\\result_" + scr_name.replace(".py", ".log") 
	if LOG and path.isfile(log_path):
		os.system("DEL " + log_path)
	files = os.listdir(pe_dir)
	for module in files:
		if module.find(".i64") >= 0 | module.find(".idb") >= 0:
			continue
		module_path = pe_dir + "\\" + module
		print("[*] current module: " + module)
		if LOG:
			with open(log_path, "ab") as log:
				pref = "========== START: " + module_path + " "
				pref += "=" * (60 - len(pref))
				log.write(b"\r\n" + pref)
		os.system(ida64_path + ' -c -A -Sida_uefi_re\\' + scr_name + " " + module_path)

def main():
	get_efi_images(fw_path)
	analyse_all("prop_guids.py")

if __name__=="__main__":
	main()