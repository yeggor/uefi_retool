import os
import json
import r2pipe
import click
import argparse

def print_info(module_path):
    r2 = r2pipe.open(module_path)
    name = json.loads(r2.cmd("ij"))["core"]["file"]
    info = json.loads(r2.cmd("ij"))
    print("[*] " + name)
    print(json.dumps(info, indent=2))

def test(module_path):
    r2 = r2pipe.open(module_path)
    r2.cmd("aa")
    json.loads(r2.cmd("ij"))["core"]["file"]
    json.loads(r2.cmd("ij"))
    """
    ...
    """

if __name__=="__main__":
    click.echo(click.style("Copyright (c) 2018 yeggor", fg="cyan"))
    program = "python " + os.path.basename(__file__)
    parser = argparse.ArgumentParser(description="Print info about UEFi module",
		prog=program)
    parser.add_argument("module", 
		type=str, 
		help="the path to UEFI module")
    args = parser.parse_args()
    print_info(args.module)
