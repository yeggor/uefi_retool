import uefi_firmware
from glob import glob
from os import path
import os

def get_files(directory_name, pe_dir):
	if path.isdir(pe_dir) == False:
		os.system("MKDIR " + pe_dir)
	files = os.listdir(directory_name)
	for obj in files:
		if path.isfile(directory_name + "\\" + obj):
			if obj[len(obj)-3:len(obj):] == ".pe":
				if len(glob(directory_name + "\\*.ui")) == 1:
					ui_path = glob(directory_name + "\\*.ui")[0]
					with open(ui_path, "rb") as ui:
						pe_name = ui.read().replace(b"\x00", b"")
					os.system("COPY {0} {1}".format(directory_name + "\\" + obj, pe_dir + "\\" + pe_name))
					print("[*] " + directory_name + "\\" + obj + " ---> " + pe_dir + "\\" + pe_name)
		if path.isdir(directory_name + "\\" + obj):
			get_files(directory_name + "\\" + obj, pe_dir)
	return True

class Dumper():
	def __init__(self, fw_name, dir_name, pe_dir):
		self.fw_name = fw_name
		self.dir_name = dir_name
		self.pe_dir = pe_dir
		if path.isdir(self.dir_name) == False:
			os.system("MKDIR " + self.dir_name)
		if path.isdir(self.pe_dir) == False:
			os.system("MKDIR " + self.pe_dir)
	
	def dump_all(self):
		if path.isfile(self.fw_name) == False:
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
