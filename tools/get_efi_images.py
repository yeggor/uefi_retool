import sys
import uefi_firmware
from glob import glob
import shutil
import os
import argparse
import click
import colorama

dir_name = "all"
pe_dir = "modules"

def get_files(directory_name, pe_dir):
	if os.path.isdir(pe_dir) == False:
		os.mkdir(pe_dir)
	files = os.listdir(directory_name)
	with click.progressbar(files,
		length=len(files),
		bar_template=click.style("%(label)s  %(bar)s | %(info)s", fg="cyan"),
		label="Obtaining UEFI images") as bar:
		for obj in bar:
			if os.path.isfile(directory_name + os.sep + obj):
				if obj[len(obj)-3:len(obj):] == ".pe":
					if len(glob(directory_name + os.sep + "*.ui")) == 1:
						ui_path = glob(directory_name + os.sep + "*.ui")[0]
						with open(ui_path, "rb") as ui:
							pe_name = ui.read().replace(b"\x00", b"")
						shutil.copy(directory_name + os.sep + obj, pe_dir + os.sep + pe_name)
			if os.path.isdir(directory_name + os.sep + obj):
				get_files(directory_name + os.sep + obj, pe_dir)
	return True

class Dumper():
	def __init__(self, fw_name, dir_name, pe_dir):
		self.fw_name = fw_name
		self.dir_name = dir_name
		self.pe_dir = pe_dir
		if os.path.isdir(self.dir_name) == False:
			os.mkdir(self.dir_name)
		if os.path.isdir(self.pe_dir) == False:
			os.mkdir(self.pe_dir)
	
	def dump_all(self):
		if os.path.isfile(self.fw_name) == False:
			print("[-] Check {0} file".format(self.fw_name))
			return False
		with open(self.fw_name, "rb") as fw:
			file_content = fw.read()
		parser = uefi_firmware.AutoParser(file_content)
		if parser.type() == "unknown":
			print("[-] This type of binary is not supported")
			return False
		firmware = parser.parse()
		firmware.dump(self.dir_name)
		return True

	def get_pe_files(self):
		get_files(self.dir_name, self.pe_dir)

def get_efi_images(fw_name):
	""" for correct color display in uefi_firmware module """
	colorama.init()
	dumper = Dumper(fw_name, dir_name, pe_dir)
	if (dumper.dump_all() == False):
		exit()
	dumper.get_pe_files()
	return True

def main():
	click.echo(click.style("Copyright (c) 2018 yeggor", fg="cyan"))
	""" for correct color display in uefi_firmware module """
	colorama.init()
	program = "python " + os.path.basename(__file__)
	parser = argparse.ArgumentParser(description="Get all UEFI PE-images",
		prog=program)
	parser.add_argument("firmware_path", 
		type=str, 
		help="the path to your UEFI firmware")
	parser.add_argument("--all_dir", 
		type=str, 
		help="the name of the directory containing all firmware items (default: 'all')", 
		default=dir_name)
	parser.add_argument("--pe_dir", 
		type=str, 
		help="the name of the directory containing all firmware PE-images (default: 'modules')", 
		default=pe_dir)
	args = parser.parse_args()
	
	dumper = Dumper(args.firmware_path, args.all_dir, args.pe_dir)
	if (dumper.dump_all() == False):
		exit()
	dumper.get_pe_files()

if __name__=="__main__":
	main()