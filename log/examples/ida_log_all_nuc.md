## Module: Acoustic
### Boot services:
* [0x32a] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* empty
## Module: ACPI
### Boot services:
* [0x2001] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x2094] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x5ccf] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xb42] EFI_BOOT_SERVICES->HandleProtocol
* [0x1feb] EFI_BOOT_SERVICES->HandleProtocol
* [0x2227] EFI_BOOT_SERVICES->HandleProtocol
* [0x41ef] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xb0b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1f9f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x21e6] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xdc9] EFI_BOOT_SERVICES->LocateProtocol
* [0x17b1] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b4d] EFI_BOOT_SERVICES->LocateProtocol
* [0x33a4] EFI_BOOT_SERVICES->LocateProtocol
* [0x381b] EFI_BOOT_SERVICES->LocateProtocol
* [0x39cb] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b67] EFI_BOOT_SERVICES->LocateProtocol
* [0x3f8e] EFI_BOOT_SERVICES->LocateProtocol
* [0x41a0] EFI_BOOT_SERVICES->LocateProtocol
* [0x63ab] EFI_BOOT_SERVICES->LocateProtocol
* [0xfa7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x6620]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x6de8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0x6df8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x6630]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB1-6F42-11D4-BCE70080C73C8881
* [0x6df8]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x6e18]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_ACPI_SUPPORT_GUID
	 - [protocol_place] edk_guids
	 - [guid] DBFF9D55-89B7-46DA-BDDF677D3DC0241D
* [0x6d18]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x6cb8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x6758]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] F109F361-370C-4D9C-B1AB7CA2D4C8B3FF
* [0x6748]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_CPU_INFO_2_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] AC9CF0A8-E551-4BE2-AD0AE1B564EEA273
* [0x6610]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 4FC0733F-6FD2-491B-A8905374521BF48F
* [0x6630]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB1-6F42-11D4-BCE70080C73C8881
* [0x6600]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: AcpiDebugTable
### Boot services:
* [0x39f] EFI_BOOT_SERVICES->HandleProtocol
* [0x36a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x340] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x24f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x24f0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x2500]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
## Module: AcpiModeEnable
### Boot services:
* [0x8fb] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x943] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x39a] EFI_BOOT_SERVICES->LocateProtocol
* [0x421] EFI_BOOT_SERVICES->LocateProtocol
* [0x807] EFI_BOOT_SERVICES->LocateProtocol
* [0x9df] EFI_BOOT_SERVICES->LocateProtocol
* [0xe31] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1400]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1430]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x1988]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1420]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: AcpiPlatform
### Boot services:
* [0x57a] EFI_BOOT_SERVICES->HandleProtocol
* [0x1e61] EFI_BOOT_SERVICES->HandleProtocol
* [0x3c5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x435] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1ad3] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1b42] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1e04] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x330] EFI_BOOT_SERVICES->LocateProtocol
* [0x717] EFI_BOOT_SERVICES->LocateProtocol
* [0x735] EFI_BOOT_SERVICES->LocateProtocol
* [0x22ea] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b4e] EFI_BOOT_SERVICES->LocateProtocol
* [0x62d9] EFI_BOOT_SERVICES->LocateProtocol
* [0x62f4] EFI_BOOT_SERVICES->LocateProtocol
* [0x649b] EFI_BOOT_SERVICES->LocateProtocol
* [0x7d37] EFI_BOOT_SERVICES->LocateProtocol
* [0x8097] EFI_BOOT_SERVICES->LocateProtocol
* [0x5f18] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xdd90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xdd50]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0xdd60]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0xdd90]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xddd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xde00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0xdd70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0xdd80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3FDDA605-A76E-4F46-AD2912F4531B3D08
* [0xdda0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AD61F191-AE5F-4C0E-B9FAE869D288C64F
* [0xdd50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0xddf0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EB97088E-CFDF-49C6-BE4BD906A5B20E86
* [0xddc0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] AB5A4DF4-F0D7-49A8-BF5CF25DA04C2533
* [0xdde0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
* [0xddb0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
## Module: AcpiPlatformFeatures
### Boot services:
* [0x6f6] EFI_BOOT_SERVICES->HandleProtocol
* [0xdbd] EFI_BOOT_SERVICES->HandleProtocol
* [0xbd7] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xc46] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xd88] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x30b] EFI_BOOT_SERVICES->LocateProtocol
* [0x418] EFI_BOOT_SERVICES->LocateProtocol
* [0x7c6] EFI_BOOT_SERVICES->LocateProtocol
* [0xd5e] EFI_BOOT_SERVICES->LocateProtocol
* [0xf43] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1320]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x1310]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x1320]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x1340]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
* [0x1310]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x1330]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_PLATFORM_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] D9035175-8CE2-47DE-A8B8CC98E5E2A885
* [0x1350]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: AcpiS3SaveDxe
### Boot services:
* [0x366] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* empty
## Module: AcpiSmm
### Boot services:
* [0x34c] EFI_BOOT_SERVICES->LocateProtocol
* [0x37a] EFI_BOOT_SERVICES->LocateProtocol
* [0x4da] EFI_BOOT_SERVICES->LocateProtocol
* [0x504] EFI_BOOT_SERVICES->LocateProtocol
* [0x52e] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x910]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x920]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x8d0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
* [0x8e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] AB5A4DF4-F0D7-49A8-BF5CF25DA04C2533
* [0x8f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3DC21D75-DE0E-4300-A0AA19C41C0CF3DF
## Module: ActiveBios
### Boot services:
* [0x30e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: Ahci
### Boot services:
* [0xa15] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xb49] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x19c5] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1c79] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x9f7] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x17a8] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x9d7] EFI_BOOT_SERVICES->HandleProtocol
* [0xa4d] EFI_BOOT_SERVICES->HandleProtocol
* [0xa77] EFI_BOOT_SERVICES->HandleProtocol
* [0x103a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3e45] EFI_BOOT_SERVICES->HandleProtocol
* [0x3db] EFI_BOOT_SERVICES->OpenProtocol
* [0x480] EFI_BOOT_SERVICES->OpenProtocol
* [0x4b2] EFI_BOOT_SERVICES->OpenProtocol
* [0x52c] EFI_BOOT_SERVICES->OpenProtocol
* [0x593] EFI_BOOT_SERVICES->OpenProtocol
* [0x623] EFI_BOOT_SERVICES->OpenProtocol
* [0x678] EFI_BOOT_SERVICES->OpenProtocol
* [0x6e5] EFI_BOOT_SERVICES->OpenProtocol
* [0xadb] EFI_BOOT_SERVICES->OpenProtocol
* [0xe27] EFI_BOOT_SERVICES->OpenProtocol
* [0xe52] EFI_BOOT_SERVICES->OpenProtocol
* [0x11b4] EFI_BOOT_SERVICES->OpenProtocol
* [0x1226] EFI_BOOT_SERVICES->OpenProtocol
* [0x12d6] EFI_BOOT_SERVICES->OpenProtocol
* [0x1329] EFI_BOOT_SERVICES->OpenProtocol
* [0x1425] EFI_BOOT_SERVICES->OpenProtocol
* [0x146a] EFI_BOOT_SERVICES->OpenProtocol
* [0x14af] EFI_BOOT_SERVICES->OpenProtocol
* [0x14fa] EFI_BOOT_SERVICES->OpenProtocol
* [0x17db] EFI_BOOT_SERVICES->OpenProtocol
* [0x1804] EFI_BOOT_SERVICES->OpenProtocol
* [0x3bc1] EFI_BOOT_SERVICES->OpenProtocol
* [0x6e43] EFI_BOOT_SERVICES->OpenProtocol
* [0x6f4f] EFI_BOOT_SERVICES->OpenProtocol
* [0x403] EFI_BOOT_SERVICES->CloseProtocol
* [0x4fc] EFI_BOOT_SERVICES->CloseProtocol
* [0x76f] EFI_BOOT_SERVICES->CloseProtocol
* [0x11f8] EFI_BOOT_SERVICES->CloseProtocol
* [0x16fb] EFI_BOOT_SERVICES->CloseProtocol
* [0x178c] EFI_BOOT_SERVICES->CloseProtocol
* [0x6ed1] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x3df4] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x69a] EFI_BOOT_SERVICES->LocateProtocol
* [0x950] EFI_BOOT_SERVICES->LocateProtocol
* [0x98b] EFI_BOOT_SERVICES->LocateProtocol
* [0xf21] EFI_BOOT_SERVICES->LocateProtocol
* [0xf48] EFI_BOOT_SERVICES->LocateProtocol
* [0xf6f] EFI_BOOT_SERVICES->LocateProtocol
* [0xf96] EFI_BOOT_SERVICES->LocateProtocol
* [0x106d] EFI_BOOT_SERVICES->LocateProtocol
* [0x1718] EFI_BOOT_SERVICES->LocateProtocol
* [0x1754] EFI_BOOT_SERVICES->LocateProtocol
* [0x701c] EFI_BOOT_SERVICES->LocateProtocol
* [0x346] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xdeb] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xe78] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xebd] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x12fd] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1350] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1372] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x73a0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] AHCI_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B2FA4764-3B6E-43D3-91DF87D15A3E5668
* [0x7a10]
	 - [service] HandleProtocol
	 - [protocol_name] ONBOARD_RAID_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5D206DD3-516A-47DC-A1BC6DA204AABE08
* [0x7a20]
	 - [service] HandleProtocol
	 - [protocol_name] HDD_UNLOCKED_GUID
	 - [protocol_place] ami_guids
	 - [guid] 1FD29BE6-70D0-42A4-A6E7E5D10E6AC376
* [0x73e0]
	 - [service] HandleProtocol
	 - [protocol_name] IDE_SECURITY_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] F4F63529-281E-4040-A313C1D6766384BE
* [0x73a0]
	 - [service] HandleProtocol
	 - [protocol_name] AHCI_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B2FA4764-3B6E-43D3-91DF87D15A3E5668
* [0x73a0]
	 - [service] OpenProtocol
	 - [protocol_name] AHCI_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B2FA4764-3B6E-43D3-91DF87D15A3E5668
* [0x73c0]
	 - [service] OpenProtocol
	 - [protocol_name] IDE_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] E159A956-3299-4EE9-917665181A4E5E9F
* [0x7360]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A1E37052-80D9-4E65-A3173E9A55C43EC9
* [0x7340]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x7350]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x7380]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x7390]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0x73e0]
	 - [service] OpenProtocol
	 - [protocol_name] IDE_SECURITY_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] F4F63529-281E-4040-A313C1D6766384BE
* [0x7a40]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] B396DA3A-52B2-4CD6-A89A13E7C4AE9790
* [0x7410]
	 - [service] OpenProtocol
	 - [protocol_name] IDE_SMART_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] FFBD9AD2-F1DB-4F92-A649EB9EEDEA86B5
* [0x73d0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiStorageSecurityCommandProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C88B0B6D-0DFC-49A7-9CB449074B4C3A78
* [0x73a0]
	 - [service] CloseProtocol
	 - [protocol_name] AHCI_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B2FA4764-3B6E-43D3-91DF87D15A3E5668
* [0x7360]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A1E37052-80D9-4E65-A3173E9A55C43EC9
* [0x7360]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A1E37052-80D9-4E65-A3173E9A55C43EC9
* [0x73a0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] AHCI_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B2FA4764-3B6E-43D3-91DF87D15A3E5668
* [0x73b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 17706D27-83FE-4770-875F4CEF4CB8F63D
* [0x7440]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C6734411-2DDA-4632-A592920F24D6ED21
* [0x7450]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 0FC50878-1633-432A-BDE4841357FC15E9
* [0x73f0]
	 - [service] LocateProtocol
	 - [protocol_name] HDD_SECURITY_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] CE6F86BB-B800-4C71-B2D13897A3BC1DAE
* [0x7430]
	 - [service] LocateProtocol
	 - [protocol_name] OPAL_SEC_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 59AF16B0-661D-4865-A38138DE68385D8D
* [0x7420]
	 - [service] LocateProtocol
	 - [protocol_name] HDD_SMART_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 9401BD4F-1A00-4990-AB56DAF0E4E348DE
* [0x79f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 10E9D800-53B7-4845-9DFF30D18A956D53
* [0x7a30]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 734AA01D-95EC-45B7-A23A2D86D8FDEBB6
* [0x7978]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x7350]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x7390]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0x7380]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x7390]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0x7380]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x7350]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: AhciSmm
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x19db] EFI_BOOT_SERVICES->LocateProtocol
* [0x1abb] EFI_BOOT_SERVICES->LocateProtocol
* [0x1c61] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1fe0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x24f8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2010]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: Aint13
### Boot services:
* [0x2fd] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x355] EFI_BOOT_SERVICES->HandleProtocol
* [0x4e0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xedd] EFI_BOOT_SERVICES->LocateProtocol
* [0xf03] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1490]
	 - [service] HandleProtocol
	 - [protocol_name] AHCI_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B2FA4764-3B6E-43D3-91DF87D15A3E5668
* [0x14a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x14b0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_LEGACY_BIOS_EXT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8E008510-9BB1-457D-9F70897ABA865DB9
## Module: AmiBoardInfo2
### Boot services:
* [0x60d] EFI_BOOT_SERVICES->HandleProtocol
* [0x5c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x351] EFI_BOOT_SERVICES->LocateProtocol
* [0x4b5] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x950]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0xec8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 4FC0733F-6FD2-491B-A8905374521BF48F
## Module: AmiCpuFeaturesDxe
### Boot services:
* empty
### Protocols:
* empty
## Module: AmiDeviceGuardApi
### Boot services:
* [0x6ee] EFI_BOOT_SERVICES->HandleProtocol
* [0x72c] EFI_BOOT_SERVICES->HandleProtocol
* [0x805] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xc05] EFI_BOOT_SERVICES->LocateProtocol
* [0x325] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x10f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x10e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x1100]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_DIGITAL_SIGNATURE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5F87BA17-957D-433D-9E15C0E7C8798899
## Module: AmiHsti
### Boot services:
* [0xbea] EFI_BOOT_SERVICES->HandleProtocol
* [0x58f] EFI_BOOT_SERVICES->OpenProtocol
* [0xb99] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x350] EFI_BOOT_SERVICES->LocateProtocol
* [0x36e] EFI_BOOT_SERVICES->LocateProtocol
* [0x38b] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a8] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c5] EFI_BOOT_SERVICES->LocateProtocol
* [0x5b0] EFI_BOOT_SERVICES->LocateProtocol
* [0x913] EFI_BOOT_SERVICES->LocateProtocol
* [0x10e9] EFI_BOOT_SERVICES->LocateProtocol
* [0x201e] EFI_BOOT_SERVICES->LocateProtocol
* [0x2357] EFI_BOOT_SERVICES->LocateProtocol
* [0x733] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x4690]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAdapterInformationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E5DD1403-D622-C24E-8488C71B17F5E802
* [0x4d40]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0x46c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x46e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x46f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x46b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x46d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0x4d50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x46a0]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_DIGITAL_SIGNATURE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5F87BA17-957D-433D-9E15C0E7C8798899
* [0x4d00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
## Module: AmiMemoryInfoConfig
### Boot services:
* [0x524] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x380] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x7c0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C6AA1F27-5597-4802-9F63D62836598635
## Module: AmiRedFishApi
### Boot services:
* [0x856] EFI_BOOT_SERVICES->HandleProtocol
* [0x899] EFI_BOOT_SERVICES->HandleProtocol
* [0x972] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x325] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xc80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0xc70]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
## Module: AmiSyncSetupData
### Boot services:
* [0x33e] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x560]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
## Module: AmiTbtInfo
### Boot services:
* [0x5b6] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x32e] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* empty
## Module: AmiTcgNvflagSample
### Boot services:
* [0x3ac] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2f2] EFI_BOOT_SERVICES->LocateProtocol
* [0x321] EFI_BOOT_SERVICES->LocateProtocol
* [0x3fc] EFI_BOOT_SERVICES->LocateProtocol
* [0x42b] EFI_BOOT_SERVICES->LocateProtocol
* [0x5b0] EFI_BOOT_SERVICES->LocateProtocol
* [0x5df] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x890]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_TPM_DEVICE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] DE161CFE-1E60-42A1-8CC3EE7EF0735212
* [0x880]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F541796D-A62E-4954-A7759584F61B9CDD
## Module: AmiTcgPlatformDxe
### Boot services:
* [0x3ea] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xb2a] EFI_BOOT_SERVICES->HandleProtocol
* [0x1c17] EFI_BOOT_SERVICES->HandleProtocol
* [0xf36] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1d12] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3feb] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x406b] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x433] EFI_BOOT_SERVICES->OpenProtocol
* [0xaed] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x344] EFI_BOOT_SERVICES->LocateProtocol
* [0x362] EFI_BOOT_SERVICES->LocateProtocol
* [0x37f] EFI_BOOT_SERVICES->LocateProtocol
* [0x39c] EFI_BOOT_SERVICES->LocateProtocol
* [0x453] EFI_BOOT_SERVICES->LocateProtocol
* [0x4db] EFI_BOOT_SERVICES->LocateProtocol
* [0x6df] EFI_BOOT_SERVICES->LocateProtocol
* [0x8c0] EFI_BOOT_SERVICES->LocateProtocol
* [0x9f7] EFI_BOOT_SERVICES->LocateProtocol
* [0xab2] EFI_BOOT_SERVICES->LocateProtocol
* [0xc62] EFI_BOOT_SERVICES->LocateProtocol
* [0xcb7] EFI_BOOT_SERVICES->LocateProtocol
* [0x1024] EFI_BOOT_SERVICES->LocateProtocol
* [0x1140] EFI_BOOT_SERVICES->LocateProtocol
* [0x1402] EFI_BOOT_SERVICES->LocateProtocol
* [0x1616] EFI_BOOT_SERVICES->LocateProtocol
* [0x16f5] EFI_BOOT_SERVICES->LocateProtocol
* [0x18d8] EFI_BOOT_SERVICES->LocateProtocol
* [0x19ff] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a21] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a55] EFI_BOOT_SERVICES->LocateProtocol
* [0x1af7] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b85] EFI_BOOT_SERVICES->LocateProtocol
* [0x1cad] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e0b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e35] EFI_BOOT_SERVICES->LocateProtocol
* [0x27f9] EFI_BOOT_SERVICES->LocateProtocol
* [0x282b] EFI_BOOT_SERVICES->LocateProtocol
* [0x284f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2876] EFI_BOOT_SERVICES->LocateProtocol
* [0x2eac] EFI_BOOT_SERVICES->LocateProtocol
* [0x3679] EFI_BOOT_SERVICES->LocateProtocol
* [0x36c7] EFI_BOOT_SERVICES->LocateProtocol
* [0x371e] EFI_BOOT_SERVICES->LocateProtocol
* [0x39f1] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a7d] EFI_BOOT_SERVICES->LocateProtocol
* [0x3aac] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ad3] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c53] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c77] EFI_BOOT_SERVICES->LocateProtocol
* [0x41a7] EFI_BOOT_SERVICES->LocateProtocol
* [0x58d7] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x5ff0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolumeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 389F751F-1838-4388-8390CD8154BD27F8
* [0x5f30]
	 - [service] HandleProtocol
	 - [protocol_name] OPROM_START_END_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] F2A128FF-257B-456E-9DE863E7C7DCDFAC
* [0x5f00]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiResetArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 27CFAC88-46CC-11D4-9A380090273FC14D
* [0x5f30]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] OPROM_START_END_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] F2A128FF-257B-456E-9DE863E7C7DCDFAC
* [0x5f40]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
* [0x5f20]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0x5fa0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x5fc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x5fd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x5f90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x5ee0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F541796D-A62E-4954-A7759584F61B9CDD
* [0x5e90]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_OS_PPI_CONFIRMATION_OVERRIDE_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5F171F5F-8385-4086-A69B1FCF06AE4A3D
* [0x5e20]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 5CF308B5-FA23-4100-8A76F326C2814880
* [0x5f60]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_TPM_DEVICE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] DE161CFE-1E60-42A1-8CC3EE7EF0735212
* [0x5e40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 6DA670E8-3D73-4EB2-A721A2DDF682FDD8
* [0x5e30]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 9C53CE0E-0E9F-4F20-B1A1150E4349D777
* [0x5e50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] A4524A9C-0B5E-492D-AEC9308631B189B4
* [0x5e60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 76F3992D-529E-4EFE-8BBE8E1ED432C223
* [0x5e80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C77DD102-1DB4-4997-AE374E8C521EF567
* [0x5f10]
	 - [service] LocateProtocol
	 - [protocol_name] TCG_PLATFORM_SETUP_POLICY_GUID
	 - [protocol_place] ami_guids
	 - [guid] BB6CBEFF-E072-40D2-A6EBBAB75BDE87E7
* [0x5f70]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_POST_MANAGER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8A91B1E1-56C7-4ADC-ABEB1C2CA1729EFF
* [0x5e70]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_BIOSPPI_FLAGS_MANAGEMENT_GUID
	 - [protocol_place] ami_guids
	 - [guid] E9008D70-2A4E-47EA-8EC472E25767E5EF
* [0x5f40]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
* [0x5f80]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: AMITSE
### Boot services:
* [0x3320] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2a031] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2a06d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2f1bb] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2f1e3] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x31946] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x36843] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4f543] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4f5cf] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4f5b5] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x3338] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x32bc] EFI_BOOT_SERVICES->HandleProtocol
* [0x3c96] EFI_BOOT_SERVICES->HandleProtocol
* [0x3ce6] EFI_BOOT_SERVICES->HandleProtocol
* [0x4255] EFI_BOOT_SERVICES->HandleProtocol
* [0x7ae1] EFI_BOOT_SERVICES->HandleProtocol
* [0x9aeb] EFI_BOOT_SERVICES->HandleProtocol
* [0x9c02] EFI_BOOT_SERVICES->HandleProtocol
* [0x9f61] EFI_BOOT_SERVICES->HandleProtocol
* [0x9f9e] EFI_BOOT_SERVICES->HandleProtocol
* [0xa083] EFI_BOOT_SERVICES->HandleProtocol
* [0xa14c] EFI_BOOT_SERVICES->HandleProtocol
* [0xa703] EFI_BOOT_SERVICES->HandleProtocol
* [0xa985] EFI_BOOT_SERVICES->HandleProtocol
* [0xadc1] EFI_BOOT_SERVICES->HandleProtocol
* [0xbaef] EFI_BOOT_SERVICES->HandleProtocol
* [0x10242] EFI_BOOT_SERVICES->HandleProtocol
* [0x1788f] EFI_BOOT_SERVICES->HandleProtocol
* [0x17df2] EFI_BOOT_SERVICES->HandleProtocol
* [0x18bbc] EFI_BOOT_SERVICES->HandleProtocol
* [0x1966b] EFI_BOOT_SERVICES->HandleProtocol
* [0x196f6] EFI_BOOT_SERVICES->HandleProtocol
* [0x19875] EFI_BOOT_SERVICES->HandleProtocol
* [0x19a86] EFI_BOOT_SERVICES->HandleProtocol
* [0x19cec] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a0c6] EFI_BOOT_SERVICES->HandleProtocol
* [0x1e7bb] EFI_BOOT_SERVICES->HandleProtocol
* [0x1fec0] EFI_BOOT_SERVICES->HandleProtocol
* [0x25983] EFI_BOOT_SERVICES->HandleProtocol
* [0x29ce8] EFI_BOOT_SERVICES->HandleProtocol
* [0x2b0e2] EFI_BOOT_SERVICES->HandleProtocol
* [0x2ba5e] EFI_BOOT_SERVICES->HandleProtocol
* [0x2c17c] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d673] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d9a3] EFI_BOOT_SERVICES->HandleProtocol
* [0x2de75] EFI_BOOT_SERVICES->HandleProtocol
* [0x2de99] EFI_BOOT_SERVICES->HandleProtocol
* [0x2df6a] EFI_BOOT_SERVICES->HandleProtocol
* [0x2df95] EFI_BOOT_SERVICES->HandleProtocol
* [0x300e5] EFI_BOOT_SERVICES->HandleProtocol
* [0x31a51] EFI_BOOT_SERVICES->HandleProtocol
* [0x34122] EFI_BOOT_SERVICES->HandleProtocol
* [0x36731] EFI_BOOT_SERVICES->HandleProtocol
* [0x37e50] EFI_BOOT_SERVICES->HandleProtocol
* [0x3818c] EFI_BOOT_SERVICES->HandleProtocol
* [0x382a0] EFI_BOOT_SERVICES->HandleProtocol
* [0x3f838] EFI_BOOT_SERVICES->HandleProtocol
* [0x4022b] EFI_BOOT_SERVICES->HandleProtocol
* [0x444bb] EFI_BOOT_SERVICES->HandleProtocol
* [0x4fd37] EFI_BOOT_SERVICES->HandleProtocol
* [0x5030f] EFI_BOOT_SERVICES->HandleProtocol
* [0x3b21] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3b82] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3be2] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x958c] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x95d8] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xc139] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x36af9] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x4f2aa] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x709] EFI_BOOT_SERVICES->OpenProtocol
* [0x4f9d2] EFI_BOOT_SERVICES->OpenProtocol
* [0x4fa2d] EFI_BOOT_SERVICES->OpenProtocol
* [0x4fa68] EFI_BOOT_SERVICES->OpenProtocol
* [0x4fe84] EFI_BOOT_SERVICES->OpenProtocol
* [0xa945] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2994c] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x29af0] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2df1f] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xa8ce] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x29906] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x29aac] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x3c60] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4229] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4500] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x7aa2] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x9f25] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa0fe] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa22b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa6bf] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x19628] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x19a2f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x19b12] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a084] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x29a70] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2b8fc] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2b9f9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2e583] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x30339] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x303a8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3243c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x32619] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x32689] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x326e9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x328ef] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x359eb] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x366e8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x37e1e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3814f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3826e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4f40c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4f834] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4fe3d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x502bf] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x33a] EFI_BOOT_SERVICES->LocateProtocol
* [0x729] EFI_BOOT_SERVICES->LocateProtocol
* [0x4277] EFI_BOOT_SERVICES->LocateProtocol
* [0x4874] EFI_BOOT_SERVICES->LocateProtocol
* [0x4957] EFI_BOOT_SERVICES->LocateProtocol
* [0xacf8] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a497] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b1b5] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b5b2] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e807] EFI_BOOT_SERVICES->LocateProtocol
* [0x1fa0f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1fbe5] EFI_BOOT_SERVICES->LocateProtocol
* [0x26d40] EFI_BOOT_SERVICES->LocateProtocol
* [0x29d5f] EFI_BOOT_SERVICES->LocateProtocol
* [0x29e82] EFI_BOOT_SERVICES->LocateProtocol
* [0x29ee9] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a25f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a288] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a2ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a2de] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a440] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a45e] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b24e] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b4f1] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b84b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2cfd8] EFI_BOOT_SERVICES->LocateProtocol
* [0x2dcce] EFI_BOOT_SERVICES->LocateProtocol
* [0x2dd06] EFI_BOOT_SERVICES->LocateProtocol
* [0x2dd34] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e1fd] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e6b2] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ecec] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f328] EFI_BOOT_SERVICES->LocateProtocol
* [0x306c9] EFI_BOOT_SERVICES->LocateProtocol
* [0x30d91] EFI_BOOT_SERVICES->LocateProtocol
* [0x321d5] EFI_BOOT_SERVICES->LocateProtocol
* [0x32b5f] EFI_BOOT_SERVICES->LocateProtocol
* [0x32ec1] EFI_BOOT_SERVICES->LocateProtocol
* [0x33a34] EFI_BOOT_SERVICES->LocateProtocol
* [0x33e43] EFI_BOOT_SERVICES->LocateProtocol
* [0x3452b] EFI_BOOT_SERVICES->LocateProtocol
* [0x345de] EFI_BOOT_SERVICES->LocateProtocol
* [0x345fb] EFI_BOOT_SERVICES->LocateProtocol
* [0x34dea] EFI_BOOT_SERVICES->LocateProtocol
* [0x35832] EFI_BOOT_SERVICES->LocateProtocol
* [0x35c3e] EFI_BOOT_SERVICES->LocateProtocol
* [0x36a2a] EFI_BOOT_SERVICES->LocateProtocol
* [0x37008] EFI_BOOT_SERVICES->LocateProtocol
* [0x370a7] EFI_BOOT_SERVICES->LocateProtocol
* [0x37294] EFI_BOOT_SERVICES->LocateProtocol
* [0x372b8] EFI_BOOT_SERVICES->LocateProtocol
* [0x379e9] EFI_BOOT_SERVICES->LocateProtocol
* [0x37d6a] EFI_BOOT_SERVICES->LocateProtocol
* [0x37dcd] EFI_BOOT_SERVICES->LocateProtocol
* [0x37ecf] EFI_BOOT_SERVICES->LocateProtocol
* [0x38018] EFI_BOOT_SERVICES->LocateProtocol
* [0x38067] EFI_BOOT_SERVICES->LocateProtocol
* [0x380b6] EFI_BOOT_SERVICES->LocateProtocol
* [0x3866f] EFI_BOOT_SERVICES->LocateProtocol
* [0x386a3] EFI_BOOT_SERVICES->LocateProtocol
* [0x3889a] EFI_BOOT_SERVICES->LocateProtocol
* [0x388be] EFI_BOOT_SERVICES->LocateProtocol
* [0x38c4a] EFI_BOOT_SERVICES->LocateProtocol
* [0x38c6f] EFI_BOOT_SERVICES->LocateProtocol
* [0x392ee] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a19e] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a4d7] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a88a] EFI_BOOT_SERVICES->LocateProtocol
* [0x3aa07] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ab66] EFI_BOOT_SERVICES->LocateProtocol
* [0x3aba7] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ae64] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f62e] EFI_BOOT_SERVICES->LocateProtocol
* [0x50cd8] EFI_BOOT_SERVICES->LocateProtocol
* [0x4a97] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4b32] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4b61] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4b90] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x36c43] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3768c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3847f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x831] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x86d] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1b1db] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x51a80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x555d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x51950]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x51980]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x51ad0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0x51940]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
* [0x51900]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x51930]
	 - [service] HandleProtocol
	 - [protocol_name] EFI_OEM_BADGING_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] 170E13C0-BF1B-4218-871D2ABDC6F887BC
* [0x53cd8]
	 - [service] HandleProtocol
	 - [protocol_name] AMI_EFIKEYCODE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 0ADFB62D-FF74-484C-8944F85C4BEA87A8
* [0x51ae0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0x52c90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DD9E7534-7762-4698-8C14F58517A625AA
* [0x51b20]
	 - [service] HandleProtocol
	 - [protocol_name] IDE_SECURITY_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] F4F63529-281E-4040-A313C1D6766384BE
* [0x51af0]
	 - [service] HandleProtocol
	 - [protocol_name] AHCI_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B2FA4764-3B6E-43D3-91DF87D15A3E5668
* [0x51aa0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0x51970]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
* [0x51b10]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] HDD_SECURITY_END_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] AD77AE29-4C20-4FDD-85048176619B676A
* [0x529d8]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0x51b20]
	 - [service] OpenProtocol
	 - [protocol_name] IDE_SECURITY_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] F4F63529-281E-4040-A313C1D6766384BE
* [0x51b00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0x51a80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x51ae0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0x52c90]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DD9E7534-7762-4698-8C14F58517A625AA
* [0x51af0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] AHCI_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B2FA4764-3B6E-43D3-91DF87D15A3E5668
* [0x51a70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x529e8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x51aa0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0x51960]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x51990]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_POST_MANAGER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8A91B1E1-56C7-4ADC-ABEB1C2CA1729EFF
* [0x54628]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3CD7C71C-CBC3-4296-A9BC3CE449B9FF64
* [0x54608]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDevicePathToTextProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8B843E20-8132-4852-90CC551A4E4A7F1C
* [0x51910]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiUnicodeCollation2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A4C751FC-23AE-4C3E-92E94964CF63F349
* [0x537d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C7A7030C-C3D8-45EE-BED95D9E76762953
* [0x51ab0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x519f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x51a00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x51a10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x51920]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiUnicodeCollationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 1D85CD7F-F43D-11D2-9A0C0090273FC14D
* [0x53548]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C298B206-7FB5-4A7E-94614F3577F1A07A
* [0x53538]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x51a20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B9D4C360-BCFB-4F9B-929853C136982258
* [0x52be0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] BEBF428C-9318-4A45-9075570C1F94A86E
* [0x53220]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 783658A3-4172-4421-A299E009079C0CB4
* [0x51a40]
	 - [service] LocateProtocol
	 - [protocol_name] TCG_PLATFORM_SETUP_POLICY_GUID
	 - [protocol_place] ami_guids
	 - [guid] BB6CBEFF-E072-40D2-A6EBBAB75BDE87E7
* [0x52d08]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 01FA319E-C36C-4F19-9D9DD0290DBEE928
* [0x51ac0]
	 - [service] LocateProtocol
	 - [protocol_name] WDT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B42B8D12-2ACB-499A-A920DD5BE6CF09B1
* [0x518f0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CONSOLE_CONTROL_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] F42F7782-012E-4C12-995649F94304F721
* [0x519d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 6725E645-4A7F-9969-82ECD18721DE5A57
* [0x519c0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
* [0x52c50]
	 - [service] LocateProtocol
	 - [protocol_name] RSDP_PLUS_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] A33319B5-8EE1-45E0-8C9F809F5B0902CC
* [0x51a30]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_DIGITAL_SIGNATURE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5F87BA17-957D-433D-9E15C0E7C8798899
* [0x52998]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x529b8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x529c8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B9D4C360-BCFB-4F9B-929853C136982258
* [0x52928]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x54628]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3CD7C71C-CBC3-4296-A9BC3CE449B9FF64
## Module: ArpDxe
### Boot services:
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x612] EFI_BOOT_SERVICES->OpenProtocol
* [0x65e] EFI_BOOT_SERVICES->OpenProtocol
* [0x832] EFI_BOOT_SERVICES->OpenProtocol
* [0x8b9] EFI_BOOT_SERVICES->OpenProtocol
* [0x8f5] EFI_BOOT_SERVICES->OpenProtocol
* [0xa85] EFI_BOOT_SERVICES->OpenProtocol
* [0xc88] EFI_BOOT_SERVICES->OpenProtocol
* [0xda3] EFI_BOOT_SERVICES->OpenProtocol
* [0xfd2] EFI_BOOT_SERVICES->OpenProtocol
* [0x7fb] EFI_BOOT_SERVICES->CloseProtocol
* [0xcef] EFI_BOOT_SERVICES->CloseProtocol
* [0xdef] EFI_BOOT_SERVICES->CloseProtocol
* [0xa06] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xf4f] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x568] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x97b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc2f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb40] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xd0d] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xe0c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x2e30]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x2e40]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x2e50]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x2e30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x2e40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x2e50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x2e60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x2e00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0x2e20]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x2df0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiArpServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F44C00EE-1F2C-4A00-AA091C9F3E0800A3
* [0x2e10]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4B427BB-BA21-4F16-BC4E43E416AB619C
* [0x2e20]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x2e20]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x2e70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 480F8AE9-0C46-4AA9-BC89DB9FBA619806
* [0x2e10]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4B427BB-BA21-4F16-BC4E43E416AB619C
* [0x2df0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiArpServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F44C00EE-1F2C-4A00-AA091C9F3E0800A3
* [0x2e10]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4B427BB-BA21-4F16-BC4E43E416AB619C
## Module: AtaPassThru
### Boot services:
* [0x332] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x591] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x63e] EFI_BOOT_SERVICES->HandleProtocol
* [0x6be] EFI_BOOT_SERVICES->HandleProtocol
* [0xd9e] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xf44] EFI_BOOT_SERVICES->LocateProtocol
* [0x5c6] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x1b30]
	 - [service] HandleProtocol
	 - [protocol_name] AHCI_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B2FA4764-3B6E-43D3-91DF87D15A3E5668
* [0x1b20]
	 - [service] HandleProtocol
	 - [protocol_name] IDE_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] E159A956-3299-4EE9-917665181A4E5E9F
* [0x1b60]
	 - [service] LocateProtocol
	 - [protocol_name] PLATFORM_IDE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 6737F69B-B8CC-45BC-9327CCF5EEF70CDE
