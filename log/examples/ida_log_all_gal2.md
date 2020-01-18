## Module: AcpiPlatform
### Boot services:
* [0x90f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x514] EFI_BOOT_SERVICES->HandleProtocol
* [0x38c4] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x4e5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x608] EFI_BOOT_SERVICES->LocateProtocol
* [0x885] EFI_BOOT_SERVICES->LocateProtocol
* [0xa4a] EFI_BOOT_SERVICES->LocateProtocol
* [0xb78] EFI_BOOT_SERVICES->LocateProtocol
* [0x11cf] EFI_BOOT_SERVICES->LocateProtocol
* [0x3d34] EFI_BOOT_SERVICES->LocateProtocol
* [0x3e7c] EFI_BOOT_SERVICES->LocateProtocol
* [0x431f] EFI_BOOT_SERVICES->LocateProtocol
* [0x447f] EFI_BOOT_SERVICES->LocateProtocol
* [0x45b2] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x4a1c]
	 - [service] InstallProtocolInterface
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
* [0x4a0c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3FDDA605-A76E-4F46-AD2912F4531B3D08
* [0x49dc]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 171E9398-269C-4081-90993844E260466C
* [0x49ec]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x49fc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EB97088E-CFDF-49C6-BE4BD906A5B20E86
* [0x496c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x49bc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x49ac]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
* [0x497c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
## Module: AcpiS3SaveDxe
### Boot services:
* [0xc4c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xdef] EFI_BOOT_SERVICES->LocateProtocol
* [0x1527] EFI_BOOT_SERVICES->LocateProtocol
* [0x165a] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1c90]
	 - [service] InstallProtocolInterface
	 - [protocol_name] EFI_ACPI_S3_SAVE_GUID
	 - [protocol_place] edk_guids
	 - [guid] 125F2DE1-FB85-440C-A54C4D99358A8D38
* [0x1c80]
	 - [service] LocateProtocol
	 - [protocol_name] FRAMEWORK_EFI_MP_SERVICES_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] F33261E7-23CB-11D5-BD5C0080C73C8881
