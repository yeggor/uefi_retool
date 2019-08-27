## Module: AcpiPlatformFeatures
### Boot services:
* [0xc6b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xcda] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xe1c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x706] EFI_BOOT_SERVICES->HandleProtocol
* [0xe51] EFI_BOOT_SERVICES->HandleProtocol
* [0x31b] EFI_BOOT_SERVICES->LocateProtocol
* [0x428] EFI_BOOT_SERVICES->LocateProtocol
* [0x841] EFI_BOOT_SERVICES->LocateProtocol
* [0xdf2] EFI_BOOT_SERVICES->LocateProtocol
* [0xfd7] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1300]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x1320]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGlobalNvsAreaProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x74e1e48, 0x8132, 0x47a1, 0x8c, 0x2c, 0x3f, 0x14, 0xad, 0x9a, 0x66, 0xdc]
* [0x1310]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_PLATFORM_INFO_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0xd9035175, 0x8ce2, 0x47de, 0xa8, 0xb8, 0xcc, 0x98, 0xe5, 0xe2, 0xa8, 0x85]
* [0x12f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
* [0x1330]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
## Module: AcpiS3SaveDxe
### Boot services:
* [0x3b0] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* empty
## Module: AcpiSmm
### Boot services:
* [0x34c] EFI_BOOT_SERVICES->LocateProtocol
* [0x37a] EFI_BOOT_SERVICES->LocateProtocol
* [0x4ea] EFI_BOOT_SERVICES->LocateProtocol
* [0x514] EFI_BOOT_SERVICES->LocateProtocol
* [0x53e] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x900]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x8b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGlobalNvsAreaProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x74e1e48, 0x8132, 0x47a1, 0x8c, 0x2c, 0x3f, 0x14, 0xad, 0x9a, 0x66, 0xdc]
## Module: ActiveBios
### Boot services:
* [0x30e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: ActiveManagement
### Boot services:
* [0x3c4] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x379] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xa40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x45de9920, 0xcd54, 0x446a, 0xa0, 0x3c, 0x22, 0xe6, 0xfb, 0xb4, 0x51, 0xe4]
## Module: Ahci
### Boot services:
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
* [0x11b0] EFI_BOOT_SERVICES->OpenProtocol
* [0x1222] EFI_BOOT_SERVICES->OpenProtocol
* [0x12d2] EFI_BOOT_SERVICES->OpenProtocol
* [0x1325] EFI_BOOT_SERVICES->OpenProtocol
* [0x1421] EFI_BOOT_SERVICES->OpenProtocol
* [0x1466] EFI_BOOT_SERVICES->OpenProtocol
* [0x14ab] EFI_BOOT_SERVICES->OpenProtocol
* [0x14f6] EFI_BOOT_SERVICES->OpenProtocol
* [0x17d7] EFI_BOOT_SERVICES->OpenProtocol
* [0x1800] EFI_BOOT_SERVICES->OpenProtocol
* [0x3a6d] EFI_BOOT_SERVICES->OpenProtocol
* [0x6cef] EFI_BOOT_SERVICES->OpenProtocol
* [0x6dfb] EFI_BOOT_SERVICES->OpenProtocol
* [0x9f7] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x17a4] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xa15] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xb49] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x19c1] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1c75] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x12f9] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x134c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x136e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x346] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xdeb] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xe73] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xeb8] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9d7] EFI_BOOT_SERVICES->HandleProtocol
* [0xa4d] EFI_BOOT_SERVICES->HandleProtocol
* [0xa77] EFI_BOOT_SERVICES->HandleProtocol
* [0x1036] EFI_BOOT_SERVICES->HandleProtocol
* [0x69a] EFI_BOOT_SERVICES->LocateProtocol
* [0x950] EFI_BOOT_SERVICES->LocateProtocol
* [0x98b] EFI_BOOT_SERVICES->LocateProtocol
* [0xf1d] EFI_BOOT_SERVICES->LocateProtocol
* [0xf44] EFI_BOOT_SERVICES->LocateProtocol
* [0xf6b] EFI_BOOT_SERVICES->LocateProtocol
* [0xf92] EFI_BOOT_SERVICES->LocateProtocol
* [0x1069] EFI_BOOT_SERVICES->LocateProtocol
* [0x1714] EFI_BOOT_SERVICES->LocateProtocol
* [0x1750] EFI_BOOT_SERVICES->LocateProtocol
* [0x6ec8] EFI_BOOT_SERVICES->LocateProtocol
* [0x6d7d] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x403] EFI_BOOT_SERVICES->CloseProtocol
* [0x4fc] EFI_BOOT_SERVICES->CloseProtocol
* [0x76f] EFI_BOOT_SERVICES->CloseProtocol
* [0x11f4] EFI_BOOT_SERVICES->CloseProtocol
* [0x16f7] EFI_BOOT_SERVICES->CloseProtocol
* [0x1788] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x78d0]
	 - [service] HandleProtocol
	 - [protocol_name] ONBOARD_RAID_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0x5d206dd3, 0x516a, 0x47dc, 0xa1, 0xbc, 0x6d, 0xa2, 0x4, 0xaa, 0xbe, 0x8]
