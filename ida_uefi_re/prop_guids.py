from idaapi import *
from idautils import *
from idc import *
from TrustedGUIDs import *

LocateProtocolGUIDs = {}
SupposedGUIDs = {}
LocateProtocolCalls = []
TianoCoreGUIDs = GetTianoCoreGUIDs()
AmiGUIDs = GetAmiGUIDs()
MdePkgGUIDs = GetMdePkgGUIDs()

LOG = True
ONLY_PROP = True
CONFIG = True

auto_wait()
Til2Idb(-1, "EFI_GUID")


def print_log(data):
	if LOG:
		with open("..\\log\\result_prop_guids.log", "ab") as log:
			log.write(b"\r\n" + data)

def add_prop_guid(data):
	if CONFIG:	
		with open("..\\log\\prop_guids.log", "ab") as config:
			config.write(b"\r\n" + data)

def SetHexRaysComment(address, text):
	if ONLY_PROP == False:
		cfunc = decompile(address)
		tl = treeloc_t()
		tl.ea = address
		tl.itp = ITP_SEMI
		cfunc.set_user_cmt(tl, text)
		cfunc.save_user_cmts()

"""
Gets LocateProtocol calls and makes comments
"""
def GetLocateProtocolCalls():
	print_log(b"---------- LocateProtocol function calls: ------------------")
	for ea_start in Functions():
		for ea in FuncItems(ea_start):
			"""for EFI_BOOT_SERVICES->LocateProtocol"""
			if (GetDisasm(ea).find("call") >= 0) and (GetDisasm(ea).find("+140h") >= 0 or GetDisasm(ea).find("EFI_BOOT_SERVICES.LocateProtocol") >= 0):
				LocateProtocolCalls.append(ea)
				print_log(b"[*] " + hex(ea) + ": EFI_BOOT_SERVICES->LocateProtocol is called in the function " + GetFunctionName(ea_start))
				#SetHexRaysComment(ea, "EFI_BOOT_SERVICES->SmmLocateProtocol")
				MakeComm(ea, "EFI_BOOT_SERVICES->LocateProtocol")
			"""for _EFI_SMM_SYSTEM_TABLE2.LocateProtocol"""
			if (GetDisasm(ea).find("call") >= 0) and (GetDisasm(ea).find("+0D0h") >= 0 or GetDisasm(ea).find("EFI_SMM_SYSTEM_TABLE2.SmmLocateProtocol") >= 0):
				LocateProtocolCalls.append(ea)
				print_log(b"[*] " + hex(ea) + ": _EFI_SMM_SYSTEM_TABLE2.LocateProtocol is called in the function " + GetFunctionName(ea_start))
				#SetHexRaysComment(ea, "EFI_SMM_SYSTEM_TABLE2->SmmLocateProtocol")
				MakeComm(ea, "EFI_SMM_SYSTEM_TABLE2->SmmLocateProtocol")
	if (len(LocateProtocolCalls) == 0):
		print_log(b"[*] LocateProtocol function calls list is empty")
		return False
	return True


"""
Gets LocateProtocol GUIDs dictionary {Address: GUID}
"""
def GetLocateProtocolGuids():
	if (GetLocateProtocolCalls()):
		for ea in LocateProtocolCalls:
			current_ea = ea
			while (GetMnem(current_ea) != "lea"):
				current_ea = PrevHead(current_ea)
			for xref in DataRefsFrom(current_ea):
				if (GetMnem(xref) == ""):
					CurrentGUID = []
					CurrentGUID.append(Dword(xref))             #Data1
					CurrentGUID.append(Word(xref + 4))          #Data2
					CurrentGUID.append(Word(xref + 6))          #Data3
					for addr in range(xref + 8, xref + 16, 1):  #Data4
						CurrentGUID.append(Byte(addr))
					LocateProtocolGUIDs[hex(xref)] = CurrentGUID
		print_log(b"--------- GUIDs from LocateProtocol function calls: --------")
		if (len(LocateProtocolGUIDs) > 0):
			for element in LocateProtocolGUIDs:
				print_log(b"[*] " + str(element) + ": " + str(map(hex, LocateProtocolGUIDs[element])))
			return True
		else:
			print_log(b"[*] LocateProtocol GUIDs list is empty")
			return False
	
	return False


