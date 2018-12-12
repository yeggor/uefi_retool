import os
import json
import r2pipe
import click
import argparse

class Analyser():
    def __init__(self, module_path):
        self.module_path = module_path
        self.r2 = r2pipe.open(module_path)
    
    def get_info(self):
        info = json.loads(self.r2.cmd("ij"))
        return json.dumps(info, indent=2)
    
    """ 
    format: {
        func_name: func_address,
        ...
    } 
    """
    def get_funcs(self):
        funcs = {}
        self.r2.cmd("aaa")
        json_funcs = json.loads(self.r2.cmd("aflj"))
        if len(json_funcs) == 0:
            return {}
        for func_info in json_funcs:
            funcs[func_info["name"]] = func_info["offset"]
        return funcs

if __name__=="__main__":
    click.echo(click.style("Copyright (c) 2018 yeggor", fg="cyan"))
    program = "python " + os.path.basename(__file__)
    parser = argparse.ArgumentParser(description="UEFi module analyser",
		prog=program)
    parser.add_argument("module", 
		type=str, 
		help="the path to UEFI module")
    args = parser.parse_args()
    analyser = Analyser(args.module)
    print analyser.get_funcs()