* [0x78e0]
	 - [service] HandleProtocol
	 - [protocol_name] HDD_UNLOCKED_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0x1fd29be6, 0x70d0, 0x42a4, 0xa6, 0xe7, 0xe5, 0xd1, 0xe, 0x6a, 0xc3, 0x76]
* [0x72a0]
	 - [service] HandleProtocol
	 - [protocol_name] IDE_SECURITY_INTERFACE_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0xf4f63529, 0x281e, 0x4040, 0xa3, 0x13, 0xc1, 0xd6, 0x76, 0x63, 0x84, 0xbe]
* [0x7270]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x17706d27, 0x83fe, 0x4770, 0x87, 0x5f, 0x4c, 0xef, 0x4c, 0xb8, 0xf6, 0x3d]
* [0x7300]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6734411, 0x2dda, 0x4632, 0xa5, 0x92, 0x92, 0xf, 0x24, 0xd6, 0xed, 0x21]
* [0x7310]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xfc50878, 0x1633, 0x432a, 0xbd, 0xe4, 0x84, 0x13, 0x57, 0xfc, 0x15, 0xe9]
* [0x72b0]
	 - [service] LocateProtocol
	 - [protocol_name] HDD_SECURITY_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0xce6f86bb, 0xb800, 0x4c71, 0xb2, 0xd1, 0x38, 0x97, 0xa3, 0xbc, 0x1d, 0xae]
* [0x72f0]
	 - [service] LocateProtocol
	 - [protocol_name] OPAL_SEC_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0x59af16b0, 0x661d, 0x4865, 0xa3, 0x81, 0x38, 0xde, 0x68, 0x38, 0x5d, 0x8d]
* [0x72e0]
	 - [service] LocateProtocol
	 - [protocol_name] HDD_SMART_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0x9401bd4f, 0x1a00, 0x4990, 0xab, 0x56, 0xda, 0xf0, 0xe4, 0xe3, 0x48, 0xde]
* [0x78b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x10e9d800, 0x53b7, 0x4845, 0x9d, 0xff, 0x30, 0xd1, 0x8a, 0x95, 0x6d, 0x53]
* [0x78f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x734aa01d, 0x95ec, 0x45b7, 0xa2, 0x3a, 0x2d, 0x86, 0xd8, 0xfd, 0xeb, 0xb6]
* [0x7838]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
## Module: AhciSmm
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x19db] EFI_BOOT_SERVICES->LocateProtocol
* [0x1abb] EFI_BOOT_SERVICES->LocateProtocol
* [0x1c61] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x24f8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2010]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: Aint13
### Boot services:
* [0x2fd] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x355] EFI_BOOT_SERVICES->HandleProtocol
* [0xedd] EFI_BOOT_SERVICES->LocateProtocol
* [0xf03] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1490]
	 - [service] HandleProtocol
	 - [protocol_name] AHCI_BUS_INIT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0xb2fa4764, 0x3b6e, 0x43d3, 0x91, 0xdf, 0x87, 0xd1, 0x5a, 0x3e, 0x56, 0x68]