* [0x1b50]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiAtaPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 1D3DE7F0-0807-424F-AA6911A54E19A46F
## Module: AudioPlayback
### Boot services:
* [0x5af] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x613] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x9ef] EFI_BOOT_SERVICES->HandleProtocol
* [0x30f] EFI_BOOT_SERVICES->OpenProtocol
* [0x3c4] EFI_BOOT_SERVICES->OpenProtocol
* [0x35a] EFI_BOOT_SERVICES->CloseProtocol
* [0x9b7] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x45b] EFI_BOOT_SERVICES->LocateProtocol
* [0x5e6] EFI_BOOT_SERVICES->LocateProtocol
* [0x1028] EFI_BOOT_SERVICES->LocateProtocol
* [0x19a9] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2340]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 116ED1E8-F9C6-4112-A49C87ADA570DEC1
* [0x1d90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x1d60]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x1d60]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x1d90]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x1d80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB1-6F42-11D4-BCE70080C73C8881
* [0x2340]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 116ED1E8-F9C6-4112-A49C87ADA570DEC1
## Module: BdatAccessHandler
### Boot services:
* [0x29d] EFI_BOOT_SERVICES->LocateProtocol
* [0x2dc] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x830]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C6AA1F27-5597-4802-9F63D62836598635
* [0x820]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
## Module: Bds
### Boot services:
* [0x1850] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1d45] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x243f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x24e1] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x6021] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xb21f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xb871] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xc98f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1868] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x9f6] EFI_BOOT_SERVICES->HandleProtocol
* [0xcac] EFI_BOOT_SERVICES->HandleProtocol
* [0x1066] EFI_BOOT_SERVICES->HandleProtocol
* [0x12a0] EFI_BOOT_SERVICES->HandleProtocol
* [0x14cd] EFI_BOOT_SERVICES->HandleProtocol
* [0x15c8] EFI_BOOT_SERVICES->HandleProtocol
* [0x15fd] EFI_BOOT_SERVICES->HandleProtocol
* [0x171c] EFI_BOOT_SERVICES->HandleProtocol
* [0x1b7b] EFI_BOOT_SERVICES->HandleProtocol
* [0x1bd1] EFI_BOOT_SERVICES->HandleProtocol
* [0x2a68] EFI_BOOT_SERVICES->HandleProtocol
* [0x2aba] EFI_BOOT_SERVICES->HandleProtocol
* [0x2cf6] EFI_BOOT_SERVICES->HandleProtocol
* [0x2f21] EFI_BOOT_SERVICES->HandleProtocol
* [0x2f7b] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fc5] EFI_BOOT_SERVICES->HandleProtocol
* [0x3f0b] EFI_BOOT_SERVICES->HandleProtocol
* [0x3f3c] EFI_BOOT_SERVICES->HandleProtocol
* [0x4086] EFI_BOOT_SERVICES->HandleProtocol
* [0x41d2] EFI_BOOT_SERVICES->HandleProtocol
* [0x427e] EFI_BOOT_SERVICES->HandleProtocol
* [0x465c] EFI_BOOT_SERVICES->HandleProtocol
* [0x4698] EFI_BOOT_SERVICES->HandleProtocol
* [0x475c] EFI_BOOT_SERVICES->HandleProtocol
* [0x47e6] EFI_BOOT_SERVICES->HandleProtocol
* [0x49ea] EFI_BOOT_SERVICES->HandleProtocol
* [0x4d90] EFI_BOOT_SERVICES->HandleProtocol
* [0x4f66] EFI_BOOT_SERVICES->HandleProtocol
* [0x5070] EFI_BOOT_SERVICES->HandleProtocol
* [0x514e] EFI_BOOT_SERVICES->HandleProtocol
* [0x51b9] EFI_BOOT_SERVICES->HandleProtocol
* [0x53af] EFI_BOOT_SERVICES->HandleProtocol
* [0x546b] EFI_BOOT_SERVICES->HandleProtocol
* [0x5dd6] EFI_BOOT_SERVICES->HandleProtocol
* [0x62df] EFI_BOOT_SERVICES->HandleProtocol
* [0x6367] EFI_BOOT_SERVICES->HandleProtocol
* [0x6460] EFI_BOOT_SERVICES->HandleProtocol
* [0x81ac] EFI_BOOT_SERVICES->HandleProtocol
* [0x83ae] EFI_BOOT_SERVICES->HandleProtocol
* [0x86e9] EFI_BOOT_SERVICES->HandleProtocol
* [0x8f61] EFI_BOOT_SERVICES->HandleProtocol
* [0x902a] EFI_BOOT_SERVICES->HandleProtocol
* [0x98da] EFI_BOOT_SERVICES->HandleProtocol
* [0x9989] EFI_BOOT_SERVICES->HandleProtocol
* [0x99da] EFI_BOOT_SERVICES->HandleProtocol
* [0x9b62] EFI_BOOT_SERVICES->HandleProtocol
* [0x9e07] EFI_BOOT_SERVICES->HandleProtocol
* [0x9ea3] EFI_BOOT_SERVICES->HandleProtocol
* [0x9f67] EFI_BOOT_SERVICES->HandleProtocol
* [0xada5] EFI_BOOT_SERVICES->HandleProtocol
* [0xadcd] EFI_BOOT_SERVICES->HandleProtocol
* [0xb3c2] EFI_BOOT_SERVICES->HandleProtocol
* [0xb4d3] EFI_BOOT_SERVICES->HandleProtocol
* [0xb529] EFI_BOOT_SERVICES->HandleProtocol
* [0xb608] EFI_BOOT_SERVICES->HandleProtocol
* [0xb667] EFI_BOOT_SERVICES->HandleProtocol
* [0xb8fc] EFI_BOOT_SERVICES->HandleProtocol
* [0xb91f] EFI_BOOT_SERVICES->HandleProtocol
* [0xb99e] EFI_BOOT_SERVICES->HandleProtocol
* [0xbc38] EFI_BOOT_SERVICES->HandleProtocol
* [0xbec4] EFI_BOOT_SERVICES->HandleProtocol
* [0xc042] EFI_BOOT_SERVICES->HandleProtocol
* [0xd125] EFI_BOOT_SERVICES->HandleProtocol
* [0xd230] EFI_BOOT_SERVICES->HandleProtocol
* [0xd259] EFI_BOOT_SERVICES->HandleProtocol
* [0xd90f] EFI_BOOT_SERVICES->HandleProtocol
* [0xdfb5] EFI_BOOT_SERVICES->HandleProtocol
* [0xe0cf] EFI_BOOT_SERVICES->HandleProtocol
* [0xe189] EFI_BOOT_SERVICES->HandleProtocol
* [0xef7c] EFI_BOOT_SERVICES->HandleProtocol
* [0x4f4] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x69b9] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xc108] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x59fb] EFI_BOOT_SERVICES->OpenProtocol
* [0xa138] EFI_BOOT_SERVICES->CloseProtocol
* [0x627d] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x9948] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xa0e5] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xa1f5] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xa247] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x6216] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x9ba] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x158c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a14] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a96] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1b43] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x25c9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2a2f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5d9d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8369] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x86a5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x98aa] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa1ab] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xb386] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xb49b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xb7d6] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xb960] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xcaa8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xcae6] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3ce] EFI_BOOT_SERVICES->LocateProtocol
* [0x553] EFI_BOOT_SERVICES->LocateProtocol
* [0xd05] EFI_BOOT_SERVICES->LocateProtocol
* [0xdf8] EFI_BOOT_SERVICES->LocateProtocol
* [0x1963] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d23] EFI_BOOT_SERVICES->LocateProtocol
* [0x24fc] EFI_BOOT_SERVICES->LocateProtocol
* [0x28f9] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ceb] EFI_BOOT_SERVICES->LocateProtocol
* [0x5a1b] EFI_BOOT_SERVICES->LocateProtocol
* [0x5d5f] EFI_BOOT_SERVICES->LocateProtocol
* [0x6063] EFI_BOOT_SERVICES->LocateProtocol
* [0x6150] EFI_BOOT_SERVICES->LocateProtocol
* [0x76aa] EFI_BOOT_SERVICES->LocateProtocol
* [0x79e3] EFI_BOOT_SERVICES->LocateProtocol
* [0x7d96] EFI_BOOT_SERVICES->LocateProtocol
* [0x7f17] EFI_BOOT_SERVICES->LocateProtocol
* [0x8325] EFI_BOOT_SERVICES->LocateProtocol
* [0x97a9] EFI_BOOT_SERVICES->LocateProtocol
* [0xad1b] EFI_BOOT_SERVICES->LocateProtocol
* [0xad40] EFI_BOOT_SERVICES->LocateProtocol
* [0xad87] EFI_BOOT_SERVICES->LocateProtocol
* [0xb141] EFI_BOOT_SERVICES->LocateProtocol
* [0xb7a7] EFI_BOOT_SERVICES->LocateProtocol
* [0xb84f] EFI_BOOT_SERVICES->LocateProtocol
* [0xbee4] EFI_BOOT_SERVICES->LocateProtocol
* [0xc176] EFI_BOOT_SERVICES->LocateProtocol
* [0xc32b] EFI_BOOT_SERVICES->LocateProtocol
* [0xc5a5] EFI_BOOT_SERVICES->LocateProtocol
* [0xc969] EFI_BOOT_SERVICES->LocateProtocol
* [0xca69] EFI_BOOT_SERVICES->LocateProtocol
* [0xd092] EFI_BOOT_SERVICES->LocateProtocol
* [0xd0c4] EFI_BOOT_SERVICES->LocateProtocol
* [0xd5a2] EFI_BOOT_SERVICES->LocateProtocol
* [0xfba7] EFI_BOOT_SERVICES->LocateProtocol
* [0x10399] EFI_BOOT_SERVICES->LocateProtocol
* [0x10444] EFI_BOOT_SERVICES->LocateProtocol
* [0x7f3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1820] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9d8a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc375] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x12a98]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 00610043-0070-0073-75006C0065005500
* [0x12570]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x12580]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x126b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x125b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x12590]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x12630]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 934CE8DA-5E2A-4184-8A158E0847988431
* [0x12650]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] DC14E697-775A-4C3B-A11AEDC38E1BE3E6
* [0x12550]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 56EC3091-954C-11D2-8E3F00A0C969723B
* [0x125d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0x125e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0x12660]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 52C78312-8EDC-4233-98F21A1AA5E388A5
* [0x11a08]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x11a28]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x12760]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x126a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0x12520]
	 - [service] HandleProtocol
	 - [protocol_name] AMI_CSM_THUNK_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2362EA9C-84E5-4DFF-83BCB5ACECB57CBB
* [0x12720]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBusSpecificDriverOverrideProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3BC1B285-8A15-4A82-AABF4D7D13FB3265
* [0x111a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x125a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
* [0x123b0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 6FF23F1D-877C-4B1B-93FCF142B2EEA6A7
* [0x11460]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0x125b0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x125b0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x12740]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A1E37052-80D9-4E65-A3173E9A55C43EC9
* [0x12750]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0x12590]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x12740]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A1E37052-80D9-4E65-A3173E9A55C43EC9
* [0x123b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 6FF23F1D-877C-4B1B-93FCF142B2EEA6A7
* [0x12670]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x125c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x12600]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_ACPI_S3_SAVE_GUID
	 - [protocol_place] edk_guids
	 - [guid] 125F2DE1-FB85-440C-A54C4D99358A8D38
* [0x122a0]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_POST_MANAGER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8A91B1E1-56C7-4ADC-ABEB1C2CA1729EFF
* [0x12640]
	 - [service] LocateProtocol
	 - [protocol_name] gEsrtManagementProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A340C064-723C-4A9C-A4DDD5B47A26FBB0
* [0x11470]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x11b28]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
* [0x12680]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
* [0x11a58]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x11420]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x11440]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x126e0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_PLATFORM_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] D9035175-8CE2-47DE-A8B8CC98E5E2A885
* [0x126f0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_USB_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2AD8E2D2-2E91-4CD1-95F5E78FE5EBE316
* [0x112d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] F38DF21C-4F6C-449B-9A7B227B52D5D7BA
* [0x112e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 23F2D944-33A6-4EBE-BF982AFB220E0DD7
* [0x122b0]
	 - [service] LocateProtocol
	 - [protocol_name] CONSOLE_IN_DEVICES_STARTED_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2DF1E051-906D-4EFF-869D24E65378FB9E
* [0x126d0]
	 - [service] LocateProtocol
	 - [protocol_name] FLASH_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 755B6596-6896-4BA3-B3DD1C629FD1EA88
* [0x126c0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CONSOLE_CONTROL_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] F42F7782-012E-4C12-995649F94304F721
## Module: BiosExtensionLoader
### Boot services:
* [0x1dd3] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x1a7f] EFI_BOOT_SERVICES->HandleProtocol
* [0x1af8] EFI_BOOT_SERVICES->HandleProtocol
* [0x1db5] EFI_BOOT_SERVICES->HandleProtocol
* [0x2271] EFI_BOOT_SERVICES->HandleProtocol
* [0x25c0] EFI_BOOT_SERVICES->HandleProtocol
* [0x2879] EFI_BOOT_SERVICES->HandleProtocol
* [0x28b4] EFI_BOOT_SERVICES->HandleProtocol
* [0x2a0c] EFI_BOOT_SERVICES->HandleProtocol
* [0x2c95] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a42] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1d52] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2236] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x257b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x280d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x312] EFI_BOOT_SERVICES->LocateProtocol
* [0xbcc] EFI_BOOT_SERVICES->LocateProtocol
* [0xf71] EFI_BOOT_SERVICES->LocateProtocol
* [0x10c3] EFI_BOOT_SERVICES->LocateProtocol
* [0x10ec] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b4d] EFI_BOOT_SERVICES->LocateProtocol
* [0x3229] EFI_BOOT_SERVICES->LocateProtocol
* [0x3250] EFI_BOOT_SERVICES->LocateProtocol
* [0x32b8] EFI_BOOT_SERVICES->LocateProtocol
* [0x336f] EFI_BOOT_SERVICES->LocateProtocol
* [0x3483] EFI_BOOT_SERVICES->LocateProtocol
* [0x3511] EFI_BOOT_SERVICES->LocateProtocol
* [0x36a4] EFI_BOOT_SERVICES->LocateProtocol
* [0x37a6] EFI_BOOT_SERVICES->LocateProtocol
* [0x374] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x3b90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x3b40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
* [0x3b30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0x3b80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAtaPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 1D3DE7F0-0807-424F-AA6911A54E19A46F
* [0x3b70]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 52C78312-8EDC-4233-98F21A1AA5E388A5
* [0x3b60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x3b50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0x3af0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
* [0x3bd0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] D25DC167-EB6A-432D-6591BF8029B005BB
* [0x3b10]
	 - [service] LocateProtocol
	 - [protocol_name] INTEL_MEBX_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 01AB1829-CECD-4CFA-A18CEA75D66F3E74
* [0x3b30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0x3ba0]
	 - [service] LocateProtocol
	 - [protocol_name] PLATFORM_ME_HOOK_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] BC52476E-F67E-4301-B262369C4878AAC2
* [0x3bb0]
	 - [service] LocateProtocol
	 - [protocol_name] WDT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B42B8D12-2ACB-499A-A920DD5BE6CF09B1
* [0x3bc0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 8D9B3387-73DB-456F-889D6FFE90826409
* [0x3b00]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 6725E645-4A7F-9969-82ECD18721DE5A57
## Module: BnWdtDxe
### Boot services:
* [0x6d3] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x760] EFI_BOOT_SERVICES->HandleProtocol
* [0x839] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x353] EFI_BOOT_SERVICES->LocateProtocol
* [0x38f] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ce] EFI_BOOT_SERVICES->LocateProtocol
* [0x532] EFI_BOOT_SERVICES->LocateProtocol
* [0x70c] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xbe0]
	 - [service] HandleProtocol
	 - [protocol_name] OPROM_START_END_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] F2A128FF-257B-456E-9DE863E7C7DCDFAC
* [0xbf0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xbd0]
	 - [service] LocateProtocol
	 - [protocol_name] WDT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B42B8D12-2ACB-499A-A920DD5BE6CF09B1
## Module: BootScriptExecutorDxe
### Boot services:
* [0x814] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x482] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x4b3] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1144] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1232] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x396e] EFI_BOOT_SERVICES->HandleProtocol
* [0x39ac] EFI_BOOT_SERVICES->HandleProtocol
* [0xed0] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3a85] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4db] EFI_BOOT_SERVICES->LocateProtocol
* [0x7e5] EFI_BOOT_SERVICES->LocateProtocol
* [0xc44] EFI_BOOT_SERVICES->LocateProtocol
* [0xd2c] EFI_BOOT_SERVICES->LocateProtocol
* [0xdf7] EFI_BOOT_SERVICES->LocateProtocol
* [0xf71] EFI_BOOT_SERVICES->LocateProtocol
* [0x119b] EFI_BOOT_SERVICES->LocateProtocol
* [0x4397] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x69f0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 47B7FA8C-F4BD-4AF6-8200333086F0D2C8
* [0x69d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x6a20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x69a0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x6960]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] FA20568B-548B-4B2B-81EF1BA08D4A3CEC
* [0x69a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x69c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x69e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x69b0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: CapsuleRuntimeDxe
### Boot services:
* [0x161d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1559] EFI_BOOT_SERVICES->LocateProtocol
* [0x106b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2050]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
* [0x2050]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
## Module: CmosDxe
### Boot services:
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x661] EFI_BOOT_SERVICES->LocateProtocol
* [0xc7c] EFI_BOOT_SERVICES->LocateProtocol
* [0xaf9] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2460]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2450]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_DXE_CMOS_ACCESS_GUID
	 - [protocol_place] ami_guids
	 - [guid] 9851740C-22E0-440D-9090EF2D71C251C9
* [0x2a60]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_DXE_CMOS_ACCESS_GUID
	 - [protocol_place] ami_guids
	 - [guid] 9851740C-22E0-440D-9090EF2D71C251C9
## Module: CmosSmm
### Boot services:
* [0xb82] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x39a] EFI_BOOT_SERVICES->LocateProtocol
* [0x421] EFI_BOOT_SERVICES->LocateProtocol
* [0x616] EFI_BOOT_SERVICES->LocateProtocol
* [0x2131] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2760]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2790]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x2c78]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2780]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: ConSplitter
### Boot services:
* [0x447] EFI_BOOT_SERVICES->HandleProtocol
* [0x53a] EFI_BOOT_SERVICES->HandleProtocol
* [0x6ac] EFI_BOOT_SERVICES->HandleProtocol
* [0x865] EFI_BOOT_SERVICES->HandleProtocol
* [0xdcb] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a73] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d48] EFI_BOOT_SERVICES->HandleProtocol
* [0x2e7e] EFI_BOOT_SERVICES->HandleProtocol
* [0x498d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xe52] EFI_BOOT_SERVICES->OpenProtocol
* [0xed3] EFI_BOOT_SERVICES->OpenProtocol
* [0xf4f] EFI_BOOT_SERVICES->OpenProtocol
* [0x1175] EFI_BOOT_SERVICES->OpenProtocol
* [0x11a1] EFI_BOOT_SERVICES->OpenProtocol
* [0x11ce] EFI_BOOT_SERVICES->OpenProtocol
* [0x130f] EFI_BOOT_SERVICES->OpenProtocol
* [0x133f] EFI_BOOT_SERVICES->OpenProtocol
* [0x1373] EFI_BOOT_SERVICES->OpenProtocol
* [0x1447] EFI_BOOT_SERVICES->OpenProtocol
* [0x168d] EFI_BOOT_SERVICES->OpenProtocol
* [0x16b9] EFI_BOOT_SERVICES->OpenProtocol
* [0x177a] EFI_BOOT_SERVICES->OpenProtocol
* [0x17d6] EFI_BOOT_SERVICES->OpenProtocol
* [0x1803] EFI_BOOT_SERVICES->OpenProtocol
* [0x1855] EFI_BOOT_SERVICES->OpenProtocol
* [0xe81] EFI_BOOT_SERVICES->CloseProtocol
* [0xf0b] EFI_BOOT_SERVICES->CloseProtocol
* [0x1000] EFI_BOOT_SERVICES->CloseProtocol
* [0x1023] EFI_BOOT_SERVICES->CloseProtocol
* [0x11f5] EFI_BOOT_SERVICES->CloseProtocol
* [0x1219] EFI_BOOT_SERVICES->CloseProtocol
* [0x123c] EFI_BOOT_SERVICES->CloseProtocol
* [0x13ca] EFI_BOOT_SERVICES->CloseProtocol
* [0x13e8] EFI_BOOT_SERVICES->CloseProtocol
* [0x1406] EFI_BOOT_SERVICES->CloseProtocol
* [0x159b] EFI_BOOT_SERVICES->CloseProtocol
* [0x15b9] EFI_BOOT_SERVICES->CloseProtocol
* [0x15d7] EFI_BOOT_SERVICES->CloseProtocol
* [0x15f9] EFI_BOOT_SERVICES->CloseProtocol
* [0x16e0] EFI_BOOT_SERVICES->CloseProtocol
* [0x1704] EFI_BOOT_SERVICES->CloseProtocol
* [0x186e] EFI_BOOT_SERVICES->CloseProtocol
* [0x1891] EFI_BOOT_SERVICES->CloseProtocol
* [0x1970] EFI_BOOT_SERVICES->CloseProtocol
* [0x1992] EFI_BOOT_SERVICES->CloseProtocol
* [0x19e8] EFI_BOOT_SERVICES->CloseProtocol
* [0x1a0a] EFI_BOOT_SERVICES->CloseProtocol
* [0x23ff] EFI_BOOT_SERVICES->LocateProtocol
* [0x4638] EFI_BOOT_SERVICES->LocateProtocol
* [0x725] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x950] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc6f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4549] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x455b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x4ce0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0x4d00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x4cd0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x4c80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x4c60]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
* [0x4c70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DD9E7534-7762-4698-8C14F58517A625AA
* [0x4c90]
	 - [service] OpenProtocol
	 - [protocol_name] AMI_EFIKEYCODE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 0ADFB62D-FF74-484C-8944F85C4BEA87A8
* [0x4ca0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8D59D32B-C655-4AE9-9B15F25904992A43
* [0x4c50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31878C87-0B75-11D5-9A4F0090273FC14D
* [0x4c80]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x4c60]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
* [0x4c90]
	 - [service] CloseProtocol
	 - [protocol_name] AMI_EFIKEYCODE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 0ADFB62D-FF74-484C-8944F85C4BEA87A8
* [0x4c70]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DD9E7534-7762-4698-8C14F58517A625AA
* [0x4c50]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31878C87-0B75-11D5-9A4F0090273FC14D
* [0x4ca0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8D59D32B-C655-4AE9-9B15F25904992A43
* [0x4cc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x5248]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x4c90]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] AMI_EFIKEYCODE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 0ADFB62D-FF74-484C-8944F85C4BEA87A8
* [0x4d20]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
## Module: CpuDxe
### Boot services:
* [0x121e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1243] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1636] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xfc8] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2238]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3FDDA605-A76E-4F46-AD2912F4531B3D08
* [0x2238]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3FDDA605-A76E-4F46-AD2912F4531B3D08
## Module: CpuInitDxe
### Boot services:
* [0xaad] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x5141] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xb33] EFI_BOOT_SERVICES->LocateProtocol
* [0x246a] EFI_BOOT_SERVICES->LocateProtocol
* [0x26a1] EFI_BOOT_SERVICES->LocateProtocol
* [0x2779] EFI_BOOT_SERVICES->LocateProtocol
* [0x2886] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a82] EFI_BOOT_SERVICES->LocateProtocol
* [0x4e05] EFI_BOOT_SERVICES->LocateProtocol
* [0xc4a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x11af] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2d65] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x5720]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMetronomeArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB2-6F42-11D4-BCE70080C73C8881
* [0x5750]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmControl2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 843DC720-AB1E-42CB-93578A0078F3561B
* [0x5760]
	 - [service] LocateProtocol
	 - [protocol_name] DXE_CPU_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] E223CF65-F6CE-4122-B3AF4BD18AFF40A1
* [0x5770]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x5730]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB1-6F42-11D4-BCE70080C73C8881
* [0x5780]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] AB5A4DF4-F0D7-49A8-BF5CF25DA04C2533
* [0x5780]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] AB5A4DF4-F0D7-49A8-BF5CF25DA04C2533
## Module: CpuIo2Dxe
### Boot services:
* [0x2b5] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: CpuIo2Smm
### Boot services:
* [0x34d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2d3] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x7d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: CpuIoDxe
### Boot services:
* [0x109e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: CpuSpSMI
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x655] EFI_BOOT_SERVICES->LocateProtocol
* [0x831] EFI_BOOT_SERVICES->LocateProtocol
* [0xa35] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xe20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1338]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xe50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: CrbDxe
### Boot services:
* [0x3d0] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x594] EFI_BOOT_SERVICES->LocateProtocol
* [0x38a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xa00]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 67269263-0AF1-45DD-93C8299921D0E1E9
* [0xa10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xa00]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 67269263-0AF1-45DD-93C8299921D0E1E9
## Module: CrbSmbiosType9
### Boot services:
* [0x2ce] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x332] EFI_BOOT_SERVICES->LocateProtocol
* [0x52f] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xdf0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0xe00]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: CrbSmi
### Boot services:
* [0x34c] EFI_BOOT_SERVICES->LocateProtocol
* [0x37a] EFI_BOOT_SERVICES->LocateProtocol
* [0x401] EFI_BOOT_SERVICES->LocateProtocol
* [0x49b] EFI_BOOT_SERVICES->LocateProtocol
* [0x677] EFI_BOOT_SERVICES->LocateProtocol
* [0x81d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xde0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xe10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x12f8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xe00]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: CryptoDXE
### Boot services:
* [0x12d3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: CryptoPPI
### Boot services:
* empty
### Protocols:
* empty
## Module: CryptoSMM
### Boot services:
* [0x1590] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x380] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b5] EFI_BOOT_SERVICES->LocateProtocol
* [0x146c] EFI_BOOT_SERVICES->LocateProtocol
* [0x17d5] EFI_BOOT_SERVICES->LocateProtocol
* [0x1567] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xd040]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xd060]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0xd5d8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xd070]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: CsmBlockIo
### Boot services:
* [0x1acd] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x1dae] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x20f8] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x244f] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x1aad] EFI_BOOT_SERVICES->HandleProtocol
* [0x1d8e] EFI_BOOT_SERVICES->HandleProtocol
* [0x20d8] EFI_BOOT_SERVICES->HandleProtocol
* [0x242f] EFI_BOOT_SERVICES->HandleProtocol
* [0x3b8] EFI_BOOT_SERVICES->OpenProtocol
* [0x40a] EFI_BOOT_SERVICES->OpenProtocol
* [0x43a] EFI_BOOT_SERVICES->OpenProtocol
* [0x47b] EFI_BOOT_SERVICES->OpenProtocol
* [0x4b3] EFI_BOOT_SERVICES->OpenProtocol
* [0x630] EFI_BOOT_SERVICES->OpenProtocol
* [0x664] EFI_BOOT_SERVICES->OpenProtocol
* [0x6a6] EFI_BOOT_SERVICES->OpenProtocol
* [0xb82] EFI_BOOT_SERVICES->OpenProtocol
* [0xce0] EFI_BOOT_SERVICES->OpenProtocol
* [0xd27] EFI_BOOT_SERVICES->OpenProtocol
* [0x3df] EFI_BOOT_SERVICES->CloseProtocol
* [0x504] EFI_BOOT_SERVICES->CloseProtocol
* [0x8ef] EFI_BOOT_SERVICES->CloseProtocol
* [0x90d] EFI_BOOT_SERVICES->CloseProtocol
* [0xc08] EFI_BOOT_SERVICES->CloseProtocol
* [0xc26] EFI_BOOT_SERVICES->CloseProtocol
* [0xd59] EFI_BOOT_SERVICES->CloseProtocol
* [0xde4] EFI_BOOT_SERVICES->CloseProtocol
* [0xe32] EFI_BOOT_SERVICES->CloseProtocol
* [0xe55] EFI_BOOT_SERVICES->CloseProtocol
* [0x381] EFI_BOOT_SERVICES->LocateProtocol
* [0x5d3] EFI_BOOT_SERVICES->LocateProtocol
* [0x5f7] EFI_BOOT_SERVICES->LocateProtocol
* [0x6ff] EFI_BOOT_SERVICES->LocateProtocol
* [0x342] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xad6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xd9b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x2820]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x2820]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x2870]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x2e38]
	 - [service] OpenProtocol
	 - [protocol_name] ONBOARD_RAID_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5D206DD3-516A-47DC-A1BC6DA204AABE08
* [0x2e48]
	 - [service] OpenProtocol
	 - [protocol_name] HDD_UNLOCKED_GUID
	 - [protocol_place] ami_guids
	 - [guid] 1FD29BE6-70D0-42A4-A6E7E5D10E6AC376
* [0x2840]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A1E37052-80D9-4E65-A3173E9A55C43EC9
* [0x2800]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x2820]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x2870]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x2800]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x27f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x2810]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_LEGACY_BIOS_EXT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8E008510-9BB1-457D-9F70897ABA865DB9
* [0x2850]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacy8259ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 38321DBA-4FE0-4E17-8AEC413055EAEDC1
* [0x2e30]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 00000000-0000-0000-D36D205D6A51DC47
* [0x2820]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x2820]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
## Module: CsmDxe
### Boot services:
* [0x3c0] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x3623] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x5929] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x595b] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x6ffc] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4be1] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x8dd9] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x363b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xc86] EFI_BOOT_SERVICES->HandleProtocol
* [0x1fa9] EFI_BOOT_SERVICES->HandleProtocol
* [0x238e] EFI_BOOT_SERVICES->HandleProtocol
* [0x2a3c] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d21] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d6f] EFI_BOOT_SERVICES->HandleProtocol
* [0x2e17] EFI_BOOT_SERVICES->HandleProtocol
* [0x2f43] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fc5] EFI_BOOT_SERVICES->HandleProtocol
* [0x374e] EFI_BOOT_SERVICES->HandleProtocol
* [0x3a17] EFI_BOOT_SERVICES->HandleProtocol
* [0x3f09] EFI_BOOT_SERVICES->HandleProtocol
* [0x3f49] EFI_BOOT_SERVICES->HandleProtocol
* [0x3f72] EFI_BOOT_SERVICES->HandleProtocol
* [0x3fb7] EFI_BOOT_SERVICES->HandleProtocol
* [0x4bc6] EFI_BOOT_SERVICES->HandleProtocol
* [0x4fec] EFI_BOOT_SERVICES->HandleProtocol
* [0x5045] EFI_BOOT_SERVICES->HandleProtocol
* [0x54fb] EFI_BOOT_SERVICES->HandleProtocol
* [0x57dc] EFI_BOOT_SERVICES->HandleProtocol
* [0x5e11] EFI_BOOT_SERVICES->HandleProtocol
* [0x650f] EFI_BOOT_SERVICES->HandleProtocol
* [0x65c5] EFI_BOOT_SERVICES->HandleProtocol
* [0x68fd] EFI_BOOT_SERVICES->HandleProtocol
* [0x6afe] EFI_BOOT_SERVICES->HandleProtocol
* [0x6ca7] EFI_BOOT_SERVICES->HandleProtocol
* [0x6e31] EFI_BOOT_SERVICES->HandleProtocol
* [0x6ee2] EFI_BOOT_SERVICES->HandleProtocol
* [0x72ea] EFI_BOOT_SERVICES->HandleProtocol
* [0x7549] EFI_BOOT_SERVICES->HandleProtocol
* [0x7fd4] EFI_BOOT_SERVICES->HandleProtocol
* [0x8157] EFI_BOOT_SERVICES->HandleProtocol
* [0x91b7] EFI_BOOT_SERVICES->HandleProtocol
* [0x9dbe] EFI_BOOT_SERVICES->HandleProtocol
* [0x99e] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x9f0] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x58f5] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x83f3] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x4fae] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x1f71] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x235e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2a05] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2db5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2f04] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x371a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x39bc] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3eb8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4b52] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x54cb] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5dd3] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x68c9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6a2c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x7f99] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x9d83] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x585] EFI_BOOT_SERVICES->LocateProtocol
* [0x5af] EFI_BOOT_SERVICES->LocateProtocol
* [0x5d9] EFI_BOOT_SERVICES->LocateProtocol
* [0x603] EFI_BOOT_SERVICES->LocateProtocol
* [0xf05] EFI_BOOT_SERVICES->LocateProtocol
* [0x2092] EFI_BOOT_SERVICES->LocateProtocol
* [0x20cb] EFI_BOOT_SERVICES->LocateProtocol
* [0x20fb] EFI_BOOT_SERVICES->LocateProtocol
* [0x244a] EFI_BOOT_SERVICES->LocateProtocol
* [0x485d] EFI_BOOT_SERVICES->LocateProtocol
* [0x59f3] EFI_BOOT_SERVICES->LocateProtocol
* [0x5b58] EFI_BOOT_SERVICES->LocateProtocol
* [0x629d] EFI_BOOT_SERVICES->LocateProtocol
* [0x6c82] EFI_BOOT_SERVICES->LocateProtocol
* [0x6ddc] EFI_BOOT_SERVICES->LocateProtocol
* [0x7d84] EFI_BOOT_SERVICES->LocateProtocol
* [0x81b7] EFI_BOOT_SERVICES->LocateProtocol
* [0x8233] EFI_BOOT_SERVICES->LocateProtocol
* [0x8735] EFI_BOOT_SERVICES->LocateProtocol
* [0x89ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x8fcd] EFI_BOOT_SERVICES->LocateProtocol
* [0x90d0] EFI_BOOT_SERVICES->LocateProtocol
* [0x935c] EFI_BOOT_SERVICES->LocateProtocol
* [0x9c0e] EFI_BOOT_SERVICES->LocateProtocol
* [0xa41b] EFI_BOOT_SERVICES->LocateProtocol
* [0x94c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x83a9] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xc740]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 9400D59B-0E9C-4F6C-B59AFC20009DB9EC
* [0xc680]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0xc660]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0xc610]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xd230]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0xc6a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31878C87-0B75-11D5-9A4F0090273FC14D
* [0xc780]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xc670]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSioProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 215FDD18-BD50-4FEB-890B58CA0B4739E9
* [0xc6d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0xc650]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0xc7c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0xc590]
	 - [service] HandleProtocol
	 - [protocol_name] AMI_CSM_THUNK_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2362EA9C-84E5-4DFF-83BCB5ACECB57CBB
