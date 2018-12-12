import os
import json
import r2pipe
import click
import time

from tools import utils
from r2_uefi_re import module_info

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
				module_info.test(module_path)
				print("[*] current module: {module}".format(module=module_path))
				time.sleep(0.01)
			except Exception:
				continue

def main():
	click.echo(click.style("UEFI_RETool", fg="cyan"))
	click.echo(click.style("A tool for full UEFI firmware analysis using radare2", fg="cyan"))
	click.echo(click.style("Copyright (c) 2018 yeggor", fg="cyan"))
	start_time = time.time()
	analyse_all()
	print("[*] spent time: {time} sec.".format(time=str((time.time() - start_time))))

if __name__=="__main__":
	main()