* [0x14a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x14b0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_LEGACY_BIOS_EXT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0x8e008510, 0x9bb1, 0x457d, 0x9f, 0x70, 0x89, 0x7a, 0xba, 0x86, 0x5d, 0xb9]
## Module: AlertStandardFormatDxe
### Boot services:
* [0x5e4] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2e2] EFI_BOOT_SERVICES->LocateProtocol
* [0x3f9] EFI_BOOT_SERVICES->LocateProtocol
* [0x64e] EFI_BOOT_SERVICES->LocateProtocol
* [0x6a4] EFI_BOOT_SERVICES->LocateProtocol
* [0x756] EFI_BOOT_SERVICES->LocateProtocol
* [0xa84] EFI_BOOT_SERVICES->LocateProtocol
* [0xb0a] EFI_BOOT_SERVICES->LocateProtocol
* [0xe3b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1251] EFI_BOOT_SERVICES->LocateProtocol
* [0x13a7] EFI_BOOT_SERVICES->LocateProtocol
* [0x1519] EFI_BOOT_SERVICES->LocateProtocol
* [0x960] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x16a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
* [0x16b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDataHubProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xae80d021, 0x618e, 0x11d4, 0xbc, 0xd7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
* [0x16c0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x16d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6725e645, 0x4a7f, 0x9969, 0x82, 0xec, 0xd1, 0x87, 0x21, 0xde, 0x5a, 0x57]
* [0x1700]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xeb97088e, 0xcfdf, 0x49c6, 0xbe, 0x4b, 0xd9, 0x6, 0xa5, 0xb2, 0xe, 0x86]
* [0x16f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xa0b5dc52, 0x4f34, 0x3990, 0xd4, 0x91, 0x10, 0x8b, 0xe8, 0xba, 0x75, 0x42]
* [0x1660]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiConsoleOutDeviceGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd3b36f2c, 0xd551, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
## Module: AmiBoardInfo2
### Boot services:
* [0x5c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4b5] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x60d] EFI_BOOT_SERVICES->HandleProtocol
* [0x351] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x950]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0xec8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x4fc0733f, 0x6fd2, 0x491b, 0xa8, 0x90, 0x53, 0x74, 0x52, 0x1b, 0xf4, 0x8f]
## Module: AmiCpuFeaturesDxe
### Boot services:
* empty
### Protocols:
* empty
## Module: AmiDeviceGuardApi
### Boot services:
* [0x7fd] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x325] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x6ea] EFI_BOOT_SERVICES->HandleProtocol
* [0x717] EFI_BOOT_SERVICES->HandleProtocol
* [0xbfd] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x10f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x10e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x1100]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_DIGITAL_SIGNATURE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0x5f87ba17, 0x957d, 0x433d, 0x9e, 0x15, 0xc0, 0xe7, 0xc8, 0x79, 0x88, 0x99]
## Module: AmiHsti
### Boot services:
* [0xbad] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5af] EFI_BOOT_SERVICES->OpenProtocol
* [0x74e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xbfe] EFI_BOOT_SERVICES->HandleProtocol
* [0x370] EFI_BOOT_SERVICES->LocateProtocol
* [0x38e] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c8] EFI_BOOT_SERVICES->LocateProtocol
* [0x3e5] EFI_BOOT_SERVICES->LocateProtocol
* [0x5d0] EFI_BOOT_SERVICES->LocateProtocol
* [0x92b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1101] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f56] EFI_BOOT_SERVICES->LocateProtocol
* [0x228f] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x45f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAdapterInformationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe5dd1403, 0xd622, 0xc24e, 0x84, 0x88, 0xc7, 0x1b, 0x17, 0xf5, 0xe8, 0x2]
* [0x4640]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x4650]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x4610]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x4630]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
* [0x4cb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x4600]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_DIGITAL_SIGNATURE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0x5f87ba17, 0x957d, 0x433d, 0x9e, 0x15, 0xc0, 0xe7, 0xc8, 0x79, 0x88, 0x99]
* [0x4c60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
## Module: AmiMemoryInfoConfig
### Boot services:
* [0x55c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x3b7] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x780]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6aa1f27, 0x5597, 0x4802, 0x9f, 0x63, 0xd6, 0x28, 0x36, 0x59, 0x86, 0x35]
## Module: AmiRedFishApi
### Boot services:
* [0x96e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x325] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x856] EFI_BOOT_SERVICES->HandleProtocol
* [0x888] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* [0xc80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc70]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
## Module: AmiTbtInfo
### Boot services:
* [0x5c2] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x33c] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* empty
## Module: AmiTcgNvflagSample
### Boot services:
* [0x38a] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2f2] EFI_BOOT_SERVICES->LocateProtocol
* [0x321] EFI_BOOT_SERVICES->LocateProtocol
* [0x3d4] EFI_BOOT_SERVICES->LocateProtocol
* [0x403] EFI_BOOT_SERVICES->LocateProtocol
* [0x588] EFI_BOOT_SERVICES->LocateProtocol
* [0x5b7] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x8b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTpmMpDriverProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xde161cfe, 0x1e60, 0x42a1, 0x8c, 0xc3, 0xee, 0x7e, 0xf0, 0x73, 0x52, 0x12]
* [0x8a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf541796d, 0xa62e, 0x4954, 0xa7, 0x75, 0x95, 0x84, 0xf6, 0x1b, 0x9c, 0xdd]
## Module: AmiTcgPlatformDxe
### Boot services:
* [0xaed] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x433] EFI_BOOT_SERVICES->OpenProtocol
* [0x3ea] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xb2a] EFI_BOOT_SERVICES->HandleProtocol
* [0x1c07] EFI_BOOT_SERVICES->HandleProtocol
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
* [0x1010] EFI_BOOT_SERVICES->LocateProtocol
* [0x112c] EFI_BOOT_SERVICES->LocateProtocol
* [0x13f2] EFI_BOOT_SERVICES->LocateProtocol
* [0x1606] EFI_BOOT_SERVICES->LocateProtocol
* [0x16e5] EFI_BOOT_SERVICES->LocateProtocol
* [0x18c8] EFI_BOOT_SERVICES->LocateProtocol
* [0x19ef] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a11] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a45] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ae7] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b75] EFI_BOOT_SERVICES->LocateProtocol
* [0x1c9d] EFI_BOOT_SERVICES->LocateProtocol
* [0x1dfb] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e25] EFI_BOOT_SERVICES->LocateProtocol
* [0x2691] EFI_BOOT_SERVICES->LocateProtocol
* [0x28b0] EFI_BOOT_SERVICES->LocateProtocol
* [0x297d] EFI_BOOT_SERVICES->LocateProtocol
* [0x29ac] EFI_BOOT_SERVICES->LocateProtocol
* [0x29d0] EFI_BOOT_SERVICES->LocateProtocol
* [0x29f7] EFI_BOOT_SERVICES->LocateProtocol
* [0x3030] EFI_BOOT_SERVICES->LocateProtocol
* [0x37fd] EFI_BOOT_SERVICES->LocateProtocol
* [0x384b] EFI_BOOT_SERVICES->LocateProtocol
* [0x38a2] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b75] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c01] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c30] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c57] EFI_BOOT_SERVICES->LocateProtocol
* [0x3dd7] EFI_BOOT_SERVICES->LocateProtocol
* [0x3dfb] EFI_BOOT_SERVICES->LocateProtocol
* [0x4297] EFI_BOOT_SERVICES->LocateProtocol
* [0x5923] EFI_BOOT_SERVICES->LocateProtocol
* [0xf3e] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1d02] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x291a] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x416f] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x41ef] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x5f90]
	 - [service] HandleProtocol
	 - [protocol_name] OPROM_START_END_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0xf2a128ff, 0x257b, 0x456e, 0x9d, 0xe8, 0x63, 0xe7, 0xc7, 0xdc, 0xdf, 0xac]