* [0xc5b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0xc700]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0xc630]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] BDS_ALL_DRIVERS_CONNECTED_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] DBC9FD21-FAD8-45B0-9E7827158867CC93
* [0xc720]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] AMI_PCI_BUS_EXT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] F42A009D-977F-4F08-9440BCA5A3BED9AF
* [0xc610]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xcf40]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] CONSOLE_IN_DEVICES_STARTED_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2DF1E051-906D-4EFF-869D24E65378FB9E
* [0xc610]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xc660]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0xc610]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xc670]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSioProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 215FDD18-BD50-4FEB-890B58CA0B4739E9
* [0xc6d0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0xc650]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0xc5b0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0xc7d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xc600]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyRegion2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 70101EAF-0085-440C-B3568EE36FEF24F0
* [0xc5c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 783658A3-4172-4421-A299E009079C0CB4
* [0xc6e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacy8259ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 38321DBA-4FE0-4E17-8AEC413055EAEDC1
* [0xc6f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyInterruptProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31CE593D-108A-485D-ADB278F21F2966BE
* [0xc640]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTimerArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB3-6F42-11D4-BCE70080C73C8881
* [0xc6c0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_AHCI_INT13_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 67820532-7613-4DD3-9ED73D9BE3A7DA63
* [0xc750]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_USB_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2AD8E2D2-2E91-4CD1-95F5E78FE5EBE316
* [0xc620]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_LEGACY_BIOS_EXT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8E008510-9BB1-457D-9F70897ABA865DB9
* [0xc5b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0xc7b0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CONSOLE_CONTROL_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] F42F7782-012E-4C12-995649F94304F721
* [0xc7a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] DC14E697-775A-4C3B-A11AEDC38E1BE3E6
* [0xce78]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0xc790]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 4FC0733F-6FD2-491B-A8905374521BF48F
* [0xc5b0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
## Module: CsmVideo
### Boot services:
* [0x124f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2c12] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x5f0] EFI_BOOT_SERVICES->HandleProtocol
* [0x2952] EFI_BOOT_SERVICES->HandleProtocol
* [0x52b] EFI_BOOT_SERVICES->OpenProtocol
* [0x62c] EFI_BOOT_SERVICES->OpenProtocol
* [0x816] EFI_BOOT_SERVICES->OpenProtocol
* [0x85e] EFI_BOOT_SERVICES->OpenProtocol
* [0xbf5] EFI_BOOT_SERVICES->OpenProtocol
* [0xd15] EFI_BOOT_SERVICES->OpenProtocol
* [0xd52] EFI_BOOT_SERVICES->OpenProtocol
* [0xe53] EFI_BOOT_SERVICES->OpenProtocol
* [0x28ea] EFI_BOOT_SERVICES->OpenProtocol
* [0x291a] EFI_BOOT_SERVICES->OpenProtocol
* [0x298a] EFI_BOOT_SERVICES->OpenProtocol
* [0x29c2] EFI_BOOT_SERVICES->OpenProtocol
* [0x2bee] EFI_BOOT_SERVICES->OpenProtocol
* [0x593] EFI_BOOT_SERVICES->CloseProtocol
* [0x7a4] EFI_BOOT_SERVICES->CloseProtocol
* [0x8ca] EFI_BOOT_SERVICES->CloseProtocol
* [0xd95] EFI_BOOT_SERVICES->CloseProtocol
* [0x2a09] EFI_BOOT_SERVICES->CloseProtocol
* [0x2c35] EFI_BOOT_SERVICES->CloseProtocol
* [0x2c53] EFI_BOOT_SERVICES->CloseProtocol
* [0x4f1] EFI_BOOT_SERVICES->LocateProtocol
* [0x653] EFI_BOOT_SERVICES->LocateProtocol
* [0x14e7] EFI_BOOT_SERVICES->LocateProtocol
* [0x35b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3c2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3e6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb0d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xbb7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc7c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2b8d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb48] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xdfd] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xe1e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x3a30]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x3a60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x3a00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x3a10]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiVgaMiniPortProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C7735A2F-88F5-4882-AE63FAAC8C8B86B3
* [0x3a30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x3a00]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x3a10]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiVgaMiniPortProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C7735A2F-88F5-4882-AE63FAAC8C8B86B3
* [0x39b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x39e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiEdidOverrideProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 48ECB431-FB72-45C0-A922F458FE040BD5
* [0x3a20]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0x3a60]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x3a10]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiVgaMiniPortProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C7735A2F-88F5-4882-AE63FAAC8C8B86B3
## Module: CustomSMBIOS
### Boot services:
* [0x864] EFI_BOOT_SERVICES->HandleProtocol
* [0x83c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x325] EFI_BOOT_SERVICES->LocateProtocol
* [0xade] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xda0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLegacyRegion2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 70101EAF-0085-440C-B3568EE36FEF24F0
* [0xdb0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_SMBIOS_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5E90A50D-6955-4A49-9032DA3812F8E8E5
* [0xdc0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 19B1DB23-E657-4D6D-B9736F4D08F07AA4
## Module: DataHubDxe
### Boot services:
* empty
### Protocols:
* empty
## Module: DevicePathDxe
### Boot services:
* [0x304] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: Dhcp4Dxe
### Boot services:
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xab6] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xe20] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x5a0] EFI_BOOT_SERVICES->OpenProtocol
* [0x872] EFI_BOOT_SERVICES->OpenProtocol
* [0xa23] EFI_BOOT_SERVICES->OpenProtocol
* [0xc90] EFI_BOOT_SERVICES->OpenProtocol
* [0xd7f] EFI_BOOT_SERVICES->OpenProtocol
* [0x353c] EFI_BOOT_SERVICES->OpenProtocol
* [0x3eda] EFI_BOOT_SERVICES->OpenProtocol
* [0x50b2] EFI_BOOT_SERVICES->OpenProtocol
* [0x5101] EFI_BOOT_SERVICES->OpenProtocol
* [0x5d7b] EFI_BOOT_SERVICES->OpenProtocol
* [0xdf6] EFI_BOOT_SERVICES->CloseProtocol
* [0xebb] EFI_BOOT_SERVICES->CloseProtocol
* [0x379f] EFI_BOOT_SERVICES->CloseProtocol
* [0x3b51] EFI_BOOT_SERVICES->CloseProtocol
* [0x515f] EFI_BOOT_SERVICES->CloseProtocol
* [0x5257] EFI_BOOT_SERVICES->CloseProtocol
* [0x5296] EFI_BOOT_SERVICES->CloseProtocol
* [0x9a7] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x3e57] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x565] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x90c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc33] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xcb7] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x67e0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x67f0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6800]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6770]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDhcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9D9A39D8-BD42-4A73-A4D58EE94BE11380
* [0x6790]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0x67e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x67f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6800]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6810]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x6780]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 83F01464-99BD-45E5-B383AF6305D8E9E6
* [0x6770]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9D9A39D8-BD42-4A73-A4D58EE94BE11380
* [0x67a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x6790]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0x67a0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x67c0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x67a0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x67d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 480F8AE9-0C46-4AA9-BC89DB9FBA619806
* [0x6790]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0x6790]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
## Module: Dhcp6Dxe
### Boot services:
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xb89] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xe47] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x6a9] EFI_BOOT_SERVICES->HandleProtocol
* [0x6735] EFI_BOOT_SERVICES->HandleProtocol
* [0x67a5] EFI_BOOT_SERVICES->HandleProtocol
* [0x6e8f] EFI_BOOT_SERVICES->HandleProtocol
* [0x968] EFI_BOOT_SERVICES->OpenProtocol
* [0x9ae] EFI_BOOT_SERVICES->OpenProtocol
* [0xb03] EFI_BOOT_SERVICES->OpenProtocol
* [0xca8] EFI_BOOT_SERVICES->OpenProtocol
* [0xd86] EFI_BOOT_SERVICES->OpenProtocol
* [0x1eea] EFI_BOOT_SERVICES->OpenProtocol
* [0x5b00] EFI_BOOT_SERVICES->OpenProtocol
* [0x5b4f] EFI_BOOT_SERVICES->OpenProtocol
* [0x66eb] EFI_BOOT_SERVICES->OpenProtocol
* [0xdfc] EFI_BOOT_SERVICES->CloseProtocol
* [0x5ba9] EFI_BOOT_SERVICES->CloseProtocol
* [0x5ca3] EFI_BOOT_SERVICES->CloseProtocol
* [0x5ce2] EFI_BOOT_SERVICES->CloseProtocol
* [0xa87] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x1e67] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x568] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9fc] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc63] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xccf] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x7060]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x7070]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x7080]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6ff0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDhcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9FB9A8A1-2F4A-43A6-889CD0F7B6C47AD5
* [0x7000]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0x7060]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x7070]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x7080]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x7090]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x7010]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp6ConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 937FE521-95AE-4D1A-892948BCD90AD31A
* [0x70a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0x7050]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x6fd0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 66ED4721-3C98-4D3E-81E3D03DD39A7254
* [0x6ff0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9FB9A8A1-2F4A-43A6-889CD0F7B6C47AD5
* [0x6fe0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x7000]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0x6fe0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x7030]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x6fe0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x7040]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 480F8AE9-0C46-4AA9-BC89DB9FBA619806
* [0x7000]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0x7000]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
## Module: DiskIoDxe
### Boot services:
* [0x35e] EFI_BOOT_SERVICES->OpenProtocol
* [0x3eb] EFI_BOOT_SERVICES->OpenProtocol
* [0x42b] EFI_BOOT_SERVICES->OpenProtocol
* [0x5f1] EFI_BOOT_SERVICES->OpenProtocol
* [0x62b] EFI_BOOT_SERVICES->OpenProtocol
* [0x381] EFI_BOOT_SERVICES->CloseProtocol
* [0x581] EFI_BOOT_SERVICES->CloseProtocol
* [0x737] EFI_BOOT_SERVICES->CloseProtocol
* [0x760] EFI_BOOT_SERVICES->CloseProtocol
* [0x31b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x50a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x51c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x686] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x6a1] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x2180]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x2190]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A77B2472-E282-4E9F-A245C2C0E27BBCC1
* [0x2160]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0x2170]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 151C8EAE-7F2C-472C-9E549828194F6A88
* [0x2180]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x2190]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiBlockIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A77B2472-E282-4E9F-A245C2C0E27BBCC1
* [0x2170]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDiskIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 151C8EAE-7F2C-472C-9E549828194F6A88
* [0x2170]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDiskIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 151C8EAE-7F2C-472C-9E549828194F6A88
## Module: DnsDxe
### Boot services:
* [0x823] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x86c] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x8b5] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xe38] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1074] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1383] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x16d2] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x309] EFI_BOOT_SERVICES->HandleProtocol
* [0x7bb] EFI_BOOT_SERVICES->HandleProtocol
* [0x845] EFI_BOOT_SERVICES->HandleProtocol
* [0x88e] EFI_BOOT_SERVICES->HandleProtocol
* [0x543a] EFI_BOOT_SERVICES->HandleProtocol
* [0x8315] EFI_BOOT_SERVICES->HandleProtocol
* [0x8385] EFI_BOOT_SERVICES->HandleProtocol
* [0x8d1b] EFI_BOOT_SERVICES->HandleProtocol
* [0xc75] EFI_BOOT_SERVICES->OpenProtocol
* [0xcb1] EFI_BOOT_SERVICES->OpenProtocol
* [0xdbf] EFI_BOOT_SERVICES->OpenProtocol
* [0xeb1] EFI_BOOT_SERVICES->OpenProtocol
* [0xeed] EFI_BOOT_SERVICES->OpenProtocol
* [0xffb] EFI_BOOT_SERVICES->OpenProtocol
* [0x115d] EFI_BOOT_SERVICES->OpenProtocol
* [0x11d6] EFI_BOOT_SERVICES->OpenProtocol
* [0x12b7] EFI_BOOT_SERVICES->OpenProtocol
* [0x14b5] EFI_BOOT_SERVICES->OpenProtocol
* [0x152e] EFI_BOOT_SERVICES->OpenProtocol
* [0x160f] EFI_BOOT_SERVICES->OpenProtocol
* [0x36a6] EFI_BOOT_SERVICES->OpenProtocol
* [0x372c] EFI_BOOT_SERVICES->OpenProtocol
* [0x5360] EFI_BOOT_SERVICES->OpenProtocol
* [0x540f] EFI_BOOT_SERVICES->OpenProtocol
* [0x5a80] EFI_BOOT_SERVICES->OpenProtocol
* [0x61a3] EFI_BOOT_SERVICES->OpenProtocol
* [0x623d] EFI_BOOT_SERVICES->OpenProtocol
* [0x827f] EFI_BOOT_SERVICES->OpenProtocol
* [0x82cb] EFI_BOOT_SERVICES->OpenProtocol
* [0x1204] EFI_BOOT_SERVICES->CloseProtocol
* [0x1330] EFI_BOOT_SERVICES->CloseProtocol
* [0x135a] EFI_BOOT_SERVICES->CloseProtocol
* [0x155c] EFI_BOOT_SERVICES->CloseProtocol
* [0x167f] EFI_BOOT_SERVICES->CloseProtocol
* [0x16a9] EFI_BOOT_SERVICES->CloseProtocol
* [0x5937] EFI_BOOT_SERVICES->CloseProtocol
* [0x5984] EFI_BOOT_SERVICES->CloseProtocol
* [0x5c5b] EFI_BOOT_SERVICES->CloseProtocol
* [0x61ed] EFI_BOOT_SERVICES->CloseProtocol
* [0x6283] EFI_BOOT_SERVICES->CloseProtocol
* [0x63b3] EFI_BOOT_SERVICES->CloseProtocol
* [0x63f2] EFI_BOOT_SERVICES->CloseProtocol
* [0x365a] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x36e3] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x85bf] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x780] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2ec] EFI_BOOT_SERVICES->LocateProtocol
* [0xd2f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xf6b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1116] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x146e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x7dfd] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xbb1] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xbeb] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1187] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x14df] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x8f50]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x8f60]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x8f70]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x8e40]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDns4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B625B186-E063-44F7-89056A74DC6F52B4
* [0x8ed0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDns6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7F1647C8-B76E-44B2-A565F70FF19CD19E
* [0x8e50]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDns4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AE3D28CC-E05B-4FA1-A0117EB55A3F1401
* [0x8ee0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDns6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CA37BC1F-A327-4AE9-828A8C40D8506A17
* [0x8f80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x8f50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x8f60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x8f70]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x8ea0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp4Config2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B446ED1-E30B-4FAA-871A3654ECA36080
* [0x8f90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0x8f40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x8e40]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B625B186-E063-44F7-89056A74DC6F52B4
* [0x8e60]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 83F01464-99BD-45E5-B383AF6305D8E9E6
* [0x8ed0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7F1647C8-B76E-44B2-A565F70FF19CD19E
* [0x8ef0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 66ED4721-3C98-4D3E-81E3D03DD39A7254
* [0x8e70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x8e50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AE3D28CC-E05B-4FA1-A0117EB55A3F1401
* [0x8f00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x8ee0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CA37BC1F-A327-4AE9-828A8C40D8506A17
* [0x8ec0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x8e90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0x8f20]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0x8e70]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x8f00]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x8e90]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0x8ec0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x8f20]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0x8f00]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x8e70]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x8f30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 480F8AE9-0C46-4AA9-BC89DB9FBA619806
* [0x8f50]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x8f50]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x8e50]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDns4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AE3D28CC-E05B-4FA1-A0117EB55A3F1401
* [0x8ee0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDns6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CA37BC1F-A327-4AE9-828A8C40D8506A17
## Module: DnsrDxe
### Boot services:
* [0x3646] EFI_BOOT_SERVICES->HandleProtocol
* [0x392e] EFI_BOOT_SERVICES->HandleProtocol
* [0x3ea2] EFI_BOOT_SERVICES->HandleProtocol
* [0x414e] EFI_BOOT_SERVICES->HandleProtocol
* [0x3899] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x40b9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x132c] EFI_BOOT_SERVICES->LocateProtocol
* [0x13c9] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d46] EFI_BOOT_SERVICES->LocateProtocol
* [0x1daa] EFI_BOOT_SERVICES->LocateProtocol
* [0x138e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x5360]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x5350]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUdp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 83F01464-99BD-45E5-B383AF6305D8E9E6
* [0x5340]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0x5330]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDhcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9D9A39D8-BD42-4A73-A4D58EE94BE11380
* [0x5350]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiUdp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 83F01464-99BD-45E5-B383AF6305D8E9E6
* [0x5330]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiDhcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9D9A39D8-BD42-4A73-A4D58EE94BE11380
* [0x5370]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 9B1B8BF5-88D3-4994-9E8B0DBAF9853447
* [0x5310]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
* [0x5320]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
## Module: DpcDxe
### Boot services:
* [0x2f2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: DpsdSetup
### Boot services:
* [0x74fb] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x751a] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xa5e] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fc5] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fea] EFI_BOOT_SERVICES->HandleProtocol
* [0x300f] EFI_BOOT_SERVICES->HandleProtocol
* [0x3990] EFI_BOOT_SERVICES->HandleProtocol
* [0x3c6e] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d20] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d4e] EFI_BOOT_SERVICES->HandleProtocol
* [0x3e29] EFI_BOOT_SERVICES->HandleProtocol
* [0x40c4] EFI_BOOT_SERVICES->HandleProtocol
* [0x417b] EFI_BOOT_SERVICES->HandleProtocol
* [0x4223] EFI_BOOT_SERVICES->HandleProtocol
* [0x4586] EFI_BOOT_SERVICES->HandleProtocol
* [0x463b] EFI_BOOT_SERVICES->HandleProtocol
* [0x46f2] EFI_BOOT_SERVICES->HandleProtocol
* [0x4a7f] EFI_BOOT_SERVICES->HandleProtocol
* [0x4aee] EFI_BOOT_SERVICES->HandleProtocol
* [0x8e50] EFI_BOOT_SERVICES->HandleProtocol
* [0xb707] EFI_BOOT_SERVICES->HandleProtocol
* [0xb78f] EFI_BOOT_SERVICES->HandleProtocol
* [0xb888] EFI_BOOT_SERVICES->HandleProtocol
* [0xc6aa] EFI_BOOT_SERVICES->HandleProtocol
* [0xcb96] EFI_BOOT_SERVICES->HandleProtocol
* [0x97f8] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3acd] EFI_BOOT_SERVICES->OpenProtocol
* [0x8d1a] EFI_BOOT_SERVICES->OpenProtocol
* [0x8d55] EFI_BOOT_SERVICES->OpenProtocol
* [0x8d90] EFI_BOOT_SERVICES->OpenProtocol
* [0xa435] EFI_BOOT_SERVICES->OpenProtocol
* [0xa473] EFI_BOOT_SERVICES->OpenProtocol
* [0xa4b1] EFI_BOOT_SERVICES->OpenProtocol
* [0xcbcc] EFI_BOOT_SERVICES->OpenProtocol
* [0x35d2] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x37da] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x3d83] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x40fe] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xb6a5] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x3590] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x379e] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0xb63e] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0xa23] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2f78] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x354e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x374b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3c1e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3ce7] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x408b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4536] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4a3d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8cb5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa2bd] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x357] EFI_BOOT_SERVICES->LocateProtocol
* [0x38d] EFI_BOOT_SERVICES->LocateProtocol
* [0x3aa] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c7] EFI_BOOT_SERVICES->LocateProtocol
* [0x3e4] EFI_BOOT_SERVICES->LocateProtocol
* [0x587] EFI_BOOT_SERVICES->LocateProtocol
* [0x9f0] EFI_BOOT_SERVICES->LocateProtocol
* [0xbe7] EFI_BOOT_SERVICES->LocateProtocol
* [0xc16] EFI_BOOT_SERVICES->LocateProtocol
* [0xc7f] EFI_BOOT_SERVICES->LocateProtocol
* [0xca8] EFI_BOOT_SERVICES->LocateProtocol
* [0x243f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2c0d] EFI_BOOT_SERVICES->LocateProtocol
* [0x2d39] EFI_BOOT_SERVICES->LocateProtocol
* [0x31ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x3fe0] EFI_BOOT_SERVICES->LocateProtocol
* [0x4e9b] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f8e] EFI_BOOT_SERVICES->LocateProtocol
* [0x514b] EFI_BOOT_SERVICES->LocateProtocol
* [0x5e13] EFI_BOOT_SERVICES->LocateProtocol
* [0x6051] EFI_BOOT_SERVICES->LocateProtocol
* [0x6a1b] EFI_BOOT_SERVICES->LocateProtocol
* [0x6d7b] EFI_BOOT_SERVICES->LocateProtocol
* [0x6de7] EFI_BOOT_SERVICES->LocateProtocol
* [0x6e0e] EFI_BOOT_SERVICES->LocateProtocol
* [0x72c5] EFI_BOOT_SERVICES->LocateProtocol
* [0x758a] EFI_BOOT_SERVICES->LocateProtocol
* [0x7deb] EFI_BOOT_SERVICES->LocateProtocol
* [0x8468] EFI_BOOT_SERVICES->LocateProtocol
* [0x92c0] EFI_BOOT_SERVICES->LocateProtocol
* [0x979e] EFI_BOOT_SERVICES->LocateProtocol
* [0x9b62] EFI_BOOT_SERVICES->LocateProtocol
* [0x9b82] EFI_BOOT_SERVICES->LocateProtocol
* [0x9bb2] EFI_BOOT_SERVICES->LocateProtocol
* [0x9cf8] EFI_BOOT_SERVICES->LocateProtocol
* [0x9d18] EFI_BOOT_SERVICES->LocateProtocol
* [0x9d47] EFI_BOOT_SERVICES->LocateProtocol
* [0xc0b6] EFI_BOOT_SERVICES->LocateProtocol
* [0xc383] EFI_BOOT_SERVICES->LocateProtocol
* [0xc8ee] EFI_BOOT_SERVICES->LocateProtocol
* [0xca6b] EFI_BOOT_SERVICES->LocateProtocol
* [0xcbf0] EFI_BOOT_SERVICES->LocateProtocol
* [0xc72a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xebe8]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] EEB0F9C4-0238-48ED-8C9B7250DB486B80
* [0xf0c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xdb60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0xdb70]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0xdb90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xdbf0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0xdb80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xdb40]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] AFA4CF3F-AF71-4C30-A4FB2910E771F9B0
* [0xdb30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0xe580]
	 - [service] HandleProtocol
	 - [protocol_name] IDE_SECURITY_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] F4F63529-281E-4040-A313C1D6766384BE
* [0xddf0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0xde10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0xf4c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xddd0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0xe510]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] F109F361-370C-4D9C-B1AB7CA2D4C8B3FF
* [0xdbe0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0xe580]
	 - [service] OpenProtocol
	 - [protocol_name] IDE_SECURITY_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] F4F63529-281E-4040-A313C1D6766384BE
* [0xdb30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0xdb90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xdcd8]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0xdb80]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xdb30]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0xdbc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xdb00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0xdb50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0xdc10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0xdbd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0xdcb8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0xdba0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] D4D2F201-50E8-4D45-8E05FD49A82A1569
* [0xdbb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0xef88]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] F38DF21C-4F6C-449B-9A7B227B52D5D7BA
* [0xef08]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0xebf8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] DAED21EC-43DC-4318-B371F6806D8E62F9
* [0xebc8]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CONSOLE_CONTROL_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] F42F7782-012E-4C12-995649F94304F721
* [0xebb8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] F38DF21C-4F6C-449B-9A7B227B52D5D7BA
* [0xdb20]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C298B206-7FB5-4A7E-94614F3577F1A07A
* [0xdb10]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_SMBIOS_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5E90A50D-6955-4A49-9032DA3812F8E8E5
* [0xe510]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] F109F361-370C-4D9C-B1AB7CA2D4C8B3FF
* [0xdc20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B9D4C360-BCFB-4F9B-929853C136982258
* [0xdad0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3CD7C71C-CBC3-4296-A9BC3CE449B9FF64
* [0xe3b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0xdc98]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0xdce8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0xf4c0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: Dptf
### Boot services:
* [0x42e] EFI_BOOT_SERVICES->HandleProtocol
* [0x516] EFI_BOOT_SERVICES->HandleProtocol
* [0x7bd] EFI_BOOT_SERVICES->HandleProtocol
* [0x997] EFI_BOOT_SERVICES->HandleProtocol
* [0x3fa] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4e4] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x78b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x965] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5cb] EFI_BOOT_SERVICES->LocateProtocol
* [0x872] EFI_BOOT_SERVICES->LocateProtocol
* [0xa4c] EFI_BOOT_SERVICES->LocateProtocol
* [0xb5f] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xf00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xee0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0xef0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0xf10]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: DxeBoardConfigInit
### Boot services:
* [0xf5b] EFI_BOOT_SERVICES->HandleProtocol
* [0x1812] EFI_BOOT_SERVICES->HandleProtocol
* [0x2092] EFI_BOOT_SERVICES->HandleProtocol
* [0x3b7] EFI_BOOT_SERVICES->LocateProtocol
* [0x5a7] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3080]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_PLATFORM_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] D9035175-8CE2-47DE-A8B8CC98E5E2A885
* [0x3090]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: DxeCore
### Boot services:
* [0x15322] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1976] EFI_BOOT_SERVICES->HandleProtocol
* [0x11d00] EFI_BOOT_SERVICES->HandleProtocol
* [0x11df2] EFI_BOOT_SERVICES->HandleProtocol
* [0x12001] EFI_BOOT_SERVICES->HandleProtocol
* [0x120b7] EFI_BOOT_SERVICES->HandleProtocol
* [0x143f6] EFI_BOOT_SERVICES->HandleProtocol
* [0x14729] EFI_BOOT_SERVICES->HandleProtocol
* [0x14766] EFI_BOOT_SERVICES->HandleProtocol
* [0x14d16] EFI_BOOT_SERVICES->HandleProtocol
* [0xf1d6] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x153bf] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x143b5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x146ed] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x14c69] EFI_BOOT_SERVICES->LocateProtocol
* [0x1506e] EFI_BOOT_SERVICES->LocateProtocol
* [0x15147] EFI_BOOT_SERVICES->LocateProtocol
* [0x158be] EFI_BOOT_SERVICES->LocateProtocol
* [0x15bf7] EFI_BOOT_SERVICES->LocateProtocol
* [0x15faa] EFI_BOOT_SERVICES->LocateProtocol
* [0x1612b] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x16f50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x16f40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x16ec0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
* [0x16ee0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFile2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4006C0C1-FCB3-403E-996D4A6C8724E06D
* [0x16ed0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 56EC3091-954C-11D2-8E3F00A0C969723B
* [0x17318]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x17308]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x171a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x171c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
## Module: DxeOverClock
### Boot services:
* [0x4e6] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x449] EFI_BOOT_SERVICES->LocateProtocol
* [0x496] EFI_BOOT_SERVICES->LocateProtocol
* [0x53c] EFI_BOOT_SERVICES->LocateProtocol
* [0x609] EFI_BOOT_SERVICES->LocateProtocol
* [0x74d] EFI_BOOT_SERVICES->LocateProtocol
* [0x8b4] EFI_BOOT_SERVICES->LocateProtocol
* [0x99c] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b9b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ce7] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e1f] EFI_BOOT_SERVICES->LocateProtocol
* [0x516] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2020]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] D4D2F201-50E8-4D45-8E05FD49A82A1569
* [0x2030]
	 - [service] LocateProtocol
	 - [protocol_name] WDT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B42B8D12-2ACB-499A-A920DD5BE6CF09B1
* [0x2020]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] D4D2F201-50E8-4D45-8E05FD49A82A1569
* [0x2050]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
* [0x2040]
	 - [service] LocateProtocol
	 - [protocol_name] WDT_APP_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 92C7D0BB-679E-479D-878DD4B82968578B
* [0x2060]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_PLATFORM_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] D9035175-8CE2-47DE-A8B8CC98E5E2A885
* [0x2080]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 8D9B3387-73DB-456F-889D6FFE90826409
## Module: DxeSignBiosAuthenticate
### Boot services:
* [0x33d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2e96] EFI_BOOT_SERVICES->HandleProtocol
* [0x3135] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xb130]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDebugMaskProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4C8A2451-C207-405B-969499EA13251341
* [0xb150]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
## Module: EbcDxe
### Boot services:
* [0x421] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4f8] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x3c9] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x5cd] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3a0] EFI_BOOT_SERVICES->HandleProtocol
* [0x5a4] EFI_BOOT_SERVICES->HandleProtocol
* [0x368] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x56f] EFI_BOOT_SERVICES->LocateHandleBuffer
### Protocols:
* empty
## Module: EnglishDxe
### Boot services:
* [0x3b8] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: EsrtDxe
### Boot services:
* [0x7d1] EFI_BOOT_SERVICES->HandleProtocol
* [0x68e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xafd] EFI_BOOT_SERVICES->LocateProtocol
* [0x36a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x14e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareManagementProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 86C77A67-0B97-4633-A18749104D0685C7
* [0x1500]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
## Module: EventLog
### Boot services:
* [0x2fd] EFI_BOOT_SERVICES->LocateProtocol
* [0x38e] EFI_BOOT_SERVICES->LocateProtocol
* [0xdaa] EFI_BOOT_SERVICES->LocateProtocol
* [0xfd0] EFI_BOOT_SERVICES->LocateProtocol
* [0xff6] EFI_BOOT_SERVICES->LocateProtocol
* [0x11a8] EFI_BOOT_SERVICES->LocateProtocol
* [0x11c6] EFI_BOOT_SERVICES->LocateProtocol
* [0xe94] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x1ae8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AD61F191-AE5F-4C0E-B9FAE869D288C64F
* [0x1ac8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] DAED21EC-43DC-4318-B371F6806D8E62F9
* [0x1470]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_DATA_HUB_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] AE80D021-618E-11D4-BCD70080C73C8881
## Module: FanDxe
### Boot services:
* [0x369] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x850]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: FastBootRuntime
### Boot services:
* [0x13c7] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x108a] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x114a] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2680]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiVariableArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 1E5668E2-8481-11D4-BCF10080C73C8881
* [0x2010]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: Fat
### Boot services:
* [0x5a9] EFI_BOOT_SERVICES->HandleProtocol
* [0x6f7] EFI_BOOT_SERVICES->HandleProtocol
* [0x72d] EFI_BOOT_SERVICES->HandleProtocol
* [0x832] EFI_BOOT_SERVICES->OpenProtocol
* [0x880] EFI_BOOT_SERVICES->OpenProtocol
* [0x95a] EFI_BOOT_SERVICES->OpenProtocol
* [0x996] EFI_BOOT_SERVICES->OpenProtocol
* [0x9cc] EFI_BOOT_SERVICES->OpenProtocol
* [0xa25] EFI_BOOT_SERVICES->OpenProtocol
* [0xade] EFI_BOOT_SERVICES->OpenProtocol
* [0x1960] EFI_BOOT_SERVICES->OpenProtocol
* [0x5e52] EFI_BOOT_SERVICES->OpenProtocol
* [0x855] EFI_BOOT_SERVICES->CloseProtocol
* [0xa4b] EFI_BOOT_SERVICES->CloseProtocol
* [0xa69] EFI_BOOT_SERVICES->CloseProtocol
* [0xb1d] EFI_BOOT_SERVICES->CloseProtocol
* [0xb3b] EFI_BOOT_SERVICES->CloseProtocol
* [0x5e74] EFI_BOOT_SERVICES->CloseProtocol
* [0x653] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x18f3] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x61b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1432] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x771] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x789] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x7ca] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x14a3] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x350]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x2c0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0x2e0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x2d0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 151C8EAE-7F2C-472C-9E549828194F6A88
* [0x2f0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
* [0x2c0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0x2d0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDiskIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 151C8EAE-7F2C-472C-9E549828194F6A88
* [0x320]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x2f0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
## Module: FileExplorerLite
### Boot services:
* [0x838] EFI_BOOT_SERVICES->HandleProtocol
* [0xa58] EFI_BOOT_SERVICES->HandleProtocol
* [0xb85] EFI_BOOT_SERVICES->HandleProtocol
* [0xbec] EFI_BOOT_SERVICES->HandleProtocol
* [0x1651] EFI_BOOT_SERVICES->HandleProtocol
* [0x16b7] EFI_BOOT_SERVICES->HandleProtocol
* [0x179e] EFI_BOOT_SERVICES->HandleProtocol
* [0x17df] EFI_BOOT_SERVICES->HandleProtocol
* [0x1b67] EFI_BOOT_SERVICES->HandleProtocol
* [0x1cb4] EFI_BOOT_SERVICES->HandleProtocol
* [0x1d4a] EFI_BOOT_SERVICES->HandleProtocol
* [0x1f5c] EFI_BOOT_SERVICES->HandleProtocol
* [0x256f] EFI_BOOT_SERVICES->HandleProtocol
* [0x975] EFI_BOOT_SERVICES->OpenProtocol
* [0x472] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x67f] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x430] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x643] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x3ee] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5eb] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa1f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xb00] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1f14] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x19c0] EFI_BOOT_SERVICES->LocateProtocol
* [0x38e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2960]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x2920]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x2970]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
* [0x2940]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x2900]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x2910]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0x28f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0x2950]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x2920]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x2970]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
* [0x2930]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
## Module: FirmwareVersionInfoDxe
### Boot services:
* [0x867] EFI_BOOT_SERVICES->HandleProtocol
* [0x8e4] EFI_BOOT_SERVICES->HandleProtocol
* [0xe0d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x833] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x7f3] EFI_BOOT_SERVICES->LocateProtocol
* [0x971] EFI_BOOT_SERVICES->LocateProtocol
* [0x9ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x9d1] EFI_BOOT_SERVICES->LocateProtocol
* [0xaa6] EFI_BOOT_SERVICES->LocateProtocol
* [0xadb] EFI_BOOT_SERVICES->LocateProtocol
* [0xb00] EFI_BOOT_SERVICES->LocateProtocol
* [0xccb] EFI_BOOT_SERVICES->LocateProtocol
* [0xe5a] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x11e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x1230]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x11e0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x11b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPxeBaseCodeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03C4E603-AC28-11D3-9A2D0090273FC14D
* [0x11c0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 651B7EBD-CE13-41D0-82E5A063ABBE9BB6
* [0x11d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x1200]
	 - [service] LocateProtocol
	 - [protocol_name] BDS_ALL_DRIVERS_CONNECTED_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] DBC9FD21-FAD8-45B0-9E7827158867CC93
* [0x11f0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_PLATFORM_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] D9035175-8CE2-47DE-A8B8CC98E5E2A885
* [0x1210]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0x1220]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: FlashDriver
### Boot services:
* [0x108a] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1175] EFI_BOOT_SERVICES->LocateProtocol
* [0x11fc] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x6040]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: FlashDriverSmm
### Boot services:
* [0x654] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x679] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x69e] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3a8] EFI_BOOT_SERVICES->LocateProtocol
* [0x3d6] EFI_BOOT_SERVICES->LocateProtocol
* [0x45d] EFI_BOOT_SERVICES->LocateProtocol
* [0x4ba] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x4460]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x4470]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
## Module: FlashSmiDxe
### Boot services:
* [0x1d85] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x115a] EFI_BOOT_SERVICES->LocateProtocol
* [0x118f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a67] EFI_BOOT_SERVICES->LocateProtocol
* [0x1aae] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3030]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3020]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x3010]
	 - [service] LocateProtocol
	 - [protocol_name] FLASH_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 755B6596-6896-4BA3-B3DD1C629FD1EA88
## Module: FlashSmiSmm
### Boot services:
* [0x300] EFI_BOOT_SERVICES->LocateProtocol
* [0x33b] EFI_BOOT_SERVICES->LocateProtocol
* [0x7f0] EFI_BOOT_SERVICES->LocateProtocol
* [0xbd5] EFI_BOOT_SERVICES->LocateProtocol
* [0xcbd] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x38d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x38c0]
	 - [service] LocateProtocol
	 - [protocol_name] FLASH_SMM_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] ECB867AB-8DF4-492D-8150A7FD1B9B5A75
* [0x38f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
* [0x4058]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: FsDxe
### Boot services:
* [0x1ec8] EFI_BOOT_SERVICES->HandleProtocol
* [0x1e3d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1f4b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1fac] EFI_BOOT_SERVICES->LocateProtocol
* [0x2053] EFI_BOOT_SERVICES->LocateProtocol
* [0x2018] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1eff] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x205d0]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] BC89139B-93C6-4338-9805C371A55761EF
* [0x205d0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] BC89139B-93C6-4338-9805C371A55761EF
* [0x205d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] BC89139B-93C6-4338-9805C371A55761EF
* [0x205d0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] BC89139B-93C6-4338-9805C371A55761EF
## Module: GenericSio
### Boot services:
* [0x3b5f] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x123c] EFI_BOOT_SERVICES->OpenProtocol
* [0x129f] EFI_BOOT_SERVICES->OpenProtocol
* [0x12d0] EFI_BOOT_SERVICES->OpenProtocol
* [0x25e0] EFI_BOOT_SERVICES->OpenProtocol
* [0x2a6d] EFI_BOOT_SERVICES->OpenProtocol
* [0x2b03] EFI_BOOT_SERVICES->OpenProtocol
* [0x1272] EFI_BOOT_SERVICES->CloseProtocol
* [0x143c] EFI_BOOT_SERVICES->CloseProtocol
* [0x2ac6] EFI_BOOT_SERVICES->CloseProtocol
* [0x2dd8] EFI_BOOT_SERVICES->CloseProtocol
* [0x2f06] EFI_BOOT_SERVICES->CloseProtocol
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x6cb] EFI_BOOT_SERVICES->LocateProtocol
* [0x75b] EFI_BOOT_SERVICES->LocateProtocol
* [0x35bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x4411] EFI_BOOT_SERVICES->LocateProtocol
* [0x4588] EFI_BOOT_SERVICES->LocateProtocol
* [0x551e] EFI_BOOT_SERVICES->LocateProtocol
* [0xd57] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x25a3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2e2c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x5870]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiVariableWriteArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6441F818-6362-4E44-B5707DBA31DD2453
* [0x5850]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x5860]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x5850]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x5860]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x5880]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x57f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 4250CEC2-DDDB-400B-8C62CF9864F6D154
* [0x57d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 9D36F7EF-6078-4419-8C462BBDB0E0C7B3
* [0x5820]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x5e30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EB97088E-CFDF-49C6-BE4BD906A5B20E86
* [0x5dd8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x5890]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 4FC0733F-6FD2-491B-A8905374521BF48F
* [0x5830]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 51E9B4F9-555D-476C-8BB5BD18D9A68878
## Module: GopDebugDxe
### Boot services:
* [0x338] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* empty
## Module: GraphicsConsole
### Boot services:
* [0x4c3] EFI_BOOT_SERVICES->HandleProtocol
* [0x34a] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x697] EFI_BOOT_SERVICES->OpenProtocol
* [0x6e5] EFI_BOOT_SERVICES->OpenProtocol
* [0x81c] EFI_BOOT_SERVICES->OpenProtocol
* [0xa1b] EFI_BOOT_SERVICES->OpenProtocol
* [0x6ba] EFI_BOOT_SERVICES->CloseProtocol
* [0x983] EFI_BOOT_SERVICES->CloseProtocol
* [0xa4d] EFI_BOOT_SERVICES->CloseProtocol
* [0xaa8] EFI_BOOT_SERVICES->CloseProtocol
* [0x48b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x581] EFI_BOOT_SERVICES->LocateProtocol
* [0x705] EFI_BOOT_SERVICES->LocateProtocol
* [0x847] EFI_BOOT_SERVICES->LocateProtocol
* [0x2112] EFI_BOOT_SERVICES->LocateProtocol
* [0x244b] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x962] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa85] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x30b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x30f0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x30d0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0x30a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x30c0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x30d0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0x30c0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x3710]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x30e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x36c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x30c0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
## Module: HardwareSignatureEntry
### Boot services:
* [0x350] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7bf] EFI_BOOT_SERVICES->HandleProtocol
* [0x148c] EFI_BOOT_SERVICES->HandleProtocol
* [0x1dd9] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x76f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x13bd] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x18dc] EFI_BOOT_SERVICES->LocateProtocol
* [0x197f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b72] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* empty
## Module: HddSecurity
### Boot services:
* [0x3da] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x709] EFI_BOOT_SERVICES->HandleProtocol
* [0x7a3] EFI_BOOT_SERVICES->HandleProtocol
* [0x877] EFI_BOOT_SERVICES->HandleProtocol
* [0x1326] EFI_BOOT_SERVICES->HandleProtocol
* [0x1e34] EFI_BOOT_SERVICES->HandleProtocol
* [0xc20] EFI_BOOT_SERVICES->OpenProtocol
* [0x6c3] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x33c] EFI_BOOT_SERVICES->LocateProtocol
* [0x499] EFI_BOOT_SERVICES->LocateProtocol
* [0x567] EFI_BOOT_SERVICES->LocateProtocol
* [0x68f] EFI_BOOT_SERVICES->LocateProtocol
* [0xe5f] EFI_BOOT_SERVICES->LocateProtocol
* [0xfe8] EFI_BOOT_SERVICES->LocateProtocol
* [0x20d0] EFI_BOOT_SERVICES->LocateProtocol
* [0x246a] EFI_BOOT_SERVICES->LocateProtocol
* [0xd6a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xf32] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x29d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x29c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x2970]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x2990]
	 - [service] OpenProtocol
	 - [protocol_name] IDE_SECURITY_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] F4F63529-281E-4040-A313C1D6766384BE
* [0x2980]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmControl2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 843DC720-AB1E-42CB-93578A0078F3561B
* [0x2f68]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x29a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x2990]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] IDE_SECURITY_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] F4F63529-281E-4040-A313C1D6766384BE
## Module: HddSmart
### Boot services:
* [0x4f7] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x787] EFI_BOOT_SERVICES->HandleProtocol
* [0x7b1] EFI_BOOT_SERVICES->HandleProtocol
* [0x201a] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x21bd] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3786] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x422] EFI_BOOT_SERVICES->OpenProtocol
* [0x14a5] EFI_BOOT_SERVICES->OpenProtocol
* [0x344] EFI_BOOT_SERVICES->LocateProtocol
* [0x362] EFI_BOOT_SERVICES->LocateProtocol
* [0x37f] EFI_BOOT_SERVICES->LocateProtocol
* [0x39c] EFI_BOOT_SERVICES->LocateProtocol
* [0x447] EFI_BOOT_SERVICES->LocateProtocol
* [0x105b] EFI_BOOT_SERVICES->LocateProtocol
* [0x28d6] EFI_BOOT_SERVICES->LocateProtocol
* [0x2c0f] EFI_BOOT_SERVICES->LocateProtocol
* [0x3594] EFI_BOOT_SERVICES->LocateProtocol
* [0x17a5] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1856] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x3cf0]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] AFA4CF3F-AF71-4C30-A4FB2910E771F9B0
* [0x3d00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 52C78312-8EDC-4233-98F21A1AA5E388A5
* [0x4338]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0x3cc0]
	 - [service] OpenProtocol
	 - [protocol_name] IDE_SMART_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] FFBD9AD2-F1DB-4F92-A649EB9EEDEA86B5
