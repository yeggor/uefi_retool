import idautils
import idaapi
import idc

def set_hexrays_comment(address, text):
    cfunc = idaapi.decompile(address)
    tl = idaapi.treeloc_t()
    tl.ea = address
    tl.itp = idaapi.ITP_SEMI
    cfunc.set_user_cmt(tl, text)
    cfunc.save_user_cmts()

def get_guid(address):
    CurrentGUID = []
    CurrentGUID.append(idc.Dword(address))
    CurrentGUID.append(idc.Word(address + 4))
    CurrentGUID.append(idc.Word(address + 6))
    for addr in range(address + 8, address + 16, 1):
        CurrentGUID.append(idc.Byte(addr))
    return CurrentGUID