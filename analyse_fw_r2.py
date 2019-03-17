import os
import json
import r2pipe
import click
import argparse

from tools import utils
from tools.get_efi_images import get_efi_images
from tools.update_edk2_guids import update
from r2_uefi_re.analyser import Analyser

LOG_FILE_ALL = "log{sep}r2_log_all.md".format(sep=os.sep)
LOG_FILE_PP_GUIDS = "log{sep}r2_log_pp_guids.md".format(sep=os.sep)

""" reads configuration data """
with open("config.json", "rb") as cfile:
	config = json.load(cfile)

pe_dir = config["PE_DIR"]

def show_item(item):
	return "current module: %s" % item

def analyse_all():
	log = open(LOG_FILE_ALL, "ab")
	if os.path.isdir(pe_dir) == 0:
		return False
	files = os.listdir(pe_dir)
	with click.progressbar(
		files,
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
						try:
							log.write("## Module: {module}\r\n".format(module=module))
							analyser = Analyser(module_path)
							analyser.get_boot_services()
							""" list boot services"""
							log.write("### Boot services:\r\n")
							empty = False
							for service in analyser.gBServices:
								for address in analyser.gBServices[service]:
									empty = True
									log.write("* [{0}] EFI_BOOT_SERVICES->{1}\r\n".format(hex(address).replace("L", ""), service))
							if (empty == False):
								log.write("* empty\r\n")
							""" list protocols information """
							analyser.get_protocols()
							analyser.get_prot_names()
							data = analyser.Protocols["All"]
							log.write("### Protocols:\r\n")
							if (len(data) == 0):
								log.write("* empty\r\n")
							for element in data:
								guid_str = "[guid] " + str(map(hex, element["guid"])).replace("L", "").replace("'", "")
								log.write("* [{0}]\r\n".format(hex(element["address"]).replace("L", "")))
								log.write("\t - [service] " + element["service"] + "\r\n")
								log.write("\t - [protocol_name] " + element["protocol_name"] + "\r\n")
								log.write("\t - [protocol_place] " + element["protocol_place"] + "\r\n")
								log.write("\t - " + guid_str + "\r\n")
						except:
							log.write("### ERROR\r\n")
							continue
	log.close()

def get_table_line(guid, module, service, address):
    line =  "| " + guid + " "
    line += "| " + module + " "
    line += "| " + service + " "
    line += "| " + address + " "
    line += "|"
    return line

def get_pp_guids():
	log = open(LOG_FILE_PP_GUIDS, "ab")
	if os.path.getsize(LOG_FILE_PP_GUIDS) == 0:
		log.write(get_table_line("Guid", "Module", "Service", "Address") + "\r\n")
		log.write(get_table_line("---", "---", "---", "---") + "\r\n")
	
	if os.path.isdir(pe_dir) == 0:
		return False
	files = os.listdir(pe_dir)
	with click.progressbar(
		files,
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
					try:
						analyser = Analyser(module_path)
						analyser.get_boot_services()
						analyser.get_protocols()
						analyser.get_prot_names()

						for protocol_record in analyser.Protocols["All"]:
							if (protocol_record["protocol_name"] == "ProprietaryProtocol"):
								guid = str(map(hex, protocol_record["guid"]))
								guid = guid.replace("L", "").replace("'", "")
								service = protocol_record["service"]
								address = hex(protocol_record["address"])
								address = address.replace("L", "")
								log.write(get_table_line(guid, module, service, address) + "\r\n")
					except:
						continue
	log.close()

def get_pp_guids_num():
	full_guids_num = 0
	pp_guids_num = 0
	if os.path.isdir(pe_dir) == 0:
		return False
	files = os.listdir(pe_dir)
	with click.progressbar(
		files,
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
					try:
						analyser = Analyser(module_path)
						analyser.get_boot_services()
						analyser.get_protocols()
						analyser.get_prot_names()
						full_guids_num += len(analyser.Protocols["All"])
						pp_guids_num += len(analyser.Protocols["PropGuids"])
					except:
						continue
	print("\t [number of proprietary protocols] {0}".format(pp_guids_num))
	print("\t [full number of protocols] {0}".format(full_guids_num))

def clear(dirname):
	for root, dirs, files in os.walk(dirname, topdown=False):
		for name in files:
			os.remove(os.path.join(root, name))
		for name in dirs:
			os.rmdir(os.path.join(root, name))

def clear_all():
	try:
		clear(config["DUMP_DIR"])
		clear(config["PE_DIR"])
	except:
		print("Error while cleaning directories")

def main():
	click.echo(click.style("UEFI_RETool", fg="cyan"))
	click.echo(click.style("A tool for UEFI firmware analysis with radare2", fg="cyan"))
	program = "python " + os.path.basename(__file__)
	parser = argparse.ArgumentParser(prog=program)
	parser.add_argument("firmware_path",
		type=str,
		help="the path to UEFI firmware for analysis")
	parser.add_argument("--all",
		action="store_true",
		help="""analyse of all UEFI firmware modules
		and out information to .{sep}log{sep}r2_log_all.md file
		(example: python analyse_fw_r2.py --all <firmware_path>)"""
		.format(sep=os.sep))
	parser.add_argument("--pp_guids", 
		action="store_true",
		help="""analyse all UEFI firmware modules
		and write a table with proprietry protocols
		to .{sep}log{sep}r2_pp_guids.md file
		(example: python analyse_fw_r2.py --pp_guids <firmware_path>)"""
		.format(sep=os.sep))
	parser.add_argument("--pp_guids_num", 
		action="store_true",
		help="""analyse all UEFI firmware modules and 
		get number of proprietry protocols
		(example: python analyse_fw_r2.py --pp_guids_num <firmware_path>)"""
		.format(sep=os.sep))
	parser.add_argument("--get_efi_images", 
		action="store_true",
		help="""get all executable images from UEFI firmware
		(images are stores in .{sep}modules directory, 
		example: python analyse_fw_r2.py --get_efi_images <firmware_path>)"""
		.format(sep=os.sep))
	parser.add_argument("--update_edk2_guids", 
		metavar="EDK2_PATH", 
		type=str, 
		help="""update list of GUIDs from EDK2
		(example: git clone https://github.com/tianocore/edk2,
		python analyse_fw_r2.py --update_edk2_guids edk2)""")
	
	args = parser.parse_args()
	
	if (args.all and os.path.isfile(args.firmware_path)):
		clear_all()
		get_efi_images(args.firmware_path)
		""" log all information """
		analyse_all()
		clear_all()
	
	if (args.pp_guids and os.path.isfile(args.firmware_path)):
		clear_all()
		get_efi_images(args.firmware_path)
		""" log proprietary protocols list """
		get_pp_guids()
		clear_all()
	
	if (args.pp_guids_num and os.path.isfile(args.firmware_path)):
		clear_all()
		get_efi_images(args.firmware_path)
		""" print number of proprietary protocols  """
		get_pp_guids_num()
		clear_all()

	if (args.get_efi_images and os.path.isfile(args.firmware_path)):
		clear_all()
		get_efi_images(args.firmware_path)
		print("Check .{sep}modules directory".format(sep=os.sep))
	
	if (args.update_edk2_guids):
		edk2_path = args.update_edk2_guids
		if os.path.isdir(edk2_path):
			data_path = "conf"
			guids_path = "r2_uefi_re{sep}guids".format(sep=os.sep)
			update(edk2_path, data_path, guids_path)

if __name__=="__main__":
	main()