* [0x3d20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x3d40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x3d50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x3d10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x4348]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x3cd0]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_POST_MANAGER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8A91B1E1-56C7-4ADC-ABEB1C2CA1729EFF
* [0x42f8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x3de0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x3cc0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] IDE_SMART_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] FFBD9AD2-F1DB-4F92-A649EB9EEDEA86B5
## Module: HeciInit
### Boot services:
* [0xe3e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xbb8] EFI_BOOT_SERVICES->HandleProtocol
* [0x58d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xb88] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x301] EFI_BOOT_SERVICES->LocateProtocol
* [0x504] EFI_BOOT_SERVICES->LocateProtocol
* [0x6d6] EFI_BOOT_SERVICES->LocateProtocol
* [0xa2e] EFI_BOOT_SERVICES->LocateProtocol
* [0xadd] EFI_BOOT_SERVICES->LocateProtocol
* [0xd8b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1666] EFI_BOOT_SERVICES->LocateProtocol
* [0x1777] EFI_BOOT_SERVICES->LocateProtocol
* [0x4d8] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2d80]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] CC9D5C0B-9010-45F1-993C832767F16777
* [0x2d90]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0x2dd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x2d90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0x2d70]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
* [0x2da0]
	 - [service] LocateProtocol
	 - [protocol_name] WDT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B42B8D12-2ACB-499A-A920DD5BE6CF09B1
* [0x2db0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] A0B5DC52-4F34-3990-D491108BE8BA7542
* [0x2dc0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 8D9B3387-73DB-456F-889D6FFE90826409
## Module: HiiDatabase
### Boot services:
* [0xe3f6] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xe44a] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x4155] EFI_BOOT_SERVICES->HandleProtocol
* [0x4463] EFI_BOOT_SERVICES->HandleProtocol
* [0x49b1] EFI_BOOT_SERVICES->HandleProtocol
* [0x889e] EFI_BOOT_SERVICES->HandleProtocol
* [0xd29f] EFI_BOOT_SERVICES->HandleProtocol
* [0x153ff] EFI_BOOT_SERVICES->HandleProtocol
* [0x8fff] EFI_BOOT_SERVICES->OpenProtocol
* [0x4418] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xd25d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3f6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x43e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8f58] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9069] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x15730]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiHiiConfigAccessProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 330D4706-F2A0-4E4F-A369B66FA8D54385
* [0x156d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x15750]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0x156a0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 348C4D62-BFBD-4882-9ECEC80BB1C4783B
* [0x156a0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 348C4D62-BFBD-4882-9ECEC80BB1C4783B
## Module: HkUpdate
### Boot services:
* [0x509] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x15d2] EFI_BOOT_SERVICES->HandleProtocol
* [0x3ac5] EFI_BOOT_SERVICES->HandleProtocol
* [0x3bb7] EFI_BOOT_SERVICES->HandleProtocol
* [0x4e8] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3bed] EFI_BOOT_SERVICES->OpenProtocol
* [0x1597] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x344] EFI_BOOT_SERVICES->LocateProtocol
* [0x362] EFI_BOOT_SERVICES->LocateProtocol
* [0x37f] EFI_BOOT_SERVICES->LocateProtocol
* [0x39c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b9] EFI_BOOT_SERVICES->LocateProtocol
* [0x757] EFI_BOOT_SERVICES->LocateProtocol
* [0x848] EFI_BOOT_SERVICES->LocateProtocol
* [0x8ef] EFI_BOOT_SERVICES->LocateProtocol
* [0x1175] EFI_BOOT_SERVICES->LocateProtocol
* [0x119d] EFI_BOOT_SERVICES->LocateProtocol
* [0x11bf] EFI_BOOT_SERVICES->LocateProtocol
* [0x1486] EFI_BOOT_SERVICES->LocateProtocol
* [0x14f4] EFI_BOOT_SERVICES->LocateProtocol
* [0x16b4] EFI_BOOT_SERVICES->LocateProtocol
* [0x16d1] EFI_BOOT_SERVICES->LocateProtocol
* [0x3462] EFI_BOOT_SERVICES->LocateProtocol
* [0x379b] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c11] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b44] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x4000]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x47e8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x41d8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x40e0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0x3fd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x3ff0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x3fe0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x4020]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x4030]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0x4040]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0x4050]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x4788]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 088C3203-070F-4ED1-8CCB1F53962083DB
* [0x4768]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3CD7C71C-CBC3-4296-A9BC3CE449B9FF64
* [0x4778]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B9D4C360-BCFB-4F9B-929853C136982258
* [0x40a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x40f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x47e8]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: HpetTimerDxe
### Boot services:
* [0x955] EFI_BOOT_SERVICES->LocateProtocol
* [0xbca] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xff0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB1-6F42-11D4-BCE70080C73C8881
## Module: HstiResultDxe
### Boot services:
* [0x685] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2ee] EFI_BOOT_SERVICES->LocateProtocol
* [0x366] EFI_BOOT_SERVICES->LocateProtocol
* [0x440] EFI_BOOT_SERVICES->LocateProtocol
* [0x5df] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x790]
	 - [service] LocateProtocol
	 - [protocol_name] AMITSE_NVRAM_UPDATE_GUID
	 - [protocol_place] ami_guids
	 - [guid] D84BEFF0-159A-4B60-9AB9AC5C474BD3B1
* [0x7c0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 0F500BE6-ECE4-4ED8-90819AA9A523FB7B
* [0x7d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] ECA27516-306C-4E28-8C944E521096695E
* [0x7e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
## Module: HstiSiliconDxe
### Boot services:
* [0x317] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x929] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x396e] EFI_BOOT_SERVICES->HandleProtocol
* [0x391d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2df] EFI_BOOT_SERVICES->LocateProtocol
* [0x7aa] EFI_BOOT_SERVICES->LocateProtocol
* [0xe58] EFI_BOOT_SERVICES->LocateProtocol
* [0x107c] EFI_BOOT_SERVICES->LocateProtocol
* [0x1607] EFI_BOOT_SERVICES->LocateProtocol
* [0x4682] EFI_BOOT_SERVICES->LocateProtocol
* [0x50f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x4880]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAdapterInformationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E5DD1403-D622-C24E-8488C71B17F5E802
* [0x4840]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] ECA27516-306C-4E28-8C944E521096695E
* [0x4830]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3FDDA605-A76E-4F46-AD2912F4531B3D08
* [0x4870]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 00C7D289-1347-4DE0-BF420E269D0EF34A
* [0x4860]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTrEEProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 607F766C-7455-42BE-930BE4D76DB2720F
## Module: HttpDxe
### Boot services:
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xb2f] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xe65] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x3e6f] EFI_BOOT_SERVICES->HandleProtocol
* [0x421e] EFI_BOOT_SERVICES->HandleProtocol
* [0x53a] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x78f] EFI_BOOT_SERVICES->OpenProtocol
* [0x8e6] EFI_BOOT_SERVICES->OpenProtocol
* [0xa5e] EFI_BOOT_SERVICES->OpenProtocol
* [0xb8c] EFI_BOOT_SERVICES->OpenProtocol
* [0xbf8] EFI_BOOT_SERVICES->OpenProtocol
* [0xe15] EFI_BOOT_SERVICES->OpenProtocol
* [0x2c05] EFI_BOOT_SERVICES->OpenProtocol
* [0x2c45] EFI_BOOT_SERVICES->OpenProtocol
* [0x2cb3] EFI_BOOT_SERVICES->OpenProtocol
* [0x2cf3] EFI_BOOT_SERVICES->OpenProtocol
* [0x2d2a] EFI_BOOT_SERVICES->OpenProtocol
* [0x3f6b] EFI_BOOT_SERVICES->OpenProtocol
* [0x4306] EFI_BOOT_SERVICES->OpenProtocol
* [0x4b33] EFI_BOOT_SERVICES->OpenProtocol
* [0x4b7f] EFI_BOOT_SERVICES->OpenProtocol
* [0x638] EFI_BOOT_SERVICES->CloseProtocol
* [0x67c] EFI_BOOT_SERVICES->CloseProtocol
* [0x2d8b] EFI_BOOT_SERVICES->CloseProtocol
* [0x2dae] EFI_BOOT_SERVICES->CloseProtocol
* [0x2df2] EFI_BOOT_SERVICES->CloseProtocol
* [0x2e1a] EFI_BOOT_SERVICES->CloseProtocol
* [0x2e3d] EFI_BOOT_SERVICES->CloseProtocol
* [0x2e81] EFI_BOOT_SERVICES->CloseProtocol
* [0x2f94] EFI_BOOT_SERVICES->CloseProtocol
* [0x2fbb] EFI_BOOT_SERVICES->CloseProtocol
* [0x3003] EFI_BOOT_SERVICES->CloseProtocol
* [0x302f] EFI_BOOT_SERVICES->CloseProtocol
* [0x3056] EFI_BOOT_SERVICES->CloseProtocol
* [0x309e] EFI_BOOT_SERVICES->CloseProtocol
* [0x4105] EFI_BOOT_SERVICES->CloseProtocol
* [0x4463] EFI_BOOT_SERVICES->CloseProtocol
* [0x993] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x9e1] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x4eb] EFI_BOOT_SERVICES->LocateProtocol
* [0x6c8] EFI_BOOT_SERVICES->LocateProtocol
* [0x5c3a] EFI_BOOT_SERVICES->LocateProtocol
* [0x82e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xd22] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x494d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5e6] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x6350]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x6360]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6370]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6280]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiHttpServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BDC8E6AF-D9BC-4379-A72AE0C4E75DAE1C
* [0x6290]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiHttpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7A59B29B-910B-4171-8242A85A0DF25B5B
* [0x6350]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x6360]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6370]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6380]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x6330]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp4Config2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B446ED1-E30B-4FAA-871A3654ECA36080
* [0x6340]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp6ConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 937FE521-95AE-4D1A-892948BCD90AD31A
* [0x62a0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiHttpUtilitiesProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3E35C163-4074-45DD-431E23989DD86B32
* [0x6280]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHttpServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BDC8E6AF-D9BC-4379-A72AE0C4E75DAE1C
* [0x62b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 00720665-67EB-4A99-BAF7D3C33A1C7CC9
* [0x62d0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EC20EB79-6C1A-4664-9A0DD2E4CC16D664
* [0x6290]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHttpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7A59B29B-910B-4171-8242A85A0DF25B5B
* [0x6300]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AE3D28CC-E05B-4FA1-A0117EB55A3F1401
* [0x6320]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CA37BC1F-A327-4AE9-828A8C40D8506A17
* [0x62c0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiTcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 65530BC7-A359-410F-B0105AADC7EC2B62
* [0x62e0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiTcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 46E44855-BD60-4AB7-AB0DA679B9447D77
* [0x62b0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiTcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 00720665-67EB-4A99-BAF7D3C33A1C7CC9
* [0x62d0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiTcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EC20EB79-6C1A-4664-9A0DD2E4CC16D664
* [0x6300]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDns4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AE3D28CC-E05B-4FA1-A0117EB55A3F1401
* [0x6320]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDns6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CA37BC1F-A327-4AE9-828A8C40D8506A17
* [0x62c0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiTcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 65530BC7-A359-410F-B0105AADC7EC2B62
* [0x62e0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiTcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 46E44855-BD60-4AB7-AB0DA679B9447D77
* [0x6390]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 480F8AE9-0C46-4AA9-BC89DB9FBA619806
* [0x62a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHttpUtilitiesProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3E35C163-4074-45DD-431E23989DD86B32
* [0x6350]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x6350]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
## Module: HttpUtilitiesDxe
### Boot services:
* [0x398] EFI_BOOT_SERVICES->HandleProtocol
* [0x316] EFI_BOOT_SERVICES->OpenProtocol
* [0x2d3] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3d2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x340] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0xe50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0xe40]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHttpUtilitiesProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3E35C163-4074-45DD-431E23989DD86B32
* [0xe40]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiHttpUtilitiesProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3E35C163-4074-45DD-431E23989DD86B32
## Module: ICBDFsRecovery
### Boot services:
* [0x460] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* empty
## Module: ICBDTSEPopupMenu
### Boot services:
* [0x1292] EFI_BOOT_SERVICES->HandleProtocol
* [0x138e] EFI_BOOT_SERVICES->HandleProtocol
* [0x486] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x13c4] EFI_BOOT_SERVICES->OpenProtocol
* [0x344] EFI_BOOT_SERVICES->LocateProtocol
* [0x362] EFI_BOOT_SERVICES->LocateProtocol
* [0x37f] EFI_BOOT_SERVICES->LocateProtocol
* [0x39c] EFI_BOOT_SERVICES->LocateProtocol
* [0x4b5] EFI_BOOT_SERVICES->LocateProtocol
* [0x4d9] EFI_BOOT_SERVICES->LocateProtocol
* [0xc32] EFI_BOOT_SERVICES->LocateProtocol
* [0xf6b] EFI_BOOT_SERVICES->LocateProtocol
* [0x13e8] EFI_BOOT_SERVICES->LocateProtocol
* [0x1312] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2508]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x2400]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x2308]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0x1da0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x1dc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x1dd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x1d90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x1d80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3CD7C71C-CBC3-4296-A9BC3CE449B9FF64
* [0x1de0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B9D4C360-BCFB-4F9B-929853C136982258
* [0x22c8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x2318]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x2508]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: IccPlatformDxe
### Boot services:
* empty
### Protocols:
* empty
## Module: IdeBusBoard
### Boot services:
* [0x2cf] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* empty
## Module: IdeBusSrc
### Boot services:
* [0x35e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1137] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1969] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1119] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x16fd] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x10f9] EFI_BOOT_SERVICES->HandleProtocol
* [0x437] EFI_BOOT_SERVICES->OpenProtocol
* [0x4ed] EFI_BOOT_SERVICES->OpenProtocol
* [0x54a] EFI_BOOT_SERVICES->OpenProtocol
* [0x64d] EFI_BOOT_SERVICES->OpenProtocol
* [0x6a3] EFI_BOOT_SERVICES->OpenProtocol
* [0x6d5] EFI_BOOT_SERVICES->OpenProtocol
* [0xb92] EFI_BOOT_SERVICES->OpenProtocol
* [0xd5d] EFI_BOOT_SERVICES->OpenProtocol
* [0xddb] EFI_BOOT_SERVICES->OpenProtocol
* [0x11b6] EFI_BOOT_SERVICES->OpenProtocol
* [0x1200] EFI_BOOT_SERVICES->OpenProtocol
* [0x12b3] EFI_BOOT_SERVICES->OpenProtocol
* [0x13ba] EFI_BOOT_SERVICES->OpenProtocol
* [0x13fc] EFI_BOOT_SERVICES->OpenProtocol
* [0x1444] EFI_BOOT_SERVICES->OpenProtocol
* [0x15c1] EFI_BOOT_SERVICES->OpenProtocol
* [0x172c] EFI_BOOT_SERVICES->OpenProtocol
* [0x7120] EFI_BOOT_SERVICES->OpenProtocol
* [0x71ef] EFI_BOOT_SERVICES->OpenProtocol
* [0x45f] EFI_BOOT_SERVICES->CloseProtocol
* [0x51d] EFI_BOOT_SERVICES->CloseProtocol
* [0x128a] EFI_BOOT_SERVICES->CloseProtocol
* [0x1658] EFI_BOOT_SERVICES->CloseProtocol
* [0x16e5] EFI_BOOT_SERVICES->CloseProtocol
* [0x716d] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x327] EFI_BOOT_SERVICES->LocateProtocol
* [0xe6c] EFI_BOOT_SERVICES->LocateProtocol
* [0xea6] EFI_BOOT_SERVICES->LocateProtocol
* [0xee9] EFI_BOOT_SERVICES->LocateProtocol
* [0xf0f] EFI_BOOT_SERVICES->LocateProtocol
* [0xf35] EFI_BOOT_SERVICES->LocateProtocol
* [0xf5b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1675] EFI_BOOT_SERVICES->LocateProtocol
* [0x16ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x181d] EFI_BOOT_SERVICES->LocateProtocol
* [0x72bc] EFI_BOOT_SERVICES->LocateProtocol
* [0x39d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xd0c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xe0f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5f22] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x656a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x12eb] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x130a] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x148e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x14d6] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x75d0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] IDE_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] E159A956-3299-4EE9-917665181A4E5E9F
* [0x75d0]
	 - [service] OpenProtocol
	 - [protocol_name] IDE_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] E159A956-3299-4EE9-917665181A4E5E9F
* [0x76c0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x7600]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x7610]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x7640]
	 - [service] OpenProtocol
	 - [protocol_name] IDE_SECURITY_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] F4F63529-281E-4040-A313C1D6766384BE
* [0x7660]
	 - [service] OpenProtocol
	 - [protocol_name] IDE_SMART_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] FFBD9AD2-F1DB-4F92-A649EB9EEDEA86B5
* [0x7680]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiStorageSecurityCommandProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C88B0B6D-0DFC-49A7-9CB449074B4C3A78
* [0x75d0]
	 - [service] CloseProtocol
	 - [protocol_name] IDE_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] E159A956-3299-4EE9-917665181A4E5E9F
* [0x76b0]
	 - [service] LocateProtocol
	 - [protocol_name] PLATFORM_IDE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 6737F69B-B8CC-45BC-9327CCF5EEF70CDE
* [0x7690]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C6734411-2DDA-4632-A592920F24D6ED21
* [0x76a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 0FC50878-1633-432A-BDE4841357FC15E9
* [0x7620]
	 - [service] LocateProtocol
	 - [protocol_name] HDD_SECURITY_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] CE6F86BB-B800-4C71-B2D13897A3BC1DAE
* [0x7c80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 10E9D800-53B7-4845-9DFF30D18A956D53
* [0x7670]
	 - [service] LocateProtocol
	 - [protocol_name] OPAL_SEC_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 59AF16B0-661D-4865-A38138DE68385D8D
* [0x7650]
	 - [service] LocateProtocol
	 - [protocol_name] HDD_SMART_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 9401BD4F-1A00-4990-AB56DAF0E4E348DE
* [0x7c90]
	 - [service] LocateProtocol
	 - [protocol_name] IDE_SETUP_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5578AE16-F1C9-4E8F-B129BA07F8FCF84A
* [0x7c08]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x7600]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x7610]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x7610]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x7600]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x76e0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] IDE_POWER_MGMT_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] 67BC3883-7E79-4BC1-A33E3AF7D17589BA
* [0x76d0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] IDE_HPA_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] 51AA65FC-82B6-49E6-95E2E6827A8D7DB4
## Module: IdeRecovery
### Boot services:
* empty
### Protocols:
* empty
## Module: IntegratedTouch
### Boot services:
* [0x3f1] EFI_BOOT_SERVICES->HandleProtocol
* [0xdfe] EFI_BOOT_SERVICES->OpenProtocol
* [0xe42] EFI_BOOT_SERVICES->OpenProtocol
* [0xfab] EFI_BOOT_SERVICES->OpenProtocol
* [0x12ef] EFI_BOOT_SERVICES->OpenProtocol
* [0x1716] EFI_BOOT_SERVICES->OpenProtocol
* [0xe8c] EFI_BOOT_SERVICES->CloseProtocol
* [0x1533] EFI_BOOT_SERVICES->CloseProtocol
* [0x2c9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x542] EFI_BOOT_SERVICES->LocateProtocol
* [0x60b] EFI_BOOT_SERVICES->LocateProtocol
* [0xbf8] EFI_BOOT_SERVICES->LocateProtocol
* [0x11af] EFI_BOOT_SERVICES->LocateProtocol
* [0x1222] EFI_BOOT_SERVICES->LocateProtocol
* [0x1beb] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d26] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ded] EFI_BOOT_SERVICES->LocateProtocol
* [0x1eff] EFI_BOOT_SERVICES->LocateProtocol
* [0x1fd3] EFI_BOOT_SERVICES->LocateProtocol
* [0x467] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x48a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xd36] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xd63] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x105e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x334] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x38b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x133e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1368] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1389] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1555] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x21a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x2170]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 2B12E46F-3C24-47FF-8B89C0602C1C6142
* [0x2150]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x2110]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8D59D32B-C655-4AE9-9B15F25904992A43
* [0x2150]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x2140]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
* [0x2130]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverSupportedEfiVersionProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5C198761-16A8-4E69-972C89D67954F81D
* [0x2120]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x2170]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 2B12E46F-3C24-47FF-8B89C0602C1C6142
* [0x2110]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8D59D32B-C655-4AE9-9B15F25904992A43
* [0x2160]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3D0479C1-6B19-4191-B8096008DD079755
* [0x2150]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
## Module: IntelGigabitLan
### Boot services:
* [0x1b564] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1b868] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1f78e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x23627] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1bad6] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1baf5] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1bb14] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1bc83] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1a8df] EFI_BOOT_SERVICES->HandleProtocol
* [0x1abcd] EFI_BOOT_SERVICES->OpenProtocol
* [0x1afb6] EFI_BOOT_SERVICES->OpenProtocol
* [0x1b2f7] EFI_BOOT_SERVICES->OpenProtocol
* [0x1b32e] EFI_BOOT_SERVICES->OpenProtocol
* [0x1b8af] EFI_BOOT_SERVICES->OpenProtocol
* [0x1ba76] EFI_BOOT_SERVICES->OpenProtocol
* [0x1faa3] EFI_BOOT_SERVICES->OpenProtocol
* [0x1fd1b] EFI_BOOT_SERVICES->OpenProtocol
* [0x212a4] EFI_BOOT_SERVICES->OpenProtocol
* [0x212dd] EFI_BOOT_SERVICES->OpenProtocol
* [0x21321] EFI_BOOT_SERVICES->OpenProtocol
* [0x25df0] EFI_BOOT_SERVICES->OpenProtocol
* [0x26149] EFI_BOOT_SERVICES->OpenProtocol
* [0x261ba] EFI_BOOT_SERVICES->OpenProtocol
* [0x265bc] EFI_BOOT_SERVICES->OpenProtocol
* [0x26687] EFI_BOOT_SERVICES->OpenProtocol
* [0x26759] EFI_BOOT_SERVICES->OpenProtocol
* [0x2682e] EFI_BOOT_SERVICES->OpenProtocol
* [0x268f0] EFI_BOOT_SERVICES->OpenProtocol
* [0x269fc] EFI_BOOT_SERVICES->OpenProtocol
* [0x283c8] EFI_BOOT_SERVICES->OpenProtocol
* [0x28421] EFI_BOOT_SERVICES->OpenProtocol
* [0x284eb] EFI_BOOT_SERVICES->OpenProtocol
* [0x28543] EFI_BOOT_SERVICES->OpenProtocol
* [0x287e5] EFI_BOOT_SERVICES->OpenProtocol
* [0x44c57] EFI_BOOT_SERVICES->OpenProtocol
* [0x1b245] EFI_BOOT_SERVICES->CloseProtocol
* [0x1b976] EFI_BOOT_SERVICES->CloseProtocol
* [0x1b999] EFI_BOOT_SERVICES->CloseProtocol
* [0x1ba01] EFI_BOOT_SERVICES->CloseProtocol
* [0x1ba28] EFI_BOOT_SERVICES->CloseProtocol
* [0x1baa9] EFI_BOOT_SERVICES->CloseProtocol
* [0x1fc8d] EFI_BOOT_SERVICES->CloseProtocol
* [0x1fd3d] EFI_BOOT_SERVICES->CloseProtocol
* [0x26179] EFI_BOOT_SERVICES->CloseProtocol
* [0x26607] EFI_BOOT_SERVICES->CloseProtocol
* [0x266d3] EFI_BOOT_SERVICES->CloseProtocol
* [0x267a5] EFI_BOOT_SERVICES->CloseProtocol
* [0x2687a] EFI_BOOT_SERVICES->CloseProtocol
* [0x2692f] EFI_BOOT_SERVICES->CloseProtocol
* [0x26a8c] EFI_BOOT_SERVICES->CloseProtocol
* [0x283f8] EFI_BOOT_SERVICES->CloseProtocol
* [0x2851b] EFI_BOOT_SERVICES->CloseProtocol
* [0x1fd83] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x1add0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1fa54] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x22f3e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2698f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x44bfe] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a944] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a962] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a97f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a99c] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f682] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f6a8] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f6ce] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f6f4] EFI_BOOT_SERVICES->LocateProtocol
* [0x4676b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1aa9d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1ab57] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1ab8f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1b4ed] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1b6c1] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1b6e3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1b799] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1b7ea] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1af18] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1af51] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1bb88] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1bbbc] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1bbfd] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1bccd] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1bcdf] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x25cf0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 0003B848-0000-0000-0080C3CC48895C24
* [0x1b48]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiFirmwareManagementProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 86C77A67-0B97-4633-A18749104D0685C7
* [0x1010]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 51DD8B21-AD8D-48E9-BC3F24F46722C748
* [0x1b20]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiAdapterInformationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E5DD1403-D622-C24E-8488C71B17F5E802
* [0x2f0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiHiiConfigAccessProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 330D4706-F2A0-4E4F-A369B66FA8D54385
* [0x3b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x3b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x2a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x2b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x1b98]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPlatformToDriverConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 642CD590-8059-4C0A-A958C5EC07D23C4B
* [0x1da8]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] E3161450-AD0F-11D9-96690800200C9A66
* [0x290]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiNetworkInterfaceIdentifierProtocolGuid_31
	 - [protocol_place] edk2_guids
	 - [guid] 1ACED566-76ED-4218-BC81767F1F977A89
* [0x1010]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 51DD8B21-AD8D-48E9-BC3F24F46722C748
* [0x2a0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x2b0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x1b98]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPlatformToDriverConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 642CD590-8059-4C0A-A958C5EC07D23C4B
* [0x1010]
	 - [service] CloseProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 51DD8B21-AD8D-48E9-BC3F24F46722C748
* [0x1da8]
	 - [service] OpenProtocolInformation
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] E3161450-AD0F-11D9-96690800200C9A66
* [0x1b98]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPlatformToDriverConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 642CD590-8059-4C0A-A958C5EC07D23C4B
* [0x2d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x300]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x2e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x330]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x2c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B9D4C360-BCFB-4F9B-929853C136982258
* [0x350]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0xe58]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] E7B62316-3151-11D6-9F330090272813AC
* [0x1da8]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] E3161450-AD0F-11D9-96690800200C9A66
* [0x2b0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x310]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverSupportedEfiVersionProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5C198761-16A8-4E69-972C89D67954F81D
* [0xe58]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] E7B62316-3151-11D6-9F330090272813AC
## Module: IntelGigabitLanDxe
### Boot services:
* [0x427] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* empty
## Module: IntelVBiosLauncher2.inf
### Boot services:
* [0x180001169] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* [0x180003000]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B9D4C360-BCFB-4F9B-929853C136982258
## Module: Ip4Dxe
### Boot services:
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xdb1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x13c7] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x457] EFI_BOOT_SERVICES->HandleProtocol
* [0x9601] EFI_BOOT_SERVICES->HandleProtocol
* [0xb647] EFI_BOOT_SERVICES->HandleProtocol
* [0xc479] EFI_BOOT_SERVICES->HandleProtocol
* [0xc4e9] EFI_BOOT_SERVICES->HandleProtocol
* [0xc5c4] EFI_BOOT_SERVICES->HandleProtocol
* [0xc614] EFI_BOOT_SERVICES->HandleProtocol
* [0xb703] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x691] EFI_BOOT_SERVICES->OpenProtocol
* [0x6c1] EFI_BOOT_SERVICES->OpenProtocol
* [0x913] EFI_BOOT_SERVICES->OpenProtocol
* [0xc3d] EFI_BOOT_SERVICES->OpenProtocol
* [0xefa] EFI_BOOT_SERVICES->OpenProtocol
* [0x11f3] EFI_BOOT_SERVICES->OpenProtocol
* [0x12ea] EFI_BOOT_SERVICES->OpenProtocol
* [0x1a08] EFI_BOOT_SERVICES->OpenProtocol
* [0x25c2] EFI_BOOT_SERVICES->OpenProtocol
* [0x2d70] EFI_BOOT_SERVICES->OpenProtocol
* [0x338a] EFI_BOOT_SERVICES->OpenProtocol
* [0x4854] EFI_BOOT_SERVICES->OpenProtocol
* [0x9714] EFI_BOOT_SERVICES->OpenProtocol
* [0xc3e3] EFI_BOOT_SERVICES->OpenProtocol
* [0xc42f] EFI_BOOT_SERVICES->OpenProtocol
* [0xb19] EFI_BOOT_SERVICES->CloseProtocol
* [0x1367] EFI_BOOT_SERVICES->CloseProtocol
* [0x139e] EFI_BOOT_SERVICES->CloseProtocol
* [0x1988] EFI_BOOT_SERVICES->CloseProtocol
* [0x1a8e] EFI_BOOT_SERVICES->CloseProtocol
* [0x1bae] EFI_BOOT_SERVICES->CloseProtocol
* [0x2669] EFI_BOOT_SERVICES->CloseProtocol
* [0x3216] EFI_BOOT_SERVICES->CloseProtocol
* [0x497a] EFI_BOOT_SERVICES->CloseProtocol
* [0x9801] EFI_BOOT_SERVICES->CloseProtocol
* [0xe28] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xe69] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xea6] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x253f] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4bc] EFI_BOOT_SERVICES->LocateProtocol
* [0x4da] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f7] EFI_BOOT_SERVICES->LocateProtocol
* [0x514] EFI_BOOT_SERVICES->LocateProtocol
* [0x531] EFI_BOOT_SERVICES->LocateProtocol
* [0x6c12] EFI_BOOT_SERVICES->LocateProtocol
* [0xbc6b] EFI_BOOT_SERVICES->LocateProtocol
* [0x633] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xca8] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x11ac] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1414] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x96ce] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x10e2] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1219] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x983c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0xdab0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0xdad0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0xdae0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0xd9f0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiIp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C51711E7-B4BF-404A-BFB80A048EF1FFE4
* [0xda00]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0xdab0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0xdad0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0xdae0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0xdb30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0xdaa0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xdb40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0xda10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0xda20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0xda10]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0xda30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiArpServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F44C00EE-1F2C-4A00-AA091C9F3E0800A3
* [0xda20]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0xd9f0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C51711E7-B4BF-404A-BFB80A048EF1FFE4
* [0xda00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0xda50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4B427BB-BA21-4F16-BC4E43E416AB619C
* [0xda70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0xda20]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0xda50]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4B427BB-BA21-4F16-BC4E43E416AB619C
* [0xda70]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0xda10]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0xda20]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0xda50]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4B427BB-BA21-4F16-BC4E43E416AB619C
* [0xda70]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0xdaf0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0xdb10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0xdb20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0xdac0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0xdb00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0xda80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiIpSec2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A3979E64-ACE8-4DDC-BC074D66B8FD0977
* [0xda00]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0xd9f0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiIp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C51711E7-B4BF-404A-BFB80A048EF1FFE4
* [0xda00]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0xdaa0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: Ip6Dxe
### Boot services:
* [0x2ddb] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x30e6] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x31b0] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x38a1] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x3c22] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x169b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x457] EFI_BOOT_SERVICES->HandleProtocol
* [0x2073] EFI_BOOT_SERVICES->HandleProtocol
* [0xf799] EFI_BOOT_SERVICES->HandleProtocol
* [0xf809] EFI_BOOT_SERVICES->HandleProtocol
* [0xf8e4] EFI_BOOT_SERVICES->HandleProtocol
* [0xf934] EFI_BOOT_SERVICES->HandleProtocol
* [0x10adf] EFI_BOOT_SERVICES->HandleProtocol
* [0xef27] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x691] EFI_BOOT_SERVICES->OpenProtocol
* [0x6c1] EFI_BOOT_SERVICES->OpenProtocol
* [0x9aa] EFI_BOOT_SERVICES->OpenProtocol
* [0xda9] EFI_BOOT_SERVICES->OpenProtocol
* [0xe00] EFI_BOOT_SERVICES->OpenProtocol
* [0xfcb] EFI_BOOT_SERVICES->OpenProtocol
* [0x130a] EFI_BOOT_SERVICES->OpenProtocol
* [0x14ff] EFI_BOOT_SERVICES->OpenProtocol
* [0x15ef] EFI_BOOT_SERVICES->OpenProtocol
* [0x73f6] EFI_BOOT_SERVICES->OpenProtocol
* [0x8182] EFI_BOOT_SERVICES->OpenProtocol
* [0x8248] EFI_BOOT_SERVICES->OpenProtocol
* [0xa255] EFI_BOOT_SERVICES->OpenProtocol
* [0x968] EFI_BOOT_SERVICES->CloseProtocol
* [0x1672] EFI_BOOT_SERVICES->CloseProtocol
* [0xa215] EFI_BOOT_SERVICES->CloseProtocol
* [0x1220] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x128b] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x7373] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4bc] EFI_BOOT_SERVICES->LocateProtocol
* [0x4da] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f7] EFI_BOOT_SERVICES->LocateProtocol
* [0x514] EFI_BOOT_SERVICES->LocateProtocol
* [0x531] EFI_BOOT_SERVICES->LocateProtocol
* [0x5e85] EFI_BOOT_SERVICES->LocateProtocol
* [0x633] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1036] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x14b8] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x16e6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x13f3] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1525] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x10cb0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x10cd0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x10ce0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x10c50]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
* [0x10cb0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x10cd0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x10ce0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x10d30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x10d40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0x10c10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0x10c20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x10ca0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x10c10]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0x10c30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiArpServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F44C00EE-1F2C-4A00-AA091C9F3E0800A3
* [0x10c20]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x10c40]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EC835DD3-FE0F-617B-A621B350C3E13388
* [0x10c50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
* [0x10c70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9FB9A8A1-2F4A-43A6-889CD0F7B6C47AD5
* [0x10c80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0x10c20]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x10c80]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0x10c20]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x10c80]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0x10cf0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x10d10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x10d20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x10cc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x10d00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0x10c90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiIpSec2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A3979E64-ACE8-4DDC-BC074D66B8FD0977
* [0x10c50]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
* [0x10c40]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiIp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EC835DD3-FE0F-617B-A621B350C3E13388
* [0x10c50]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
## Module: IScsiDxe
### Boot services:
* [0x8a4] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xaab] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xdb7] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x100a] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x17ad] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1880] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xa81] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xd75] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xe74] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xf50] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xf85] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1259] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2757] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2789] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x435] EFI_BOOT_SERVICES->HandleProtocol
* [0x45a] EFI_BOOT_SERVICES->HandleProtocol
* [0x9d0] EFI_BOOT_SERVICES->HandleProtocol
* [0xa1f] EFI_BOOT_SERVICES->HandleProtocol
* [0x14aa] EFI_BOOT_SERVICES->HandleProtocol
* [0x14fd] EFI_BOOT_SERVICES->HandleProtocol
* [0x153d] EFI_BOOT_SERVICES->HandleProtocol
* [0x1589] EFI_BOOT_SERVICES->HandleProtocol
* [0x22c8] EFI_BOOT_SERVICES->HandleProtocol
* [0x231a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3114] EFI_BOOT_SERVICES->HandleProtocol
* [0xed77] EFI_BOOT_SERVICES->HandleProtocol
* [0x109c1] EFI_BOOT_SERVICES->HandleProtocol
* [0x10a31] EFI_BOOT_SERVICES->HandleProtocol
* [0x10b05] EFI_BOOT_SERVICES->HandleProtocol
* [0x10b4a] EFI_BOOT_SERVICES->HandleProtocol
* [0x618] EFI_BOOT_SERVICES->OpenProtocol
* [0x653] EFI_BOOT_SERVICES->OpenProtocol
* [0x6be] EFI_BOOT_SERVICES->OpenProtocol
* [0x774] EFI_BOOT_SERVICES->OpenProtocol
* [0x7b2] EFI_BOOT_SERVICES->OpenProtocol
* [0x876] EFI_BOOT_SERVICES->OpenProtocol
* [0x104d] EFI_BOOT_SERVICES->OpenProtocol
* [0x110b] EFI_BOOT_SERVICES->OpenProtocol
* [0x1200] EFI_BOOT_SERVICES->OpenProtocol
* [0x32ab] EFI_BOOT_SERVICES->OpenProtocol
* [0x34d5] EFI_BOOT_SERVICES->OpenProtocol
* [0x3562] EFI_BOOT_SERVICES->OpenProtocol
* [0x3f97] EFI_BOOT_SERVICES->OpenProtocol
* [0xb24f] EFI_BOOT_SERVICES->OpenProtocol
* [0xbefc] EFI_BOOT_SERVICES->OpenProtocol
* [0xc975] EFI_BOOT_SERVICES->OpenProtocol
* [0x1092b] EFI_BOOT_SERVICES->OpenProtocol
* [0x10977] EFI_BOOT_SERVICES->OpenProtocol
* [0x1165] EFI_BOOT_SERVICES->CloseProtocol
* [0x1184] EFI_BOOT_SERVICES->CloseProtocol
* [0x122f] EFI_BOOT_SERVICES->CloseProtocol
* [0x32c9] EFI_BOOT_SERVICES->CloseProtocol
* [0x6762] EFI_BOOT_SERVICES->CloseProtocol
* [0xb410] EFI_BOOT_SERVICES->CloseProtocol
* [0xc03e] EFI_BOOT_SERVICES->CloseProtocol
* [0xce8e] EFI_BOOT_SERVICES->CloseProtocol
* [0xcecc] EFI_BOOT_SERVICES->CloseProtocol
* [0x3511] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x10df3] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x3e7] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x97d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1350] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x338] EFI_BOOT_SERVICES->LocateProtocol
* [0x356] EFI_BOOT_SERVICES->LocateProtocol
* [0x373] EFI_BOOT_SERVICES->LocateProtocol
* [0x390] EFI_BOOT_SERVICES->LocateProtocol
* [0x1701] EFI_BOOT_SERVICES->LocateProtocol
* [0x1847] EFI_BOOT_SERVICES->LocateProtocol
* [0xa9fc] EFI_BOOT_SERVICES->LocateProtocol
* [0xf922] EFI_BOOT_SERVICES->LocateProtocol
* [0x11bdc] EFI_BOOT_SERVICES->LocateProtocol
* [0xa175] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xf521] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x108c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1456] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x14ce] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1521] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1561] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x15ad] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x15e8] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1615] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x18cf] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x190d] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x194c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xa1d2] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xa315] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x14250]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiExtScsiPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 143B7632-B81B-4CB7-ABD3B625A5B9BFFE
* [0x14250]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiExtScsiPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 143B7632-B81B-4CB7-ABD3B625A5B9BFFE
* [0x14270]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x14360]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x142a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAdapterInformationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E5DD1403-D622-C24E-8488C71B17F5E802
* [0x14250]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiExtScsiPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 143B7632-B81B-4CB7-ABD3B625A5B9BFFE
* [0x14270]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x141c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x14330]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0x14350]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0x14340]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x14200]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9FB9A8A1-2F4A-43A6-889CD0F7B6C47AD5
* [0x14220]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 46E44855-BD60-4AB7-AB0DA679B9447D77
* [0x14250]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiExtScsiPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 143B7632-B81B-4CB7-ABD3B625A5B9BFFE
* [0x141e0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0x141d0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0x14220]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiTcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 46E44855-BD60-4AB7-AB0DA679B9447D77
* [0x14210]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiTcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 65530BC7-A359-410F-B0105AADC7EC2B62
* [0x141e0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0x141d0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0x14210]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiTcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 65530BC7-A359-410F-B0105AADC7EC2B62
* [0x142c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x142e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x142f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x142b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x14280]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiIScsiInitiatorNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 59324945-EC44-4C0D-B1CD9DB139DF070C
* [0x14290]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAuthenticationInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7671D9D0-53DB-4173-AA692327F21F0BC7
* [0x141a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x14320]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B9D4C360-BCFB-4F9B-929853C136982258
* [0x14370]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_POST_MANAGER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8A91B1E1-56C7-4ADC-ABEB1C2CA1729EFF
* [0x141b0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x14250]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiExtScsiPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 143B7632-B81B-4CB7-ABD3B625A5B9BFFE
* [0x14290]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiAuthenticationInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7671D9D0-53DB-4173-AA692327F21F0BC7
* [0x141b0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x14280]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiIScsiInitiatorNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 59324945-EC44-4C0D-B1CD9DB139DF070C
* [0x14270]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: ITK50
### Boot services:
* [0x32f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x357] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4d1] EFI_BOOT_SERVICES->HandleProtocol
* [0xa51] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xb0b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xbb9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xc74] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xd22] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x13f4] EFI_BOOT_SERVICES->LocateProtocol
* [0x15d2] EFI_BOOT_SERVICES->LocateProtocol
* [0x16fc] EFI_BOOT_SERVICES->LocateProtocol
* [0x26c7] EFI_BOOT_SERVICES->LocateProtocol
* [0x2c21] EFI_BOOT_SERVICES->LocateProtocol
* [0x2df6] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f6d] EFI_BOOT_SERVICES->LocateProtocol
* [0x412b] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f4b] EFI_BOOT_SERVICES->LocateProtocol
* [0x51cb] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x64f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x64d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x6bc0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CONSOLE_CONTROL_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] F42F7782-012E-4C12-995649F94304F721
* [0x6bf0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C298B206-7FB5-4A7E-94614F3577F1A07A
* [0x64e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x6be0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
## Module: ItkSmmVars
### Boot services:
* [0x350] EFI_BOOT_SERVICES->LocateProtocol
* [0x38b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2161] EFI_BOOT_SERVICES->LocateProtocol
* [0x2242] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x4d60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x4da0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
* [0x5518]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: ItkSmmVarsDxe
### Boot services:
* [0x2e5] EFI_BOOT_SERVICES->LocateProtocol
* [0x529] EFI_BOOT_SERVICES->LocateProtocol
* [0xbf5] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1090]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1080]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CONSOLE_CONTROL_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] F42F7782-012E-4C12-995649F94304F721
* [0x1980]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C298B206-7FB5-4A7E-94614F3577F1A07A
## Module: KbcEmul
### Boot services:
* [0x4fe] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x64f] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1aac] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2100] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2a4b] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2dd] EFI_BOOT_SERVICES->LocateProtocol
* [0x3be] EFI_BOOT_SERVICES->LocateProtocol
* [0x4b7] EFI_BOOT_SERVICES->LocateProtocol
* [0x555] EFI_BOOT_SERVICES->LocateProtocol
* [0x32ad] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3800]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3e08]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3860]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_USB_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2AD8E2D2-2E91-4CD1-95F5E78FE5EBE316
* [0x3880]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: KbcEmulDxe
### Boot services:
* [0x395] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x35c] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x860]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AD61F191-AE5F-4C0E-B9FAE869D288C64F
## Module: LegacyInterrupt
### Boot services:
* [0x2d5] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: MeFwDowngrade
### Boot services:
* [0x33e] EFI_BOOT_SERVICES->LocateProtocol
* [0x40f] EFI_BOOT_SERVICES->LocateProtocol
* [0x4e5] EFI_BOOT_SERVICES->LocateProtocol
* [0x82e] EFI_BOOT_SERVICES->LocateProtocol
* [0x8f3] EFI_BOOT_SERVICES->LocateProtocol
* [0x959] EFI_BOOT_SERVICES->LocateProtocol
* [0x980] EFI_BOOT_SERVICES->LocateProtocol
* [0x9e8] EFI_BOOT_SERVICES->LocateProtocol
* [0xa89] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1060]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
* [0x1070]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] A0B5DC52-4F34-3990-D491108BE8BA7542
* [0x10a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 8D9B3387-73DB-456F-889D6FFE90826409
* [0x1080]
	 - [service] LocateProtocol
	 - [protocol_name] PLATFORM_ME_HOOK_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] BC52476E-F67E-4301-B262369C4878AAC2
