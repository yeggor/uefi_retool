import os
import sys
import json
import argparse
import uefi_firmware
from glob import glob
import click

from tools import utils
from tools.get_efi_images import get_efi_images
from tools.update_edk2_guids import update


""" reads configuration data """
with open("config.json", "rb") as cfile:
	config = json.load(cfile)

dump_dir = config["DUMP_DIR"]
pe_dir = config["PE_DIR"]
ida64_path = '"%s"' % config["IDA64_PATH"]

def show_item(item):
	return "current module: %s" % item

def analyse_all(scr_name):
	log_path = "log" + os.sep + "result_" + scr_name.replace(".py", ".log")
	if os.path.isfile(log_path):
		os.remove(log_path)
	files = os.listdir(pe_dir)
	with click.progressbar(files,
						length=len(files),
						bar_template=click.style("%(label)s  %(bar)s | %(info)s", fg="cyan"),
						label="Modules analysis",
						item_show_func=show_item,
						) as bar:
		for module in bar:
			if module.find(".i64") == -1 and module.find(".idb") == -1:
				module_path = pe_dir + os.sep + module
				""" x64 only """
				if utils.get_machine_type(module_path) == utils.IMAGE_FILE_MACHINE_IA64:
					if (os.system(ida64_path + ' -c -A -Sida_uefi_re' + os.sep + scr_name + " " + module_path) != 0):
						exit("[-] Error, check your config.json file")
				if utils.get_machine_type(module_path) == utils.IMAGE_FILE_MACHINE_I386:
					continue

def main():
	click.echo(click.style("UEFI_RETool", fg="cyan"))
	click.echo(click.style("A tool for full UEFI firmware analysis using IDA Pro", fg="cyan"))
	click.echo(click.style("Copyright (c) 2018 yeggor", fg="cyan"))
	program = "python " + os.path.basename(__file__)
	parser = argparse.ArgumentParser(prog=program)
	parser.add_argument("firmware_path",
						type=str,
						help="the path to your UEFI firmware for analysis")
	parser.add_argument("--all",
						action="store_true", 
						help="""analyse all UEFI firmware modules
						and output information to .{0}log{0}result_log_all.md file
						(example: python analyse_fw.py --all <firmware_path>)"""
						.format(os.sep))
	parser.add_argument("--pp_guids", 
						action="store_true", 
						help="""analyse all UEFI firmware modules
						and write a table with proprietry protocols
						to .{0}log{0}result_pp_guids.md file
						(example: python analyse_fw.py --pp_guids <firmware_path>)"""
						.format(os.sep))
	parser.add_argument("--get_efi_images", 
						action="store_true", 
						help="""get all UEFI firmware images
						(images are store in .{0}modules directory, 
						example: python analyse_fw.py --get_efi_images <firmware_path>)"""
						.format(os.sep))
	parser.add_argument("--update_edk2_guids", 
						metavar="EDK2_PATH", 
						type=str, 
						help="""update list of GUIDs from EDK2 
						(example: git clone https://github.com/tianocore/edk2,
						python --update_edk2_guids edk2)""")
	args = parser.parse_args()
	help_msg = True

	if (args.all and os.path.isfile(args.firmware_path)):
#		get_efi_images(args.firmware_path)
		analyse_all("log_all.py")
		print("Check .{0}log{0}result_log_all.md file".format(os.sep))
		help_msg = False
	
	if (args.pp_guids and os.path.isfile(args.firmware_path)):
		get_efi_images(args.firmware_path)
		analyse_all("log_pp_guids.py")
		print("Check .{0}log{0}result_pp_guids.md file".format(os.sep))
		help_msg = False
	
	if (args.get_efi_images and os.path.isfile(args.firmware_path)):
		get_efi_images(args.firmware_path)
		print("Check .{0}modules directory".format(os.sep))
		help_msg = False
	
	if (args.update_edk2_guids):
		edk2_path = args.update_edk2_guids
		if os.path.isdir(edk2_path):
			data_path = "conf"
			guids_path = "ida_uefi_re{0}guids".format(os.sep)
			update(edk2_path, data_path, guids_path)
			help_msg = False

	if help_msg:
		parser.print_help()

if __name__=="__main__":
	main()