* [0x6020]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x6030]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x5ff0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x5f40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf541796d, 0xa62e, 0x4954, 0xa7, 0x75, 0x95, 0x84, 0xf6, 0x1b, 0x9c, 0xdd]
* [0x5e80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5cf308b5, 0xfa23, 0x4100, 0x8a, 0x76, 0xf3, 0x26, 0xc2, 0x81, 0x48, 0x80]
* [0x5ea0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6da670e8, 0x3d73, 0x4eb2, 0xa7, 0x21, 0xa2, 0xdd, 0xf6, 0x82, 0xfd, 0xd8]
* [0x5e90]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x9c53ce0e, 0xe9f, 0x4f20, 0xb1, 0xa1, 0x15, 0xe, 0x43, 0x49, 0xd7, 0x77]
* [0x5eb0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xa4524a9c, 0xb5e, 0x492d, 0xae, 0xc9, 0x30, 0x86, 0x31, 0xb1, 0x89, 0xb4]
* [0x5ec0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x76f3992d, 0x529e, 0x4efe, 0x8b, 0xbe, 0x8e, 0x1e, 0xd4, 0x32, 0xc2, 0x23]
* [0x5fc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTpmMpDriverProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xde161cfe, 0x1e60, 0x42a1, 0x8c, 0xc3, 0xee, 0x7e, 0xf0, 0x73, 0x52, 0x12]
* [0x5fa0]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
* [0x5f70]
	 - [service] LocateProtocol
	 - [protocol_name] TCG_PLATFORM_SETUP_POLICY_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0xbb6cbeff, 0xe072, 0x40d2, 0xa6, 0xeb, 0xba, 0xb7, 0x5b, 0xde, 0x87, 0xe7]
