import idautils
import idaapi
import idc

"""
definitions from PE file structure
"""
IMAGE_FILE_MACHINE_IA64 = 0x8664
IMAGE_FILE_MACHINE_I386 = 0x014c
PE_OFFSET = 0x3c
IMAGE_SUBSYSTEM_EFI_APPLICATION = 0xa
IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER = 0xb
IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER = 0xc

def set_hexrays_comment(address, text):
    """
    set comment in decompiled code
    """
    cfunc = idaapi.decompile(address)
    tl = idaapi.treeloc_t()
    tl.ea = address
    tl.itp = idaapi.ITP_SEMI
    cfunc.set_user_cmt(tl, text)
    cfunc.save_user_cmts()

def check_guid(address):
    """
    correctness is determined based on the number of unique bytes
    """
    return (len(set(idaapi.get_many_bytes(address, 16))) > 8)

def get_guid(address):
    """
    get GUID located by address
    """
    CurrentGUID = []
    CurrentGUID.append(idc.Dword(address))
    CurrentGUID.append(idc.Word(address + 4))
    CurrentGUID.append(idc.Word(address + 6))
    for addr in range(address + 8, address + 16, 1):
        CurrentGUID.append(idc.Byte(addr))
    return CurrentGUID

def get_num_le(bytearr):
    """
    translate a set of bytes into a number in the little endian format
    """
    num_le = 0
    for i in range(len(bytearr)):
        num_le += bytearr[i] * pow(256, i)
    return num_le

def get_machine_type(header):
    """
    get the architecture of the investigated file
    """
    if len(header) < PE_OFFSET + 1:
        return "unknown"
    PE_POINTER = header[PE_OFFSET]
    FH_POINTER = PE_POINTER + 4
    if len(header) < FH_POINTER + 3:
        return "unknown"
    machine_type = header[FH_POINTER:FH_POINTER+2:]
    type_value = get_num_le(machine_type)
    if type_value == IMAGE_FILE_MACHINE_I386:
        return "x86"
    if type_value == IMAGE_FILE_MACHINE_IA64:
        return "x64"
    return "unknown"

def check_subsystem(header):
    """
    get the subsystem of the investigated file
    """
    if len(header) < PE_OFFSET + 1:
        return False
    PE_POINTER = header[PE_OFFSET]
    if len(header) < PE_POINTER + 0x5d:
        return False
    subsystem = header[PE_POINTER + 0x5c]
    return (subsystem == IMAGE_SUBSYSTEM_EFI_APPLICATION or \
            subsystem == IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER or \
            subsystem == IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER)

def get_header_idb():
    """
    get file header from idb
    """
    if idc.SegName(0) == "HEADER":
        header = bytearray([idc.Byte(ea) for ea in range(0, idc.SegEnd(0))])
        return header
    return bytearray(b"")
