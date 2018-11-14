import idautils
import idaapi
import idc

from guids import edk_guids, ami_guids, edk2_guids

LocateProtocolGUIDs = {}
SupposedGUIDs = {}
LocateProtocolCalls = []

TianoCoreOldGUIDs = edk_guids.edk_guids
TianoCoreNewGUIDs = edk2_guids.edk2_guids
AmiGUIDs = ami_guids.ami_guids

LOG = False
ONLY_PROP = True
CONFIG = False

idc.auto_wait()
idc.Til2Idb(-1, "EFI_GUID")

def print_log(data):
	if LOG:
		with open("..\\result.log", "ab") as log:
			log.write(b"\r\n" + data)
	else:
		print(data)

def add_prop_guid(data):
	if CONFIG:	
		with open("..\\prop_guids.config", "ab") as config:
			config.write(b"\r\n" + data)

def SetHexRaysComment(address, text):
	if ONLY_PROP == False:
		cfunc = idaapi.decompile(address)
		tl = idaapi.treeloc_t()
		tl.ea = address
		tl.itp = idaapi.ITP_SEMI
		cfunc.set_user_cmt(tl, text)
		cfunc.save_user_cmts()

"""
Gets LocateProtocol calls and makes comments
"""
def GetLocateProtocolCalls():
	print_log(b"---------- LocateProtocol function calls: ------------------")
	for ea_start in idautils.Functions():
		for ea in idautils.FuncItems(ea_start):
			"""for EFI_BOOT_SERVICES->LocateProtocol"""
			if (idc.GetDisasm(ea).find("call") >= 0) and (idc.GetDisasm(ea).find("+140h") >= 0 or idc.GetDisasm(ea).find("EFI_BOOT_SERVICES.LocateProtocol") >= 0):
				LocateProtocolCalls.append(ea)
				print_log(b"[*] " + hex(ea) + ": EFI_BOOT_SERVICES->LocateProtocol is called in the function " + idc.GetFunctionName(ea_start))
				SetHexRaysComment(ea, "EFI_BOOT_SERVICES->LocateProtocol")
				idc.MakeComm(ea, "EFI_BOOT_SERVICES->LocateProtocol")

			"""for EFI_BOOT_SERVICES->HandleProtocol"""
			if (idc.GetDisasm(ea).find("call") >= 0) and (idc.GetDisasm(ea).find("+98h") >= 0 or idc.GetDisasm(ea).find("EFI_BOOT_SERVICES.HandleProtocol") >= 0):
				LocateProtocolCalls.append(ea)
				print_log(b"[*] " + hex(ea) + ": EFI_BOOT_SERVICES->HandleProtocol is called in the function " + idc.GetFunctionName(ea_start))
				SetHexRaysComment(ea, "EFI_BOOT_SERVICES->HandleProtocol")
				idc.MakeComm(ea, "EFI_BOOT_SERVICES->HandleProtocol")	

			"""for EFI_BOOT_SERVICES->InstallProtocolInterface"""
			if (idc.GetDisasm(ea).find("call") >= 0) and (idc.GetDisasm(ea).find("+80h") >= 0 or idc.GetDisasm(ea).find("EFI_BOOT_SERVICES.InstallProtocolInterface") >= 0):
				LocateProtocolCalls.append(ea)
				print_log(b"[*] " + hex(ea) + ": _EFI_SMM_SYSTEM_TABLE2.LocateProtocol is called in the function " + idc.GetFunctionName(ea_start))
				SetHexRaysComment(ea, "_EFI_SMM_SYSTEM_TABLE2->SmmLocateProtocol")
				idc.MakeComm(ea, "_EFI_SMM_SYSTEM_TABLE2->SmmLocateProtocol")
			
			"""for _EFI_SMM_SYSTEM_TABLE2.LocateProtocol"""
			if (idc.GetDisasm(ea).find("call") >= 0) and (idc.GetDisasm(ea).find("+0D0h") >= 0 or idc.GetDisasm(ea).find("EFI_SMM_SYSTEM_TABLE2.SmmLocateProtocol") >= 0):
				LocateProtocolCalls.append(ea)
				print_log(b"[*] " + hex(ea) + ": _EFI_SMM_SYSTEM_TABLE2.LocateProtocol is called in the function " + idc.GetFunctionName(ea_start))
				SetHexRaysComment(ea, "_EFI_SMM_SYSTEM_TABLE2->SmmLocateProtocol")
				idc.MakeComm(ea, "_EFI_SMM_SYSTEM_TABLE2->SmmLocateProtocol")
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
			while (idc.GetMnem(current_ea) != "lea"):
				current_ea = idc.PrevHead(current_ea)
			for xref in idautils.DataRefsFrom(current_ea):
				if (idc.GetMnem(xref) == ""):
					CurrentGUID = []
					CurrentGUID.append(idc.Word(xref))              #Data1
					CurrentGUID.append(idc.Word(xref + 4))          #Data2
					CurrentGUID.append(idc.Word(xref + 6))          #Data3
					for addr in range(xref + 8, xref + 16, 1):      #Data4
						CurrentGUID.append(idc.Byte(addr))
					LocateProtocolGUIDs[hex(xref)] = CurrentGUID
		print_log(b"--------- GUIDs from LocateProtocol function calls: --------")
		if (len(LocateProtocolGUIDs) > 0):
			for element in LocateProtocolGUIDs:
				print_log(b"[*] " + str(element) + ": " + str(LocateProtocolGUIDs[element]))
			return True
		else:
			print_log(b"[*] LocateProtocol GUIDs list is empty")
			return False
	
	return False