* [0x5fd0]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_POST_MANAGER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0x5ed0]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_BIOSPPI_FLAGS_MANAGEMENT_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0xe9008d70, 0x2a4e, 0x47ea, 0x8e, 0xc4, 0x72, 0xe2, 0x57, 0x67, 0xe5, 0xef]
* [0x5fe0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
* [0x5f60]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiResetArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x27cfac88, 0x46cc, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x5f90]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] OPROM_START_END_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0xf2a128ff, 0x257b, 0x456e, 0x9d, 0xe8, 0x63, 0xe7, 0xc7, 0xdc, 0xdf, 0xac]
* [0x5fa0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
## Module: AMITSE
### Boot services:
* [0x4409] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x7a16] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8c19] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x9fa1] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa10f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa62f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x16cce] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x19da4] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a1ab] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a28e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a800] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1b008] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2a928] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2c392] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2c572] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2ce76] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2fbc5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2fdfd] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x30def] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x30f16] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x31295] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x314fe] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x31618] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6da] EFI_BOOT_SERVICES->OpenProtocol
* [0x3484] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2e8b8] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x346c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x29ab1] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2af13] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2af4d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2e8a0] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2e96c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xa83e] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x2a7be] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x2a964] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x33f86] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x7fd] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x839] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1badf] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x4ba7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4bee] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4c1d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4c4c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x308e6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x318b3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3408] EFI_BOOT_SERVICES->HandleProtocol
* [0x4435] EFI_BOOT_SERVICES->HandleProtocol
* [0x7a55] EFI_BOOT_SERVICES->HandleProtocol
* [0x8c67] EFI_BOOT_SERVICES->HandleProtocol
* [0x9b3c] EFI_BOOT_SERVICES->HandleProtocol
* [0x9c4b] EFI_BOOT_SERVICES->HandleProtocol
* [0x9cbb] EFI_BOOT_SERVICES->HandleProtocol
* [0x9fdd] EFI_BOOT_SERVICES->HandleProtocol
* [0xa01a] EFI_BOOT_SERVICES->HandleProtocol
* [0xa673] EFI_BOOT_SERVICES->HandleProtocol
* [0xa8f5] EFI_BOOT_SERVICES->HandleProtocol
* [0xad3a] EFI_BOOT_SERVICES->HandleProtocol
* [0xbb2b] EFI_BOOT_SERVICES->HandleProtocol
* [0x1050e] EFI_BOOT_SERVICES->HandleProtocol
* [0x16d42] EFI_BOOT_SERVICES->HandleProtocol
* [0x181b3] EFI_BOOT_SERVICES->HandleProtocol
* [0x18716] EFI_BOOT_SERVICES->HandleProtocol
* [0x19338] EFI_BOOT_SERVICES->HandleProtocol
* [0x19de7] EFI_BOOT_SERVICES->HandleProtocol
* [0x19e72] EFI_BOOT_SERVICES->HandleProtocol
* [0x19ff1] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a202] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a468] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a842] EFI_BOOT_SERVICES->HandleProtocol
* [0x1b02f] EFI_BOOT_SERVICES->HandleProtocol
* [0x1f0c7] EFI_BOOT_SERVICES->HandleProtocol
* [0x20794] EFI_BOOT_SERVICES->HandleProtocol
* [0x26257] EFI_BOOT_SERVICES->HandleProtocol
* [0x2aba0] EFI_BOOT_SERVICES->HandleProtocol
* [0x2c3dd] EFI_BOOT_SERVICES->HandleProtocol
* [0x2c450] EFI_BOOT_SERVICES->HandleProtocol
* [0x2c514] EFI_BOOT_SERVICES->HandleProtocol
* [0x2c5a6] EFI_BOOT_SERVICES->HandleProtocol
* [0x2cedb] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d678] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fc0b] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fe49] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fec9] EFI_BOOT_SERVICES->HandleProtocol
* [0x2ff36] EFI_BOOT_SERVICES->HandleProtocol
* [0x30db6] EFI_BOOT_SERVICES->HandleProtocol
* [0x30e21] EFI_BOOT_SERVICES->HandleProtocol
* [0x30f48] EFI_BOOT_SERVICES->HandleProtocol
* [0x312d2] EFI_BOOT_SERVICES->HandleProtocol
* [0x3153b] EFI_BOOT_SERVICES->HandleProtocol
* [0x31655] EFI_BOOT_SERVICES->HandleProtocol
* [0x32350] EFI_BOOT_SERVICES->HandleProtocol
* [0x3238c] EFI_BOOT_SERVICES->HandleProtocol
* [0x3246c] EFI_BOOT_SERVICES->HandleProtocol
* [0x3252a] EFI_BOOT_SERVICES->HandleProtocol
* [0x326be] EFI_BOOT_SERVICES->HandleProtocol
* [0x3271e] EFI_BOOT_SERVICES->HandleProtocol
* [0x3404f] EFI_BOOT_SERVICES->HandleProtocol
* [0x340d7] EFI_BOOT_SERVICES->HandleProtocol
* [0x389b0] EFI_BOOT_SERVICES->HandleProtocol
* [0x392fb] EFI_BOOT_SERVICES->HandleProtocol
* [0x3c520] EFI_BOOT_SERVICES->HandleProtocol
* [0x6fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x4457] EFI_BOOT_SERVICES->LocateProtocol
* [0x4a14] EFI_BOOT_SERVICES->LocateProtocol
* [0x9840] EFI_BOOT_SERVICES->LocateProtocol
* [0xac68] EFI_BOOT_SERVICES->LocateProtocol
* [0xc7aa] EFI_BOOT_SERVICES->LocateProtocol
* [0x16c8e] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ac13] EFI_BOOT_SERVICES->LocateProtocol
* [0x1bab9] EFI_BOOT_SERVICES->LocateProtocol
* [0x1bebb] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f113] EFI_BOOT_SERVICES->LocateProtocol
* [0x202e3] EFI_BOOT_SERVICES->LocateProtocol
* [0x204b9] EFI_BOOT_SERVICES->LocateProtocol
* [0x27614] EFI_BOOT_SERVICES->LocateProtocol
* [0x29acc] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ac17] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ad3a] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ada6] EFI_BOOT_SERVICES->LocateProtocol
* [0x2aeb9] EFI_BOOT_SERVICES->LocateProtocol
* [0x2af73] EFI_BOOT_SERVICES->LocateProtocol
* [0x2affb] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b0b8] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b1f5] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b33b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b364] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b389] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b3ba] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b51c] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b53a] EFI_BOOT_SERVICES->LocateProtocol
* [0x2c6ae] EFI_BOOT_SERVICES->LocateProtocol
* [0x2c763] EFI_BOOT_SERVICES->LocateProtocol
* [0x2c9e1] EFI_BOOT_SERVICES->LocateProtocol
* [0x2cd3b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e103] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e364] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e419] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e563] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e623] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e713] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e74e] EFI_BOOT_SERVICES->LocateProtocol
* [0x2eae8] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ebc8] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f31d] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f493] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f4fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x2fd38] EFI_BOOT_SERVICES->LocateProtocol
* [0x3028f] EFI_BOOT_SERVICES->LocateProtocol
* [0x30435] EFI_BOOT_SERVICES->LocateProtocol
* [0x306ef] EFI_BOOT_SERVICES->LocateProtocol
* [0x30728] EFI_BOOT_SERVICES->LocateProtocol
* [0x307d3] EFI_BOOT_SERVICES->LocateProtocol
* [0x308a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x30d0e] EFI_BOOT_SERVICES->LocateProtocol
* [0x30d71] EFI_BOOT_SERVICES->LocateProtocol
* [0x30ec5] EFI_BOOT_SERVICES->LocateProtocol
* [0x30fc7] EFI_BOOT_SERVICES->LocateProtocol
* [0x310c5] EFI_BOOT_SERVICES->LocateProtocol
* [0x3115e] EFI_BOOT_SERVICES->LocateProtocol
* [0x311ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x311fc] EFI_BOOT_SERVICES->LocateProtocol
* [0x313ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x313d6] EFI_BOOT_SERVICES->LocateProtocol
* [0x31f86] EFI_BOOT_SERVICES->LocateProtocol
* [0x320fb] EFI_BOOT_SERVICES->LocateProtocol
* [0x331f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x3352f] EFI_BOOT_SERVICES->LocateProtocol
* [0x338e2] EFI_BOOT_SERVICES->LocateProtocol
* [0x33a5f] EFI_BOOT_SERVICES->LocateProtocol
* [0x33bbe] EFI_BOOT_SERVICES->LocateProtocol
* [0x33bff] EFI_BOOT_SERVICES->LocateProtocol
* [0x33ebc] EFI_BOOT_SERVICES->LocateProtocol
* [0x40be6] EFI_BOOT_SERVICES->LocateProtocol
* [0xa8b5] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2a804] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2a9a8] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x33fed] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x3c29] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3c8a] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3cea] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x958c] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x95d8] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xc175] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2e470] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2e7f8] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2e84d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3037e] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x30955] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x48c10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x48af0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x48b20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x48c50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2b2f68d6, 0xcd2, 0x44cf, 0x8e, 0x8b, 0xbb, 0xa2, 0xb, 0x1b, 0x5b, 0x75]
* [0x48ae0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4b068]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x48aa0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x48ad0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiOEMBadgingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x170e13c0, 0xbf1b, 0x4218, 0x87, 0x1d, 0x2a, 0xbd, 0xc6, 0xf8, 0x87, 0xbc]
* [0x4a5d8]
	 - [service] HandleProtocol
	 - [protocol_name] AMI_EFIKEYCODE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0xadfb62d, 0xff74, 0x484c, 0x89, 0x44, 0xf8, 0x5c, 0x4b, 0xea, 0x87, 0xa8]