* [0x1090]
	 - [service] LocateProtocol
	 - [protocol_name] WDT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B42B8D12-2ACB-499A-A920DD5BE6CF09B1
## Module: MePlatformReset
### Boot services:
* [0x13d6] EFI_BOOT_SERVICES->HandleProtocol
* [0x1994] EFI_BOOT_SERVICES->HandleProtocol
* [0x1397] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1964] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a99] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ac0] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b28] EFI_BOOT_SERVICES->LocateProtocol
* [0x1be3] EFI_BOOT_SERVICES->LocateProtocol
* [0x1048] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2060]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] F46DD670-36C2-4437-93C58E046582E6C3
* [0x20d0]
	 - [service] HandleProtocol
	 - [protocol_name] PCH_RESET_CALLBACK_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 3A3300AB-C929-487D-AB34159BC13562C0
* [0x2080]
	 - [service] LocateProtocol
	 - [protocol_name] PLATFORM_ME_HOOK_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] BC52476E-F67E-4301-B262369C4878AAC2
* [0x2090]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
* [0x20a0]
	 - [service] LocateProtocol
	 - [protocol_name] WDT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B42B8D12-2ACB-499A-A920DD5BE6CF09B1
* [0x20b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 8D9B3387-73DB-456F-889D6FFE90826409
## Module: MeSmbiosDxe
### Boot services:
* [0x34e] EFI_BOOT_SERVICES->LocateProtocol
* [0x454] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xa70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0xa60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
## Module: MnpDxe
### Boot services:
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x50c3] EFI_BOOT_SERVICES->HandleProtocol
* [0x58c5] EFI_BOOT_SERVICES->HandleProtocol
* [0x5935] EFI_BOOT_SERVICES->HandleProtocol
* [0x59c8] EFI_BOOT_SERVICES->HandleProtocol
* [0x5a18] EFI_BOOT_SERVICES->HandleProtocol
* [0x5c2] EFI_BOOT_SERVICES->OpenProtocol
* [0x6e4] EFI_BOOT_SERVICES->OpenProtocol
* [0x8d5] EFI_BOOT_SERVICES->OpenProtocol
* [0x909] EFI_BOOT_SERVICES->OpenProtocol
* [0xb65] EFI_BOOT_SERVICES->OpenProtocol
* [0xc67] EFI_BOOT_SERVICES->OpenProtocol
* [0x112c] EFI_BOOT_SERVICES->OpenProtocol
* [0x158e] EFI_BOOT_SERVICES->OpenProtocol
* [0x204f] EFI_BOOT_SERVICES->OpenProtocol
* [0x212c] EFI_BOOT_SERVICES->OpenProtocol
* [0x21c2] EFI_BOOT_SERVICES->OpenProtocol
* [0x5e5] EFI_BOOT_SERVICES->CloseProtocol
* [0xcb4] EFI_BOOT_SERVICES->CloseProtocol
* [0x136c] EFI_BOOT_SERVICES->CloseProtocol
* [0x1677] EFI_BOOT_SERVICES->CloseProtocol
* [0x2071] EFI_BOOT_SERVICES->CloseProtocol
* [0x20a6] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x568] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x746] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb23] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x15e4] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2223] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x84a] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x996] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xbcc] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xcd1] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x163f] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x169b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x6360]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x6370]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6380]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6360]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x6370]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6380]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6390]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x6350]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x6320]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0x6310]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0x6330]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x6320]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0x6340]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiVlanConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9E23D768-D2F3-4366-9FC33A7ABA864374
* [0x6310]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0x6330]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x6350]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x6320]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0x6310]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0x6340]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiVlanConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9E23D768-D2F3-4366-9FC33A7ABA864374
* [0x6310]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0x63a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 480F8AE9-0C46-4AA9-BC89DB9FBA619806
* [0x6340]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiVlanConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9E23D768-D2F3-4366-9FC33A7ABA864374
* [0x6330]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x6310]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0x6350]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: MouseDriver
### Boot services:
* [0x3f04] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x11bc] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1216] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3f5e] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x125a] EFI_BOOT_SERVICES->OpenProtocol
* [0x1298] EFI_BOOT_SERVICES->OpenProtocol
* [0x12d9] EFI_BOOT_SERVICES->OpenProtocol
* [0x130b] EFI_BOOT_SERVICES->OpenProtocol
* [0x1383] EFI_BOOT_SERVICES->OpenProtocol
* [0x13ce] EFI_BOOT_SERVICES->OpenProtocol
* [0x14dc] EFI_BOOT_SERVICES->OpenProtocol
* [0x152e] EFI_BOOT_SERVICES->OpenProtocol
* [0x1648] EFI_BOOT_SERVICES->OpenProtocol
* [0x1736] EFI_BOOT_SERVICES->OpenProtocol
* [0x1337] EFI_BOOT_SERVICES->CloseProtocol
* [0x1506] EFI_BOOT_SERVICES->CloseProtocol
* [0x15d6] EFI_BOOT_SERVICES->CloseProtocol
* [0x17d7] EFI_BOOT_SERVICES->CloseProtocol
* [0x1add] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1b3d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3fae] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4041] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1859] EFI_BOOT_SERVICES->LocateProtocol
* [0x3cec] EFI_BOOT_SERVICES->LocateProtocol
* [0x115d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x5020]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31878C87-0B75-11D5-9A4F0090273FC14D
* [0x5030]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8D59D32B-C655-4AE9-9B15F25904992A43
* [0x5040]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0x5000]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiEdidDiscoveredProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 1C0C34F6-D380-41FA-A0498AD06C1A66AA
* [0x5050]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x5020]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31878C87-0B75-11D5-9A4F0090273FC14D
* [0x5030]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8D59D32B-C655-4AE9-9B15F25904992A43
* [0x5020]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31878C87-0B75-11D5-9A4F0090273FC14D
* [0x5000]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiEdidDiscoveredProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 1C0C34F6-D380-41FA-A0498AD06C1A66AA
* [0x5030]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8D59D32B-C655-4AE9-9B15F25904992A43
* [0x5020]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31878C87-0B75-11D5-9A4F0090273FC14D
* [0x5030]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8D59D32B-C655-4AE9-9B15F25904992A43
* [0x5040]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0x5010]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
## Module: Mtftp4Dxe
### Boot services:
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xa09] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xe08] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x5a0] EFI_BOOT_SERVICES->OpenProtocol
* [0x75a] EFI_BOOT_SERVICES->OpenProtocol
* [0x939] EFI_BOOT_SERVICES->OpenProtocol
* [0xbd7] EFI_BOOT_SERVICES->OpenProtocol
* [0xc1b] EFI_BOOT_SERVICES->OpenProtocol
* [0xd37] EFI_BOOT_SERVICES->OpenProtocol
* [0x1082] EFI_BOOT_SERVICES->OpenProtocol
* [0x3b61] EFI_BOOT_SERVICES->OpenProtocol
* [0x47a2] EFI_BOOT_SERVICES->OpenProtocol
* [0x47f1] EFI_BOOT_SERVICES->OpenProtocol
* [0x611f] EFI_BOOT_SERVICES->OpenProtocol
* [0xc49] EFI_BOOT_SERVICES->CloseProtocol
* [0xd95] EFI_BOOT_SERVICES->CloseProtocol
* [0xdbe] EFI_BOOT_SERVICES->CloseProtocol
* [0xdec] EFI_BOOT_SERVICES->CloseProtocol
* [0x11c8] EFI_BOOT_SERVICES->CloseProtocol
* [0x484f] EFI_BOOT_SERVICES->CloseProtocol
* [0x4947] EFI_BOOT_SERVICES->CloseProtocol
* [0x4986] EFI_BOOT_SERVICES->CloseProtocol
* [0x8b9] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xfff] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x565] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x7d0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb71] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc6c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x6a00]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x6a10]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6a20]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6990]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiMtftp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2FE800BE-8F01-4AA6-946BD71388E1833F
* [0x69b0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiMtftp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 78247C57-63DB-4708-99C2A8B4A9A61F6B
* [0x6a00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x6a10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6a20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6a30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x69a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 83F01464-99BD-45E5-B383AF6305D8E9E6
* [0x6990]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2FE800BE-8F01-4AA6-946BD71388E1833F
* [0x69c0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x69b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 78247C57-63DB-4708-99C2A8B4A9A61F6B
* [0x69c0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x69e0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x69c0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x69f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 480F8AE9-0C46-4AA9-BC89DB9FBA619806
* [0x69b0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiMtftp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 78247C57-63DB-4708-99C2A8B4A9A61F6B
* [0x69b0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiMtftp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 78247C57-63DB-4708-99C2A8B4A9A61F6B
## Module: Mtftp6Dxe
### Boot services:
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xb48] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xe19] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x8b0] EFI_BOOT_SERVICES->OpenProtocol
* [0x8f6] EFI_BOOT_SERVICES->OpenProtocol
* [0xa78] EFI_BOOT_SERVICES->OpenProtocol
* [0xc3b] EFI_BOOT_SERVICES->OpenProtocol
* [0xd1b] EFI_BOOT_SERVICES->OpenProtocol
* [0x10ad] EFI_BOOT_SERVICES->OpenProtocol
* [0x26d6] EFI_BOOT_SERVICES->OpenProtocol
* [0x3919] EFI_BOOT_SERVICES->OpenProtocol
* [0x42ce] EFI_BOOT_SERVICES->OpenProtocol
* [0x431d] EFI_BOOT_SERVICES->OpenProtocol
* [0x601f] EFI_BOOT_SERVICES->OpenProtocol
* [0xd91] EFI_BOOT_SERVICES->CloseProtocol
* [0xdc1] EFI_BOOT_SERVICES->CloseProtocol
* [0xdf0] EFI_BOOT_SERVICES->CloseProtocol
* [0x1f68] EFI_BOOT_SERVICES->CloseProtocol
* [0x437b] EFI_BOOT_SERVICES->CloseProtocol
* [0x4473] EFI_BOOT_SERVICES->CloseProtocol
* [0x44b2] EFI_BOOT_SERVICES->CloseProtocol
* [0x9f9] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2653] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x568] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x96c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xbf6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc62] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x6dc0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x6dd0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6de0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6d70]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiMtftp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D9760FF3-3CCA-4267-80F97527FAFA4223
* [0x6d80]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiMtftp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BF0A78BA-EC29-49CF-A1C97AE54EAB6A51
* [0x6dc0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x6dd0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6de0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6df0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x6d50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 66ED4721-3C98-4D3E-81E3D03DD39A7254
* [0x6d70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D9760FF3-3CCA-4267-80F97527FAFA4223
* [0x6d60]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x6d80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BF0A78BA-EC29-49CF-A1C97AE54EAB6A51
* [0x6d60]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x6da0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x6d60]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x6db0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 480F8AE9-0C46-4AA9-BC89DB9FBA619806
* [0x6d80]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiMtftp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BF0A78BA-EC29-49CF-A1C97AE54EAB6A51
## Module: NbDxe
### Boot services:
* [0x39c] EFI_BOOT_SERVICES->HandleProtocol
* [0x406] EFI_BOOT_SERVICES->HandleProtocol
* [0xa4c] EFI_BOOT_SERVICES->HandleProtocol
* [0x757] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x17fd] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x421] EFI_BOOT_SERVICES->LocateProtocol
* [0x573] EFI_BOOT_SERVICES->LocateProtocol
* [0x590] EFI_BOOT_SERVICES->LocateProtocol
* [0x774] EFI_BOOT_SERVICES->LocateProtocol
* [0x918] EFI_BOOT_SERVICES->LocateProtocol
* [0x9a2] EFI_BOOT_SERVICES->LocateProtocol
* [0xd90] EFI_BOOT_SERVICES->LocateProtocol
* [0x11ff] EFI_BOOT_SERVICES->LocateProtocol
* [0x170c] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x40c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x40b0]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3279A703-BA93-4CBC-AD115C2A82C94A80
* [0x3950]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3DC21D75-DE0E-4300-A0AA19C41C0CF3DF
* [0x3990]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3980]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C6AA1F27-5597-4802-9F63D62836598635
* [0x3920]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0x3930]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x40f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 783658A3-4172-4421-A299E009079C0CB4
* [0x3970]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
* [0x3940]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x3950]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3DC21D75-DE0E-4300-A0AA19C41C0CF3DF
* [0x3ed8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
## Module: NbSmi
### Boot services:
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x39a] EFI_BOOT_SERVICES->LocateProtocol
* [0x421] EFI_BOOT_SERVICES->LocateProtocol
* [0x697] EFI_BOOT_SERVICES->LocateProtocol
* [0x9db] EFI_BOOT_SERVICES->LocateProtocol
* [0xbe9] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2e60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2e90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x3398]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2e80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: NTFS
### Boot services:
* [0x180001c6a] EFI_BOOT_SERVICES->OpenProtocol
* [0x180001cd0] EFI_BOOT_SERVICES->OpenProtocol
* [0x180001d3c] EFI_BOOT_SERVICES->OpenProtocol
* [0x180002145] EFI_BOOT_SERVICES->OpenProtocol
* [0x180002402] EFI_BOOT_SERVICES->OpenProtocol
* [0x18000244d] EFI_BOOT_SERVICES->OpenProtocol
* [0x180004263] EFI_BOOT_SERVICES->OpenProtocol
* [0x180001ca3] EFI_BOOT_SERVICES->CloseProtocol
* [0x180001da5] EFI_BOOT_SERVICES->CloseProtocol
* [0x180002470] EFI_BOOT_SERVICES->CloseProtocol
* [0x1800024bb] EFI_BOOT_SERVICES->CloseProtocol
* [0x180001b95] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1800020a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x180002117] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x180002383] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x180001c1e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x180001d82] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x180004c60]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0x180004c50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x180004d38]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
* [0x180004c30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x180004c60]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0x180004c80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiUnicodeCollation2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A4C751FC-23AE-4C3E-92E94964CF63F349
* [0x180004c20]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x180004d38]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
* [0x180004c20]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x180004d38]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
## Module: Nvme
### Boot services:
* [0xe76] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xe58] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xe38] EFI_BOOT_SERVICES->HandleProtocol
* [0x33f3] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a9] EFI_BOOT_SERVICES->HandleProtocol
* [0x425f] EFI_BOOT_SERVICES->HandleProtocol
* [0x44df] EFI_BOOT_SERVICES->HandleProtocol
* [0x5053] EFI_BOOT_SERVICES->HandleProtocol
* [0x402] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x44c] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x591] EFI_BOOT_SERVICES->OpenProtocol
* [0x601] EFI_BOOT_SERVICES->OpenProtocol
* [0x664] EFI_BOOT_SERVICES->OpenProtocol
* [0x776] EFI_BOOT_SERVICES->OpenProtocol
* [0x7c7] EFI_BOOT_SERVICES->OpenProtocol
* [0x809] EFI_BOOT_SERVICES->OpenProtocol
* [0xc2c] EFI_BOOT_SERVICES->OpenProtocol
* [0xed0] EFI_BOOT_SERVICES->OpenProtocol
* [0xfc4] EFI_BOOT_SERVICES->OpenProtocol
* [0x1018] EFI_BOOT_SERVICES->OpenProtocol
* [0x1168] EFI_BOOT_SERVICES->OpenProtocol
* [0x11ae] EFI_BOOT_SERVICES->OpenProtocol
* [0x11f0] EFI_BOOT_SERVICES->OpenProtocol
* [0x1259] EFI_BOOT_SERVICES->OpenProtocol
* [0x1314] EFI_BOOT_SERVICES->OpenProtocol
* [0x1368] EFI_BOOT_SERVICES->OpenProtocol
* [0x13de] EFI_BOOT_SERVICES->OpenProtocol
* [0x1674] EFI_BOOT_SERVICES->OpenProtocol
* [0x16c8] EFI_BOOT_SERVICES->OpenProtocol
* [0x171a] EFI_BOOT_SERVICES->OpenProtocol
* [0x176c] EFI_BOOT_SERVICES->OpenProtocol
* [0x19a9] EFI_BOOT_SERVICES->OpenProtocol
* [0x245d] EFI_BOOT_SERVICES->OpenProtocol
* [0x2733] EFI_BOOT_SERVICES->OpenProtocol
* [0x51e4] EFI_BOOT_SERVICES->OpenProtocol
* [0x638] EFI_BOOT_SERVICES->CloseProtocol
* [0x68e] EFI_BOOT_SERVICES->CloseProtocol
* [0x10bb] EFI_BOOT_SERVICES->CloseProtocol
* [0x143b] EFI_BOOT_SERVICES->CloseProtocol
* [0x1459] EFI_BOOT_SERVICES->CloseProtocol
* [0x33b9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x383d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x420e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4477] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xcd5] EFI_BOOT_SERVICES->LocateProtocol
* [0xd4e] EFI_BOOT_SERVICES->LocateProtocol
* [0xda1] EFI_BOOT_SERVICES->LocateProtocol
* [0xea1] EFI_BOOT_SERVICES->LocateProtocol
* [0x2852] EFI_BOOT_SERVICES->LocateProtocol
* [0x2d36] EFI_BOOT_SERVICES->LocateProtocol
* [0x2da7] EFI_BOOT_SERVICES->LocateProtocol
* [0x3abf] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b5e] EFI_BOOT_SERVICES->LocateProtocol
* [0x412a] EFI_BOOT_SERVICES->LocateProtocol
* [0x414e] EFI_BOOT_SERVICES->LocateProtocol
* [0x496] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb18] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc83] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xf22] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2066] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x24ae] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x263f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2680] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x28e7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2ec7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2f3a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1231] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x12e7] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x133b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x138f] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x169c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x16ee] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1740] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1792] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x6b80]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] AFA4CF3F-AF71-4C30-A4FB2910E771F9B0
* [0x6ba0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x6d08]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] BDS_CONNECT_DRIVERS_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 3AA83745-9454-4F7A-A7C090DBD02FAB8E
* [0x6c80]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] BDS_ALL_DRIVERS_CONNECTED_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] DBC9FD21-FAD8-45B0-9E7827158867CC93
* [0x6b80]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] AFA4CF3F-AF71-4C30-A4FB2910E771F9B0
* [0x6ba0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x6b50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x6c50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiStorageSecurityCommandProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C88B0B6D-0DFC-49A7-9CB449074B4C3A78
* [0x6b90]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 4B215191-9A25-43FD-86B574E7AF723315
* [0x6c20]
	 - [service] OpenProtocol
	 - [protocol_name] IDE_SECURITY_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] F4F63529-281E-4040-A313C1D6766384BE
* [0x6cf8]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] B396DA3A-52B2-4CD6-A89A13E7C4AE9790
* [0x6c40]
	 - [service] OpenProtocol
	 - [protocol_name] IDE_SMART_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] FFBD9AD2-F1DB-4F92-A649EB9EEDEA86B5
* [0x6be0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 52C78312-8EDC-4233-98F21A1AA5E388A5
* [0x6b70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x6bf0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0x6ba0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x6b50]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x6c30]
	 - [service] LocateProtocol
	 - [protocol_name] HDD_SMART_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 9401BD4F-1A00-4990-AB56DAF0E4E348DE
* [0x6c00]
	 - [service] LocateProtocol
	 - [protocol_name] HDD_SECURITY_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] CE6F86BB-B800-4C71-B2D13897A3BC1DAE
* [0x6ce8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 734AA01D-95EC-45B7-A23A2D86D8FDEBB6
* [0x6c60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 7F955A3E-AFB5-4122-B9254B1171F693F5
* [0x6c90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTrEEProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 607F766C-7455-42BE-930BE4D76DB2720F
* [0x6ca0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmControl2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 843DC720-AB1E-42CB-93578A0078F3561B
* [0x6bd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x6bc0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] D4E79DAE-AAFC-4382-95403E3FA42D4255
* [0x6c70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x6be0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 52C78312-8EDC-4233-98F21A1AA5E388A5
* [0x6c50]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiStorageSecurityCommandProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C88B0B6D-0DFC-49A7-9CB449074B4C3A78
* [0x6c50]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiStorageSecurityCommandProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C88B0B6D-0DFC-49A7-9CB449074B4C3A78
* [0x6b80]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] AFA4CF3F-AF71-4C30-A4FB2910E771F9B0
* [0x6b90]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 4B215191-9A25-43FD-86B574E7AF723315
* [0x6be0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 52C78312-8EDC-4233-98F21A1AA5E388A5
* [0x6b70]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x6bf0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D432A67F-14DC-484B-B3BB3F0291849327
* [0x6ba0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: NvmeInt13
### Boot services:
* [0x38c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2cf] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x660]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_LEGACY_BIOS_EXT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8E008510-9BB1-457D-9F70897ABA865DB9
## Module: NvmeSmm
### Boot services:
* [0xd1f] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xe70] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2e2] EFI_BOOT_SERVICES->LocateProtocol
* [0xdd1] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2450]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: NvramDxe
### Boot services:
* [0x4ec9] EFI_BOOT_SERVICES->HandleProtocol
* [0x8385] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x9329] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x4e93] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1100] EFI_BOOT_SERVICES->LocateProtocol
* [0x11fe] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ca7] EFI_BOOT_SERVICES->LocateProtocol
* [0x6c7d] EFI_BOOT_SERVICES->LocateProtocol
* [0x81d8] EFI_BOOT_SERVICES->LocateProtocol
* [0x8311] EFI_BOOT_SERVICES->LocateProtocol
* [0x961f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1bc2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1c4b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1cdc] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xc190]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0xc8f8]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] BDS_CONNECT_DRIVERS_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 3AA83745-9454-4F7A-A7C090DBD02FAB8E
* [0xc200]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xc1b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0xc1a0]
	 - [service] LocateProtocol
	 - [protocol_name] FLASH_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 755B6596-6896-4BA3-B3DD1C629FD1EA88
* [0xced0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0xc210]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
* [0xc230]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_DIGITAL_SIGNATURE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5F87BA17-957D-433D-9E15C0E7C8798899
## Module: NvramSmm
### Boot services:
* [0x3a45] EFI_BOOT_SERVICES->HandleProtocol
* [0xd5d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xd83] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xda9] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x8215] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3a0f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x37f] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x431] EFI_BOOT_SERVICES->LocateProtocol
* [0x471] EFI_BOOT_SERVICES->LocateProtocol
* [0x7210] EFI_BOOT_SERVICES->LocateProtocol
* [0x7349] EFI_BOOT_SERVICES->LocateProtocol
* [0x7432] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xac60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0xb3b8]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] BDS_CONNECT_DRIVERS_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 3AA83745-9454-4F7A-A7C090DBD02FAB8E
* [0xaca0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xacd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0xb990]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0xacc0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
* [0xb950]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: OCDxe
### Boot services:
* empty
### Protocols:
* empty
## Module: OEMActivation
### Boot services:
* [0x391] EFI_BOOT_SERVICES->LocateProtocol
* [0x40e] EFI_BOOT_SERVICES->LocateProtocol
* [0x7bd] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1038]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 19B1DB23-E657-4D6D-B9736F4D08F07AA4
* [0xa60]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_ACPI_SUPPORT_GUID
	 - [protocol_place] edk_guids
	 - [guid] DBFF9D55-89B7-46DA-BDDF677D3DC0241D
## Module: OemBoardDxe
### Boot services:
* [0x657] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x11e1] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* empty
## Module: OemBoardSmi
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x6f9] EFI_BOOT_SERVICES->LocateProtocol
* [0x981] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xed0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x13d8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xef0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: OemEventDxe
### Boot services:
* [0x1cc1] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x11d6] EFI_BOOT_SERVICES->LocateProtocol
* [0x1285] EFI_BOOT_SERVICES->LocateProtocol
* [0x13e0] EFI_BOOT_SERVICES->LocateProtocol
* [0x142d] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b19] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x30b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x3060]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] D4D2F201-50E8-4D45-8E05FD49A82A1569
* [0x3070]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiRealTimeClockArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 27CFAC87-46CC-11D4-9A380090273FC14D
* [0x3080]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C298B206-7FB5-4A7E-94614F3577F1A07A
## Module: OemGop
### Boot services:
* [0x65b] EFI_BOOT_SERVICES->HandleProtocol
* [0x32f] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x620] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2cb] EFI_BOOT_SERVICES->LocateProtocol
* [0x741] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xa40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0xa30]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gPlatformGOPPolicyGuid
	 - [protocol_place] edk2_guids
	 - [guid] EC2E931B-3281-48A5-8107DF8A8BED3C5D
* [0xa50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xa30]
	 - [service] LocateProtocol
	 - [protocol_name] gPlatformGOPPolicyGuid
	 - [protocol_place] edk2_guids
	 - [guid] EC2E931B-3281-48A5-8107DF8A8BED3C5D
## Module: OemUsbPort
### Boot services:
* [0x749] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3b8] EFI_BOOT_SERVICES->LocateProtocol
* [0x6e2] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x7f0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_USB_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2AD8E2D2-2E91-4CD1-95F5E78FE5EBE316
* [0x7e0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_USB_POLICY_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5859CB76-6BEF-468A-BE2DB3DD1A27F012
## Module: OpalSecurity
### Boot services:
* [0x332] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x93a] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3f1] EFI_BOOT_SERVICES->OpenProtocol
* [0x4cb] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x524] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0xd90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiStorageSecurityCommandProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C88B0B6D-0DFC-49A7-9CB449074B4C3A78
* [0xd90]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiStorageSecurityCommandProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C88B0B6D-0DFC-49A7-9CB449074B4C3A78
## Module: OverclockInterface
### Boot services:
* [0x644] EFI_BOOT_SERVICES->HandleProtocol
* [0x60f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5d1] EFI_BOOT_SERVICES->LocateProtocol
* [0x88c] EFI_BOOT_SERVICES->LocateProtocol
* [0x8dd] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d7b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ecc] EFI_BOOT_SERVICES->LocateProtocol
* [0x2017] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2260]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x2200]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x2210]
	 - [service] LocateProtocol
	 - [protocol_name] WDT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B42B8D12-2ACB-499A-A920DD5BE6CF09B1
* [0x2230]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
* [0x2250]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
* [0x2270]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 8D9B3387-73DB-456F-889D6FFE90826409
## Module: OverClockSmiHandler
### Boot services:
* [0x28df] EFI_BOOT_SERVICES->LocateProtocol
* [0x29fd] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a94] EFI_BOOT_SERVICES->LocateProtocol
* [0x2c09] EFI_BOOT_SERVICES->LocateProtocol
* [0x2cea] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3190]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
* [0x31b0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_PLATFORM_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] D9035175-8CE2-47DE-A8B8CC98E5E2A885
* [0x3160]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x31d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
* [0x36b8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: PartitionDxe
### Boot services:
* [0x39a] EFI_BOOT_SERVICES->OpenProtocol
* [0x404] EFI_BOOT_SERVICES->OpenProtocol
* [0x457] EFI_BOOT_SERVICES->OpenProtocol
* [0x4e9] EFI_BOOT_SERVICES->OpenProtocol
* [0x522] EFI_BOOT_SERVICES->OpenProtocol
* [0x568] EFI_BOOT_SERVICES->OpenProtocol
* [0x5ad] EFI_BOOT_SERVICES->OpenProtocol
* [0x5ee] EFI_BOOT_SERVICES->OpenProtocol
* [0x88b] EFI_BOOT_SERVICES->OpenProtocol
* [0x8b5] EFI_BOOT_SERVICES->OpenProtocol
* [0x9d5] EFI_BOOT_SERVICES->OpenProtocol
* [0x1389] EFI_BOOT_SERVICES->OpenProtocol
* [0x3d7] EFI_BOOT_SERVICES->CloseProtocol
* [0x42c] EFI_BOOT_SERVICES->CloseProtocol
* [0x72e] EFI_BOOT_SERVICES->CloseProtocol
* [0x74c] EFI_BOOT_SERVICES->CloseProtocol
* [0x76a] EFI_BOOT_SERVICES->CloseProtocol
* [0x7ec] EFI_BOOT_SERVICES->CloseProtocol
* [0x80a] EFI_BOOT_SERVICES->CloseProtocol
* [0x828] EFI_BOOT_SERVICES->CloseProtocol
* [0x8dc] EFI_BOOT_SERVICES->CloseProtocol
* [0x31b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1326] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x134d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x954] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x999] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x2e00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0x2df0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x2dd0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x2de0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A77B2472-E282-4E9F-A245C2C0E27BBCC1
* [0x2e10]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 151C8EAE-7F2C-472C-9E549828194F6A88
* [0x2e00]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0x2df0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x2e10]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDiskIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 151C8EAE-7F2C-472C-9E549828194F6A88
* [0x2df0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: PauseKey
### Boot services:
* [0x545] EFI_BOOT_SERVICES->HandleProtocol
* [0x4ec] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x41c] EFI_BOOT_SERVICES->OpenProtocol
* [0x344] EFI_BOOT_SERVICES->LocateProtocol
* [0x362] EFI_BOOT_SERVICES->LocateProtocol
* [0x37f] EFI_BOOT_SERVICES->LocateProtocol
* [0x39c] EFI_BOOT_SERVICES->LocateProtocol
* [0x441] EFI_BOOT_SERVICES->LocateProtocol
* [0x5ea] EFI_BOOT_SERVICES->LocateProtocol
* [0xede] EFI_BOOT_SERVICES->LocateProtocol
* [0x1217] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2130]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DD9E7534-7762-4698-8C14F58517A625AA
* [0x2130]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DD9E7534-7762-4698-8C14F58517A625AA
* [0x2770]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0x2160]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x2180]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x2190]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x2150]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x2780]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x2140]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_POST_MANAGER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8A91B1E1-56C7-4ADC-ABEB1C2CA1729EFF
* [0x2730]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
## Module: PcdDxe
### Boot services:
* [0x253e] EFI_BOOT_SERVICES->HandleProtocol
* [0x257c] EFI_BOOT_SERVICES->HandleProtocol
* [0x3b4] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2309] EFI_BOOT_SERVICES->LocateProtocol
* [0x330] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x36b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x26c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x26d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x26b0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
* [0x26b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
## Module: PchInitDxe
### Boot services:
* [0xa3f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2f22] EFI_BOOT_SERVICES->HandleProtocol
* [0xb3b] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2ee] EFI_BOOT_SERVICES->LocateProtocol
* [0x4de] EFI_BOOT_SERVICES->LocateProtocol
* [0x59e] EFI_BOOT_SERVICES->LocateProtocol
* [0x4bd1] EFI_BOOT_SERVICES->LocateProtocol
* [0x7a0f] EFI_BOOT_SERVICES->LocateProtocol
* [0xa61] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xae4] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x17ea] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x8b50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x8b60]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiPciEnumerationCompleteProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 30CFE3E7-3DE1-4586-BE20DEABA1B3B793
* [0x8b90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x8b60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciEnumerationCompleteProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 30CFE3E7-3DE1-4586-BE20DEABA1B3B793
* [0x8b70]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 0D66A1CF-79AD-494B-978BB25981689334
* [0x8b40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x8ba0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EB97088E-CFDF-49C6-BE4BD906A5B20E86
## Module: PchInitSmm
### Boot services:
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x39a] EFI_BOOT_SERVICES->LocateProtocol
* [0x705] EFI_BOOT_SERVICES->LocateProtocol
* [0x7ce] EFI_BOOT_SERVICES->LocateProtocol
* [0x127f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x4900]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x4910]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x4890]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 2E058B2B-EDC1-4431-87D9C6C4EA102BE3
## Module: PchResetRuntime
### Boot services:
* [0x170c] EFI_BOOT_SERVICES->HandleProtocol
* [0x16dc] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1811] EFI_BOOT_SERVICES->LocateProtocol
* [0x1838] EFI_BOOT_SERVICES->LocateProtocol
* [0x18a0] EFI_BOOT_SERVICES->LocateProtocol
* [0x195b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1086] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2060]
	 - [service] HandleProtocol
	 - [protocol_name] PCH_RESET_CALLBACK_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 3A3300AB-C929-487D-AB34159BC13562C0
* [0x2080]
	 - [service] LocateProtocol
	 - [protocol_name] PLATFORM_ME_HOOK_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] BC52476E-F67E-4301-B262369C4878AAC2
