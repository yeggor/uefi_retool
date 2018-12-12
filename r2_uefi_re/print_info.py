import os
import json
import r2pipe

def print_info(module_path):
    r2 = r2pipe.open(module_path)
    r2.cmd("aaa")
    name = json.loads(r2.cmd("ij"))["core"]["file"]
    info = json.loads(r2.cmd("ij"))
    print("[*] " + name)
    print(json.dumps(info, indent=2))

if __name__=="__main__":
    pass