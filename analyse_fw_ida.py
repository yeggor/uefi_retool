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
	log_path = "log" + os.sep + "ida_" + scr_name.replace(".py", ".log")
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
			if (
				module.find(".idb") == -1 and module.find(".i64") == -1 and \
				module.find(".id1") == -1 and module.find(".id2") == -1 and \
				module.find(".nam") == -1 and module.find(".til") == -1
			):
				module_path = pe_dir + os.sep + module
				""" x64 only """
				machine_type = utils.get_machine_type(module_path)
				if machine_type == utils.IMAGE_FILE_MACHINE_IA64:
					if (os.system(ida64_path + ' -c -A -Sida_uefi_re' + os.sep + scr_name + " " + module_path) != 0):
						exit("[-] Error, check your config.json file")

def clear(dirname):
	for root, dirs, files in os.walk(dirname, topdown=False):
		for name in files:
			os.remove(os.path.join(root, name))
		for name in dirs:
			os.rmdir(os.path.join(root, name))

def clear_all():
	clear(config["DUMP_DIR"])
	clear(config["PE_DIR"])

def main():
	click.echo(click.style("UEFI_RETool", fg="cyan"))
	click.echo(click.style("A tool for UEFI firmware analysis with IDA Pro", fg="cyan"))
	program = "python " + os.path.basename(__file__)
	parser = argparse.ArgumentParser(prog=program)
	parser.add_argument("firmware_path",
		type=str,
		help="path to UEFI firmware for analysis")
	parser.add_argument("--all",
		action="store_true",
		help="""analyse of all UEFI firmware modules
		and output of information to .{sep}log{sep}ida_log_all.md file
		(example: python analyse_fw_ida.py --all <firmware_path>)"""
		.format(sep=os.sep))
	parser.add_argument("--pp_guids", 
		action="store_true",
		help="""analyse all UEFI firmware modules
		and save a table with proprietry protocols
		to .{sep}log{sep}ida_pp_guids.md file
		(example: python analyse_fw_ida.py --pp_guids <firmware_path>)"""
		.format(sep=os.sep))
	parser.add_argument("--get_efi_images", 
		action="store_true",
		help="""get all executable images from UEFI firmware
		(images are stored in .{sep}modules directory, 
		example: python analyse_fw_ida.py --get_efi_images <firmware_path>)"""
		.format(sep=os.sep))
	parser.add_argument("--update_edk2_guids", 
		metavar="EDK2_PATH", 
		type=str, 
		help="""update list of GUIDs from EDK2
		(example: git clone https://github.com/tianocore/edk2,
		python analyse_fw_ida.py --update_edk2_guids edk2)""")
	
	args = parser.parse_args()

	if (args.all and os.path.isfile(args.firmware_path)):
		clear_all()
		get_efi_images(args.firmware_path)
		analyse_all("log_all.py")
		print("Check .{sep}log{sep}ida_log_all.md file".format(sep=os.sep))
		clear_all()
	
	if (args.pp_guids and os.path.isfile(args.firmware_path)):
		clear_all()
		get_efi_images(args.firmware_path)
		analyse_all("log_pp_guids.py")
		print("Check .{sep}log{sep}ida_pp_guids.md file".format(sep=os.sep))
		clear_all()
	
	if (args.get_efi_images and os.path.isfile(args.firmware_path)):
		clear_all()
		get_efi_images(args.firmware_path)
		print("Check .{sep}modules directory".format(sep=os.sep))
	
	if (args.update_edk2_guids):
		edk2_path = args.update_edk2_guids
		if os.path.isdir(edk2_path):
			data_path = "conf"
			guids_path = "ida_uefi_re{sep}guids".format(sep=os.sep)
			update(edk2_path, data_path, guids_path)
	
if __name__=="__main__":
	main()