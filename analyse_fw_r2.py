import os
import json
import r2pipe
import click
import time
import argparse

from tools import utils
from tools.get_efi_images import get_efi_images
from r2_uefi_re import module_info
from r2_uefi_re.analyser import Analyser

""" reads configuration data """
with open("config.json", "rb") as cfile:
	config = json.load(cfile)

pe_dir = config["PE_DIR"]

def analyse_all():
	if os.path.isdir(pe_dir) == 0:
		return False
	files = os.listdir(pe_dir)
	for module in files:
		if (
			module.find(".idb") == -1 and module.find(".i64") == -1 and \
			module.find(".id1") == -1 and module.find(".id2") == -1 and \
			module.find(".nam") == -1 and module.find(".til") == -1
		):
			module_path = pe_dir + os.sep + module
			try:
				""" print all """
				print("\n[*] current module: {module}".format(module=module_path))
				analyser = Analyser(module_path)
				analyser.get_boot_services()
				print("\r\nBoot services:")
				analyser.list_boot_services()
				analyser.get_protocols()
				analyser.get_prot_names()
				data = analyser.Protocols["All"]
				print("\r\nProtocols:")
				if len(data) == 0:
					print(" * list is empty")
				for element in data:
					guid_str = "[guid] " + str(map(hex, element["guid"]))
					print("\t [address] " + hex(element["address"]))
					print("\t [service] " + element["service"])
					print("\t [protocol_name] " + element["protocol_name"])
					print("\t [protocol_place] " + element["protocol_place"])
					print("\t " + guid_str)
					print("\t " + "*" * len(guid_str))
				time.sleep(0.01)
				""" --------- """
			except Exception:
				print("[-] ERROR")
				continue

def main():
	click.echo(click.style("UEFI_RETool", fg="cyan"))
	click.echo(click.style("A tool for full UEFI firmware analysis using radare2", fg="cyan"))
	click.echo(click.style("Copyright (c) 2018 yeggor", fg="cyan"))
	start_time = time.time()
	program = "python " + os.path.basename(__file__)
	parser = argparse.ArgumentParser(prog=program)
	parser.add_argument("firmware_path",
		type=str,
		help="the path to your UEFI firmware for analysis")
	args = parser.parse_args()
	
	get_efi_images(args.firmware_path)
	analyse_all()
	print("[*] spent time: {time} sec.".format(time=str((time.time() - start_time))))

if __name__=="__main__":
	main()