* [0x1c50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
## Module: AcpiSmmPlatform
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x1d35] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x924] EFI_BOOT_SERVICES->LocateProtocol
* [0x979] EFI_BOOT_SERVICES->LocateProtocol
* [0x18d3] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a71] EFI_BOOT_SERVICES->LocateProtocol
* [0x280b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2953] EFI_BOOT_SERVICES->LocateProtocol
* [0x3252] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x38a0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
* [0x3880]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 171E9398-269C-4081-90993844E260466C
* [0x3860]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3830]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x3820]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x3850]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
## Module: AcpiTableDxe
### Boot services:
* [0x17b4] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x3adf] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x178d] EFI_BOOT_SERVICES->LocateProtocol
* [0x490] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4aa] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x3fcc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
## Module: BdsDxe
### Boot services:
* [0x50f4] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x5253] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xb7c1] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xbb4b] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xbf4c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xcc74] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xb7d2] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xd3b] EFI_BOOT_SERVICES->HandleProtocol
* [0x2dc2] EFI_BOOT_SERVICES->HandleProtocol
* [0x531e] EFI_BOOT_SERVICES->HandleProtocol
* [0x55a2] EFI_BOOT_SERVICES->HandleProtocol
* [0x59ff] EFI_BOOT_SERVICES->HandleProtocol
* [0x5ca8] EFI_BOOT_SERVICES->HandleProtocol
* [0x5d2f] EFI_BOOT_SERVICES->HandleProtocol
* [0x63f9] EFI_BOOT_SERVICES->HandleProtocol
* [0x6499] EFI_BOOT_SERVICES->HandleProtocol
* [0x66e1] EFI_BOOT_SERVICES->HandleProtocol
* [0x67c5] EFI_BOOT_SERVICES->HandleProtocol
* [0x6bb3] EFI_BOOT_SERVICES->HandleProtocol
* [0x6d06] EFI_BOOT_SERVICES->HandleProtocol
* [0x6fde] EFI_BOOT_SERVICES->HandleProtocol
* [0x7a88] EFI_BOOT_SERVICES->HandleProtocol
* [0x7cfe] EFI_BOOT_SERVICES->HandleProtocol
* [0x7e8d] EFI_BOOT_SERVICES->HandleProtocol
* [0x82ff] EFI_BOOT_SERVICES->HandleProtocol
* [0x83cf] EFI_BOOT_SERVICES->HandleProtocol
* [0x95bc] EFI_BOOT_SERVICES->HandleProtocol
* [0x97d7] EFI_BOOT_SERVICES->HandleProtocol
* [0x9ad2] EFI_BOOT_SERVICES->HandleProtocol
* [0xa299] EFI_BOOT_SERVICES->HandleProtocol
* [0xa2d9] EFI_BOOT_SERVICES->HandleProtocol
* [0xaf19] EFI_BOOT_SERVICES->HandleProtocol
* [0xb145] EFI_BOOT_SERVICES->HandleProtocol
* [0xb198] EFI_BOOT_SERVICES->HandleProtocol
* [0xb1e5] EFI_BOOT_SERVICES->HandleProtocol
* [0xb9bb] EFI_BOOT_SERVICES->HandleProtocol
* [0xbc21] EFI_BOOT_SERVICES->HandleProtocol
* [0xd3c8] EFI_BOOT_SERVICES->HandleProtocol
* [0xd653] EFI_BOOT_SERVICES->HandleProtocol
* [0xd707] EFI_BOOT_SERVICES->HandleProtocol
* [0xd938] EFI_BOOT_SERVICES->HandleProtocol
* [0xd9c6] EFI_BOOT_SERVICES->HandleProtocol
* [0xdbe2] EFI_BOOT_SERVICES->HandleProtocol
* [0xdc67] EFI_BOOT_SERVICES->HandleProtocol
* [0xe7bc] EFI_BOOT_SERVICES->HandleProtocol
* [0xe7ed] EFI_BOOT_SERVICES->HandleProtocol
* [0xe80b] EFI_BOOT_SERVICES->HandleProtocol
* [0xf1b3] EFI_BOOT_SERVICES->HandleProtocol
* [0xf1e4] EFI_BOOT_SERVICES->HandleProtocol
* [0xf690] EFI_BOOT_SERVICES->HandleProtocol
* [0xf6c1] EFI_BOOT_SERVICES->HandleProtocol
* [0x401b] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x5af7] EFI_BOOT_SERVICES->OpenProtocol
* [0x5b22] EFI_BOOT_SERVICES->OpenProtocol
* [0x5bc5] EFI_BOOT_SERVICES->OpenProtocol
* [0x5bfe] EFI_BOOT_SERVICES->OpenProtocol
* [0xa2ba] EFI_BOOT_SERVICES->OpenProtocol
* [0x5aaa] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x51b3] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5213] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x52cb] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x597a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x59cf] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5b9a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x64f2] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6b6a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6d7b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6fa3] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x7cb4] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x7e5a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x7f84] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x9595] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x9aaf] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa4df] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xae6e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xaee0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xb1bc] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xb957] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xbbf5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xd7d7] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x172b] EFI_BOOT_SERVICES->LocateProtocol
* [0x17ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x476e] EFI_BOOT_SERVICES->LocateProtocol
* [0x48b6] EFI_BOOT_SERVICES->LocateProtocol
* [0x4e9a] EFI_BOOT_SERVICES->LocateProtocol
* [0x4ee6] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f32] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f7e] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f98] EFI_BOOT_SERVICES->LocateProtocol
* [0x6abe] EFI_BOOT_SERVICES->LocateProtocol
* [0x7bec] EFI_BOOT_SERVICES->LocateProtocol
* [0xaa4d] EFI_BOOT_SERVICES->LocateProtocol
* [0xae2a] EFI_BOOT_SERVICES->LocateProtocol
* [0xae99] EFI_BOOT_SERVICES->LocateProtocol
* [0xb8f6] EFI_BOOT_SERVICES->LocateProtocol
* [0xbb17] EFI_BOOT_SERVICES->LocateProtocol
* [0xc04c] EFI_BOOT_SERVICES->LocateProtocol
* [0xc075] EFI_BOOT_SERVICES->LocateProtocol
* [0xc4af] EFI_BOOT_SERVICES->LocateProtocol
* [0xc630] EFI_BOOT_SERVICES->LocateProtocol
* [0xcc1b] EFI_BOOT_SERVICES->LocateProtocol
* [0xcdb2] EFI_BOOT_SERVICES->LocateProtocol
* [0xe1df] EFI_BOOT_SERVICES->LocateProtocol
* [0xe312] EFI_BOOT_SERVICES->LocateProtocol
* [0xe444] EFI_BOOT_SERVICES->LocateProtocol
* [0xe59a] EFI_BOOT_SERVICES->LocateProtocol
* [0xe890] EFI_BOOT_SERVICES->LocateProtocol
* [0xf210] EFI_BOOT_SERVICES->LocateProtocol
* [0xf240] EFI_BOOT_SERVICES->LocateProtocol
* [0x10493] EFI_BOOT_SERVICES->LocateProtocol
* [0x633] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x10b10]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x10990]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] D088A413-0A70-4217-BA559A3CB65C41B3
* [0x10aa0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x11334]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 00000000-4146-4154-4C204552524F523A
* [0x10b30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
* [0x10b40]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
* [0x10aa0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x10ba0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x10a80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x10a60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x10a50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x10ac0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x10a70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0x109a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDevicePathToTextProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8B843E20-8132-4852-90CC551A4E4A7F1C
* [0x10a30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiBootLogoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CDEA2BD3-FC25-4C1C-B97CB31186064990
* [0x10980]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGenericMemTestProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 309DE7F1-7F5E-4ACE-B49C531BE5AA95EF
* [0x10a20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiUserManagerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6FD5B00C-D426-4283-98876CF5CF1CB1FE
* [0x10970]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 07D75280-27D4-4D69-90D05643E238B341
* [0x10950]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_ACPI_S3_SAVE_GUID
	 - [protocol_place] edk_guids
	 - [guid] 125F2DE1-FB85-440C-A54C4D99358A8D38
* [0x10bb0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 122B109B-DB9B-4F03-969C17F14E10FECD
* [0x10be0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 171E9398-269C-4081-90993844E260466C
* [0x10bd0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 1156EFC6-EA32-4396-B5D526932E83C313
* [0x10b00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x10a10]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_OEM_BADGING_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] 170E13C0-BF1B-4218-871D2ABDC6F887BC
* [0x10a40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 41C7F059-081A-4F45-B1F0C5A988915221
* [0x10c00]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiBdsArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 665E3FF6-46CC-11D4-9A380090273FC14D
## Module: BootManagerMenuApp
### Boot services:
* [0x20ac] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x21b0] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x227b] EFI_BOOT_SERVICES->HandleProtocol
* [0x239c] EFI_BOOT_SERVICES->HandleProtocol
* [0x2645] EFI_BOOT_SERVICES->HandleProtocol
* [0x26cc] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d96] EFI_BOOT_SERVICES->HandleProtocol
* [0x2e36] EFI_BOOT_SERVICES->HandleProtocol
* [0x307e] EFI_BOOT_SERVICES->HandleProtocol
* [0x3162] EFI_BOOT_SERVICES->HandleProtocol
* [0x3550] EFI_BOOT_SERVICES->HandleProtocol
* [0x36a3] EFI_BOOT_SERVICES->HandleProtocol
* [0x397b] EFI_BOOT_SERVICES->HandleProtocol
* [0x4425] EFI_BOOT_SERVICES->HandleProtocol
* [0x469b] EFI_BOOT_SERVICES->HandleProtocol
* [0x482a] EFI_BOOT_SERVICES->HandleProtocol
* [0x4c9c] EFI_BOOT_SERVICES->HandleProtocol
* [0x4d6c] EFI_BOOT_SERVICES->HandleProtocol
* [0x5b56] EFI_BOOT_SERVICES->HandleProtocol
* [0x5b96] EFI_BOOT_SERVICES->HandleProtocol
* [0x630b] EFI_BOOT_SERVICES->HandleProtocol
* [0x7036] EFI_BOOT_SERVICES->HandleProtocol
* [0x8812] EFI_BOOT_SERVICES->HandleProtocol
* [0x88c6] EFI_BOOT_SERVICES->HandleProtocol
* [0x8a34] EFI_BOOT_SERVICES->HandleProtocol
* [0x8ac2] EFI_BOOT_SERVICES->HandleProtocol
* [0x8cde] EFI_BOOT_SERVICES->HandleProtocol
* [0x8d63] EFI_BOOT_SERVICES->HandleProtocol
* [0x2494] EFI_BOOT_SERVICES->OpenProtocol
* [0x24bf] EFI_BOOT_SERVICES->OpenProtocol
* [0x2562] EFI_BOOT_SERVICES->OpenProtocol
* [0x259b] EFI_BOOT_SERVICES->OpenProtocol
* [0x5b77] EFI_BOOT_SERVICES->OpenProtocol
* [0x2447] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2170] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2228] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2317] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x236c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2537] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2e8f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3507] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3718] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3940] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4651] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x47f7] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4921] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5d9c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xf46] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a66] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ab2] EFI_BOOT_SERVICES->LocateProtocol
* [0x1afe] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b4a] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b64] EFI_BOOT_SERVICES->LocateProtocol
* [0x345b] EFI_BOOT_SERVICES->LocateProtocol
* [0x4589] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x9580]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x95a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiBootLogoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CDEA2BD3-FC25-4C1C-B97CB31186064990
* [0x9530]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x9510]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x9500]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x9540]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x9520]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0x9440]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDevicePathToTextProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8B843E20-8132-4852-90CC551A4E4A7F1C
## Module: BootScriptExecutorDxe
### Boot services:
* [0x67c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x4687] EFI_BOOT_SERVICES->HandleProtocol
* [0x473b] EFI_BOOT_SERVICES->HandleProtocol
* [0x104c] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x480b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x64c] EFI_BOOT_SERVICES->LocateProtocol
* [0xd97] EFI_BOOT_SERVICES->LocateProtocol
* [0xeca] EFI_BOOT_SERVICES->LocateProtocol
* [0x1558] EFI_BOOT_SERVICES->LocateProtocol
* [0x16a0] EFI_BOOT_SERVICES->LocateProtocol
* [0x4e7f] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x6c7c]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] FA20568B-548B-4B2B-81EF1BA08D4A3CEC
* [0x6c1c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x6bec]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x6bfc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x6c2c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
## Module: CapsuleRuntimeDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x2589] EFI_BOOT_SERVICES->LocateProtocol
* [0x84e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2e94]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 41C7F059-081A-4F45-B1F0C5A988915221
## Module: ConPlatformDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x4e6] EFI_BOOT_SERVICES->OpenProtocol
* [0x506] EFI_BOOT_SERVICES->OpenProtocol
* [0x570] EFI_BOOT_SERVICES->OpenProtocol
* [0x8f1] EFI_BOOT_SERVICES->OpenProtocol
* [0x95f] EFI_BOOT_SERVICES->OpenProtocol
* [0xa89] EFI_BOOT_SERVICES->OpenProtocol
* [0xab4] EFI_BOOT_SERVICES->OpenProtocol
* [0xc17] EFI_BOOT_SERVICES->OpenProtocol
* [0xc87] EFI_BOOT_SERVICES->OpenProtocol
* [0xcb2] EFI_BOOT_SERVICES->OpenProtocol
* [0x51e] EFI_BOOT_SERVICES->CloseProtocol
* [0x92d] EFI_BOOT_SERVICES->CloseProtocol
* [0x9bc] EFI_BOOT_SERVICES->CloseProtocol
* [0xb60] EFI_BOOT_SERVICES->CloseProtocol
* [0xddb] EFI_BOOT_SERVICES->CloseProtocol
* [0xbdc] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xb00] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb4b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xd15] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xda3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xdc2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x171a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x175b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x588] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x1f98]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x1f88]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
* [0x1f78]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x1fc8]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiConsoleInDeviceGuid
	 - [protocol_place] edk2_guids
	 - [guid] D3B36F2B-D551-11D4-9A460090273FC14D
* [0x1fd8]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiConsoleOutDeviceGuid
	 - [protocol_place] edk2_guids
	 - [guid] D3B36F2C-D551-11D4-9A460090273FC14D
* [0x1fe8]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiStandardErrorDeviceGuid
	 - [protocol_place] edk2_guids
	 - [guid] D3B36F2D-D551-11D4-9A460090273FC14D