"""
Gets supposed GUIDs dictionary {Address: GUID}
"""
def GetSupposedGuids():
	for seg in Segments():
		if SegName(seg) == ".data":
			seg_start = SegStart(seg)
			seg_end = SegEnd(seg)
			break
	ea = seg_start
	while (ea <= seg_end - 15):
		if Name(ea).find("unk_") != -1:
			CurrentGUID = []
			CurrentGUID.append(Dword(ea))               #Data1
			CurrentGUID.append(Word(ea + 4))            #Data2
			CurrentGUID.append(Word(ea + 6))            #Data3
			for addr in range(ea + 8, ea + 16, 1):      #Data4
				CurrentGUID.append(Byte(addr))
			SupposedGUIDs[hex(ea)] = CurrentGUID
		ea += 1

	if (len(SupposedGUIDs) > 0):
		return True
	else:
		return False

"""
Gets and renames trusted GUIDs 
"""
def TrustedGuids(GUIDs):
	TrustedGUIDs = []
	for element in GUIDs:
		for name in TianoCoreGUIDs:
			if (GUIDs[element] == TianoCoreGUIDs[name]):
				if TrustedGUIDs.count(element) == 0:
					print_log(b"[*] " + element + ": " + str(map(hex, GUIDs[element])) + " is " + name + " from TianoCoreGUIDs list")
					MakeName(int(element.replace("L", ""), 16), name + "_" + element)
					MakeStruct(int(element.replace("L", ""), 16), "EFI_GUID")
					TrustedGUIDs.append(element)
	for element in GUIDs:
		for name in AmiGUIDs:
			if (GUIDs[element] == AmiGUIDs[name]):
				if TrustedGUIDs.count(element) == 0:
					print_log(b"[*] " + element + ": " + str(map(hex, GUIDs[element])) + " is " + name + " from AmiGUIDs list")
					MakeName(int(element.replace("L", ""), 16), name + "_" + element)
					MakeStruct(int(element.replace("L", ""), 16), "EFI_GUID")
					TrustedGUIDs.append(element)
	for element in GUIDs:
		for name in MdePkgGUIDs:
			if (GUIDs[element] == MdePkgGUIDs[name]):
				if TrustedGUIDs.count(element) == 0:
					print_log(b"[*] " + element + ": " + str(map(hex, GUIDs[element])) + " is " + name + " from MdePkgGUIDs list")
					MakeName(int(element.replace("L", ""), 16), name + "_" + element)
					MakeStruct(int(element.replace("L", ""), 16), "EFI_GUID")
					TrustedGUIDs.append(element)
	return TrustedGUIDs

"""
Renames trusted GUIDs and finds proprietary GUIDs
"""
def RenameGuids(GUIDs):
	print_log(b"---------- Trusted GUIDs: ----------------------------------")
	TrustedGUIDs = TrustedGuids(GUIDs)
	if (len(TrustedGUIDs) == 0):
		print_log(b"[*] Trusted GUIDs list is empty")
	
	print_log(b"---------- Proprietary GUIDs: ------------------------------")
	empty = True
	for element in GUIDs:
		if (TrustedGUIDs.count(element) == 0):
			print_log(b"[!] " + element + ": " + str(map(hex, GUIDs[element])) + " is proprietary GUID")
			
			add_prop_guid(str(map(hex, GUIDs[element])))
			
			MakeName(int(element.replace("L", ""), 16), "PROPRIETARY_GUID_" + element)
			MakeStruct(int(element.replace("L", ""), 16), "EFI_GUID")
			empty = False
	if (empty):
		print_log(b"[*] Proprietary GUIDs list is empty")
	
	return True


def RenameLocateProtocolGuids():
	GUIDs = LocateProtocolGUIDs
	return RenameGuids(GUIDs)


def RenameDataSegmentGuids():
	print_log(b"--------- GUIDs from .data segment: ------------------------")
	GUIDs = SupposedGUIDs
	RenGUIDs = TrustedGuids(GUIDs)
	if (len(RenGUIDs) == 0):
		print_log(b"[*] List is empty")

def main():
#	print_log(b"========== START: ==========================================")
	
	if (GetLocateProtocolGuids()):
		RenameLocateProtocolGuids()
	if ONLY_PROP == False:
		if (GetSupposedGuids()):
			RenameDataSegmentGuids()

	print_log(b"========== END: ============================================\r\n")

	return True

main()
qexit(0)