* [0x2090]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
* [0x20a0]
	 - [service] LocateProtocol
	 - [protocol_name] WDT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B42B8D12-2ACB-499A-A920DD5BE6CF09B1
* [0x20b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 8D9B3387-73DB-456F-889D6FFE90826409
## Module: PchSerialGpio
### Boot services:
* [0x369] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: PchSmbusDxe
### Boot services:
* [0x520] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x16d0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiSmbusHcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E49D33ED-513D-4634-B6986F55AA751C1B
## Module: PchSmbusSmm
### Boot services:
* [0x479] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2b1] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xeb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: PchSmiDispatcher
### Boot services:
* [0x1200] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x530] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x566] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x589] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x5ac] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x5cf] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x5f2] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x6a7] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x6cc] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x70f] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x73e] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x39a] EFI_BOOT_SERVICES->LocateProtocol
* [0x66b] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x5820]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x58f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
## Module: PchSpiRuntime
### Boot services:
* [0x127b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: PchSpiSmm
### Boot services:
* [0x39d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x29d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1050]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: PciBus
### Boot services:
* [0xf5d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1f35] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x8f34] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x7cc1] EFI_BOOT_SERVICES->HandleProtocol
* [0x7dd2] EFI_BOOT_SERVICES->HandleProtocol
* [0x7f26] EFI_BOOT_SERVICES->HandleProtocol
* [0x8024] EFI_BOOT_SERVICES->HandleProtocol
* [0xba79] EFI_BOOT_SERVICES->HandleProtocol
* [0xd0b5] EFI_BOOT_SERVICES->HandleProtocol
* [0x483] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x7ffa] EFI_BOOT_SERVICES->OpenProtocol
* [0xaa5d] EFI_BOOT_SERVICES->OpenProtocol
* [0xad3b] EFI_BOOT_SERVICES->OpenProtocol
* [0xb079] EFI_BOOT_SERVICES->OpenProtocol
* [0xb0d8] EFI_BOOT_SERVICES->OpenProtocol
* [0xae13] EFI_BOOT_SERVICES->CloseProtocol
* [0xb0af] EFI_BOOT_SERVICES->CloseProtocol
* [0xb0fe] EFI_BOOT_SERVICES->CloseProtocol
* [0xb45a] EFI_BOOT_SERVICES->CloseProtocol
* [0x7d1d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xba4b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xd070] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x7e01] EFI_BOOT_SERVICES->LocateProtocol
* [0x7e25] EFI_BOOT_SERVICES->LocateProtocol
* [0x7e46] EFI_BOOT_SERVICES->LocateProtocol
* [0x80ed] EFI_BOOT_SERVICES->LocateProtocol
* [0x966f] EFI_BOOT_SERVICES->LocateProtocol
* [0x9b87] EFI_BOOT_SERVICES->LocateProtocol
* [0x9f6a] EFI_BOOT_SERVICES->LocateProtocol
* [0x9f90] EFI_BOOT_SERVICES->LocateProtocol
* [0xb177] EFI_BOOT_SERVICES->LocateProtocol
* [0xb1d1] EFI_BOOT_SERVICES->LocateProtocol
* [0xb1f7] EFI_BOOT_SERVICES->LocateProtocol
* [0xb9fd] EFI_BOOT_SERVICES->LocateProtocol
* [0xbae7] EFI_BOOT_SERVICES->LocateProtocol
* [0xbbd4] EFI_BOOT_SERVICES->LocateProtocol
* [0xcc3a] EFI_BOOT_SERVICES->LocateProtocol
* [0x435] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa69c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa837] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa867] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xaa0c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb3ab] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xaf00] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xb51f] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0xea60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0xea70]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xe9e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xeb70]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0xeb20]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0xea60]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0xea70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xea60]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0xea70]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xeb50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xeae0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 07D75280-27D4-4D69-90D05643E238B341
* [0xeaf0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciOverrideProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B5B35764-460C-4A06-99FC77A17C1B5CEB
* [0xea80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiIncompatiblePciDeviceSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EB23F55A-7863-4AC2-8D3D956535DE0375
* [0xead0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciHotPlugInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AA0E8BC1-DABC-46B0-A84437B8169B2BEA
* [0xeb30]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 38D65EC3-8F39-4660-B8A6F36AA3925475
* [0xeac0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDecompressProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D8117CFE-94A6-11D4-9A3A0090273FC14D
* [0xeaa0]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_OPROM_POLICY_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 542D6248-4198-4960-9F592384646D63B4
* [0xeb00]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] DC14E697-775A-4C3B-A11AEDC38E1BE3E6
* [0xea90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0xeb80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] EC63428D-66CA-4BF9-82AE840F6D5C2305
* [0xeab0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] EA4B0675-1F36-4ABE-BB3A6D60760A02A2
* [0xeb20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0xeb40]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
* [0xf518]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0xeb60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 4FC0733F-6FD2-491B-A8905374521BF48F
* [0xeb10]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 934CE8DA-5E2A-4184-8A158E0847988431
* [0xea10]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] AMI_PCI_BUS_EXT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] F42A009D-977F-4F08-9440BCA5A3BED9AF
## Module: PciDxeInit
### Boot services:
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x4fe] EFI_BOOT_SERVICES->LocateProtocol
* [0x524] EFI_BOOT_SERVICES->LocateProtocol
* [0x6b2] EFI_BOOT_SERVICES->LocateProtocol
* [0x368] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2e30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2e40]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_OPROM_POLICY_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 542D6248-4198-4960-9F592384646D63B4
* [0x2e50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] DC14E697-775A-4C3B-A11AEDC38E1BE3E6
* [0x2e10]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 4FC0733F-6FD2-491B-A8905374521BF48F
## Module: PciDynamicSetup
### Boot services:
* [0x2a9e] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fba] EFI_BOOT_SERVICES->HandleProtocol
* [0x3118] EFI_BOOT_SERVICES->HandleProtocol
* [0x32cd] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2fef] EFI_BOOT_SERVICES->OpenProtocol
* [0x2a4b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x344] EFI_BOOT_SERVICES->LocateProtocol
* [0x362] EFI_BOOT_SERVICES->LocateProtocol
* [0x37f] EFI_BOOT_SERVICES->LocateProtocol
* [0x39c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3013] EFI_BOOT_SERVICES->LocateProtocol
* [0x3afe] EFI_BOOT_SERVICES->LocateProtocol
* [0x3e37] EFI_BOOT_SERVICES->LocateProtocol
* [0x49e2] EFI_BOOT_SERVICES->LocateProtocol
* [0x31a6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x5ba0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x6220]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x6410]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x6400]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] AMITSE_SETUP_ENTER_GUID
	 - [protocol_place] ami_guids
	 - [guid] 71202EEE-5F53-40D9-AB3D9E0C26D96657
* [0x6128]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0x5bc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x5be0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x5bf0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x5bb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x6138]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x60e8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x5b90]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 4FC0733F-6FD2-491B-A8905374521BF48F
* [0x6410]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: PcieSataController
### Boot services:
* [0x19e7] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a85] EFI_BOOT_SERVICES->HandleProtocol
* [0x1b45] EFI_BOOT_SERVICES->HandleProtocol
* [0xfca] EFI_BOOT_SERVICES->OpenProtocol
* [0x102a] EFI_BOOT_SERVICES->OpenProtocol
* [0x1114] EFI_BOOT_SERVICES->OpenProtocol
* [0x121c] EFI_BOOT_SERVICES->OpenProtocol
* [0x1566] EFI_BOOT_SERVICES->OpenProtocol
* [0x1f71] EFI_BOOT_SERVICES->OpenProtocol
* [0x1fd1] EFI_BOOT_SERVICES->OpenProtocol
* [0x21bc] EFI_BOOT_SERVICES->OpenProtocol
* [0xff1] EFI_BOOT_SERVICES->CloseProtocol
* [0x10b0] EFI_BOOT_SERVICES->CloseProtocol
* [0x114a] EFI_BOOT_SERVICES->CloseProtocol
* [0x14f8] EFI_BOOT_SERVICES->CloseProtocol
* [0x15d0] EFI_BOOT_SERVICES->CloseProtocol
* [0x1f98] EFI_BOOT_SERVICES->CloseProtocol
* [0x2054] EFI_BOOT_SERVICES->CloseProtocol
* [0x20f8] EFI_BOOT_SERVICES->CloseProtocol
* [0x2605] EFI_BOOT_SERVICES->CloseProtocol
* [0x1787] EFI_BOOT_SERVICES->LocateProtocol
* [0x1905] EFI_BOOT_SERVICES->LocateProtocol
* [0x19c2] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d86] EFI_BOOT_SERVICES->LocateProtocol
* [0x44d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x49a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x147d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x255c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x159e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x2cc0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x2c80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x2c80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x2c90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A1E37052-80D9-4E65-A3173E9A55C43EC9
* [0x2ca0]
	 - [service] OpenProtocol
	 - [protocol_name] SATA_CONTROLLER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2ACB6627-DF02-4E23-B4F96A93FA6E9DA6
* [0x2cc0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x2cc0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x2c80]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x3450]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x32b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0x2cd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x2ca0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] SATA_CONTROLLER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2ACB6627-DF02-4E23-B4F96A93FA6E9DA6
## Module: PciHostBridge
### Boot services:
* [0x983] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x134c] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x808] EFI_BOOT_SERVICES->LocateProtocol
* [0xb9c] EFI_BOOT_SERVICES->LocateProtocol
* [0xbb9] EFI_BOOT_SERVICES->LocateProtocol
* [0x115f] EFI_BOOT_SERVICES->LocateProtocol
* [0x12f8] EFI_BOOT_SERVICES->LocateProtocol
* [0x27f2] EFI_BOOT_SERVICES->LocateProtocol
* [0xbee] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x4a40]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3DC21D75-DE0E-4300-A0AA19C41C0CF3DF
* [0x4a60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x4a40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3DC21D75-DE0E-4300-A0AA19C41C0CF3DF
* [0x49f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AD61F191-AE5F-4C0E-B9FAE869D288C64F
* [0x4a30]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C6AA1F27-5597-4802-9F63D62836598635
* [0x4a50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 4FC0733F-6FD2-491B-A8905374521BF48F
* [0x4a70]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: PciOutOfResourceSetupPage
### Boot services:
* [0x10d9] EFI_BOOT_SERVICES->HandleProtocol
* [0x11cb] EFI_BOOT_SERVICES->HandleProtocol
* [0x37d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1201] EFI_BOOT_SERVICES->OpenProtocol
* [0xa76] EFI_BOOT_SERVICES->LocateProtocol
* [0xdaf] EFI_BOOT_SERVICES->LocateProtocol
* [0x1225] EFI_BOOT_SERVICES->LocateProtocol
* [0x1158] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2300]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x21b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x22f0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] BDS_ALL_DRIVERS_CONNECTED_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] DBC9FD21-FAD8-45B0-9E7827158867CC93
* [0x20b8]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0x2078]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x20c8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x2300]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: PciPort
### Boot services:
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x429] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xce0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: PepBccdSmm
### Boot services:
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a7] EFI_BOOT_SERVICES->LocateProtocol
* [0x62f] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xe60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xe90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0xe80]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: PeriodicSmiControl
### Boot services:
* [0x565] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x39a] EFI_BOOT_SERVICES->LocateProtocol
* [0x421] EFI_BOOT_SERVICES->LocateProtocol
* [0x4b6] EFI_BOOT_SERVICES->LocateProtocol
* [0x603] EFI_BOOT_SERVICES->LocateProtocol
* [0x7a9] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xd40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xd70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x1258]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xd60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: PiSmmCommunicationSmm
### Boot services:
* [0x32f] EFI_BOOT_SERVICES->LocateProtocol
* [0x35d] EFI_BOOT_SERVICES->LocateProtocol
* [0x557] EFI_BOOT_SERVICES->LocateProtocol
* [0x64f] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x9a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x9c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x990]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x9b0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: PiSmmCore
### Boot services:
* [0x1a90] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x1aee] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x13eb] EFI_BOOT_SERVICES->HandleProtocol
* [0x1d8e] EFI_BOOT_SERVICES->HandleProtocol
* [0x1db6] EFI_BOOT_SERVICES->HandleProtocol
* [0x1f37] EFI_BOOT_SERVICES->HandleProtocol
* [0x535] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1cd7] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3f1] EFI_BOOT_SERVICES->LocateProtocol
* [0x13a4] EFI_BOOT_SERVICES->LocateProtocol
* [0x13ca] EFI_BOOT_SERVICES->LocateProtocol
* [0x388e] EFI_BOOT_SERVICES->LocateProtocol
* [0x768] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x17ad] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x65a8]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 72617453-4974-616D-67653A0000000000
* [0x6060]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x6070]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x60a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x6050]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSecurity2ArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 94AB2F58-1438-4EF1-915218941A3A0E68
* [0x6040]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSecurityArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A46423E3-4617-49F1-B9FFD1BFA9115839
## Module: PiSmmCpuDxeSmm
### Boot services:
* [0x16e8] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x171e] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x378] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a6] EFI_BOOT_SERVICES->LocateProtocol
* [0x106b] EFI_BOOT_SERVICES->LocateProtocol
* [0x11b5] EFI_BOOT_SERVICES->LocateProtocol
* [0x4743] EFI_BOOT_SERVICES->LocateProtocol
* [0x16c2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x9570]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x9510]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x9520]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3FDDA605-A76E-4F46-AD2912F4531B3D08
* [0x9580]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: PiSmmIpl
### Boot services:
* [0x1689] EFI_BOOT_SERVICES->HandleProtocol
* [0x35cb] EFI_BOOT_SERVICES->HandleProtocol
* [0x2152] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1641] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x14cd] EFI_BOOT_SERVICES->LocateProtocol
* [0x1545] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b06] EFI_BOOT_SERVICES->LocateProtocol
* [0x1edf] EFI_BOOT_SERVICES->LocateProtocol
* [0x1efc] EFI_BOOT_SERVICES->LocateProtocol
* [0x201b] EFI_BOOT_SERVICES->LocateProtocol
* [0x20e7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x40f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x40d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x40b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26EEB3DE-B689-492E-80F0BE8BD7DA4BA7
* [0x40a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x40c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmControl2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 843DC720-AB1E-42CB-93578A0078F3561B
* [0x40e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB1-6F42-11D4-BCE70080C73C8881
## Module: PlatformConfigDxe
### Boot services:
* [0x1a74] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1aa3] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2bf1] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x317] EFI_BOOT_SERVICES->LocateProtocol
* [0x34d] EFI_BOOT_SERVICES->LocateProtocol
* [0x36a] EFI_BOOT_SERVICES->LocateProtocol
* [0x387] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a4] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c1] EFI_BOOT_SERVICES->LocateProtocol
* [0x4eb] EFI_BOOT_SERVICES->LocateProtocol
* [0xa62] EFI_BOOT_SERVICES->LocateProtocol
* [0x1371] EFI_BOOT_SERVICES->LocateProtocol
* [0x1fba] EFI_BOOT_SERVICES->LocateProtocol
* [0x22f3] EFI_BOOT_SERVICES->LocateProtocol
* [0x26b2] EFI_BOOT_SERVICES->LocateProtocol
* [0x282f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a00] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x37e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3800]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x3820]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x3830]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x37f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x3810]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0x3e00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x3fd0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CONSOLE_CONTROL_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] F42F7782-012E-4C12-995649F94304F721
* [0x3de0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x3d68]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
## Module: PlatformIdPage
### Boot services:
* [0x410] EFI_BOOT_SERVICES->HandleProtocol
* [0x1201] EFI_BOOT_SERVICES->HandleProtocol
* [0x447] EFI_BOOT_SERVICES->OpenProtocol
* [0x344] EFI_BOOT_SERVICES->LocateProtocol
* [0x362] EFI_BOOT_SERVICES->LocateProtocol
* [0x37f] EFI_BOOT_SERVICES->LocateProtocol
* [0x39c] EFI_BOOT_SERVICES->LocateProtocol
* [0x46b] EFI_BOOT_SERVICES->LocateProtocol
* [0xb9e] EFI_BOOT_SERVICES->LocateProtocol
* [0xed7] EFI_BOOT_SERVICES->LocateProtocol
* [0x1280] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2200]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x22f8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x2108]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0x1bb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x1bd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x1be0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x1ba0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x2118]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x20c8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x22f8]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: PlatformInfoDxe
### Boot services:
* [0x37f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x3c4] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x4bf] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xb10]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiVariableWriteArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6441F818-6362-4E44-B5707DBA31DD2453
* [0xb20]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: PlatformInitDxe
### Boot services:
* [0x17b0] EFI_BOOT_SERVICES->HandleProtocol
* [0xf09] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x137d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1775] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2ee] EFI_BOOT_SERVICES->LocateProtocol
* [0x32f] EFI_BOOT_SERVICES->LocateProtocol
* [0x4c2] EFI_BOOT_SERVICES->LocateProtocol
* [0x80d] EFI_BOOT_SERVICES->LocateProtocol
* [0x8b8] EFI_BOOT_SERVICES->LocateProtocol
* [0xa8c] EFI_BOOT_SERVICES->LocateProtocol
* [0xaeb] EFI_BOOT_SERVICES->LocateProtocol
* [0xc3e] EFI_BOOT_SERVICES->LocateProtocol
* [0xe13] EFI_BOOT_SERVICES->LocateProtocol
* [0xe7d] EFI_BOOT_SERVICES->LocateProtocol
* [0xebc] EFI_BOOT_SERVICES->LocateProtocol
* [0xfc4] EFI_BOOT_SERVICES->LocateProtocol
* [0x106a] EFI_BOOT_SERVICES->LocateProtocol
* [0x10ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x110d] EFI_BOOT_SERVICES->LocateProtocol
* [0x1447] EFI_BOOT_SERVICES->LocateProtocol
* [0x1caf] EFI_BOOT_SERVICES->LocateProtocol
* [0x20c7] EFI_BOOT_SERVICES->LocateProtocol
* [0x2fd7] EFI_BOOT_SERVICES->LocateProtocol
* [0x318a] EFI_BOOT_SERVICES->LocateProtocol
* [0x34bb] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3ac0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x3af0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] BDS_ALL_DRIVERS_CONNECTED_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] DBC9FD21-FAD8-45B0-9E7827158867CC93
* [0x3ac0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x3b10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x3b30]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
* [0x3ab0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_PLATFORM_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] D9035175-8CE2-47DE-A8B8CC98E5E2A885
* [0x3a80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] D4D2F201-50E8-4D45-8E05FD49A82A1569
* [0x3aa0]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
* [0x3a90]
	 - [service] LocateProtocol
	 - [protocol_name] DXE_CPU_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] E223CF65-F6CE-4122-B3AF4BD18AFF40A1
* [0x3ad0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C6AA1F27-5597-4802-9F63D62836598635
* [0x3ae0]
	 - [service] LocateProtocol
	 - [protocol_name] gPlatformGOPPolicyGuid
	 - [protocol_place] edk2_guids
	 - [guid] EC2E931B-3281-48A5-8107DF8A8BED3C5D
* [0x3b00]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
* [0x3b20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0x3b40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 8D9B3387-73DB-456F-889D6FFE90826409
## Module: PlatformSetup
### Boot services:
* [0x1995] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x301] EFI_BOOT_SERVICES->LocateProtocol
* [0x5b2] EFI_BOOT_SERVICES->LocateProtocol
* [0x106c] EFI_BOOT_SERVICES->LocateProtocol
* [0x1087] EFI_BOOT_SERVICES->LocateProtocol
* [0x10a4] EFI_BOOT_SERVICES->LocateProtocol
* [0x1537] EFI_BOOT_SERVICES->LocateProtocol
* [0x1269] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x1d60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x1ce0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3FDDA605-A76E-4F46-AD2912F4531B3D08
* [0x1cd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0x1d20]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_PLATFORM_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] D9035175-8CE2-47DE-A8B8CC98E5E2A885
* [0x1d40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C6AA1F27-5597-4802-9F63D62836598635
* [0x1d50]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: PolicyInitDxe
### Boot services:
* [0x89d] EFI_BOOT_SERVICES->HandleProtocol
* [0x862] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x78a] EFI_BOOT_SERVICES->LocateProtocol
* [0x99b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1090] EFI_BOOT_SERVICES->LocateProtocol
* [0x1209] EFI_BOOT_SERVICES->LocateProtocol
* [0x50e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5e2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x618] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x68d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x3cd0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x3d20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3d10]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_PLATFORM_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] D9035175-8CE2-47DE-A8B8CC98E5E2A885
* [0x3d30]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
* [0x3d50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3C7BC880-41F8-4869-AEFC870A3ED28299
## Module: PowerButton
### Boot services:
* [0x300] EFI_BOOT_SERVICES->LocateProtocol
* [0x32e] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b5] EFI_BOOT_SERVICES->LocateProtocol
* [0x454] EFI_BOOT_SERVICES->LocateProtocol
* [0x535] EFI_BOOT_SERVICES->LocateProtocol
* [0x71d] EFI_BOOT_SERVICES->LocateProtocol
* [0x805] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xdb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xdf0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x12d8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xde0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: PowerMgmtDxe
### Boot services:
* [0x754] EFI_BOOT_SERVICES->HandleProtocol
* [0x71c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2ae] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x148f] EFI_BOOT_SERVICES->LocateProtocol
* [0x36b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x16c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x16e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x16b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] AB5A4DF4-F0D7-49A8-BF5CF25DA04C2533
* [0x16d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EB97088E-CFDF-49C6-BE4BD906A5B20E86
## Module: PowerMgmtSmm
### Boot services:
* [0x32c] EFI_BOOT_SERVICES->LocateProtocol
* [0x35a] EFI_BOOT_SERVICES->LocateProtocol
* [0x410] EFI_BOOT_SERVICES->LocateProtocol
* [0x7df] EFI_BOOT_SERVICES->LocateProtocol
* [0x15c2] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1c20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1c70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x1c60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] AB5A4DF4-F0D7-49A8-BF5CF25DA04C2533
## Module: RaidDriver
### Boot services:
* [0xf833] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xff17] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x9013] EFI_BOOT_SERVICES->OpenProtocol
* [0x9282] EFI_BOOT_SERVICES->OpenProtocol
* [0x92d7] EFI_BOOT_SERVICES->OpenProtocol
* [0x94df] EFI_BOOT_SERVICES->OpenProtocol
* [0x9bf0] EFI_BOOT_SERVICES->CloseProtocol
* [0x9c8a] EFI_BOOT_SERVICES->CloseProtocol
* [0x2a35] EFI_BOOT_SERVICES->LocateProtocol
* [0x30cd] EFI_BOOT_SERVICES->LocateProtocol
* [0x312f] EFI_BOOT_SERVICES->LocateProtocol
* [0x318b] EFI_BOOT_SERVICES->LocateProtocol
* [0x31ea] EFI_BOOT_SERVICES->LocateProtocol
* [0x3207] EFI_BOOT_SERVICES->LocateProtocol
* [0x8a5e] EFI_BOOT_SERVICES->LocateProtocol
* [0x8ad8] EFI_BOOT_SERVICES->LocateProtocol
* [0x8b56] EFI_BOOT_SERVICES->LocateProtocol
* [0x8bd2] EFI_BOOT_SERVICES->LocateProtocol
* [0x8e42] EFI_BOOT_SERVICES->LocateProtocol
* [0x91db] EFI_BOOT_SERVICES->LocateProtocol
* [0x9213] EFI_BOOT_SERVICES->LocateProtocol
* [0x92a6] EFI_BOOT_SERVICES->LocateProtocol
* [0x96cc] EFI_BOOT_SERVICES->LocateProtocol
* [0x96ff] EFI_BOOT_SERVICES->LocateProtocol
* [0xb452] EFI_BOOT_SERVICES->LocateProtocol
* [0x22225] EFI_BOOT_SERVICES->LocateProtocol
* [0x5548] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x77bd] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x7f31] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x86d0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8968] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x915d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x94a0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x952a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x560c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x89b8] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x9b0b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x9cbf] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x9ced] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x9d20] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xf8d9] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x30a30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x30c20]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x30a30]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x30b00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] B9D4C360-BCFB-4F9B-929853C136982258
* [0x30cc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x30bd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x30b50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x30c40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x30c10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0x30a80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0x30a20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x30c30]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_ACPI_SUPPORT_GUID
	 - [protocol_place] edk_guids
	 - [guid] DBFF9D55-89B7-46DA-BDDF677D3DC0241D
* [0x30cf0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x30b70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x30c20]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x30b30]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiHiiConfigAccessProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 330D4706-F2A0-4E4F-A369B66FA8D54385
* [0x30d50]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] B36E8BE4-9C7D-4A89-A2A0810329F0F83C
* [0x30c20]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x30a90]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x30b60]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiStorageSecurityCommandProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C88B0B6D-0DFC-49A7-9CB449074B4C3A78
## Module: Recovery
### Boot services:
* [0x2b7] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4b6] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x521] EFI_BOOT_SERVICES->HandleProtocol
* [0x6a3] EFI_BOOT_SERVICES->HandleProtocol
* [0x6c3] EFI_BOOT_SERVICES->HandleProtocol
* [0x85b] EFI_BOOT_SERVICES->HandleProtocol
* [0x8dc] EFI_BOOT_SERVICES->HandleProtocol
* [0x928] EFI_BOOT_SERVICES->HandleProtocol
* [0xa60] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* empty
## Module: RngDxe
### Boot services:
* [0x303] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: RomLayoutDxe
### Boot services:
* [0x867] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x9bb] EFI_BOOT_SERVICES->HandleProtocol
* [0x51e] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x544] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xb28]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] BDS_CONNECT_DRIVERS_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 3AA83745-9454-4F7A-A7C090DBD02FAB8E
## Module: RsdpPlus
### Boot services:
* [0xa0c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xb9b] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xc30] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xd01] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2f3] EFI_BOOT_SERVICES->LocateProtocol
* [0x357] EFI_BOOT_SERVICES->LocateProtocol
* [0xb55] EFI_BOOT_SERVICES->LocateProtocol
* [0xbc3] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1000]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1700]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_ACPI_SUPPORT_GUID
	 - [protocol_place] edk_guids
	 - [guid] DBFF9D55-89B7-46DA-BDDF677D3DC0241D
* [0xff0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
## Module: RstOneClickEnable
### Boot services:
* empty
### Protocols:
* empty
## Module: RtcWakeup
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x98b] EFI_BOOT_SERVICES->LocateProtocol
* [0xb61] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xf00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1408]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xf20]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: RtkSdCardDxe
### Boot services:
* empty
### Protocols:
* empty
## Module: RuntimeDxe
### Boot services:
* [0x1257] EFI_BOOT_SERVICES->HandleProtocol
* [0x1356] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2040]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
## Module: RuntimeSmm
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x497] EFI_BOOT_SERVICES->LocateProtocol
* [0x63d] EFI_BOOT_SERVICES->LocateProtocol
* [0x3fd] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x9c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xec8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x9e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: S3SaveStateDxe
### Boot services:
* [0x338] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x42a] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x45b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x24ac] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x25cf] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x24fb] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1c78] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e04] EFI_BOOT_SERVICES->LocateProtocol
* [0x1eec] EFI_BOOT_SERVICES->LocateProtocol
* [0x1fde] EFI_BOOT_SERVICES->LocateProtocol
* [0x20fc] EFI_BOOT_SERVICES->LocateProtocol
* [0x223d] EFI_BOOT_SERVICES->LocateProtocol
* [0x233b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2538] EFI_BOOT_SERVICES->LocateProtocol
* [0x2d4f] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2f30]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 47B7FA8C-F4BD-4AF6-8200333086F0D2C8
* [0x2f20]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x2ee0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLockBoxProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BD445D79-B7AD-4F04-9AD829BD2040EB3C
* [0x2f00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C68ED8E2-9DC6-4CBD-9D94DB65ACC5C332
* [0x2f20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x2f10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2ef0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: SaInitDxe
### Boot services:
* [0x548] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x725] EFI_BOOT_SERVICES->HandleProtocol
* [0x8ed] EFI_BOOT_SERVICES->HandleProtocol
* [0x1b31] EFI_BOOT_SERVICES->HandleProtocol
* [0x1dbf] EFI_BOOT_SERVICES->HandleProtocol
* [0x2411] EFI_BOOT_SERVICES->HandleProtocol
* [0x460] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x4fb] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x6f0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8bb] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1aff] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1d94] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x23cd] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x312] EFI_BOOT_SERVICES->LocateProtocol
* [0x342] EFI_BOOT_SERVICES->LocateProtocol
* [0x57e] EFI_BOOT_SERVICES->LocateProtocol
* [0x6b2] EFI_BOOT_SERVICES->LocateProtocol
* [0x986] EFI_BOOT_SERVICES->LocateProtocol
* [0xae6] EFI_BOOT_SERVICES->LocateProtocol
* [0xf1d] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ad6] EFI_BOOT_SERVICES->LocateProtocol
* [0x1c9a] EFI_BOOT_SERVICES->LocateProtocol
* [0x1cdf] EFI_BOOT_SERVICES->LocateProtocol
* [0x1cff] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e60] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ebb] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f3e] EFI_BOOT_SERVICES->LocateProtocol
* [0x20ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x20e7] EFI_BOOT_SERVICES->LocateProtocol
* [0x41e6] EFI_BOOT_SERVICES->LocateProtocol
* [0x8126] EFI_BOOT_SERVICES->LocateProtocol
* [0xb75] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2365] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x84d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x84b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x8490]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiPciEnumerationCompleteProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 30CFE3E7-3DE1-4586-BE20DEABA1B3B793
* [0x8520]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x84a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0x8490]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciEnumerationCompleteProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 30CFE3E7-3DE1-4586-BE20DEABA1B3B793
* [0x8450]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x8470]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C6AA1F27-5597-4802-9F63D62836598635
* [0x8500]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 1861E089-CAA3-473E-8432DC1F94C6C1A6
* [0x84e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x84f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 651B7EBD-CE13-41D0-82E5A063ABBE9BB6
* [0x8460]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3DC21D75-DE0E-4300-A0AA19C41C0CF3DF
* [0x8480]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB1-6F42-11D4-BCE70080C73C8881
## Module: SaLateInitSmm
### Boot services:
* [0x34c] EFI_BOOT_SERVICES->LocateProtocol
* [0x37a] EFI_BOOT_SERVICES->LocateProtocol
* [0x546] EFI_BOOT_SERVICES->LocateProtocol
* [0x2026] EFI_BOOT_SERVICES->LocateProtocol
* [0x59a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x2430]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2440]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x2400]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C6AA1F27-5597-4802-9F63D62836598635
## Module: SataController
### Boot services:
* [0x363] EFI_BOOT_SERVICES->OpenProtocol
* [0x3b6] EFI_BOOT_SERVICES->OpenProtocol
* [0x54d] EFI_BOOT_SERVICES->OpenProtocol
* [0x742] EFI_BOOT_SERVICES->OpenProtocol
* [0xc0a] EFI_BOOT_SERVICES->OpenProtocol
* [0x38a] EFI_BOOT_SERVICES->CloseProtocol
* [0x406] EFI_BOOT_SERVICES->CloseProtocol
* [0x411] EFI_BOOT_SERVICES->CloseProtocol
* [0x6e8] EFI_BOOT_SERVICES->CloseProtocol
* [0x79c] EFI_BOOT_SERVICES->CloseProtocol
* [0xc2c] EFI_BOOT_SERVICES->CloseProtocol
* [0x31b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x6bd] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x779] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x1150]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x1160]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x1140]
	 - [service] OpenProtocol
	 - [protocol_name] PCH_SATA_CONTROLLER_DRIVER_GUID
	 - [protocol_place] ami_guids
	 - [guid] BB929DA9-68F7-4035-B22CA3BB3F23DA55
* [0x1150]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x1160]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x1140]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] PCH_SATA_CONTROLLER_DRIVER_GUID
	 - [protocol_place] ami_guids
	 - [guid] BB929DA9-68F7-4035-B22CA3BB3F23DA55
## Module: SaveMemoryConfig
### Boot services:
* [0x442] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x5f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
## Module: SavePegConfig
### Boot services:
* [0x3db] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x620]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
## Module: SbDxe
### Boot services:
* [0x4a2] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4d6] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x8bc] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xdda] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1368] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xfc7] EFI_BOOT_SERVICES->HandleProtocol
* [0x1175] EFI_BOOT_SERVICES->HandleProtocol
* [0x1424] EFI_BOOT_SERVICES->HandleProtocol
* [0x294f] EFI_BOOT_SERVICES->HandleProtocol
* [0x2a03] EFI_BOOT_SERVICES->HandleProtocol
* [0x2b1c] EFI_BOOT_SERVICES->HandleProtocol
* [0x2b53] EFI_BOOT_SERVICES->HandleProtocol
* [0x3e79] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xf92] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2ade] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x779] EFI_BOOT_SERVICES->LocateProtocol
* [0x79e] EFI_BOOT_SERVICES->LocateProtocol
* [0xb13] EFI_BOOT_SERVICES->LocateProtocol
* [0xe24] EFI_BOOT_SERVICES->LocateProtocol
* [0xf21] EFI_BOOT_SERVICES->LocateProtocol
* [0x15c5] EFI_BOOT_SERVICES->LocateProtocol
* [0x16d7] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f2f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f8b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2102] EFI_BOOT_SERVICES->LocateProtocol
* [0x3d44] EFI_BOOT_SERVICES->LocateProtocol
* [0x3f79] EFI_BOOT_SERVICES->LocateProtocol
* [0x504] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x860] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x6860]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiPciHotPlugInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AA0E8BC1-DABC-46B0-A84437B8169B2BEA
* [0x6800]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x67a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x6810]
	 - [service] HandleProtocol
	 - [protocol_name] OPROM_START_END_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] F2A128FF-257B-456E-9DE863E7C7DCDFAC
