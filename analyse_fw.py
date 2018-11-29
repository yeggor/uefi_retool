import uefi_firmware
from glob import glob
from os import path
import os
import sys
import json
import argparse
import colorama

# x64 only
"""
from tools import utils
"""
from tools.get_efi_images import get_efi_images
from tools.update_edk2_guids import update

with open("config.json", "rb") as cfile:
	config = json.load(cfile)

fw_path = config["FW_PATH"]
dump_dir = config["DUMP_DIR"]
pe_dir = config["PE_DIR"]

# x64 only
"""
ida_path = '"%s"' % config["IDA_PATH"]
"""
ida64_path = '"%s"' % config["IDA64_PATH"]


def analyse_all(scr_name):
	print(colorama.Style.RESET_ALL + colorama.Fore.CYAN)
	log_path = "log\\result_" + scr_name.replace(".py", ".log")
	if path.isfile(log_path):
		os.system("DEL " + log_path)
	files = os.listdir(pe_dir)
	for module in files:
		if module.find(".i64") == -1 and module.find(".idb") == -1:
			module_path = pe_dir + "\\" + module
			# x64 only
			"""
			if utils.get_machine_type(module_path) == utils.IMAGE_FILE_MACHINE_IA64:
				print("[*] current module: " + module)
				os.system(ida64_path + ' -c -A -Sida_uefi_re\\' + scr_name + " " + module_path)
			if utils.get_machine_type(module_path) == utils.IMAGE_FILE_MACHINE_I386:
				print("[*] current module: " + module)
				os.system(ida_path + ' -c -A -Sida_uefi_re\\' + scr_name + " " + module_path)
			"""
			print("[*] current module: " + module)
			os.system(ida64_path + ' -c -A -Sida_uefi_re\\' + scr_name + " " + module_path)
	print(colorama.Style.RESET_ALL)


def main():
	colorama.init()
	
	print(colorama.Fore.MAGENTA)
	print("UEFI_RETool")
	print("A tool for full UEFI firmware analysis using IDA Pro")
	print("Copyright (c) 2018 yeggor")
	print(colorama.Style.RESET_ALL)
	program = "python " + os.path.basename(__file__)
	parser = argparse.ArgumentParser(prog=program)
	parser.add_argument("--fw_path", type=str, help="path to your UEFI firmware for analysis (default path: .\\fw.bin)", default=fw_path)
	parser.add_argument("--all", action="store_true", help="""analyse all firmware's modules
						and output information to file .\\log\\result_log_all.md
						(example: {0}python analyse_fw.py --all --fw_path <FW_PATH>{1})""".format(colorama.Fore.CYAN, colorama.Style.RESET_ALL))
	parser.add_argument("--pp_guids", action="store_true", help="""analyse all firmware's modules
						and output a table with GUIDs of proprietry protocols 
						to file .\\log\\result_pp_guids.md
						(example: {0}python analyse_fw.py --pp_guids --fw_path <FW_PATH>{1})""".format(colorama.Fore.CYAN, colorama.Style.RESET_ALL))
	parser.add_argument("--get_efi_images", action="store_true", help="""get all UEFI firmware images and exit 
						(images are store in .\\modules directory, 
						example: {0}python analyse_fw.py --get_efi_images --fw_path <FW_PATH>{1})""".format(colorama.Fore.CYAN, colorama.Style.RESET_ALL))
	parser.add_argument("--update_edk2_guids", metavar="EDK2_PATH", type=str, help="""update list of GUIDs from EDK2 
						(example: {0}git clone https://github.com/tianocore/edk2{1}, 
						{0}python --update_edk2_guids edk2{1})""".format(colorama.Fore.CYAN, colorama.Style.RESET_ALL))
	args = parser.parse_args()
	help_msg = True

	print(colorama.Fore.CYAN)

	if (args.all and os.path.isfile(args.fw_path)):
		get_efi_images(args.fw_path)
		analyse_all("log_all.py")
		print("{0}Check .\\log\\result_log_all.md file{1}".format(colorama.Fore.MAGENTA, colorama.Style.RESET_ALL))
		help_msg = False
	
	if (args.pp_guids and os.path.isfile(args.fw_path)):
		get_efi_images(args.fw_path)
		analyse_all("log_pp_guids.py")
		print("{0}Check .\\log\\result_pp_guids.md file{1}".format(colorama.Fore.MAGENTA, colorama.Style.RESET_ALL))
		help_msg = False
	
	if (args.get_efi_images and os.path.isfile(args.fw_path)):
		get_efi_images(args.fw_path)
		print("{0}Check .\\modules directory{1}".format(colorama.Fore.MAGENTA, colorama.Style.RESET_ALL))
		help_msg = False
	
	if (args.update_edk2_guids):
		edk2_path = args.update_edk2_guids
		if os.path.isdir(edk2_path):
			data_path = "conf"
			guids_path = "ida_uefi_re\\guids"
			update(edk2_path, data_path, guids_path)
			help_msg = False
	
	print(colorama.Style.RESET_ALL)
	if help_msg:
		parser.print_help()


if __name__=="__main__":
	main()