* [0x49bd8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdd9e7534, 0x7762, 0x4698, 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa]
* [0x49948]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x49968]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x49a58]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x48c30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x48b00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x48b30]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_POST_MANAGER_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0x48be0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb9d4c360, 0xbcfb, 0x4f9b, 0x92, 0x98, 0x53, 0xc1, 0x36, 0x98, 0x22, 0x58]
* [0x4af30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDevicePathToTextProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8b843e20, 0x8132, 0x4852, 0x90, 0xcc, 0x55, 0x1a, 0x4e, 0x4a, 0x7f, 0x1c]
* [0x48ab0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiUnicodeCollation2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa4c751fc, 0x23ae, 0x4c3e, 0x92, 0xe9, 0x49, 0x64, 0xcf, 0x63, 0xf3, 0x49]
* [0x4a120]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x96fd60f3, 0xbc8, 0x4a11, 0x84, 0xf1, 0x2e, 0xb1, 0xcb, 0x5b, 0xa5, 0xa3]
* [0x4a130]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x96fd60f3, 0xbc8, 0x4a11, 0x84, 0xf1, 0x2e, 0xb1, 0xcb, 0x5b, 0xa5, 0xa3]
* [0x48c40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x48bb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x48bc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x48bd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x49c68]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_LEGACY_BIOS_EXT_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0x8e008510, 0x9bb1, 0x457d, 0x9f, 0x70, 0x89, 0x7a, 0xba, 0x86, 0x5d, 0xb9]
* [0x48b80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x919383de, 0xebac, 0x4924, 0x1, 0x94, 0x52, 0x59, 0xe0, 0xd, 0x65, 0x7a]
* [0x48b60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x45de9920, 0xcd54, 0x446a, 0xa0, 0x3c, 0x22, 0xe6, 0xfb, 0xb4, 0x51, 0xe4]
* [0x48a90]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CONSOLE_CONTROL_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] [0xf42f7782, 0x12e, 0x4c12, 0x99, 0x56, 0x49, 0xf9, 0x43, 0x4, 0xf7, 0x21]
* [0x48b90]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6725e645, 0x4a7f, 0x9969, 0x82, 0xec, 0xd1, 0x87, 0x21, 0xde, 0x5a, 0x57]
* [0x48b70]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x48bf0]
	 - [service] LocateProtocol
	 - [protocol_name] AMI_DIGITAL_SIGNATURE_PROTOCOL_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0x5f87ba17, 0x957d, 0x433d, 0x9e, 0x15, 0xc0, 0xe7, 0xc8, 0x79, 0x88, 0x99]
* [0x48c00]
	 - [service] LocateProtocol
	 - [protocol_name] TCG_PLATFORM_SETUP_POLICY_GUID
	 - [protocol_place] ami_guids
	 - [guid] [0xbb6cbeff, 0xe072, 0x40d2, 0xa6, 0xeb, 0xba, 0xb7, 0x5b, 0xde, 0x87, 0xe7]
* [0x49a08]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x49a28]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x49a38]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb9d4c360, 0xbcfb, 0x4f9b, 0x92, 0x98, 0x53, 0xc1, 0x36, 0x98, 0x22, 0x58]
* [0x49998]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x48c30]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x4a100]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x1172381f, 0x7ae6, 0x4652, 0x8d, 0x85, 0xb6, 0x51, 0x69, 0x7b, 0xe3, 0xcf]
* [0x4a110]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd3431c06, 0x2b4c, 0x4337, 0x93, 0x34, 0xff, 0xd9, 0xc0, 0x55, 0x15, 0x21]
* [0x48b10]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c1, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