* [0x6850]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x6830]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x6840]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x6780]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0x6770]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x67b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x67d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 2E058B2B-EDC1-4431-87D9C6C4EA102BE3
* [0x67c0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_SMBIOS_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5E90A50D-6955-4A49-9032DA3812F8E8E5
* [0x7428]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_USB_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2AD8E2D2-2E91-4CD1-95F5E78FE5EBE316
* [0x67f0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
* [0x71e8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x7158]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EB97088E-CFDF-49C6-BE4BD906A5B20E86
## Module: SbRun
### Boot services:
* [0x1575] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x150a] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x110c] EFI_BOOT_SERVICES->LocateProtocol
* [0x1fa0] EFI_BOOT_SERVICES->LocateProtocol
* [0x20d9] EFI_BOOT_SERVICES->LocateProtocol
* [0x15f7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x4070]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiMetronomeArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB2-6F42-11D4-BCE70080C73C8881
* [0x4090]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiResetArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 27CFAC88-46CC-11D4-9A380090273FC14D
* [0x40c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x4618]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x40a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: SbRunSmm
### Boot services:
* [0x358] EFI_BOOT_SERVICES->LocateProtocol
* [0x386] EFI_BOOT_SERVICES->LocateProtocol
* [0x40d] EFI_BOOT_SERVICES->LocateProtocol
* [0x843] EFI_BOOT_SERVICES->LocateProtocol
* [0x1208] EFI_BOOT_SERVICES->LocateProtocol
* [0x1341] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x27b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x27e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x2d68]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2da8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x27d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: ScsiBus
### Boot services:
* [0x709] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x952] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x387] EFI_BOOT_SERVICES->OpenProtocol
* [0x429] EFI_BOOT_SERVICES->OpenProtocol
* [0x53a] EFI_BOOT_SERVICES->OpenProtocol
* [0x59c] EFI_BOOT_SERVICES->OpenProtocol
* [0x5e9] EFI_BOOT_SERVICES->OpenProtocol
* [0x669] EFI_BOOT_SERVICES->OpenProtocol
* [0x7ae] EFI_BOOT_SERVICES->OpenProtocol
* [0x91c] EFI_BOOT_SERVICES->OpenProtocol
* [0xa01] EFI_BOOT_SERVICES->OpenProtocol
* [0xab4] EFI_BOOT_SERVICES->OpenProtocol
* [0x10d9] EFI_BOOT_SERVICES->OpenProtocol
* [0x3f6] EFI_BOOT_SERVICES->CloseProtocol
* [0x483] EFI_BOOT_SERVICES->CloseProtocol
* [0x4b9] EFI_BOOT_SERVICES->CloseProtocol
* [0x62c] EFI_BOOT_SERVICES->CloseProtocol
* [0x74b] EFI_BOOT_SERVICES->CloseProtocol
* [0x777] EFI_BOOT_SERVICES->CloseProtocol
* [0x976] EFI_BOOT_SERVICES->CloseProtocol
* [0x994] EFI_BOOT_SERVICES->CloseProtocol
* [0x9b2] EFI_BOOT_SERVICES->CloseProtocol
* [0xa40] EFI_BOOT_SERVICES->CloseProtocol
* [0x31b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1056] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa6e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x1bc0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 0167CCC4-D0F7-4F21-A3EF9E64B7CDCE8B
* [0x1c10]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiExtScsiPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 143B7632-B81B-4CB7-ABD3B625A5B9BFFE
* [0x1c00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiScsiPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A59E8FCF-BDA0-43BB-90B1D3732ECAA877
* [0x1bf0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x1bc0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 0167CCC4-D0F7-4F21-A3EF9E64B7CDCE8B
* [0x1be0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiScsiIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 932F47E6-2362-4002-803E3CD54B138F85
* [0x1c10]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiExtScsiPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 143B7632-B81B-4CB7-ABD3B625A5B9BFFE
* [0x1c00]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiScsiPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A59E8FCF-BDA0-43BB-90B1D3732ECAA877
* [0x1bf0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x1bf0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: ScsiDisk
### Boot services:
* [0x8f7] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xa43] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x297a] EFI_BOOT_SERVICES->HandleProtocol
* [0x2b2a] EFI_BOOT_SERVICES->HandleProtocol
* [0x362] EFI_BOOT_SERVICES->OpenProtocol
* [0x448] EFI_BOOT_SERVICES->OpenProtocol
* [0x75e] EFI_BOOT_SERVICES->OpenProtocol
* [0x2d3e] EFI_BOOT_SERVICES->OpenProtocol
* [0x2da1] EFI_BOOT_SERVICES->OpenProtocol
* [0x3b6] EFI_BOOT_SERVICES->CloseProtocol
* [0x531] EFI_BOOT_SERVICES->CloseProtocol
* [0x6a4] EFI_BOOT_SERVICES->CloseProtocol
* [0x6fe] EFI_BOOT_SERVICES->CloseProtocol
* [0x7be] EFI_BOOT_SERVICES->CloseProtocol
* [0x2d60] EFI_BOOT_SERVICES->CloseProtocol
* [0x2908] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x28c9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x31b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x60c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x79b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x3b50]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x3b90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x3b60]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiScsiIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 932F47E6-2362-4002-803E3CD54B138F85
* [0x3b50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x3b60]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiScsiIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 932F47E6-2362-4002-803E3CD54B138F85
* [0x3bf8]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 00000000-0000-0000-AA4BF70836EAD941
* [0x3b50]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
## Module: SecureBootDXE
### Boot services:
* [0x35a] EFI_BOOT_SERVICES->HandleProtocol
* [0x314] EFI_BOOT_SERVICES->LocateHandleBuffer
### Protocols:
* [0x1100]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
## Module: SecurityStubDxe
### Boot services:
* [0x569] EFI_BOOT_SERVICES->HandleProtocol
* [0x98a] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d8] EFI_BOOT_SERVICES->HandleProtocol
* [0x49cf] EFI_BOOT_SERVICES->HandleProtocol
* [0x4be8] EFI_BOOT_SERVICES->HandleProtocol
* [0x4c9e] EFI_BOOT_SERVICES->HandleProtocol
* [0x360] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3f4] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x85a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xe37] EFI_BOOT_SERVICES->LocateProtocol
* [0x25d7] EFI_BOOT_SERVICES->LocateProtocol
* [0x2650] EFI_BOOT_SERVICES->LocateProtocol
* [0x27ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x2de] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x6c80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x6ca0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x6cd0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
* [0x6cc0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFile2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4006C0C1-FCB3-403E-996D4A6C8724E06D
* [0x6cb0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 56EC3091-954C-11D2-8E3F00A0C969723B
* [0x6d10]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x6c50]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] BDS_CONNECT_DRIVERS_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 3AA83745-9454-4F7A-A7C090DBD02FAB8E
* [0x6ca0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x6d30]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 38D65EC3-8F39-4660-B8A6F36AA3925475
* [0x6d20]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_DIGITAL_SIGNATURE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5F87BA17-957D-433D-9E15C0E7C8798899
* [0x6d40]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_TCG_PLATFORM_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] 8C4C9A41-BF56-4627-9E0AC8386D66115C
## Module: Shell_Full
### Boot services:
* [0x66cf6] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x67cbd] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x6ebc1] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x65791] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x66e09] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x66e44] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x6cfe7] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x6d048] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x6d145] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x6d183] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x6ec23] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x7274e] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x7287e] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x72987] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x72a3a] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x76711] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x76ed3] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x77a8d] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x86d3e] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x9b8d3] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x9bf06] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xa09f2] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x65785] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x65d7b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x65de5] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x66d2d] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x66d96] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6cd30] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6cd4f] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6cd6b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6d38b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x83fc8] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x83fdf] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x8ea6e] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x8ea85] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6534e] EFI_BOOT_SERVICES->HandleProtocol
* [0x65abb] EFI_BOOT_SERVICES->HandleProtocol
* [0x65b7f] EFI_BOOT_SERVICES->HandleProtocol
* [0x65bac] EFI_BOOT_SERVICES->HandleProtocol
* [0x65e7d] EFI_BOOT_SERVICES->HandleProtocol
* [0x677ee] EFI_BOOT_SERVICES->HandleProtocol
* [0x67977] EFI_BOOT_SERVICES->HandleProtocol
* [0x67b2d] EFI_BOOT_SERVICES->HandleProtocol
* [0x67b69] EFI_BOOT_SERVICES->HandleProtocol
* [0x67c30] EFI_BOOT_SERVICES->HandleProtocol
* [0x67ccb] EFI_BOOT_SERVICES->HandleProtocol
* [0x67d10] EFI_BOOT_SERVICES->HandleProtocol
* [0x68fc1] EFI_BOOT_SERVICES->HandleProtocol
* [0x69014] EFI_BOOT_SERVICES->HandleProtocol
* [0x6ce41] EFI_BOOT_SERVICES->HandleProtocol
* [0x6ce7a] EFI_BOOT_SERVICES->HandleProtocol
* [0x6d1ba] EFI_BOOT_SERVICES->HandleProtocol
* [0x6ebfe] EFI_BOOT_SERVICES->HandleProtocol
* [0x6ecf8] EFI_BOOT_SERVICES->HandleProtocol
* [0x6ef4b] EFI_BOOT_SERVICES->HandleProtocol
* [0x700aa] EFI_BOOT_SERVICES->HandleProtocol
* [0x7666e] EFI_BOOT_SERVICES->HandleProtocol
* [0x76b4b] EFI_BOOT_SERVICES->HandleProtocol
* [0x76b6c] EFI_BOOT_SERVICES->HandleProtocol
* [0x76e0d] EFI_BOOT_SERVICES->HandleProtocol
* [0x76e56] EFI_BOOT_SERVICES->HandleProtocol
* [0x77978] EFI_BOOT_SERVICES->HandleProtocol
* [0x779c2] EFI_BOOT_SERVICES->HandleProtocol
* [0x77a4d] EFI_BOOT_SERVICES->HandleProtocol
* [0x7a25c] EFI_BOOT_SERVICES->HandleProtocol
* [0x7ac1a] EFI_BOOT_SERVICES->HandleProtocol
* [0x7ad74] EFI_BOOT_SERVICES->HandleProtocol
* [0x81908] EFI_BOOT_SERVICES->HandleProtocol
* [0x81c0e] EFI_BOOT_SERVICES->HandleProtocol
* [0x81d67] EFI_BOOT_SERVICES->HandleProtocol
* [0x83fb3] EFI_BOOT_SERVICES->HandleProtocol
* [0x84f3a] EFI_BOOT_SERVICES->HandleProtocol
* [0x854b9] EFI_BOOT_SERVICES->HandleProtocol
* [0x86510] EFI_BOOT_SERVICES->HandleProtocol
* [0x86c89] EFI_BOOT_SERVICES->HandleProtocol
* [0x87280] EFI_BOOT_SERVICES->HandleProtocol
* [0x87349] EFI_BOOT_SERVICES->HandleProtocol
* [0x87397] EFI_BOOT_SERVICES->HandleProtocol
* [0x87472] EFI_BOOT_SERVICES->HandleProtocol
* [0x87a2e] EFI_BOOT_SERVICES->HandleProtocol
* [0x87b58] EFI_BOOT_SERVICES->HandleProtocol
* [0x87b89] EFI_BOOT_SERVICES->HandleProtocol
* [0x87f9c] EFI_BOOT_SERVICES->HandleProtocol
* [0x88008] EFI_BOOT_SERVICES->HandleProtocol
* [0x8804b] EFI_BOOT_SERVICES->HandleProtocol
* [0x886eb] EFI_BOOT_SERVICES->HandleProtocol
* [0x8871d] EFI_BOOT_SERVICES->HandleProtocol
* [0x8a376] EFI_BOOT_SERVICES->HandleProtocol
* [0x8a575] EFI_BOOT_SERVICES->HandleProtocol
* [0x8a7dd] EFI_BOOT_SERVICES->HandleProtocol
* [0x8a8d8] EFI_BOOT_SERVICES->HandleProtocol
* [0x8afa1] EFI_BOOT_SERVICES->HandleProtocol
* [0x8afd2] EFI_BOOT_SERVICES->HandleProtocol
* [0x8ea59] EFI_BOOT_SERVICES->HandleProtocol
* [0x96a9c] EFI_BOOT_SERVICES->HandleProtocol
* [0x96aca] EFI_BOOT_SERVICES->HandleProtocol
* [0x96d01] EFI_BOOT_SERVICES->HandleProtocol
* [0x96e46] EFI_BOOT_SERVICES->HandleProtocol
* [0x971bf] EFI_BOOT_SERVICES->HandleProtocol
* [0x9792a] EFI_BOOT_SERVICES->HandleProtocol
* [0x9b8b6] EFI_BOOT_SERVICES->HandleProtocol
* [0x9beeb] EFI_BOOT_SERVICES->HandleProtocol
* [0x9e7d8] EFI_BOOT_SERVICES->HandleProtocol
* [0x9e8c8] EFI_BOOT_SERVICES->HandleProtocol
* [0x9e903] EFI_BOOT_SERVICES->HandleProtocol
* [0xa0df8] EFI_BOOT_SERVICES->HandleProtocol
* [0xa1d0a] EFI_BOOT_SERVICES->HandleProtocol
* [0xa1d88] EFI_BOOT_SERVICES->HandleProtocol
* [0xaa7a2] EFI_BOOT_SERVICES->HandleProtocol
* [0xaa7ef] EFI_BOOT_SERVICES->HandleProtocol
* [0xaa83c] EFI_BOOT_SERVICES->HandleProtocol
* [0xad6ae] EFI_BOOT_SERVICES->HandleProtocol
* [0xad72c] EFI_BOOT_SERVICES->HandleProtocol
* [0xafae6] EFI_BOOT_SERVICES->HandleProtocol
* [0xafb33] EFI_BOOT_SERVICES->HandleProtocol
* [0xafb80] EFI_BOOT_SERVICES->HandleProtocol
* [0xafeb2] EFI_BOOT_SERVICES->HandleProtocol
* [0xafeff] EFI_BOOT_SERVICES->HandleProtocol
* [0xaff4c] EFI_BOOT_SERVICES->HandleProtocol
* [0x65cad] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x678bc] EFI_BOOT_SERVICES->OpenProtocol
* [0x69c4c] EFI_BOOT_SERVICES->OpenProtocol
* [0x79b39] EFI_BOOT_SERVICES->OpenProtocol
* [0x79b76] EFI_BOOT_SERVICES->OpenProtocol
* [0x79caa] EFI_BOOT_SERVICES->OpenProtocol
* [0x79ce0] EFI_BOOT_SERVICES->OpenProtocol
* [0x79d16] EFI_BOOT_SERVICES->OpenProtocol
* [0x79d4b] EFI_BOOT_SERVICES->OpenProtocol
* [0x79ef6] EFI_BOOT_SERVICES->OpenProtocol
* [0x79f32] EFI_BOOT_SERVICES->OpenProtocol
* [0x79f66] EFI_BOOT_SERVICES->OpenProtocol
* [0x79fa2] EFI_BOOT_SERVICES->OpenProtocol
* [0x7a10a] EFI_BOOT_SERVICES->OpenProtocol
* [0x7a6d8] EFI_BOOT_SERVICES->OpenProtocol
* [0x7a70c] EFI_BOOT_SERVICES->OpenProtocol
* [0x7a73a] EFI_BOOT_SERVICES->OpenProtocol
* [0x7a763] EFI_BOOT_SERVICES->OpenProtocol
* [0x7a791] EFI_BOOT_SERVICES->OpenProtocol
* [0x80a1f] EFI_BOOT_SERVICES->OpenProtocol
* [0x80a60] EFI_BOOT_SERVICES->OpenProtocol
* [0x81323] EFI_BOOT_SERVICES->OpenProtocol
* [0x84e2e] EFI_BOOT_SERVICES->OpenProtocol
* [0x88dc8] EFI_BOOT_SERVICES->OpenProtocol
* [0x88dfe] EFI_BOOT_SERVICES->OpenProtocol
* [0x89240] EFI_BOOT_SERVICES->OpenProtocol
* [0x896d9] EFI_BOOT_SERVICES->OpenProtocol
* [0x8970d] EFI_BOOT_SERVICES->OpenProtocol
* [0x8b30a] EFI_BOOT_SERVICES->OpenProtocol
* [0x8e37f] EFI_BOOT_SERVICES->OpenProtocol
* [0x91914] EFI_BOOT_SERVICES->OpenProtocol
* [0x91954] EFI_BOOT_SERVICES->OpenProtocol
* [0x9197e] EFI_BOOT_SERVICES->OpenProtocol
* [0x919b0] EFI_BOOT_SERVICES->OpenProtocol
* [0x919dd] EFI_BOOT_SERVICES->OpenProtocol
* [0x91a0f] EFI_BOOT_SERVICES->OpenProtocol
* [0x96bad] EFI_BOOT_SERVICES->OpenProtocol
* [0x96eaf] EFI_BOOT_SERVICES->OpenProtocol
* [0x972a8] EFI_BOOT_SERVICES->OpenProtocol
* [0x98e29] EFI_BOOT_SERVICES->OpenProtocol
* [0x98e60] EFI_BOOT_SERVICES->OpenProtocol
* [0x99650] EFI_BOOT_SERVICES->OpenProtocol
* [0x99cd4] EFI_BOOT_SERVICES->OpenProtocol
* [0x99d04] EFI_BOOT_SERVICES->OpenProtocol
* [0x9aef6] EFI_BOOT_SERVICES->OpenProtocol
* [0x9af72] EFI_BOOT_SERVICES->OpenProtocol
* [0x9afaa] EFI_BOOT_SERVICES->OpenProtocol
* [0x9b069] EFI_BOOT_SERVICES->OpenProtocol
* [0x9b1b9] EFI_BOOT_SERVICES->OpenProtocol
* [0xa4740] EFI_BOOT_SERVICES->OpenProtocol
* [0xa479c] EFI_BOOT_SERVICES->OpenProtocol
* [0x812f9] EFI_BOOT_SERVICES->CloseProtocol
* [0x8e0c4] EFI_BOOT_SERVICES->CloseProtocol
* [0x8e5ba] EFI_BOOT_SERVICES->CloseProtocol
* [0x9b113] EFI_BOOT_SERVICES->CloseProtocol
* [0x672e0] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x690b0] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x8a2fc] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x96936] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x67084] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x67dcb] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x7ab7c] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x96c43] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x65662] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x66ffe] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x67687] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x67863] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x80bb8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x815fd] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x87fd0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8a299] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8a9e0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8af45] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa1d4b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xad6ef] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x685b8] EFI_BOOT_SERVICES->LocateProtocol
* [0x80b2f] EFI_BOOT_SERVICES->LocateProtocol
* [0x84190] EFI_BOOT_SERVICES->LocateProtocol
* [0x89fc1] EFI_BOOT_SERVICES->LocateProtocol
* [0x8a0da] EFI_BOOT_SERVICES->LocateProtocol
* [0x8a9aa] EFI_BOOT_SERVICES->LocateProtocol
* [0x902ef] EFI_BOOT_SERVICES->LocateProtocol
* [0x93c20] EFI_BOOT_SERVICES->LocateProtocol
* [0x9653f] EFI_BOOT_SERVICES->LocateProtocol
* [0xa113a] EFI_BOOT_SERVICES->LocateProtocol
* [0xa14c6] EFI_BOOT_SERVICES->LocateProtocol
* [0xa1796] EFI_BOOT_SERVICES->LocateProtocol
* [0xa1b1b] EFI_BOOT_SERVICES->LocateProtocol
* [0xaaf3a] EFI_BOOT_SERVICES->LocateProtocol
* [0xab790] EFI_BOOT_SERVICES->LocateProtocol
* [0xac2ed] EFI_BOOT_SERVICES->LocateProtocol
* [0xb13a6] EFI_BOOT_SERVICES->LocateProtocol
* [0xb1ea8] EFI_BOOT_SERVICES->LocateProtocol
* [0xb22e3] EFI_BOOT_SERVICES->LocateProtocol
* [0xb2bb6] EFI_BOOT_SERVICES->LocateProtocol
* [0xb428a] EFI_BOOT_SERVICES->LocateProtocol
* [0x659eb] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8fc0c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x93ce1] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x65819] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x6833d] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x6835b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x54d50]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiShellEnvironment2Guid
	 - [protocol_place] edk2_guids
	 - [guid] 47C7B221-C42A-11D2-8E5700A0C969723B
* [0x98f0]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiShellInterfaceGuid
	 - [protocol_place] edk2_guids
	 - [guid] 47C7B223-C42A-11D2-8E5700A0C969723B
* [0x460]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
* [0x470]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x530]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x54d50]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiShellEnvironment2Guid
	 - [protocol_place] edk2_guids
	 - [guid] 47C7B221-C42A-11D2-8E5700A0C969723B
* [0x470]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x460]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
* [0x580]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x98f0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiShellInterfaceGuid
	 - [protocol_place] edk2_guids
	 - [guid] 47C7B223-C42A-11D2-8E5700A0C969723B
* [0x5a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x580]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x98f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiShellInterfaceGuid
	 - [protocol_place] edk2_guids
	 - [guid] 47C7B223-C42A-11D2-8E5700A0C969723B
* [0x54d50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiShellEnvironment2Guid
	 - [protocol_place] edk2_guids
	 - [guid] 47C7B221-C42A-11D2-8E5700A0C969723B
* [0x590]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleFileSystemProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B22-6459-11D2-8E3900A0C969723B
* [0x5b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolumeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 389F751F-1838-4388-8390CD8154BD27F8
* [0x5c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x530]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x600]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDebugMaskProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4C8A2451-C207-405B-969499EA13251341
* [0x3f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSerialIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BB25CF6F-F1D4-11D2-9A0C0090273FC1FD
* [0x560]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x470]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C2-69C7-11D2-8E3900A0C969723B
* [0x460]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
* [0x410]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0x5e0]
	 - [service] HandleProtocol
	 - [protocol_name] EFI_NIC_IP4_CONFIG_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] 0DCA3D4D-12DA-4728-BF7E86CEB928D067
* [0x3a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp4ConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3B95AA31-3793-434B-8667C8070892E05E
* [0x380]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0x370]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0x360]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPxeBaseCodeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03C4E603-AC28-11D3-9A2D0090273FC14D
* [0x5d0]
	 - [service] HandleProtocol
	 - [protocol_name] EFI_PXE_DHCP4_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] 03C4E624-AC28-11D3-9A2D0090293FC14D
* [0x350]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31878C87-0B75-11D5-9A4F0090273FC14D
* [0x560]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x5a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x540]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDriverConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772B-D5E1-11D4-9A460090273FC14D
* [0x4e0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDriverConfiguration2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BFD7DC1D-24F1-40D9-82E72E09BB6B4EBE
* [0x520]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDriverDiagnosticsProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0784924F-E296-11D4-9A490090273FC14D
* [0x510]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDriverDiagnostics2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4D330321-025F-4AAC-90D85ED900173B63
* [0x580]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x420]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C51711E7-B4BF-404A-BFB80A048EF1FFE4
* [0x430]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0x430]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0x400]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0x340]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 26BACCB1-6F42-11D4-BCE70080C73C8881
* [0x3b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x390]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDecompressProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D8117CFE-94A6-11D4-9A3A0090273FC14D
* [0x5828]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_TELNET_SERVER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 6D3569D4-85E5-4943-AE46EE67A6E1AB5A
* [0x380]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
* [0x490]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
## Module: SiInitDxe
### Boot services:
* [0x1141] EFI_BOOT_SERVICES->HandleProtocol
* [0x1224] EFI_BOOT_SERVICES->HandleProtocol
* [0x12fe] EFI_BOOT_SERVICES->HandleProtocol
* [0x380] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1105] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x11e8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2ee] EFI_BOOT_SERVICES->LocateProtocol
* [0x329] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ec] EFI_BOOT_SERVICES->LocateProtocol
* [0x426] EFI_BOOT_SERVICES->LocateProtocol
* [0x57f] EFI_BOOT_SERVICES->LocateProtocol
* [0x5a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x1721] EFI_BOOT_SERVICES->LocateProtocol
* [0x18b7] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b81] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2ef0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x2eb0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x2ee0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverSupportedEfiVersionProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5C198761-16A8-4E69-972C89D67954F81D
* [0x2e90]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0x2ec0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x2e90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0x2ea0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] ECA27516-306C-4E28-8C944E521096695E
* [0x2ed0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C6AA1F27-5597-4802-9F63D62836598635
* [0x2f10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x2f00]
	 - [service] LocateProtocol
	 - [protocol_name] INTEL_MEBX_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 01AB1829-CECD-4CFA-A18CEA75D66F3E74
## Module: SioDxeInit
### Boot services:
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x9ed] EFI_BOOT_SERVICES->LocateProtocol
* [0x368] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xd20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xd30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EB97088E-CFDF-49C6-BE4BD906A5B20E86
## Module: SleepSmi
### Boot services:
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x39a] EFI_BOOT_SERVICES->LocateProtocol
* [0x421] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f0] EFI_BOOT_SERVICES->LocateProtocol
* [0x786] EFI_BOOT_SERVICES->LocateProtocol
* [0xf25] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3160]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3190]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x3698]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3180]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: Smbios
### Boot services:
* [0x2fa6] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2fcc] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2071] EFI_BOOT_SERVICES->HandleProtocol
* [0x20d4] EFI_BOOT_SERVICES->HandleProtocol
* [0x2c6a] EFI_BOOT_SERVICES->HandleProtocol
* [0x2049] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x20ac] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2c2f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x21aa] EFI_BOOT_SERVICES->LocateProtocol
* [0x24db] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b50] EFI_BOOT_SERVICES->LocateProtocol
* [0x3093] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3580]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLegacyRegion2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 70101EAF-0085-440C-B3568EE36FEF24F0
* [0x3590]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x4420]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x3580]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiLegacyRegion2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 70101EAF-0085-440C-B3568EE36FEF24F0
* [0x3590]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0x35b0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x3610]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x35a0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_LEGACY_BIOS_EXT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8E008510-9BB1-457D-9F70897ABA865DB9
* [0x35f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
* [0x35d0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_SMBIOS_BOARD_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 0903DD14-2CA0-458A-B5EB0C0CA30D785C
* [0x3600]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: SmbiosBoard
### Boot services:
* [0x35e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2e5] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a1] EFI_BOOT_SERVICES->LocateProtocol
* [0x491] EFI_BOOT_SERVICES->LocateProtocol
* [0x5a8] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x910]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: SmbiosMisc
### Boot services:
* [0x2ca] EFI_BOOT_SERVICES->LocateProtocol
* [0x33c] EFI_BOOT_SERVICES->LocateProtocol
* [0x35a] EFI_BOOT_SERVICES->LocateProtocol
* [0x377] EFI_BOOT_SERVICES->LocateProtocol
* [0x394] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b1] EFI_BOOT_SERVICES->LocateProtocol
* [0x3f5] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x7a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0x7d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0x7b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0x7f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0x7c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0x7e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
## Module: SmbiosUpdateData
### Boot services:
* [0x32d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x309] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x680]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_SMBIOS_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5E90A50D-6955-4A49-9032DA3812F8E8E5
## Module: SmmAccess
### Boot services:
* [0x300] EFI_BOOT_SERVICES->LocateProtocol
* [0x483] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x940]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2F707EBB-4A1A-11D4-9A380090273FC14D
## Module: SmmControl
### Boot services:
* [0x116b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: SmmGenericSio
### Boot services:
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x39a] EFI_BOOT_SERVICES->LocateProtocol
* [0x10c3] EFI_BOOT_SERVICES->LocateProtocol
* [0x1157] EFI_BOOT_SERVICES->LocateProtocol
* [0x1355] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a8d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1e90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1eb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x23e8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1e70]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 7576CC89-8FA3-4CAD-BA026119B46ED44A
* [0x1ec0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
* [0x1ed0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EB97088E-CFDF-49C6-BE4BD906A5B20E86
## Module: SmmHddSecurity
### Boot services:
* [0x364] EFI_BOOT_SERVICES->LocateProtocol
* [0x397] EFI_BOOT_SERVICES->LocateProtocol
* [0x10df] EFI_BOOT_SERVICES->LocateProtocol
* [0x1171] EFI_BOOT_SERVICES->LocateProtocol
* [0x1775] EFI_BOOT_SERVICES->LocateProtocol
* [0x185d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1bf0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1c40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x2158]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1c50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: SmmLockBox
### Boot services:
* [0x463] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x330] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xd10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
## Module: SmmPcieSataController
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x4eb] EFI_BOOT_SERVICES->LocateProtocol
* [0x57d] EFI_BOOT_SERVICES->LocateProtocol
* [0x6c9] EFI_BOOT_SERVICES->LocateProtocol
* [0x7a6] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xbc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x10d8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xbe0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: SmmPciRbIo
### Boot services:
* [0x11ca] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
* [0x395] EFI_BOOT_SERVICES->LocateProtocol
* [0x106d] EFI_BOOT_SERVICES->LocateProtocol
* [0x10fe] EFI_BOOT_SERVICES->LocateProtocol
* [0x1178] EFI_BOOT_SERVICES->LocateProtocol
* [0x1305] EFI_BOOT_SERVICES->LocateProtocol
* [0x17c3] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1ac0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSmmPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8BC1714D-FFCB-41C3-89DC6C74D06D98EA
* [0x1ae0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1b20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x2018]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1ad0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 6FCE3BB9-9742-4CFD-8E9E39F98DCA3271
* [0x1b10]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
* [0x1af0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: SmmPlatform
### Boot services:
* [0x13cf] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1417] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x32c] EFI_BOOT_SERVICES->LocateProtocol
* [0x35a] EFI_BOOT_SERVICES->LocateProtocol
* [0x16b8] EFI_BOOT_SERVICES->LocateProtocol
* [0x16e8] EFI_BOOT_SERVICES->LocateProtocol
* [0x1718] EFI_BOOT_SERVICES->LocateProtocol
* [0x1997] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x23c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2420]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x23a0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
* [0x2390]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] AB5A4DF4-F0D7-49A8-BF5CF25DA04C2533
* [0x2380]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 3DC21D75-DE0E-4300-A0AA19C41C0CF3DF
* [0x2410]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: SmmS3SaveState
### Boot services:
* [0x54e] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x57f] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x218c] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x22af] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2fe] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x21db] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x39c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ca] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f8d] EFI_BOOT_SERVICES->LocateProtocol
* [0x2218] EFI_BOOT_SERVICES->LocateProtocol
* [0x29c7] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2bc0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 47B7FA8C-F4BD-4AF6-8200333086F0D2C8
* [0x2bb0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x2b80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2ba0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x2bb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 60FF8964-E906-41D0-AFEDF241E974E08E
* [0x2b90]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: SmramSaveInfoHandlerSmm
### Boot services:
* [0x2e0] EFI_BOOT_SERVICES->LocateProtocol
* [0x30e] EFI_BOOT_SERVICES->LocateProtocol
* [0x3d3] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x790]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x7a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x780]
	 - [service] LocateProtocol
	 - [protocol_name] DXE_CPU_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] E223CF65-F6CE-4122-B3AF4BD18AFF40A1
## Module: SnpDxe
### Boot services:
* [0xb6e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xf0f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1059] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x46c] EFI_BOOT_SERVICES->HandleProtocol
* [0x1df6] EFI_BOOT_SERVICES->HandleProtocol
* [0x6b1] EFI_BOOT_SERVICES->OpenProtocol
* [0x6e9] EFI_BOOT_SERVICES->OpenProtocol
* [0x809] EFI_BOOT_SERVICES->OpenProtocol
* [0x873] EFI_BOOT_SERVICES->OpenProtocol
* [0x8aa] EFI_BOOT_SERVICES->OpenProtocol
* [0x1021] EFI_BOOT_SERVICES->OpenProtocol
* [0x25fa] EFI_BOOT_SERVICES->OpenProtocol
* [0x265a] EFI_BOOT_SERVICES->OpenProtocol
* [0x75e] EFI_BOOT_SERVICES->CloseProtocol
* [0x8d5] EFI_BOOT_SERVICES->CloseProtocol
* [0xf89] EFI_BOOT_SERVICES->CloseProtocol
* [0xfad] EFI_BOOT_SERVICES->CloseProtocol
* [0x10b3] EFI_BOOT_SERVICES->CloseProtocol
* [0x10d1] EFI_BOOT_SERVICES->CloseProtocol
* [0x261c] EFI_BOOT_SERVICES->CloseProtocol
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1dbe] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x548] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x4f60]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x4f70]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x4f80]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x4f60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x4f70]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x4f80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x4f90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x4f30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0x4f40]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x4f50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiNetworkInterfaceIdentifierProtocolGuid_31
	 - [protocol_place] edk2_guids
	 - [guid] 1ACED566-76ED-4218-BC81767F1F977A89
* [0x4f20]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0x4f30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0x4f50]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiNetworkInterfaceIdentifierProtocolGuid_31
	 - [protocol_place] edk2_guids
	 - [guid] 1ACED566-76ED-4218-BC81767F1F977A89
* [0x4f40]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0x4f30]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
## Module: StatusCodeDxe
### Boot services:
* [0x1c58] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x25ea] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x44f3] EFI_BOOT_SERVICES->OpenProtocol
* [0x44a7] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1102] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e9a] EFI_BOOT_SERVICES->LocateProtocol
* [0x24b4] EFI_BOOT_SERVICES->LocateProtocol
* [0x2575] EFI_BOOT_SERVICES->LocateProtocol
* [0x41b9] EFI_BOOT_SERVICES->LocateProtocol
* [0x42a1] EFI_BOOT_SERVICES->LocateProtocol
* [0x1cdd] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x5060]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] EFI_DATA_HUB_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] AE80D021-618E-11D4-BCD70080C73C8881
* [0x50b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0x5080]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x5060]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_DATA_HUB_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] AE80D021-618E-11D4-BCD70080C73C8881
* [0x5668]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0x5070]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: StatusCodeSmm
### Boot services:
* [0x887] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x8b1] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x8d4] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x39a] EFI_BOOT_SERVICES->LocateProtocol
* [0x421] EFI_BOOT_SERVICES->LocateProtocol
* [0x2571] EFI_BOOT_SERVICES->LocateProtocol
* [0x2659] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x31b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x31c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
## Module: StdDefaultsUpdate
### Boot services:
* [0x127f] EFI_BOOT_SERVICES->HandleProtocol
* [0x18cc] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x193c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1162] EFI_BOOT_SERVICES->LocateProtocol
* [0x1865] EFI_BOOT_SERVICES->LocateProtocol
* [0x1c2d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3000]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x3518]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x3010]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C298B206-7FB5-4A7E-94614F3577F1A07A
* [0x3020]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: TbtDxe
### Boot services:
* [0xcda] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x365] EFI_BOOT_SERVICES->HandleProtocol
* [0xcbb] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2ee] EFI_BOOT_SERVICES->LocateProtocol
* [0x848] EFI_BOOT_SERVICES->LocateProtocol
* [0x908] EFI_BOOT_SERVICES->LocateProtocol
* [0xa20] EFI_BOOT_SERVICES->LocateProtocol
* [0xd23] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x19c0]
	 - [service] HandleProtocol
	 - [protocol_name] OPROM_START_END_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] F2A128FF-257B-456E-9DE863E7C7DCDFAC
* [0x19c0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] OPROM_START_END_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] F2A128FF-257B-456E-9DE863E7C7DCDFAC
* [0x19f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x19b0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
* [0x2078]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_ACPI_SUPPORT_GUID
	 - [protocol_place] edk_guids
	 - [guid] DBFF9D55-89B7-46DA-BDDF677D3DC0241D
* [0x19e0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: TbtSmm
### Boot services:
* [0x1a51] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x36f] EFI_BOOT_SERVICES->LocateProtocol
* [0x39d] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a1f] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x61a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x61b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
* [0x6160]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
## Module: Tcg2Dxe
### Boot services:
* [0x6962] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x5954] EFI_BOOT_SERVICES->HandleProtocol
* [0x6805] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x68f7] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x6c3d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x345] EFI_BOOT_SERVICES->LocateProtocol
* [0x6f5] EFI_BOOT_SERVICES->LocateProtocol
* [0xcc8] EFI_BOOT_SERVICES->LocateProtocol
* [0xd47] EFI_BOOT_SERVICES->LocateProtocol
* [0xdcd] EFI_BOOT_SERVICES->LocateProtocol
* [0x1c9b] EFI_BOOT_SERVICES->LocateProtocol
* [0x3141] EFI_BOOT_SERVICES->LocateProtocol
* [0x3883] EFI_BOOT_SERVICES->LocateProtocol
* [0x38b1] EFI_BOOT_SERVICES->LocateProtocol
* [0x49fd] EFI_BOOT_SERVICES->LocateProtocol
* [0x4a2b] EFI_BOOT_SERVICES->LocateProtocol
* [0x58cb] EFI_BOOT_SERVICES->LocateProtocol
* [0x6144] EFI_BOOT_SERVICES->LocateProtocol
* [0x6183] EFI_BOOT_SERVICES->LocateProtocol
* [0x62f7] EFI_BOOT_SERVICES->LocateProtocol
* [0x671f] EFI_BOOT_SERVICES->LocateProtocol
* [0x6868] EFI_BOOT_SERVICES->LocateProtocol
* [0xd73f] EFI_BOOT_SERVICES->LocateProtocol
* [0x66af] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x6d05] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xea20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xe9f0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] BDS_ALL_DRIVERS_CONNECTED_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] DBC9FD21-FAD8-45B0-9E7827158867CC93
* [0xea00]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
* [0xe9b0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiResetArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 27CFAC88-46CC-11D4-9A380090273FC14D
* [0xe9a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTrEEProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 607F766C-7455-42BE-930BE4D76DB2720F
* [0xe990]
	 - [service] LocateProtocol
	 - [protocol_name] TCG_PLATFORM_SETUP_POLICY_GUID
	 - [protocol_place] ami_guids
	 - [guid] BB6CBEFF-E072-40D2-A6EBBAB75BDE87E7
* [0xe930]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 48E40CAD-A6D2-4756-8AEB81F468D4A856
* [0xe9e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 9C98C00A-2E9B-4896-95C8AC64358284E5
* [0xe9d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 78092548-48CF-449B-9BDBF63849856460
* [0xea00]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
## Module: TcgDxe
### Boot services:
* [0x178f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x17b1] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xf77] EFI_BOOT_SERVICES->HandleProtocol
* [0xf9a] EFI_BOOT_SERVICES->HandleProtocol
* [0x2541] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x389] EFI_BOOT_SERVICES->LocateProtocol
* [0xc12] EFI_BOOT_SERVICES->LocateProtocol
* [0xc36] EFI_BOOT_SERVICES->LocateProtocol
* [0xfba] EFI_BOOT_SERVICES->LocateProtocol
* [0xfde] EFI_BOOT_SERVICES->LocateProtocol
* [0x13e0] EFI_BOOT_SERVICES->LocateProtocol
* [0x14f5] EFI_BOOT_SERVICES->LocateProtocol
* [0x1573] EFI_BOOT_SERVICES->LocateProtocol
* [0x161e] EFI_BOOT_SERVICES->LocateProtocol
* [0x16d2] EFI_BOOT_SERVICES->LocateProtocol
* [0x22e2] EFI_BOOT_SERVICES->LocateProtocol
* [0x2415] EFI_BOOT_SERVICES->LocateProtocol
* [0x24ee] EFI_BOOT_SERVICES->LocateProtocol
* [0x26e5] EFI_BOOT_SERVICES->LocateProtocol
* [0x2702] EFI_BOOT_SERVICES->LocateProtocol
* [0x2917] EFI_BOOT_SERVICES->LocateProtocol
* [0x15d4] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1649] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2883] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x28e3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x49a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x49c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0x49b0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] EFI_ACPI_SUPPORT_GUID
	 - [protocol_place] edk_guids
	 - [guid] DBFF9D55-89B7-46DA-BDDF677D3DC0241D
* [0x4970]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F541796D-A62E-4954-A7759584F61B9CDD
* [0x4960]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_TPM_DEVICE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] DE161CFE-1E60-42A1-8CC3EE7EF0735212
* [0x4980]
	 - [service] LocateProtocol
	 - [protocol_name] TCG_PLATFORM_SETUP_POLICY_GUID
	 - [protocol_place] ami_guids
	 - [guid] BB6CBEFF-E072-40D2-A6EBBAB75BDE87E7