## Module: ConSplitterDxe
### Boot services:
* [0x2eb7] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x1097] EFI_BOOT_SERVICES->OpenProtocol
* [0x1134] EFI_BOOT_SERVICES->OpenProtocol
* [0x1155] EFI_BOOT_SERVICES->OpenProtocol
* [0x117a] EFI_BOOT_SERVICES->OpenProtocol
* [0x11e7] EFI_BOOT_SERVICES->OpenProtocol
* [0x1b5f] EFI_BOOT_SERVICES->OpenProtocol
* [0x1c06] EFI_BOOT_SERVICES->OpenProtocol
* [0x2ca0] EFI_BOOT_SERVICES->OpenProtocol
* [0x2cd2] EFI_BOOT_SERVICES->OpenProtocol
* [0x4787] EFI_BOOT_SERVICES->OpenProtocol
* [0x10af] EFI_BOOT_SERVICES->CloseProtocol
* [0x119a] EFI_BOOT_SERVICES->CloseProtocol
* [0x11b0] EFI_BOOT_SERVICES->CloseProtocol
* [0x1201] EFI_BOOT_SERVICES->CloseProtocol
* [0x1212] EFI_BOOT_SERVICES->CloseProtocol
* [0x479d] EFI_BOOT_SERVICES->CloseProtocol
* [0x47f4] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x3d5b] EFI_BOOT_SERVICES->LocateProtocol
* [0x182f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x187b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x18c7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2bf7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2c21] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4693] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x46d4] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2ed5] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x4e34]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
## Module: CpuArchDxe
### Boot services:
* [0x6f3] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x650] EFI_BOOT_SERVICES->LocateProtocol
* [0x2499] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x4a40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3FDDA605-A76E-4F46-AD2912F4531B3D08
* [0x4a10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
## Module: CpuIo2Dxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x779] EFI_BOOT_SERVICES->LocateProtocol
* [0x7a1] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x1320]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AD61F191-AE5F-4C0E-B9FAE869D288C64F
## Module: CpuIo2Smm
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x852] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1005] EFI_BOOT_SERVICES->LocateProtocol
* [0x113a] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1658]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1648]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
## Module: CpuIoDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x945] EFI_BOOT_SERVICES->LocateProtocol
* [0x96d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x1964]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CPU_IO_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] B0732526-38C8-4B40-887761C7B06AAC45
## Module: CpuMpDxe
### Boot services:
* [0x752] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x70c4] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x8e9] EFI_BOOT_SERVICES->LocateProtocol
* [0xba5] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b8c] EFI_BOOT_SERVICES->LocateProtocol
* [0x1cfe] EFI_BOOT_SERVICES->LocateProtocol
* [0x2fd3] EFI_BOOT_SERVICES->LocateProtocol
* [0x5d41] EFI_BOOT_SERVICES->LocateProtocol
* [0x5dc3] EFI_BOOT_SERVICES->LocateProtocol
* [0x732c] EFI_BOOT_SERVICES->LocateProtocol
* [0x7378] EFI_BOOT_SERVICES->LocateProtocol
* [0x73c4] EFI_BOOT_SERVICES->LocateProtocol
* [0x7410] EFI_BOOT_SERVICES->LocateProtocol
* [0x742a] EFI_BOOT_SERVICES->LocateProtocol
* [0x8bc7] EFI_BOOT_SERVICES->LocateProtocol
* [0x8d0f] EFI_BOOT_SERVICES->LocateProtocol
* [0x9708] EFI_BOOT_SERVICES->LocateProtocol
* [0x983b] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x9c5c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTimerArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB3-6F42-11D4-BCE70080C73C8881
* [0x9c6c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26EEB3DE-B689-492E-80F0BE8BD7DA4BA7
* [0x9c8c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGenericMemTestProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 309DE7F1-7F5E-4ACE-B49C531BE5AA95EF
* [0x9c7c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x9cac]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0x9c2c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
* [0x9c3c]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
* [0x9c0c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x9bec]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x9bdc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x9c1c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x9bfc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0x9b9c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x9bac]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x9bcc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
## Module: DataHubDxe
### Boot services:
* [0xac0] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* empty
## Module: DataHubStdErrDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x479] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xde0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_DATA_HUB_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] AE80D021-618E-11D4-BCD70080C73C8881
## Module: DevicePathDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x408] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: DiskIoDxe
### Boot services:
* [0x47c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x539] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x442] EFI_BOOT_SERVICES->OpenProtocol
* [0x4f3] EFI_BOOT_SERVICES->OpenProtocol
* [0xad2] EFI_BOOT_SERVICES->OpenProtocol
* [0x4b0] EFI_BOOT_SERVICES->CloseProtocol
* [0x552] EFI_BOOT_SERVICES->CloseProtocol
* [0xaee] EFI_BOOT_SERVICES->CloseProtocol
* [0x11e2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1223] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x1880]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0x1870]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x1870]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
## Module: DxeCore
### Boot services:
* [0x10dc5] EFI_BOOT_SERVICES->HandleProtocol
* [0x10e53] EFI_BOOT_SERVICES->HandleProtocol
* [0x1106f] EFI_BOOT_SERVICES->HandleProtocol
* [0x110f4] EFI_BOOT_SERVICES->HandleProtocol
* [0xe84b] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x10ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x12cdd] EFI_BOOT_SERVICES->LocateProtocol
* [0xf7ea] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x14554]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSecurityPolicyProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 78E4D245-CD4D-4A05-A2BA4743E86CFCAB
## Module: DxePlatform
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xb64] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x561] EFI_BOOT_SERVICES->LocateProtocol
* [0x5ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x676] EFI_BOOT_SERVICES->LocateProtocol
* [0x7e9] EFI_BOOT_SERVICES->LocateProtocol
* [0xf6c] EFI_BOOT_SERVICES->LocateProtocol
* [0x10b4] EFI_BOOT_SERVICES->LocateProtocol
* [0x16ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x16f9] EFI_BOOT_SERVICES->LocateProtocol
* [0x1745] EFI_BOOT_SERVICES->LocateProtocol
* [0x1791] EFI_BOOT_SERVICES->LocateProtocol
* [0x17ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x3046] EFI_BOOT_SERVICES->LocateProtocol
* [0x3179] EFI_BOOT_SERVICES->LocateProtocol
* [0x32ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x3401] EFI_BOOT_SERVICES->LocateProtocol
* [0x612] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x3764]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x3754]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x3744]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
* [0x3704]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x3714]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x36e4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x3724]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x36d4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0x3734]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x3774]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 2977064F-AB96-4FA9-8545F9C40251E07F
## Module: EhciDxe
### Boot services:
* [0x1b13] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x8f8] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1ca5] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x19e5] EFI_BOOT_SERVICES->HandleProtocol
* [0x447] EFI_BOOT_SERVICES->OpenProtocol
* [0x890] EFI_BOOT_SERVICES->OpenProtocol
* [0x1867] EFI_BOOT_SERVICES->OpenProtocol
* [0x189c] EFI_BOOT_SERVICES->OpenProtocol
* [0x4467] EFI_BOOT_SERVICES->OpenProtocol
* [0x531c] EFI_BOOT_SERVICES->OpenProtocol
* [0x49c] EFI_BOOT_SERVICES->CloseProtocol
* [0x987] EFI_BOOT_SERVICES->CloseProtocol
* [0x1a8e] EFI_BOOT_SERVICES->CloseProtocol
* [0x1cfa] EFI_BOOT_SERVICES->CloseProtocol
* [0x5332] EFI_BOOT_SERVICES->CloseProtocol
* [0x19a8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5228] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5269] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x5a34]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiUsb2HcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3E745226-9818-45B6-A2ACD7CD0E8BA2BC
* [0x5a44]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x5a24]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x5a44]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
## Module: EnglishDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x734] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x778] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x10d4]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 00000000-3130-3332-3435363738395C2E
## Module: Fat
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x457] EFI_BOOT_SERVICES->OpenProtocol
* [0x47d] EFI_BOOT_SERVICES->OpenProtocol
* [0x4b7] EFI_BOOT_SERVICES->OpenProtocol
* [0x516] EFI_BOOT_SERVICES->OpenProtocol
* [0x599] EFI_BOOT_SERVICES->OpenProtocol
* [0x5d0] EFI_BOOT_SERVICES->OpenProtocol
* [0x71b] EFI_BOOT_SERVICES->OpenProtocol
* [0x59a2] EFI_BOOT_SERVICES->OpenProtocol
* [0x4d5] EFI_BOOT_SERVICES->CloseProtocol
* [0x532] EFI_BOOT_SERVICES->CloseProtocol
* [0x5b5] EFI_BOOT_SERVICES->CloseProtocol
* [0x59b8] EFI_BOOT_SERVICES->CloseProtocol
* [0x658] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6c1] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x120a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x57bf] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5800] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xe03] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x6168]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
* [0x6168]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
## Module: FwBlockService
### Boot services:
* [0x1d4a] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1bef] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x155b] EFI_BOOT_SERVICES->HandleProtocol
* [0x15a7] EFI_BOOT_SERVICES->HandleProtocol
* [0x1ba4] EFI_BOOT_SERVICES->HandleProtocol
* [0x1c7f] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x67c] EFI_BOOT_SERVICES->LocateProtocol
* [0x16ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x1765] EFI_BOOT_SERVICES->LocateProtocol
* [0x242c] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b39] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1c2b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x3658]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 171E9398-269C-4081-90993844E260466C
* [0x3688]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x36b8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 1156EFC6-EA32-4396-B5D526932E83C313
* [0x3638]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
* [0x36d8]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] EFI_FVB_EXTENSION_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] 53A4C71B-B581-4170-91B38DB87A4B5C46
## Module: FwBlockServiceSmm
### Boot services:
* [0x1d0b] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1bb0] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x151c] EFI_BOOT_SERVICES->HandleProtocol
* [0x1568] EFI_BOOT_SERVICES->HandleProtocol
* [0x1b65] EFI_BOOT_SERVICES->HandleProtocol
* [0x1c40] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x63d] EFI_BOOT_SERVICES->LocateProtocol
* [0x166c] EFI_BOOT_SERVICES->LocateProtocol
* [0x1726] EFI_BOOT_SERVICES->LocateProtocol
* [0x2499] EFI_BOOT_SERVICES->LocateProtocol
* [0x25cd] EFI_BOOT_SERVICES->LocateProtocol
* [0x276b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1afa] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1bec] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x3444]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 171E9398-269C-4081-90993844E260466C
* [0x3474]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x34a4]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 1156EFC6-EA32-4396-B5D526932E83C313
* [0x3414]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
* [0x3404]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x34c4]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] EFI_FVB_EXTENSION_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] 53A4C71B-B581-4170-91B38DB87A4B5C46
## Module: GraphicsConsoleDxe
### Boot services:
* [0x4b8] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xa47] EFI_BOOT_SERVICES->HandleProtocol
* [0xa64] EFI_BOOT_SERVICES->HandleProtocol
* [0x22fb] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x475] EFI_BOOT_SERVICES->OpenProtocol
* [0xa9e] EFI_BOOT_SERVICES->OpenProtocol
* [0xacb] EFI_BOOT_SERVICES->OpenProtocol
* [0xaf1] EFI_BOOT_SERVICES->OpenProtocol
* [0x1508] EFI_BOOT_SERVICES->OpenProtocol
* [0x153d] EFI_BOOT_SERVICES->OpenProtocol
* [0x4f3] EFI_BOOT_SERVICES->CloseProtocol
* [0xb0f] EFI_BOOT_SERVICES->CloseProtocol
* [0xb48] EFI_BOOT_SERVICES->CloseProtocol
* [0x176c] EFI_BOOT_SERVICES->CloseProtocol
* [0x5bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x2040] EFI_BOOT_SERVICES->LocateProtocol
* [0x208c] EFI_BOOT_SERVICES->LocateProtocol
* [0x20d8] EFI_BOOT_SERVICES->LocateProtocol
* [0x2124] EFI_BOOT_SERVICES->LocateProtocol
* [0x213e] EFI_BOOT_SERVICES->LocateProtocol
* [0x16f2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x219a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x21db] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2bdc]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0x2bcc]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUgaDrawProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 982C298B-F4FA-41CB-B83877AA688FB839
* [0x2bcc]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUgaDrawProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 982C298B-F4FA-41CB-B83877AA688FB839
* [0x2bac]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x2b8c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x2b6c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x2bbc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x2b7c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0x2bec]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
## Module: HiiDatabase
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x3b8d] EFI_BOOT_SERVICES->HandleProtocol
* [0x47ba] EFI_BOOT_SERVICES->HandleProtocol
* [0x5185] EFI_BOOT_SERVICES->HandleProtocol
* [0x9839] EFI_BOOT_SERVICES->HandleProtocol
* [0xdf97] EFI_BOOT_SERVICES->HandleProtocol
* [0xa05a] EFI_BOOT_SERVICES->OpenProtocol
* [0x3b4d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x43a] EFI_BOOT_SERVICES->LocateProtocol
* [0x46b] EFI_BOOT_SERVICES->LocateProtocol
* [0x49c] EFI_BOOT_SERVICES->LocateProtocol
* [0x4cd] EFI_BOOT_SERVICES->LocateProtocol
* [0x4fe] EFI_BOOT_SERVICES->LocateProtocol
* [0x5a9] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5e3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9f9c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa0d0] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0xf7f8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0xf7e8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0xf818]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0xf828]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0xf808]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0xf888]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 348C4D62-BFBD-4882-9ECEC80BB1C4783B
## Module: I2CDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xa34] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: IohInitDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x9cc] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xdd4] EFI_BOOT_SERVICES->LocateProtocol
* [0xf1c] EFI_BOOT_SERVICES->LocateProtocol
* [0x16f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x1868] EFI_BOOT_SERVICES->LocateProtocol
* [0x199b] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1c64]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x1c74]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1c94]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
* [0x1c84]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
## Module: IohSerialDxe
### Boot services:
* [0x149d] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x587] EFI_BOOT_SERVICES->HandleProtocol
* [0x43c] EFI_BOOT_SERVICES->OpenProtocol
* [0x551] EFI_BOOT_SERVICES->OpenProtocol
* [0x618] EFI_BOOT_SERVICES->OpenProtocol
* [0x6b7] EFI_BOOT_SERVICES->OpenProtocol
* [0x165f] EFI_BOOT_SERVICES->OpenProtocol
* [0x16be] EFI_BOOT_SERVICES->OpenProtocol
* [0x176d] EFI_BOOT_SERVICES->OpenProtocol
* [0x19fa] EFI_BOOT_SERVICES->OpenProtocol
* [0x4fd] EFI_BOOT_SERVICES->CloseProtocol
* [0x5cd] EFI_BOOT_SERVICES->CloseProtocol
* [0x5e5] EFI_BOOT_SERVICES->CloseProtocol
* [0x662] EFI_BOOT_SERVICES->CloseProtocol
* [0x17cd] EFI_BOOT_SERVICES->CloseProtocol
* [0x193c] EFI_BOOT_SERVICES->CloseProtocol
* [0x1954] EFI_BOOT_SERVICES->CloseProtocol
* [0x1909] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2930] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2971] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x688] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x2f90]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: Legacy8259
### Boot services:
* [0x8b7] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x43d] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* empty
## Module: MemorySubClass
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x4ca] EFI_BOOT_SERVICES->LocateProtocol
* [0x1686] EFI_BOOT_SERVICES->LocateProtocol
* [0x16d2] EFI_BOOT_SERVICES->LocateProtocol
* [0x171e] EFI_BOOT_SERVICES->LocateProtocol
* [0x176a] EFI_BOOT_SERVICES->LocateProtocol
* [0x1784] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2670]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0x2640]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x2620]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x2610]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x2650]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x2630]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
## Module: Metronome
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x41e] EFI_BOOT_SERVICES->LocateProtocol
* [0x446] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x1044]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMetronomeArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB2-6F42-11D4-BCE70080C73C8881
## Module: MonotonicCounterRuntimeDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x6de] EFI_BOOT_SERVICES->LocateProtocol
* [0x7bc] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x15c4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMonotonicCounterArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 1DA97072-BDDC-4B30-99F172A0B56FFF2A
## Module: NullMemoryTestDxe
### Boot services:
* [0x5f7] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* empty
## Module: OhciDxe
### Boot services:
* [0x2b57] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2cd5] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x471] EFI_BOOT_SERVICES->OpenProtocol
* [0x2a06] EFI_BOOT_SERVICES->OpenProtocol
* [0x2d2b] EFI_BOOT_SERVICES->OpenProtocol
* [0x42bd] EFI_BOOT_SERVICES->OpenProtocol
* [0x5148] EFI_BOOT_SERVICES->OpenProtocol
* [0x4c6] EFI_BOOT_SERVICES->CloseProtocol
* [0x2c69] EFI_BOOT_SERVICES->CloseProtocol
* [0x2d52] EFI_BOOT_SERVICES->CloseProtocol
* [0x515e] EFI_BOOT_SERVICES->CloseProtocol
* [0x5054] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5095] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2c21] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x5b38]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiUsbHcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F5089266-1AA0-4953-97D8562F8A73B519
* [0x5b48]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x5b48]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
## Module: PartitionDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x453] EFI_BOOT_SERVICES->OpenProtocol
* [0x495] EFI_BOOT_SERVICES->OpenProtocol
* [0x4b3] EFI_BOOT_SERVICES->OpenProtocol
* [0x4e6] EFI_BOOT_SERVICES->OpenProtocol
* [0x7ae] EFI_BOOT_SERVICES->OpenProtocol
* [0x7d4] EFI_BOOT_SERVICES->OpenProtocol
* [0x8d0] EFI_BOOT_SERVICES->OpenProtocol
* [0x93f] EFI_BOOT_SERVICES->OpenProtocol
* [0x9b9] EFI_BOOT_SERVICES->OpenProtocol
* [0x9fb] EFI_BOOT_SERVICES->OpenProtocol
* [0x1121] EFI_BOOT_SERVICES->OpenProtocol
* [0x5a2] EFI_BOOT_SERVICES->CloseProtocol
* [0x5b7] EFI_BOOT_SERVICES->CloseProtocol
* [0x5cf] EFI_BOOT_SERVICES->CloseProtocol
* [0x746] EFI_BOOT_SERVICES->CloseProtocol
* [0x75e] EFI_BOOT_SERVICES->CloseProtocol
* [0x779] EFI_BOOT_SERVICES->CloseProtocol
* [0x81a] EFI_BOOT_SERVICES->CloseProtocol
* [0x99c] EFI_BOOT_SERVICES->CloseProtocol
* [0x9e0] EFI_BOOT_SERVICES->CloseProtocol
* [0x10c9] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x10f6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3580] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x35c1] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x86f] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x8a4] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x3c38]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: PcdDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x8b0] EFI_BOOT_SERVICES->LocateProtocol
* [0x8e9] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x29d4]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: PchSpiRuntime
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x2331] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x28e6] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a2e] EFI_BOOT_SERVICES->LocateProtocol
* [0x3146] EFI_BOOT_SERVICES->LocateProtocol
* [0x3745] EFI_BOOT_SERVICES->LocateProtocol
* [0x3878] EFI_BOOT_SERVICES->LocateProtocol
* [0x39aa] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b00] EFI_BOOT_SERVICES->LocateProtocol
* [0x7a6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x3cd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x3ce0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3d20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
* [0x3d00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x3d30]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 1156EFC6-EA32-4396-B5D526932E83C313
## Module: PchSpiSmm
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x66d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2328] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x179f] EFI_BOOT_SERVICES->LocateProtocol
* [0x193d] EFI_BOOT_SERVICES->LocateProtocol
* [0x27a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x28ed] EFI_BOOT_SERVICES->LocateProtocol
* [0x3025] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3850]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] D9072C35-EB8F-43AD-A22034D40E2A8285
* [0x3820]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3810]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x3800]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x3830]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
## Module: PciBusDxe
### Boot services:
* [0x74b] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x27d0] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x2641] EFI_BOOT_SERVICES->HandleProtocol
* [0x2685] EFI_BOOT_SERVICES->HandleProtocol
* [0x3457] EFI_BOOT_SERVICES->HandleProtocol
* [0xb611] EFI_BOOT_SERVICES->HandleProtocol
* [0x43c] EFI_BOOT_SERVICES->OpenProtocol
* [0x4b6] EFI_BOOT_SERVICES->OpenProtocol
* [0x5b4] EFI_BOOT_SERVICES->OpenProtocol
* [0xb37] EFI_BOOT_SERVICES->OpenProtocol
* [0xb8f] EFI_BOOT_SERVICES->OpenProtocol
* [0xca8] EFI_BOOT_SERVICES->OpenProtocol
* [0xcfb] EFI_BOOT_SERVICES->OpenProtocol
* [0x1015] EFI_BOOT_SERVICES->OpenProtocol
* [0x1055] EFI_BOOT_SERVICES->OpenProtocol
* [0x2714] EFI_BOOT_SERVICES->OpenProtocol
* [0x2743] EFI_BOOT_SERVICES->OpenProtocol
* [0x281a] EFI_BOOT_SERVICES->OpenProtocol
* [0x2936] EFI_BOOT_SERVICES->OpenProtocol
* [0x2a62] EFI_BOOT_SERVICES->OpenProtocol
* [0x3ac5] EFI_BOOT_SERVICES->OpenProtocol
* [0x9e8d] EFI_BOOT_SERVICES->OpenProtocol
* [0x9f6a] EFI_BOOT_SERVICES->OpenProtocol
* [0x499] EFI_BOOT_SERVICES->CloseProtocol
* [0x4d9] EFI_BOOT_SERVICES->CloseProtocol
* [0x665] EFI_BOOT_SERVICES->CloseProtocol
* [0x67a] EFI_BOOT_SERVICES->CloseProtocol
* [0xbfc] EFI_BOOT_SERVICES->CloseProtocol
* [0x510] EFI_BOOT_SERVICES->LocateProtocol
* [0x534] EFI_BOOT_SERVICES->LocateProtocol
* [0x562] EFI_BOOT_SERVICES->LocateProtocol
* [0x2c13] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b1c] EFI_BOOT_SERVICES->LocateProtocol
* [0x89be] EFI_BOOT_SERVICES->LocateProtocol
* [0xa23c] EFI_BOOT_SERVICES->LocateProtocol
* [0x94b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa38] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xab8] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb70b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb74c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa64] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xae4] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xb0e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xc7f] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xcc6] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0xc3dc]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiPciHotPlugRequestProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 19CB87AB-2CB9-4665-8360DDCF6054F79D
* [0xc33c]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiPciEnumerationCompleteProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 30CFE3E7-3DE1-4586-BE20DEABA1B3B793
* [0xc36c]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciHostBridgeResourceAllocationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CF8034BE-6768-4D8B-B7397CCE683A9FBE
* [0xc3cc]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xc32c]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0xc31c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiIncompatiblePciDeviceSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EB23F55A-7863-4AC2-8D3D956535DE0375
* [0xc35c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 07D75280-27D4-4D69-90D05643E238B341
* [0xc34c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciOverrideProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B5B35764-460C-4A06-99FC77A17C1B5CEB
* [0xc38c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDecompressProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D8117CFE-94A6-11D4-9A3A0090273FC14D
* [0xc2fc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDevicePathToTextProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8B843E20-8132-4852-90CC551A4E4A7F1C
* [0xc37c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciHotPlugInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AA0E8BC1-DABC-46B0-A84437B8169B2BEA
* [0xc3bc]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: PciHostBridge
### Boot services:
* [0x1502] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x1408] EFI_BOOT_SERVICES->LocateProtocol
* [0x2dc0] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e0c] EFI_BOOT_SERVICES->LocateProtocol
* [0x184d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x3c88]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiPciHostBridgeResourceAllocationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CF8034BE-6768-4D8B-B7397CCE683A9FBE
* [0x3cb8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] A7CED760-C71C-4E1A-ACB189604D5216CB
* [0x3cd8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMetronomeArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB2-6F42-11D4-BCE70080C73C8881
* [0x3cc8]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CPU_IO_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] B0732526-38C8-4B40-887761C7B06AAC45
* [0x3ca8]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: PciPlatform
### Boot services:
* [0x51c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x462] EFI_BOOT_SERVICES->HandleProtocol
* [0x829] EFI_BOOT_SERVICES->HandleProtocol
* [0x8dd] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* empty
## Module: PcRtc
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x6b3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: PiSmmCommunicationSmm
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x8cb] EFI_BOOT_SERVICES->LocateProtocol
* [0xef2] EFI_BOOT_SERVICES->LocateProtocol
* [0x1090] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1668]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x1648]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1638]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
## Module: PiSmmCore
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x19e2] EFI_BOOT_SERVICES->HandleProtocol
* [0x22bf] EFI_BOOT_SERVICES->HandleProtocol
* [0x24c7] EFI_BOOT_SERVICES->HandleProtocol
* [0x25ff] EFI_BOOT_SERVICES->HandleProtocol
* [0x2630] EFI_BOOT_SERVICES->HandleProtocol
* [0x25ab] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x197d] EFI_BOOT_SERVICES->LocateProtocol
* [0x19a1] EFI_BOOT_SERVICES->LocateProtocol
* [0x2659] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e7f] EFI_BOOT_SERVICES->LocateProtocol
* [0x376d] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d8b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x6784]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSecurity2ArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 94AB2F58-1438-4EF1-915218941A3A0E68
* [0x6794]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSecurityArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A46423E3-4617-49F1-B9FFD1BFA9115839
* [0x6754]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x6774]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
## Module: PiSmmCpuDxeSmm
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x189c] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x18e9] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1936] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3c9c] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x11fb] EFI_BOOT_SERVICES->LocateProtocol
* [0x148c] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f7f] EFI_BOOT_SERVICES->LocateProtocol
* [0x644e] EFI_BOOT_SERVICES->LocateProtocol
* [0x64d0] EFI_BOOT_SERVICES->LocateProtocol
* [0x6706] EFI_BOOT_SERVICES->LocateProtocol
* [0x687c] EFI_BOOT_SERVICES->LocateProtocol
* [0x184c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x19f1] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x8ecc]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSmmCpuServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 1D202CAB-C8AB-4D5C-94F73CFCC0D3D335
* [0x8f3c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x8f2c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3FDDA605-A76E-4F46-AD2912F4531B3D08
* [0x8e9c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
* [0x8eac]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
* [0x8e8c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x8f1c]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiSmmConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26EEB3DE-B689-492E-80F0BE8BD7DA4BA7
## Module: PiSmmIpl
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x344e] EFI_BOOT_SERVICES->HandleProtocol
* [0x352a] EFI_BOOT_SERVICES->HandleProtocol
* [0x2281] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x34f2] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x872] EFI_BOOT_SERVICES->LocateProtocol
* [0x92d] EFI_BOOT_SERVICES->LocateProtocol
* [0xde8] EFI_BOOT_SERVICES->LocateProtocol
* [0xe34] EFI_BOOT_SERVICES->LocateProtocol
* [0xe86] EFI_BOOT_SERVICES->LocateProtocol
* [0x1169] EFI_BOOT_SERVICES->LocateProtocol
* [0x139f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x37d4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x3804]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x37e4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmControl2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 843DC720-AB1E-42CB-93578A0078F3561B
* [0x37f4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26EEB3DE-B689-492E-80F0BE8BD7DA4BA7
* [0x37c4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB1-6F42-11D4-BCE70080C73C8881
## Module: PlatformInitDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xdca] EFI_BOOT_SERVICES->HandleProtocol
* [0x258d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x807] EFI_BOOT_SERVICES->LocateProtocol
* [0x8de] EFI_BOOT_SERVICES->LocateProtocol
* [0xa22] EFI_BOOT_SERVICES->LocateProtocol
* [0xc59] EFI_BOOT_SERVICES->LocateProtocol
* [0xebf] EFI_BOOT_SERVICES->LocateProtocol
* [0x1767] EFI_BOOT_SERVICES->LocateProtocol
* [0x18ce] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a0c] EFI_BOOT_SERVICES->LocateProtocol
* [0x29cc] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b14] EFI_BOOT_SERVICES->LocateProtocol
* [0x39ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b0b] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c3e] EFI_BOOT_SERVICES->LocateProtocol
* [0x3d70] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ec6] EFI_BOOT_SERVICES->LocateProtocol
* [0x69a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x7a7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xf0a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x4260]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 855B7D58-874B-47EB-A5CF98EDAC806796
* [0x4280]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26EEB3DE-B689-492E-80F0BE8BD7DA4BA7
* [0x4290]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB1-6F42-11D4-BCE70080C73C8881
* [0x4270]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 7A5DBC75-5B2B-4E67-BDE1D48EEE761562
* [0x42b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 41C7F059-081A-4F45-B1F0C5A988915221
* [0x4220]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 1156EFC6-EA32-4396-B5D526932E83C313
* [0x42d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 171E9398-269C-4081-90993844E260466C
* [0x41e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x4200]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x4240]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
* [0x41f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
## Module: QNCInitDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x29aa] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xc7d] EFI_BOOT_SERVICES->LocateProtocol
* [0x1712] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a1a] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a3e] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a8a] EFI_BOOT_SERVICES->LocateProtocol
* [0x2db2] EFI_BOOT_SERVICES->LocateProtocol
* [0x2efa] EFI_BOOT_SERVICES->LocateProtocol
* [0x49d1] EFI_BOOT_SERVICES->LocateProtocol
* [0x4d8a] EFI_BOOT_SERVICES->LocateProtocol
* [0x4ebd] EFI_BOOT_SERVICES->LocateProtocol
* [0x4fef] EFI_BOOT_SERVICES->LocateProtocol
* [0x5145] EFI_BOOT_SERVICES->LocateProtocol
* [0xe60] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x13f2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x173a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1c15] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x539c]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_PCH_S3_SUPPORT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] E287D20B-D897-4E1E-A5D9977763936A04
* [0x53bc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyInterruptProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31CE593D-108A-485D-ADB278F21F2966BE
* [0x53dc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTimerArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB3-6F42-11D4-BCE70080C73C8881
* [0x53ac]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB1-6F42-11D4-BCE70080C73C8881
* [0x53cc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacy8259ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 38321DBA-4FE0-4E17-8AEC413055EAEDC1
* [0x534c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x535c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x537c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
* [0x536c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x568c]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 00000000-0200-0604-080A0C0E1018506E
## Module: QncS3Support
### Boot services:
* [0x7d4] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x13d9] EFI_BOOT_SERVICES->HandleProtocol
* [0x148d] EFI_BOOT_SERVICES->HandleProtocol
* [0x1028] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x155d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x628] EFI_BOOT_SERVICES->LocateProtocol
* [0x9ff] EFI_BOOT_SERVICES->LocateProtocol
* [0xbc1] EFI_BOOT_SERVICES->LocateProtocol
* [0xc43] EFI_BOOT_SERVICES->LocateProtocol
* [0x11a1] EFI_BOOT_SERVICES->LocateProtocol
* [0x12d4] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a04] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b4c] EFI_BOOT_SERVICES->LocateProtocol
* [0xaa2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x5014]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C7EA9787-CA0A-43B4-B1E525EF87391F8D
* [0x4fa4]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] D088A413-0A70-4217-BA559A3CB65C41B3
* [0x5014]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C7EA9787-CA0A-43B4-B1E525EF87391F8D
* [0x4f84]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
* [0x4f94]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
* [0x4f74]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x4f44]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x4f54]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x4fc4]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] EFI_PCH_S3_SUPPORT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] E287D20B-D897-4E1E-A5D9977763936A04
## Module: QNCSmmDispatcher
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x94f] EFI_BOOT_SERVICES->HandleProtocol
* [0x9ab] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x142a] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2fbf] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x267a] EFI_BOOT_SERVICES->LocateProtocol
* [0x27af] EFI_BOOT_SERVICES->LocateProtocol
* [0x33fe] EFI_BOOT_SERVICES->LocateProtocol
* [0x3546] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a78] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x40b4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x40a4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x4094]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x40c4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
## Module: ReportStatusCodeRouterRuntimeDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xbc3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: ReportStatusCodeRouterSmm
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x72b] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x774] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xd15] EFI_BOOT_SERVICES->LocateProtocol
* [0xe4a] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1740]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1730]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
## Module: ResetSystemRuntimeDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x5ba] EFI_BOOT_SERVICES->LocateProtocol
* [0x5eb] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x18a8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiResetArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 27CFAC88-46CC-11D4-9A380090273FC14D
## Module: RuntimeDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x951] EFI_BOOT_SERVICES->HandleProtocol
* [0x9cc] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: S3SaveStateDxe
### Boot services:
* [0x8fb] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xccf] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x110e] EFI_BOOT_SERVICES->LocateProtocol
* [0x1256] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a79] EFI_BOOT_SERVICES->LocateProtocol
* [0x2beb] EFI_BOOT_SERVICES->LocateProtocol
* [0x2d1e] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e50] EFI_BOOT_SERVICES->LocateProtocol
* [0x2fa6] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3290]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x32a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x32d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
* [0x32c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
## Module: SaveMemoryConfig
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* empty
## Module: SDController
### Boot services:
* [0x152f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1611] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x433] EFI_BOOT_SERVICES->OpenProtocol
* [0x140e] EFI_BOOT_SERVICES->OpenProtocol
* [0x15c4] EFI_BOOT_SERVICES->OpenProtocol
* [0x16ed] EFI_BOOT_SERVICES->OpenProtocol
* [0x1f8f] EFI_BOOT_SERVICES->OpenProtocol
* [0x47d] EFI_BOOT_SERVICES->CloseProtocol
* [0x163d] EFI_BOOT_SERVICES->CloseProtocol
* [0x1fa5] EFI_BOOT_SERVICES->CloseProtocol
* [0x1e9b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1edc] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x281c]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] B63F8EC7-A9C9-4472-A4C04D8BF365CC51
* [0x282c]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
## Module: SDMediaDevice
### Boot services:
* [0x603] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x73c] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x433] EFI_BOOT_SERVICES->OpenProtocol
* [0x6fa] EFI_BOOT_SERVICES->OpenProtocol
* [0x7d8] EFI_BOOT_SERVICES->OpenProtocol
* [0x3053] EFI_BOOT_SERVICES->OpenProtocol
* [0x7a1] EFI_BOOT_SERVICES->CloseProtocol
* [0x7f6] EFI_BOOT_SERVICES->CloseProtocol
* [0x392c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x396d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x41d8]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x41e8]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] B63F8EC7-A9C9-4472-A4C04D8BF365CC51
## Module: SectionExtractionDxe
### Boot services:
* [0x3a6] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x60d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x7e4] EFI_BOOT_SERVICES->LocateProtocol
* [0x94f] EFI_BOOT_SERVICES->LocateProtocol
* [0x10af] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1dc8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDecompressProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D8117CFE-94A6-11D4-9A3A0090273FC14D
## Module: SecurityStubDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xb38] EFI_BOOT_SERVICES->OpenProtocol
* [0xb8f] EFI_BOOT_SERVICES->OpenProtocol
* [0x4ac] EFI_BOOT_SERVICES->LocateProtocol
* [0x4dd] EFI_BOOT_SERVICES->LocateProtocol
* [0x9fe] EFI_BOOT_SERVICES->LocateProtocol
* [0xab7] EFI_BOOT_SERVICES->LocateProtocol
* [0x511] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x1798]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSecurity2ArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 94AB2F58-1438-4EF1-915218941A3A0E68
* [0x17a8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSecurityArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A46423E3-4617-49F1-B9FFD1BFA9115839
* [0x1738]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDevicePathToTextProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8B843E20-8132-4852-90CC551A4E4A7F1C
* [0x1728]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 122B109B-DB9B-4F03-969C17F14E10FECD
## Module: SetupBrowser
### Boot services:
* [0x458e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4644] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x2b6f] EFI_BOOT_SERVICES->HandleProtocol
* [0x128ce] EFI_BOOT_SERVICES->HandleProtocol
* [0x4404] EFI_BOOT_SERVICES->LocateProtocol
* [0x4450] EFI_BOOT_SERVICES->LocateProtocol
* [0x449c] EFI_BOOT_SERVICES->LocateProtocol
* [0x7696] EFI_BOOT_SERVICES->LocateProtocol
* [0x83ef] EFI_BOOT_SERVICES->LocateProtocol
* [0x14ab7] EFI_BOOT_SERVICES->LocateProtocol
* [0x14b03] EFI_BOOT_SERVICES->LocateProtocol
* [0x14b4f] EFI_BOOT_SERVICES->LocateProtocol
* [0x14b9b] EFI_BOOT_SERVICES->LocateProtocol
* [0x14bb5] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x16a20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiHiiConfigAccessProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 330D4706-F2A0-4E4F-A369B66FA8D54385
* [0x169d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x16a10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x169e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x169c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiUnicodeCollation2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A4C751FC-23AE-4C3E-92E94964CF63F349
* [0x169b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiUserManagerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6FD5B00C-D426-4283-98876CF5CF1CB1FE
* [0x16980]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x16970]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
## Module: SmbiosDxe
### Boot services:
* [0x113c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* empty
## Module: SmbiosMisc
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x46c] EFI_BOOT_SERVICES->LocateProtocol
* [0x8ff] EFI_BOOT_SERVICES->LocateProtocol
* [0x190c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3860] EFI_BOOT_SERVICES->LocateProtocol
* [0x38ac] EFI_BOOT_SERVICES->LocateProtocol
* [0x38f8] EFI_BOOT_SERVICES->LocateProtocol
* [0x3944] EFI_BOOT_SERVICES->LocateProtocol
* [0x395e] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x517c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0x516c]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 171E9398-269C-4081-90993844E260466C
* [0x513c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x511c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x510c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x514c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x512c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
## Module: SMIFlashDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x2560] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1c18] EFI_BOOT_SERVICES->LocateProtocol
* [0x1de2] EFI_BOOT_SERVICES->LocateProtocol
* [0x2968] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ab0] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f2c] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x33ac]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x338c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x337c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x339c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
## Module: SmmAccess
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xeea] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x548] EFI_BOOT_SERVICES->LocateProtocol
* [0x1448] EFI_BOOT_SERVICES->LocateProtocol
* [0x1590] EFI_BOOT_SERVICES->LocateProtocol
* [0x1bfa] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f5f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2092] EFI_BOOT_SERVICES->LocateProtocol
* [0x6c0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x23c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0x2360]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x2370]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2390]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
* [0x2380]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
## Module: SmmControlDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x697] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: SmmFaultTolerantWriteDxe
### Boot services:
* [0x5fe] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x5ae] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2fb1] EFI_BOOT_SERVICES->LocateProtocol
* [0x30e6] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x37c8]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiSmmFaultTolerantWriteProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3868FC3B-7E45-43A7-906C4BA47DE1754D
* [0x37c8]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSmmFaultTolerantWriteProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3868FC3B-7E45-43A7-906C4BA47DE1754D
* [0x37a8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3798]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
## Module: SmmLockBox
### Boot services:
* [0xa5b] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x8ad] EFI_BOOT_SERVICES->LocateProtocol
* [0xedd] EFI_BOOT_SERVICES->LocateProtocol
* [0x107b] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1e90]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiLockBoxProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BD445D79-B7AD-4F04-9AD829BD2040EB3C
* [0x1ea0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x1e70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: SmmPowerManagement
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x9d8] EFI_BOOT_SERVICES->HandleProtocol
* [0x17af] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x9a9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x703] EFI_BOOT_SERVICES->LocateProtocol
* [0x74f] EFI_BOOT_SERVICES->LocateProtocol
* [0x79b] EFI_BOOT_SERVICES->LocateProtocol
* [0xf89] EFI_BOOT_SERVICES->LocateProtocol
* [0x10be] EFI_BOOT_SERVICES->LocateProtocol
* [0x1bee] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d36] EFI_BOOT_SERVICES->LocateProtocol
* [0x2436] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x27f4]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
* [0x27c4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EB97088E-CFDF-49C6-BE4BD906A5B20E86
* [0x27b4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x27d4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3FDDA605-A76E-4F46-AD2912F4531B3D08
* [0x2784]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2774]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x2754]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x2794]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 13A3F0F6-264A-3EF0-F2E0DEC512342F34
## Module: SmmRuntime
### Boot services:
* [0xddc] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xa40] EFI_BOOT_SERVICES->LocateProtocol
* [0xc2a] EFI_BOOT_SERVICES->LocateProtocol
* [0x1295] EFI_BOOT_SERVICES->LocateProtocol
* [0x1433] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1a20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1a00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x1a10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
## Module: StatusCodeHandlerRuntimeDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x760] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3034]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiRscHandlerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 86212936-0E76-41C8-A03A2AF2FC1C39E2
## Module: StatusCodeHandlerSmm
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xf46] EFI_BOOT_SERVICES->LocateProtocol
* [0x107b] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2ac4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2ab4]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
## Module: TerminalDxe
### Boot services:
* [0x14ac] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1722] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xad2] EFI_BOOT_SERVICES->HandleProtocol
* [0x43c] EFI_BOOT_SERVICES->OpenProtocol
* [0x51b] EFI_BOOT_SERVICES->OpenProtocol
* [0xb04] EFI_BOOT_SERVICES->OpenProtocol
* [0xbc9] EFI_BOOT_SERVICES->OpenProtocol
* [0xc7d] EFI_BOOT_SERVICES->OpenProtocol
* [0xe52] EFI_BOOT_SERVICES->OpenProtocol
* [0xe8a] EFI_BOOT_SERVICES->OpenProtocol
* [0xec8] EFI_BOOT_SERVICES->OpenProtocol
* [0x14da] EFI_BOOT_SERVICES->OpenProtocol
* [0x1578] EFI_BOOT_SERVICES->OpenProtocol
* [0x15d3] EFI_BOOT_SERVICES->OpenProtocol
* [0x1954] EFI_BOOT_SERVICES->OpenProtocol
* [0x455a] EFI_BOOT_SERVICES->OpenProtocol
* [0x4fe] EFI_BOOT_SERVICES->CloseProtocol
* [0x544] EFI_BOOT_SERVICES->CloseProtocol
* [0xb7b] EFI_BOOT_SERVICES->CloseProtocol
* [0xb93] EFI_BOOT_SERVICES->CloseProtocol
* [0xc13] EFI_BOOT_SERVICES->CloseProtocol
* [0x4570] EFI_BOOT_SERVICES->CloseProtocol
* [0xfac] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x150c] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x45c7] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x16f9] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4466] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x44a7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb4e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xc4e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x4ef0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x4ec0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x4ec0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x4ef0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x4f00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSerialIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BB25CF6F-F1D4-11D2-9A0C0090273FC1FD
* [0x4f80]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 9E863906-A40F-4875-977F5B93FF237FC6
* [0x4ee0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
* [0x4ee0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
## Module: UsbBusDxe
### Boot services:
* [0x1281] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xb5c] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1403] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d3f] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d94] EFI_BOOT_SERVICES->HandleProtocol
* [0x9dd] EFI_BOOT_SERVICES->OpenProtocol
* [0xa6c] EFI_BOOT_SERVICES->OpenProtocol
* [0x1059] EFI_BOOT_SERVICES->OpenProtocol
* [0x10bd] EFI_BOOT_SERVICES->OpenProtocol
* [0x110c] EFI_BOOT_SERVICES->OpenProtocol
* [0x1194] EFI_BOOT_SERVICES->OpenProtocol
* [0x11eb] EFI_BOOT_SERVICES->OpenProtocol
* [0x1211] EFI_BOOT_SERVICES->OpenProtocol
* [0x14bf] EFI_BOOT_SERVICES->OpenProtocol
* [0x1538] EFI_BOOT_SERVICES->OpenProtocol
* [0x1595] EFI_BOOT_SERVICES->OpenProtocol
* [0x2537] EFI_BOOT_SERVICES->OpenProtocol
* [0xb7a] EFI_BOOT_SERVICES->CloseProtocol
* [0xb9b] EFI_BOOT_SERVICES->CloseProtocol
* [0xbb6] EFI_BOOT_SERVICES->CloseProtocol
* [0x10ec] EFI_BOOT_SERVICES->CloseProtocol
* [0x112f] EFI_BOOT_SERVICES->CloseProtocol
* [0x1424] EFI_BOOT_SERVICES->CloseProtocol
* [0x1448] EFI_BOOT_SERVICES->CloseProtocol
* [0x1466] EFI_BOOT_SERVICES->CloseProtocol
* [0x257a] EFI_BOOT_SERVICES->CloseProtocol
* [0x2ce4] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3927] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5486] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x54c7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3810] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x397c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x5a5c]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 240612B7-A063-11D4-9A3A0090273FC14D
* [0x5a1c]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x5a0c]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUsb2HcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3E745226-9818-45B6-A2ACD7CD0E8BA2BC
* [0x59fc]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUsbHcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F5089266-1AA0-4953-97D8562F8A73B519
* [0x5a0c]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUsb2HcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3E745226-9818-45B6-A2ACD7CD0E8BA2BC
* [0x59fc]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUsbHcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F5089266-1AA0-4953-97D8562F8A73B519
* [0x5a1c]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: UsbKbDxe
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x4ce] EFI_BOOT_SERVICES->OpenProtocol
* [0x548] EFI_BOOT_SERVICES->OpenProtocol
* [0x59c] EFI_BOOT_SERVICES->OpenProtocol
* [0xe63] EFI_BOOT_SERVICES->OpenProtocol
* [0xe8f] EFI_BOOT_SERVICES->OpenProtocol
* [0x2305] EFI_BOOT_SERVICES->OpenProtocol
* [0x2355] EFI_BOOT_SERVICES->OpenProtocol
* [0x502] EFI_BOOT_SERVICES->CloseProtocol
* [0x8f6] EFI_BOOT_SERVICES->CloseProtocol
* [0xf12] EFI_BOOT_SERVICES->CloseProtocol
* [0x2324] EFI_BOOT_SERVICES->CloseProtocol
* [0x118e] EFI_BOOT_SERVICES->LocateProtocol
* [0x121c] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e6f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ebb] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f07] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f53] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f6d] EFI_BOOT_SERVICES->LocateProtocol
* [0x781] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2fc9] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x7ff] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xf34] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x3f68]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0x3f58]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x3f68]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0x3f28]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x3ef8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x3ed8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x3f08]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x3ee8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0x3f48]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
## Module: UsbMassStorageDxe
### Boot services:
* [0x182c] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x43a] EFI_BOOT_SERVICES->OpenProtocol
* [0x7fb] EFI_BOOT_SERVICES->OpenProtocol
* [0x902] EFI_BOOT_SERVICES->OpenProtocol
* [0x9cc] EFI_BOOT_SERVICES->OpenProtocol
* [0xac1] EFI_BOOT_SERVICES->OpenProtocol
* [0xd42] EFI_BOOT_SERVICES->OpenProtocol
* [0xe6c] EFI_BOOT_SERVICES->OpenProtocol
* [0x1073] EFI_BOOT_SERVICES->OpenProtocol
* [0x10b2] EFI_BOOT_SERVICES->OpenProtocol
* [0x4a3] EFI_BOOT_SERVICES->CloseProtocol
* [0x817] EFI_BOOT_SERVICES->CloseProtocol
* [0x82c] EFI_BOOT_SERVICES->CloseProtocol
* [0x8ac] EFI_BOOT_SERVICES->CloseProtocol
* [0x94f] EFI_BOOT_SERVICES->CloseProtocol
* [0xb47] EFI_BOOT_SERVICES->CloseProtocol
* [0xe05] EFI_BOOT_SERVICES->CloseProtocol
* [0xfab] EFI_BOOT_SERVICES->CloseProtocol
* [0x10ed] EFI_BOOT_SERVICES->CloseProtocol
* [0x1124] EFI_BOOT_SERVICES->CloseProtocol
* [0x1139] EFI_BOOT_SERVICES->CloseProtocol
* [0xcfc] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xf70] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3457] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3498] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x88c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x97f] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xd8e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x3ac8]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0x3ac8]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0x3aa8]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
## Module: UsbMouseDxe
### Boot services:
* [0xb61] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4eb] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xbd0] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x45f] EFI_BOOT_SERVICES->OpenProtocol
* [0x7dc] EFI_BOOT_SERVICES->OpenProtocol
* [0x9bd] EFI_BOOT_SERVICES->OpenProtocol
* [0xa1d] EFI_BOOT_SERVICES->OpenProtocol
* [0xd18] EFI_BOOT_SERVICES->OpenProtocol
* [0xd68] EFI_BOOT_SERVICES->OpenProtocol
* [0x507] EFI_BOOT_SERVICES->CloseProtocol
* [0x810] EFI_BOOT_SERVICES->CloseProtocol
* [0xc72] EFI_BOOT_SERVICES->CloseProtocol
* [0xd37] EFI_BOOT_SERVICES->CloseProtocol
* [0x18b5] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x18f6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x261c]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31878C87-0B75-11D5-9A4F0090273FC14D
* [0x263c]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0x262c]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x263c]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
## Module: VariableSmm
### Boot services:
* [0x6f0] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xb52] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0xab5] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3b3c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c71] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x470c]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x46fc]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
## Module: VariableSmmRuntimeDxe
### Boot services:
* [0x631] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x761] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x1aec] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x611] EFI_BOOT_SERVICES->LocateProtocol
* [0x685] EFI_BOOT_SERVICES->LocateProtocol
* [0x6a8] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1da0]
	 - [service] LocateProtocol
	 - [protocol_name] gSmmVariableWriteGuid
	 - [protocol_place] edk2_guids
	 - [guid] 93BA1826-DFFB-45DD-82A7E7DCAA3BBDF3
* [0x1d10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmVariableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] ED32D533-99E6-4209-9CC02D72CDD998A7
* [0x1d20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
## Module: WatchdogTimer
### Boot services:
* [0x2be] EFI_BOOT_SERVICES->HandleProtocol
* [0x509] EFI_BOOT_SERVICES->LocateProtocol
* [0x583] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xe80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiWatchdogTimerArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 665E3FF5-46CC-11D4-9A380090273FC14D
