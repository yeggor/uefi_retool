IMAGE_FILE_MACHINE_IA64 = 0x8664
IMAGE_FILE_MACHINE_I386 = 0x014c
PE_OFFSET = 0x3c

def get_num_le(bytearr):
	num_le = 0
	for i in range(len(bytearr)):
		num_le += ord(bytearr[i]) * pow(256, i)
	return num_le

def get_machine_type(module_path):
	with open(module_path, "rb") as module:
		data = module.read()
	PE_POINTER = get_num_le(data[PE_OFFSET:PE_OFFSET+1:])
	FH_POINTER = PE_POINTER + 4
	machine_type = data[FH_POINTER:FH_POINTER+2:]
	type_value = get_num_le(machine_type)
	return type_value