"""
Gets supposed GUIDs dictionary {Address: GUID}
"""
def GetSupposedGuids():
	for seg in idautils.Segments():
		if idc.SegName(seg) == ".data":
			seg_start = idc.SegStart(seg)
			seg_end = idc.SegEnd(seg)
			break
	ea = seg_start
	while (ea <= seg_end - 15):
		if idc.Name(ea).find("unk_") != -1:
			CurrentGUID = []
			CurrentGUID.append(idc.Word(ea))                #Data1
			CurrentGUID.append(idc.Word(ea + 4))            #Data2
			CurrentGUID.append(idc.Word(ea + 6))            #Data3
			for addr in range(ea + 8, ea + 16, 1):          #Data4
				CurrentGUID.append(idc.Byte(addr))
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
		for name in TianoCoreOldGUIDs:
			if (GUIDs[element] == TianoCoreOldGUIDs[name]):
				if TrustedGUIDs.count(element) == 0:
					print_log(b"[*] " + element + ": " + str(GUIDs[element]) + " is " + name + " from TianoCoreOldGUIDs list")
					idc.MakeName(int(element.replace("L", ""), 16), name + "_" + element)
					idc.MakeStruct(int(element.replace("L", ""), 16), "EFI_GUID")
					TrustedGUIDs.append(element)
	for name in TianoCoreNewGUIDs:
		if (GUIDs[element] == TianoCoreNewGUIDs[name]):
			if TrustedGUIDs.count(element) == 0:
				print_log(b"[*] " + element + ": " + str(GUIDs[element]) + " is " + name + " from TianoCoreNewGUIDs list")
				idc.MakeName(int(element.replace("L", ""), 16), name + "_" + element)
				idc.MakeStruct(int(element.replace("L", ""), 16), "EFI_GUID")
				TrustedGUIDs.append(element)
	for element in GUIDs:
		for name in AmiGUIDs:
			if (GUIDs[element] == AmiGUIDs[name]):
				if TrustedGUIDs.count(element) == 0:
					print_log(b"[*] " + element + ": " + str(GUIDs[element]) + " is " + name + " from AmiGUIDs list")
					idc.MakeName(int(element.replace("L", ""), 16), name + "_" + element)
					idc.MakeStruct(int(element.replace("L", ""), 16), "EFI_GUID")
					TrustedGUIDs.append(element)
	return TrustedGUIDs

"""
Renames trusted GUIDs and finds proprietary GUIDs
"""
def RenameGuids(GUIDs):
	print_log(b"---------- Trusted GUIDs: ----------------------------------")
	TrustedGUIDs = TrustedGuids(GUIDs)
	print(TrustedGUIDs)
	if (len(TrustedGUIDs) == 0):
		print_log(b"[*] Trusted GUIDs list is empty")
	
	print_log(b"---------- Proprietary GUIDs: ------------------------------")
	empty = True
	for element in GUIDs:
		if (TrustedGUIDs.count(element) == 0):
			print_log(b"[!] " + element + ": " + str(GUIDs[element]) + " is proprietary GUID")
			
			add_prop_guid(str(GUIDs[element]).replace("L", ""))
			
			idc.MakeName(int(element.replace("L", ""), 16), "PROPRIETARY_GUID_" + element)
			idc.MakeStruct(int(element.replace("L", ""), 16), "EFI_GUID")
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
	print_log(b"========== START: ==========================================")
	
	if (GetLocateProtocolGuids()):
		RenameLocateProtocolGuids()
	if ONLY_PROP == False:
		if (GetSupposedGuids()):
			RenameDataSegmentGuids()

	print_log(b"========== END: ============================================\r\n")

	return True

main()
#qexit(0)