* [0x49e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] A062CF1F-8473-4BF3-8793600BC4FFA9A9
* [0x49b0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_ACPI_SUPPORT_GUID
	 - [protocol_place] edk_guids
	 - [guid] DBFF9D55-89B7-46DA-BDDF677D3DC0241D
* [0x49f0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: TcgDxeplatform
### Boot services:
* [0x330] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x580]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 8C939604-0700-4415-9D621161DB8164A6
## Module: TcgLegacy
### Boot services:
* [0x544] EFI_BOOT_SERVICES->HandleProtocol
* [0x504] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x81d] EFI_BOOT_SERVICES->LocateProtocol
* [0x844] EFI_BOOT_SERVICES->LocateProtocol
* [0x86f] EFI_BOOT_SERVICES->LocateProtocol
* [0x893] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xf00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0xee0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F541796D-A62E-4954-A7759584F61B9CDD
* [0xf20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTrEEProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 607F766C-7455-42BE-930BE4D76DB2720F
* [0xef0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
* [0xf10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyRegion2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 70101EAF-0085-440C-B3568EE36FEF24F0
## Module: TcgPlatformSetupPolicy
### Boot services:
* [0x702] EFI_BOOT_SERVICES->LocateProtocol
* [0xc87] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0xde0]
	 - [service] LocateProtocol
	 - [protocol_name] TCG_PLATFORM_SETUP_POLICY_GUID
	 - [protocol_place] ami_guids
	 - [guid] BB6CBEFF-E072-40D2-A6EBBAB75BDE87E7
## Module: TcgSmm
### Boot services:
* [0x32c] EFI_BOOT_SERVICES->LocateProtocol
* [0x35a] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1470]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x14a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
## Module: TcoSmi
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x402] EFI_BOOT_SERVICES->LocateProtocol
* [0x56b] EFI_BOOT_SERVICES->LocateProtocol
* [0x711] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xab0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xfb8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0xad0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: TcpDxe
### Boot services:
* [0x4140] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x75c6] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7732] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7d4c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1b89] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0xa11b] EFI_BOOT_SERVICES->HandleProtocol
* [0x6de] EFI_BOOT_SERVICES->OpenProtocol
* [0x71d] EFI_BOOT_SERVICES->OpenProtocol
* [0xa77] EFI_BOOT_SERVICES->OpenProtocol
* [0xbc5] EFI_BOOT_SERVICES->OpenProtocol
* [0xc01] EFI_BOOT_SERVICES->OpenProtocol
* [0xca5] EFI_BOOT_SERVICES->OpenProtocol
* [0xce1] EFI_BOOT_SERVICES->OpenProtocol
* [0xdb1] EFI_BOOT_SERVICES->OpenProtocol
* [0xde7] EFI_BOOT_SERVICES->OpenProtocol
* [0x1038] EFI_BOOT_SERVICES->OpenProtocol
* [0x1070] EFI_BOOT_SERVICES->OpenProtocol
* [0x1c83] EFI_BOOT_SERVICES->OpenProtocol
* [0x446e] EFI_BOOT_SERVICES->OpenProtocol
* [0x44f4] EFI_BOOT_SERVICES->OpenProtocol
* [0x5b8d] EFI_BOOT_SERVICES->OpenProtocol
* [0x7363] EFI_BOOT_SERVICES->OpenProtocol
* [0x73a6] EFI_BOOT_SERVICES->OpenProtocol
* [0x73d9] EFI_BOOT_SERVICES->OpenProtocol
* [0x749f] EFI_BOOT_SERVICES->OpenProtocol
* [0xe0f] EFI_BOOT_SERVICES->CloseProtocol
* [0x1d66] EFI_BOOT_SERVICES->CloseProtocol
* [0x7477] EFI_BOOT_SERVICES->CloseProtocol
* [0x9fd] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x4422] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x44ab] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x905] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5a05] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9ead] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5c0] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xb43] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x5a74] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x5bae] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0xad50]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xadf0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0xae00]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0xae10]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0xad50]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xadf0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0xae00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0xae10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0xae20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0xae30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp4Config2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B446ED1-E30B-4FAA-871A3654ECA36080
* [0xadd0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EC20EB79-6C1A-4664-9A0DD2E4CC16D664
* [0xad90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 00720665-67EB-4A99-BAF7D3C33A1C7CC9
* [0xad70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C51711E7-B4BF-404A-BFB80A048EF1FFE4
* [0xadb0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EC835DD3-FE0F-617B-A621B350C3E13388
* [0xad50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xad80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 65530BC7-A359-410F-B0105AADC7EC2B62
* [0xadc0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 46E44855-BD60-4AB7-AB0DA679B9447D77
* [0xad50]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xad60]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0xada0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
* [0xada0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
* [0xad60]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0xade0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 480F8AE9-0C46-4AA9-BC89DB9FBA619806
* [0xadf0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0xadf0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
## Module: TimestampDxe
### Boot services:
* [0x2ff] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* [0x3c0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiTimestampProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] AFBFDE41-2E6E-4262-BA6562B9236E5495
## Module: TouchInputFilterDriver
### Boot services:
* [0x3f1] EFI_BOOT_SERVICES->HandleProtocol
* [0x9e1] EFI_BOOT_SERVICES->HandleProtocol
* [0x80a] EFI_BOOT_SERVICES->OpenProtocol
* [0x848] EFI_BOOT_SERVICES->OpenProtocol
* [0x878] EFI_BOOT_SERVICES->OpenProtocol
* [0xad7] EFI_BOOT_SERVICES->OpenProtocol
* [0xc7e] EFI_BOOT_SERVICES->OpenProtocol
* [0x2c9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x72a] EFI_BOOT_SERVICES->LocateProtocol
* [0x467] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x48a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9ab] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x334] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x38b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xb0a] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x1260]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x1200]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8D59D32B-C655-4AE9-9B15F25904992A43
* [0x1230]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 2599ED9D-61EE-4E32-92579C7C0D9C40A3
* [0x1200]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8D59D32B-C655-4AE9-9B15F25904992A43
* [0x11c0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 91B1D27B-E126-48D1-8234D28B81C88362
* [0x1230]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 2599ED9D-61EE-4E32-92579C7C0D9C40A3
* [0x1220]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverSupportedEfiVersionProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5C198761-16A8-4E69-972C89D67954F81D
* [0x1210]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x1230]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 2599ED9D-61EE-4E32-92579C7C0D9C40A3
## Module: Tpm20Acpi
### Boot services:
* [0x2d4] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x484] EFI_BOOT_SERVICES->LocateProtocol
* [0x4ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x4e7] EFI_BOOT_SERVICES->LocateProtocol
* [0x857] EFI_BOOT_SERVICES->LocateProtocol
* [0xa6b] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xde0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] BDS_ALL_DRIVERS_CONNECTED_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] DBC9FD21-FAD8-45B0-9E7827158867CC93
* [0xdb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0xdc0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_ACPI_SUPPORT_GUID
	 - [protocol_place] edk_guids
	 - [guid] DBFF9D55-89B7-46DA-BDDF677D3DC0241D
* [0xdd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTrEEProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 607F766C-7455-42BE-930BE4D76DB2720F
* [0xdf0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: Tpm20PlatformDxe
### Boot services:
* [0x1082] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xa32] EFI_BOOT_SERVICES->HandleProtocol
* [0xa62] EFI_BOOT_SERVICES->HandleProtocol
* [0xf64] EFI_BOOT_SERVICES->HandleProtocol
* [0x1ac5] EFI_BOOT_SERVICES->HandleProtocol
* [0x1d76] EFI_BOOT_SERVICES->HandleProtocol
* [0x5ed1] EFI_BOOT_SERVICES->HandleProtocol
* [0x30fa] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x5f9f] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x623e] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x6456] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x64c7] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x658e] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x5ff0] EFI_BOOT_SERVICES->OpenProtocol
* [0xefd] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a62] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1d18] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x324] EFI_BOOT_SERVICES->LocateProtocol
* [0x342] EFI_BOOT_SERVICES->LocateProtocol
* [0x35f] EFI_BOOT_SERVICES->LocateProtocol
* [0x37c] EFI_BOOT_SERVICES->LocateProtocol
* [0x399] EFI_BOOT_SERVICES->LocateProtocol
* [0x3e0] EFI_BOOT_SERVICES->LocateProtocol
* [0x615] EFI_BOOT_SERVICES->LocateProtocol
* [0x68b] EFI_BOOT_SERVICES->LocateProtocol
* [0x898] EFI_BOOT_SERVICES->LocateProtocol
* [0xdde] EFI_BOOT_SERVICES->LocateProtocol
* [0x1533] EFI_BOOT_SERVICES->LocateProtocol
* [0x1755] EFI_BOOT_SERVICES->LocateProtocol
* [0x1c36] EFI_BOOT_SERVICES->LocateProtocol
* [0x26b4] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ba7] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f03] EFI_BOOT_SERVICES->LocateProtocol
* [0x324f] EFI_BOOT_SERVICES->LocateProtocol
* [0x3737] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c2b] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c6a] EFI_BOOT_SERVICES->LocateProtocol
* [0x4d51] EFI_BOOT_SERVICES->LocateProtocol
* [0x4e19] EFI_BOOT_SERVICES->LocateProtocol
* [0x5259] EFI_BOOT_SERVICES->LocateProtocol
* [0x52eb] EFI_BOOT_SERVICES->LocateProtocol
* [0x580b] EFI_BOOT_SERVICES->LocateProtocol
* [0x5907] EFI_BOOT_SERVICES->LocateProtocol
* [0x5945] EFI_BOOT_SERVICES->LocateProtocol
* [0x5c14] EFI_BOOT_SERVICES->LocateProtocol
* [0x5d8f] EFI_BOOT_SERVICES->LocateProtocol
* [0x6021] EFI_BOOT_SERVICES->LocateProtocol
* [0x6528] EFI_BOOT_SERVICES->LocateProtocol
* [0x6773] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xd630]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0xd640]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CE345171-BA0B-11D2-8E4F00A0C969723B
* [0xd720]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xd700]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 52C78312-8EDC-4233-98F21A1AA5E388A5
* [0xd660]
	 - [service] HandleProtocol
	 - [protocol_name] OPROM_START_END_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] F2A128FF-257B-456E-9DE863E7C7DCDFAC
* [0xd6e0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiResetArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 27CFAC88-46CC-11D4-9A380090273FC14D
* [0xd660]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] OPROM_START_END_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] F2A128FF-257B-456E-9DE863E7C7DCDFAC
* [0xd6b0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] BDS_ALL_DRIVERS_CONNECTED_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] DBC9FD21-FAD8-45B0-9E7827158867CC93
* [0xd6d0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
* [0xd680]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTrEEProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 607F766C-7455-42BE-930BE4D76DB2720F
* [0xd670]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A1EE763-D47A-43B4-AABEEF1DE2AB56FC
* [0xd630]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0xd700]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 52C78312-8EDC-4233-98F21A1AA5E388A5
* [0xd740]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0xd750]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0xd760]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0xd730]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0xd650]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0xd680]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTrEEProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 607F766C-7455-42BE-930BE4D76DB2720F
* [0xd6a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 78092548-48CF-449B-9BDBF63849856460
* [0xd690]
	 - [service] LocateProtocol
	 - [protocol_name] TCG_PLATFORM_SETUP_POLICY_GUID
	 - [protocol_place] ami_guids
	 - [guid] BB6CBEFF-E072-40D2-A6EBBAB75BDE87E7
* [0xd5c0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 47144F62-B423-4524-AC6A90106BAA89FB
* [0xd6c0]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_POST_MANAGER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8A91B1E1-56C7-4ADC-ABEB1C2CA1729EFF
* [0xd5a0]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_OS_PPI_CONFIRMATION_OVERRIDE_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5F171F5F-8385-4086-A69B1FCF06AE4A3D
* [0xd6d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] CD3D0A05-9E24-437C-A8911EE053DB7638
* [0xd6f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 9C98C00A-2E9B-4896-95C8AC64358284E5
* [0xd710]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: TpmClearOnRollbackSmm
### Boot services:
* [0x5eb] EFI_BOOT_SERVICES->HandleProtocol
* [0x489] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x5b0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x34c] EFI_BOOT_SERVICES->LocateProtocol
* [0x37a] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1270]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x1250]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1260]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C2702B74-800C-4131-87468FB5B89CE4AC
## Module: TpmNvmeSupport
### Boot services:
* [0x447] EFI_BOOT_SERVICES->HandleProtocol
* [0x3bd] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x40a] EFI_BOOT_SERVICES->LocateHandleBuffer
### Protocols:
* [0x560]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 52C78312-8EDC-4233-98F21A1AA5E388A5
* [0x560]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 52C78312-8EDC-4233-98F21A1AA5E388A5
## Module: TpmSmbiosDxe
### Boot services:
* [0xb73] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xd63] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x343] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3ba] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x71a] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2ec] EFI_BOOT_SERVICES->LocateProtocol
* [0x360] EFI_BOOT_SERVICES->LocateProtocol
* [0x40e] EFI_BOOT_SERVICES->LocateProtocol
* [0x6c3] EFI_BOOT_SERVICES->LocateProtocol
* [0x99a] EFI_BOOT_SERVICES->LocateProtocol
* [0xbfa] EFI_BOOT_SERVICES->LocateProtocol
* [0xc1e] EFI_BOOT_SERVICES->LocateProtocol
* [0xdd7] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x10b0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTrEEProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 607F766C-7455-42BE-930BE4D76DB2720F
* [0x10c0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F541796D-A62E-4954-A7759584F61B9CDD
* [0x10a0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0x10b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTrEEProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 607F766C-7455-42BE-930BE4D76DB2720F
* [0x10c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F541796D-A62E-4954-A7759584F61B9CDD
* [0x10a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 03583FF6-CB36-4940-947EB9B39F4AFAF7
* [0x10e0]
	 - [service] LocateProtocol
	 - [protocol_name] TCG_PLATFORM_SETUP_POLICY_GUID
	 - [protocol_place] ami_guids
	 - [guid] BB6CBEFF-E072-40D2-A6EBBAB75BDE87E7
* [0x10f0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: TxtDxe
### Boot services:
* [0x2fc] EFI_BOOT_SERVICES->LocateProtocol
* [0x383] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x19c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E857CAF6-C046-45DC-BE3FEE0765FBA887
* [0x19b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3FDDA605-A76E-4F46-AD2912F4531B3D08
## Module: Udp4Dxe
### Boot services:
* [0x336e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x34da] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x3ac4] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x649] EFI_BOOT_SERVICES->OpenProtocol
* [0x685] EFI_BOOT_SERVICES->OpenProtocol
* [0x821] EFI_BOOT_SERVICES->OpenProtocol
* [0xacf] EFI_BOOT_SERVICES->OpenProtocol
* [0xb16] EFI_BOOT_SERVICES->OpenProtocol
* [0xbdf] EFI_BOOT_SERVICES->OpenProtocol
* [0xf22] EFI_BOOT_SERVICES->OpenProtocol
* [0x310b] EFI_BOOT_SERVICES->OpenProtocol
* [0x314e] EFI_BOOT_SERVICES->OpenProtocol
* [0x3181] EFI_BOOT_SERVICES->OpenProtocol
* [0x3247] EFI_BOOT_SERVICES->OpenProtocol
* [0xc36] EFI_BOOT_SERVICES->CloseProtocol
* [0xc60] EFI_BOOT_SERVICES->CloseProtocol
* [0x321f] EFI_BOOT_SERVICES->CloseProtocol
* [0x7a2] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xe9f] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x576] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x710] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa82] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8f2] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xa16] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xc7d] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x63e0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x63f0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6400]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x63e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x63f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6400]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6410]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x6370]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 83F01464-99BD-45E5-B383AF6305D8E9E6
* [0x6380]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] C51711E7-B4BF-404A-BFB80A048EF1FFE4
* [0x63a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0x6390]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x63a0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0x63b0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
* [0x63a0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0x63d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 480F8AE9-0C46-4AA9-BC89DB9FBA619806
* [0x6390]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0x6370]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiUdp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 83F01464-99BD-45E5-B383AF6305D8E9E6
* [0x6390]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
## Module: Udp6Dxe
### Boot services:
* [0x30ca] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x3236] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x3896] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x5ed] EFI_BOOT_SERVICES->OpenProtocol
* [0x629] EFI_BOOT_SERVICES->OpenProtocol
* [0x828] EFI_BOOT_SERVICES->OpenProtocol
* [0xabf] EFI_BOOT_SERVICES->OpenProtocol
* [0xb06] EFI_BOOT_SERVICES->OpenProtocol
* [0xbcf] EFI_BOOT_SERVICES->OpenProtocol
* [0xf7a] EFI_BOOT_SERVICES->OpenProtocol
* [0x2e67] EFI_BOOT_SERVICES->OpenProtocol
* [0x2eaa] EFI_BOOT_SERVICES->OpenProtocol
* [0x2edd] EFI_BOOT_SERVICES->OpenProtocol
* [0x2fa3] EFI_BOOT_SERVICES->OpenProtocol
* [0xc26] EFI_BOOT_SERVICES->CloseProtocol
* [0xc50] EFI_BOOT_SERVICES->CloseProtocol
* [0x2f7b] EFI_BOOT_SERVICES->CloseProtocol
* [0x7a9] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xef7] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x576] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x6b2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa72] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x900] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xa06] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xc6d] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0x61e0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x61f0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6200]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x61e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0x61f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0x6200]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0x6210]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x6190]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 66ED4721-3C98-4D3E-81E3D03DD39A7254
* [0x6180]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EC835DD3-FE0F-617B-A621B350C3E13388
* [0x6170]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
* [0x61a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x6170]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
* [0x6170]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
* [0x61d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 480F8AE9-0C46-4AA9-BC89DB9FBA619806
* [0x61a0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0x6190]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiUdp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 66ED4721-3C98-4D3E-81E3D03DD39A7254
* [0x61a0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
## Module: UefiPxeBcDxe
### Boot services:
* [0x13ac] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1a6f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1da3] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7e5a] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xae4] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xdfe] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1e27] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1fe0] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x801c] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x457] EFI_BOOT_SERVICES->HandleProtocol
* [0xeaa] EFI_BOOT_SERVICES->HandleProtocol
* [0x1288] EFI_BOOT_SERVICES->HandleProtocol
* [0x193d] EFI_BOOT_SERVICES->HandleProtocol
* [0x427f] EFI_BOOT_SERVICES->HandleProtocol
* [0x7e08] EFI_BOOT_SERVICES->HandleProtocol
* [0xbabf] EFI_BOOT_SERVICES->HandleProtocol
* [0xc1f9] EFI_BOOT_SERVICES->HandleProtocol
* [0xc269] EFI_BOOT_SERVICES->HandleProtocol
* [0xc2fc] EFI_BOOT_SERVICES->HandleProtocol
* [0xc34c] EFI_BOOT_SERVICES->HandleProtocol
* [0x102c] EFI_BOOT_SERVICES->OpenProtocol
* [0x1088] EFI_BOOT_SERVICES->OpenProtocol
* [0x10e4] EFI_BOOT_SERVICES->OpenProtocol
* [0x1140] EFI_BOOT_SERVICES->OpenProtocol
* [0x1199] EFI_BOOT_SERVICES->OpenProtocol
* [0x11f2] EFI_BOOT_SERVICES->OpenProtocol
* [0x13ed] EFI_BOOT_SERVICES->OpenProtocol
* [0x1567] EFI_BOOT_SERVICES->OpenProtocol
* [0x172a] EFI_BOOT_SERVICES->OpenProtocol
* [0x178e] EFI_BOOT_SERVICES->OpenProtocol
* [0x17f2] EFI_BOOT_SERVICES->OpenProtocol
* [0x1856] EFI_BOOT_SERVICES->OpenProtocol
* [0x1ab0] EFI_BOOT_SERVICES->OpenProtocol
* [0x1b9b] EFI_BOOT_SERVICES->OpenProtocol
* [0x1bc7] EFI_BOOT_SERVICES->OpenProtocol
* [0x1c54] EFI_BOOT_SERVICES->OpenProtocol
* [0x1d39] EFI_BOOT_SERVICES->OpenProtocol
* [0x1d76] EFI_BOOT_SERVICES->OpenProtocol
* [0x1ebc] EFI_BOOT_SERVICES->OpenProtocol
* [0x1f10] EFI_BOOT_SERVICES->OpenProtocol
* [0x1f4e] EFI_BOOT_SERVICES->OpenProtocol
* [0x20e7] EFI_BOOT_SERVICES->OpenProtocol
* [0x7c6a] EFI_BOOT_SERVICES->OpenProtocol
* [0xc163] EFI_BOOT_SERVICES->OpenProtocol
* [0xc1af] EFI_BOOT_SERVICES->OpenProtocol
* [0x8fb] EFI_BOOT_SERVICES->CloseProtocol
* [0x938] EFI_BOOT_SERVICES->CloseProtocol
* [0x975] EFI_BOOT_SERVICES->CloseProtocol
* [0x9b2] EFI_BOOT_SERVICES->CloseProtocol
* [0x9ef] EFI_BOOT_SERVICES->CloseProtocol
* [0xa2c] EFI_BOOT_SERVICES->CloseProtocol
* [0xa71] EFI_BOOT_SERVICES->CloseProtocol
* [0xb89] EFI_BOOT_SERVICES->CloseProtocol
* [0xbcc] EFI_BOOT_SERVICES->CloseProtocol
* [0xc0f] EFI_BOOT_SERVICES->CloseProtocol
* [0xc52] EFI_BOOT_SERVICES->CloseProtocol
* [0xc95] EFI_BOOT_SERVICES->CloseProtocol
* [0xd8c] EFI_BOOT_SERVICES->CloseProtocol
* [0x7cf2] EFI_BOOT_SERVICES->CloseProtocol
* [0x6b9] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x6f7] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x735] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x76f] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x7a9] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x7f1] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x82f] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x869] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x8a3] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x77f5] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x7964] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x7fa7] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x9fef] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa07e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4bc] EFI_BOOT_SERVICES->LocateProtocol
* [0x4da] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f7] EFI_BOOT_SERVICES->LocateProtocol
* [0x514] EFI_BOOT_SERVICES->LocateProtocol
* [0x531] EFI_BOOT_SERVICES->LocateProtocol
* [0x4857] EFI_BOOT_SERVICES->LocateProtocol
* [0x48ed] EFI_BOOT_SERVICES->LocateProtocol
* [0x1379] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1a3c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xbddd] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x678] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xabf] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xdd9] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x7e8d] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x7ffd] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0xdfc0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0xdf70]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0xdf90]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0xdfa0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0xdfc0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0xdd20]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] B95E9FDA-26DE-48D2-88071F9107AC5E3A
* [0xdee0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiPxeBaseCodeCallbackProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 245DCA21-FB7B-11D3-8F0100A0C969723B
* [0xdf70]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0xdf90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 107A772C-D5E1-11D4-9A460090273FC14D
* [0xdfa0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 6A7A5CFF-E8D9-4F70-BADA75AB3025CE14
* [0xdfb0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0xdf10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAdapterInformationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E5DD1403-D622-C24E-8488C71B17F5E802
* [0xdde0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp4Config2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B446ED1-E30B-4FAA-871A3654ECA36080
* [0xde10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp6ConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 937FE521-95AE-4D1A-892948BCD90AD31A
* [0xdee0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPxeBaseCodeCallbackProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 245DCA21-FB7B-11D3-8F0100A0C969723B
* [0xdd80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xdfc0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] A19832B9-AC25-11D3-9A2D0090273FC14D
* [0xdfe0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F36FF770-A7E1-42CF-9ED256F0F271F44C
* [0xdfd0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 7AB33A91-ACE5-4326-B572E7EE33D39F16
* [0xde70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0xde50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 78247C57-63DB-4708-99C2A8B4A9A61F6B
* [0xde30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0xddb0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4B427BB-BA21-4F16-BC4E43E416AB619C
* [0xddd0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0xdd20]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] B95E9FDA-26DE-48D2-88071F9107AC5E3A
* [0xded0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0xdeb0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BF0A78BA-EC29-49CF-A1C97AE54EAB6A51
* [0xde90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0xde00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
* [0xdea0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D9760FF3-3CCA-4267-80F97527FAFA4223
* [0xdd80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xdd90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiNetworkInterfaceIdentifierProtocolGuid_31
	 - [protocol_place] edk2_guids
	 - [guid] 1ACED566-76ED-4218-BC81767F1F977A89
* [0xdf00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 56EC3091-954C-11D2-8E3F00A0C969723B
* [0xddb0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4B427BB-BA21-4F16-BC4E43E416AB619C
* [0xddd0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0xde30]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0xde50]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiMtftp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 78247C57-63DB-4708-99C2A8B4A9A61F6B
* [0xde70]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0xdd20]
	 - [service] CloseProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] B95E9FDA-26DE-48D2-88071F9107AC5E3A
* [0xde00]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
* [0xde90]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0xdeb0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiMtftp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BF0A78BA-EC29-49CF-A1C97AE54EAB6A51
* [0xded0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0xddb0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4B427BB-BA21-4F16-BC4E43E416AB619C
* [0xddd0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 41D94CD2-35B6-455A-8258D4E51334AADD
* [0xde30]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3AD9DF29-4501-478D-B1F87F7FE70E50F3
* [0xde70]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8A219718-4EF5-4761-91C8C0F04BDA9E56
* [0xde50]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiMtftp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 78247C57-63DB-4708-99C2A8B4A9A61F6B
* [0xde00]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2C8759D5-5C2D-66EF-925FB66C101957E2
* [0xde90]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4F948815-B4B9-43CB-8A3390E060B34955
* [0xded0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 87C8BAD7-0595-4053-8297DEDE395F5D5B
* [0xdeb0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiMtftp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] BF0A78BA-EC29-49CF-A1C97AE54EAB6A51
* [0xdf30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 0FD96974-23AA-4CDC-B9CB98D17750322A
* [0xdf50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] EF9FC172-A1B2-4693-B3276D32FC416042
* [0xdf60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 587E72D7-CC50-4F79-8209CA291FC1A10F
* [0xdf20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E9CA4775-8657-47FC-97E77ED65A084324
* [0xdf40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31A6406A-6BDF-4E46-B2A2EBAA89C40920
* [0xe000]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_POST_MANAGER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8A91B1E1-56C7-4ADC-ABEB1C2CA1729EFF
* [0xdf80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 9042A9DE-23DC-4A38-96FB7ADED080516A
* [0xdd80]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xdf70]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0xdf70]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 18A031AB-B443-4D1A-A5C00C09261E9F71
* [0xdd80]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
## Module: Uhcd
### Boot services:
* [0x79d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x84a] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x996] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x18f1] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7354] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7379] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7d39] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x983f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x9be9] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x9631] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x9c53] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xce3] EFI_BOOT_SERVICES->HandleProtocol
* [0x1bab] EFI_BOOT_SERVICES->HandleProtocol
* [0x4773] EFI_BOOT_SERVICES->HandleProtocol
* [0x7cd2] EFI_BOOT_SERVICES->HandleProtocol
* [0xaa9] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xb42] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xb7a7] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xda6] EFI_BOOT_SERVICES->OpenProtocol
* [0xe63] EFI_BOOT_SERVICES->OpenProtocol
* [0xed1] EFI_BOOT_SERVICES->OpenProtocol
* [0xf93] EFI_BOOT_SERVICES->OpenProtocol
* [0x11f2] EFI_BOOT_SERVICES->OpenProtocol
* [0x122f] EFI_BOOT_SERVICES->OpenProtocol
* [0x227f] EFI_BOOT_SERVICES->OpenProtocol
* [0x2378] EFI_BOOT_SERVICES->OpenProtocol
* [0x416a] EFI_BOOT_SERVICES->OpenProtocol
* [0x473a] EFI_BOOT_SERVICES->OpenProtocol
* [0x49d3] EFI_BOOT_SERVICES->OpenProtocol
* [0x4a51] EFI_BOOT_SERVICES->OpenProtocol
* [0x4c86] EFI_BOOT_SERVICES->OpenProtocol
* [0x4cc0] EFI_BOOT_SERVICES->OpenProtocol
* [0x8edb] EFI_BOOT_SERVICES->OpenProtocol
* [0x8f92] EFI_BOOT_SERVICES->OpenProtocol
* [0x909e] EFI_BOOT_SERVICES->OpenProtocol
* [0x9262] EFI_BOOT_SERVICES->OpenProtocol
* [0x9324] EFI_BOOT_SERVICES->OpenProtocol
* [0x94eb] EFI_BOOT_SERVICES->OpenProtocol
* [0x9521] EFI_BOOT_SERVICES->OpenProtocol
* [0x960a] EFI_BOOT_SERVICES->OpenProtocol
* [0x9c2f] EFI_BOOT_SERVICES->OpenProtocol
* [0xaaed] EFI_BOOT_SERVICES->OpenProtocol
* [0xab1f] EFI_BOOT_SERVICES->OpenProtocol
* [0xdeb] EFI_BOOT_SERVICES->CloseProtocol
* [0xe86] EFI_BOOT_SERVICES->CloseProtocol
* [0xf20] EFI_BOOT_SERVICES->CloseProtocol
* [0xfb5] EFI_BOOT_SERVICES->CloseProtocol
* [0x1016] EFI_BOOT_SERVICES->CloseProtocol
* [0x1156] EFI_BOOT_SERVICES->CloseProtocol
* [0x1174] EFI_BOOT_SERVICES->CloseProtocol
* [0x1326] EFI_BOOT_SERVICES->CloseProtocol
* [0x1349] EFI_BOOT_SERVICES->CloseProtocol
* [0x4322] EFI_BOOT_SERVICES->CloseProtocol
* [0x4a19] EFI_BOOT_SERVICES->CloseProtocol
* [0x4b65] EFI_BOOT_SERVICES->CloseProtocol
* [0x8efe] EFI_BOOT_SERVICES->CloseProtocol
* [0x9009] EFI_BOOT_SERVICES->CloseProtocol
* [0x904d] EFI_BOOT_SERVICES->CloseProtocol
* [0x90d4] EFI_BOOT_SERVICES->CloseProtocol
* [0x9285] EFI_BOOT_SERVICES->CloseProtocol
* [0x93cb] EFI_BOOT_SERVICES->CloseProtocol
* [0x96ce] EFI_BOOT_SERVICES->CloseProtocol
* [0xaf0] EFI_BOOT_SERVICES->LocateProtocol
* [0xb6d] EFI_BOOT_SERVICES->LocateProtocol
* [0xd09] EFI_BOOT_SERVICES->LocateProtocol
* [0x48e9] EFI_BOOT_SERVICES->LocateProtocol
* [0x4e59] EFI_BOOT_SERVICES->LocateProtocol
* [0xa1d9] EFI_BOOT_SERVICES->LocateProtocol
* [0xb548] EFI_BOOT_SERVICES->LocateProtocol
* [0xb99f] EFI_BOOT_SERVICES->LocateProtocol
* [0xa1e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4102] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4987] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x86db] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x916a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x921f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9408] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xaa91] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x12a0] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x4365] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x8766] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x969c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xab9b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
### Protocols:
* [0xbe90]
	 - [service] InstallProtocolInterface
	 - [protocol_name] USB_TIMING_POLICY_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 89E3C1DC-B5E3-4D34-AEADDD7EB2828C18
* [0xbf50]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8D59D32B-C655-4AE9-9B15F25904992A43
* [0xbf20]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31878C87-0B75-11D5-9A4F0090273FC14D
* [0xbec0]
	 - [service] HandleProtocol
	 - [protocol_name] EFI_NONSMMEMUL6064TRAP_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 68B81E51-2583-4582-95DBC5723236C4F1
* [0xbe80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xbee0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0xbe80]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xbf40]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiLegacyBiosPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 783658A3-4172-4421-A299E009079C0CB4
* [0xbe80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xbed0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xbe30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUsbHcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F5089266-1AA0-4953-97D8562F8A73B519
* [0xbe70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUsb2HcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3E745226-9818-45B6-A2ACD7CD0E8BA2BC
* [0xbee0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0xbef0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0xd118]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 1FEDE521-031C-4BC5-8050F3D6161E2E92
* [0xbf50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 8D59D32B-C655-4AE9-9B15F25904992A43
* [0xbf20]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 31878C87-0B75-11D5-9A4F0090273FC14D
* [0xbf00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
* [0xbe20]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DD9E7534-7762-4698-8C14F58517A625AA
* [0xbe80]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xbed0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 09576E91-6D3F-11D2-8E3900A0C969723B
* [0xbe70]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUsb2HcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 3E745226-9818-45B6-A2ACD7CD0E8BA2BC
* [0xbee0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0xbf40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 783658A3-4172-4421-A299E009079C0CB4
* [0xbec0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_NONSMMEMUL6064TRAP_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 68B81E51-2583-4582-95DBC5723236C4F1
* [0xbf70]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 9400D59B-0E9C-4F6C-B59AFC20009DB9EC
* [0xbe60]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_USB_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2AD8E2D2-2E91-4CD1-95F5E78FE5EBE316
* [0xbea0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmControl2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 843DC720-AB1E-42CB-93578A0078F3561B
* [0xbf60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] B295BD1C-63E3-48E3-B265F7DFA2070123
* [0xc4d8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] D2B2B828-0826-48A7-B3DF983C006024F0
* [0xbee0]
	 - [service] InstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0xbe30]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiUsbHcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F5089266-1AA0-4953-97D8562F8A73B519
* [0xbee0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0xbef0]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0xd118]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 1FEDE521-031C-4BC5-8050F3D6161E2E92
* [0xbf00]
	 - [service] UninstallMultipleProtocolInterfaces
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 387477C1-69C7-11D2-8E3900A0C969723B
## Module: UpdateMemoryRecord
### Boot services:
* [0x2f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x314] EFI_BOOT_SERVICES->LocateProtocol
* [0x33b] EFI_BOOT_SERVICES->LocateProtocol
* [0x358] EFI_BOOT_SERVICES->LocateProtocol
* [0x373] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xe00]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_SMBIOS_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5E90A50D-6955-4A49-9032DA3812F8E8E5
* [0xe10]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 67269263-0AF1-45DD-93C8299921D0E1E9
* [0xe20]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] D4D2F201-50E8-4D45-8E05FD49A82A1569
* [0xe30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbusHcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] E49D33ED-513D-4634-B6986F55AA751C1B
* [0xe40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] C6AA1F27-5597-4802-9F63D62836598635
## Module: UpdateSmbiosType41
### Boot services:
* [0x776] EFI_BOOT_SERVICES->HandleProtocol
* [0x735] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2b4] EFI_BOOT_SERVICES->LocateProtocol
* [0x2d1] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xaf0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 4CF5B200-68B8-4CA5-9EECB23E3F50029A
* [0xad0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_SMBIOS_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5E90A50D-6955-4A49-9032DA3812F8E8E5
* [0xae0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 67269263-0AF1-45DD-93C8299921D0E1E9
## Module: UsbInt13
### Boot services:
* [0x9db] EFI_BOOT_SERVICES->HandleProtocol
* [0xa1e] EFI_BOOT_SERVICES->HandleProtocol
* [0x9a3] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3d0] EFI_BOOT_SERVICES->LocateProtocol
* [0x4aa] EFI_BOOT_SERVICES->LocateProtocol
* [0x6b9] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x12e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 2B2F68D6-0CD2-44CF-8E8BBBA20B1B5B75
* [0x12f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x12f0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 964E5B21-6459-11D2-8E3900A0C969723B
* [0x12d0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_USB_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2AD8E2D2-2E91-4CD1-95F5E78FE5EBE316
* [0x12c0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_LEGACY_BIOS_EXT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 8E008510-9BB1-457D-9F70897ABA865DB9
* [0x12b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] DB9A1E3D-45CB-4ABB-853BE5387FDB2E2D
## Module: UsbPei
### Boot services:
* [0x52c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7b7] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xac4] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xcb7] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xdfe] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xf5f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1018] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x546] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x7ce] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xc1b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xcd2] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xe1f] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xf7d] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1035] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x105d] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x5e5d] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x5eec] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x5f3b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x5f8a] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x5fd3] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x601d] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6094] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x60c0] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6327] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x63e5] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x63f2] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6468] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x64b6] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x64c3] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x65ff] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x66c3] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6735] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6879] EFI_BOOT_SERVICES->UninstallProtocolInterface
### Protocols:
* empty
## Module: UsbRtDxe
### Boot services:
* [0x3e0] EFI_BOOT_SERVICES->LocateProtocol
* [0x17c9b] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x18020]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_USB_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2AD8E2D2-2E91-4CD1-95F5E78FE5EBE316
## Module: UsbRtSmm
### Boot services:
* [0x215b] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x22bc] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2471] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x532f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x176b9] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x55a6] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x567b] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xfb9] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x56d3] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x57ee] EFI_BOOT_SERVICES->OpenProtocol
* [0x55d1] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x354] EFI_BOOT_SERVICES->LocateProtocol
* [0xd3b] EFI_BOOT_SERVICES->LocateProtocol
* [0xddf] EFI_BOOT_SERVICES->LocateProtocol
* [0x198d1] EFI_BOOT_SERVICES->LocateProtocol
* [0x199b9] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a5ef] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a807] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1ad10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1b298]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x1aca0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_USB_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2AD8E2D2-2E91-4CD1-95F5E78FE5EBE316
* [0x1ad40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
* [0x1ad70]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_USB_POLICY_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 5859CB76-6BEF-468A-BE2DB3DD1A27F012
## Module: UsbS5Wakeup
### Boot services:
* [0x8f7] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xebe] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x334] EFI_BOOT_SERVICES->LocateProtocol
* [0x109b] EFI_BOOT_SERVICES->LocateProtocol
* [0x112f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1459] EFI_BOOT_SERVICES->LocateProtocol
* [0x1541] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x21f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x2718]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] F4CCBFB7-F6E0-47FD-9DD410A8F150C191
* [0x21c0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_USB_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 2AD8E2D2-2E91-4CD1-95F5E78FE5EBE316
* [0x2220]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] 36232936-0E76-31C8-A13A3AF2FC1C3932
## Module: UsbTypeCDxe
### Boot services:
* [0x48a] EFI_BOOT_SERVICES->HandleProtocol
* [0x4c8] EFI_BOOT_SERVICES->HandleProtocol
* [0x34d] EFI_BOOT_SERVICES->LocateProtocol
* [0x389] EFI_BOOT_SERVICES->LocateProtocol
* [0x457] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x620]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 5B1B31A1-9562-11D2-8E3F00A0C969723B
* [0x630]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 220E73B6-6BDB-4413-8405B974B108619A
* [0x5f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] FFE06BDD-6107-46A6-7BB25A9C7EC5275C
* [0x600]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_GLOBAL_NVS_AREA_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 074E1E48-8132-47A1-8C2C3F14AD9A66DC
* [0x610]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: WdtAppDxe
### Boot services:
* [0x3c2] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2f8] EFI_BOOT_SERVICES->LocateProtocol
* [0x408] EFI_BOOT_SERVICES->LocateProtocol
* [0x4d1] EFI_BOOT_SERVICES->LocateProtocol
* [0x53b] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x5b0]
	 - [service] LocateProtocol
	 - [protocol_name] WDT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B42B8D12-2ACB-499A-A920DD5BE6CF09B1
* [0x5d0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] 11B34006-D85B-4D0A-A290D5A571310EF7
## Module: WdtDxe
### Boot services:
* [0x33a] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x35d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x39a] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3bc] EFI_BOOT_SERVICES->UninstallProtocolInterface
### Protocols:
* [0x700]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] WDT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] B42B8D12-2ACB-499A-A920DD5BE6CF09B1
* [0x710]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] PCH_RESET_CALLBACK_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] 3A3300AB-C929-487D-AB34159BC13562C0
