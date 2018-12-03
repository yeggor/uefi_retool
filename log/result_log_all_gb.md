## Module: Acoustic
### Boot services:
* [0x32a] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* [0xee8]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x10e9d800, 0x53b7, 0x4845, 0x9d, 0xff, 0x30, 0xd1, 0x8a, 0x95, 0x6d, 0x53]
## Module: ACPI
### Boot services:
* [0xb47] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1fdb] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2222] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5a39] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6073] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xfe3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x203d] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x20d0] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xb7e] EFI_BOOT_SERVICES->HandleProtocol
* [0x2027] EFI_BOOT_SERVICES->HandleProtocol
* [0x2263] EFI_BOOT_SERVICES->HandleProtocol
* [0x5a7e] EFI_BOOT_SERVICES->HandleProtocol
* [0xe05] EFI_BOOT_SERVICES->LocateProtocol
* [0x17ed] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b89] EFI_BOOT_SERVICES->LocateProtocol
* [0x3370] EFI_BOOT_SERVICES->LocateProtocol
* [0x393b] EFI_BOOT_SERVICES->LocateProtocol
* [0x3aeb] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c87] EFI_BOOT_SERVICES->LocateProtocol
* [0x40ae] EFI_BOOT_SERVICES->LocateProtocol
* [0x42c0] EFI_BOOT_SERVICES->LocateProtocol
* [0x6483] EFI_BOOT_SERVICES->LocateProtocol
* [0x430f] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x6700]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x6e78]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6710]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSioProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x215fdd18, 0xbd50, 0x4feb, 0x89, 0xb, 0x58, 0xca, 0xb, 0x47, 0x39, 0xe9]
* [0x8488]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x630041, 0x70, 0x69, 0x52, 0x0, 0x65, 0x0, 0x73, 0x0, 0x65, 0x0]
* [0x6700]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x6e78]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6e88]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x6710]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSioProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x215fdd18, 0xbd50, 0x4feb, 0x89, 0xb, 0x58, 0xca, 0xb, 0x47, 0x39, 0xe9]
* [0x6e98]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdbff9d55, 0x89b7, 0x46da, 0xbd, 0xdf, 0x67, 0x7d, 0x3d, 0xc0, 0x24, 0x1d]
* [0x6da8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x6d48]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x67f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xf109f361, 0x370c, 0x4d9c, 0xb1, 0xab, 0x7c, 0xa2, 0xd4, 0xc8, 0xb3, 0xff]
* [0x67e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xac9cf0a8, 0xe551, 0x4be2, 0xad, 0xa, 0xe1, 0xb5, 0x64, 0xee, 0xa2, 0x73]
* [0x66f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x4fc0733f, 0x6fd2, 0x491b, 0xa8, 0x90, 0x53, 0x74, 0x52, 0x1b, 0xf4, 0x8f]
* [0x6720]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26baccb1, 0x6f42, 0x11d4, 0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
* [0x66e0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
* [0x6720]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26baccb1, 0x6f42, 0x11d4, 0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
## Module: AcpiDebugTable
### Boot services:
* [0x36a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x39f] EFI_BOOT_SERVICES->HandleProtocol
* [0x340] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x22d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x22e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
## Module: AcpiModeEnable
### Boot services:
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a1] EFI_BOOT_SERVICES->LocateProtocol
* [0x474] EFI_BOOT_SERVICES->LocateProtocol
* [0x85a] EFI_BOOT_SERVICES->LocateProtocol
* [0xa3b] EFI_BOOT_SERVICES->LocateProtocol
* [0xe8d] EFI_BOOT_SERVICES->LocateProtocol
* [0x955] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x99d] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x13e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1410]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x1968]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1400]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: AcpiPlatform
### Boot services:
* [0x3c9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x439] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x19f7] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a66] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5c29] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x57e] EFI_BOOT_SERVICES->HandleProtocol
* [0x2f0] EFI_BOOT_SERVICES->LocateProtocol
* [0x339] EFI_BOOT_SERVICES->LocateProtocol
* [0x780] EFI_BOOT_SERVICES->LocateProtocol
* [0x79e] EFI_BOOT_SERVICES->LocateProtocol
* [0x2219] EFI_BOOT_SERVICES->LocateProtocol
* [0x38fc] EFI_BOOT_SERVICES->LocateProtocol
* [0x5feb] EFI_BOOT_SERVICES->LocateProtocol
* [0x6009] EFI_BOOT_SERVICES->LocateProtocol
* [0x6195] EFI_BOOT_SERVICES->LocateProtocol
* [0x78c3] EFI_BOOT_SERVICES->LocateProtocol
* [0x7b43] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xd5b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xd5e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0xd550]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xd560]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3fdda605, 0xa76e, 0x4f46, 0xad, 0x29, 0x12, 0xf4, 0x53, 0x1b, 0x3d, 0x8]
* [0xd580]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xad61f191, 0xae5f, 0x4c0e, 0xb9, 0xfa, 0xe8, 0x69, 0xd2, 0x88, 0xc6, 0x4f]
* [0xd530]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
* [0xd5d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xeb97088e, 0xcfdf, 0x49c6, 0xbe, 0x4b, 0xd9, 0x6, 0xa5, 0xb2, 0xe, 0x86]
* [0xd5a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xab5a4df4, 0xf0d7, 0x49a8, 0xbf, 0x5c, 0xf2, 0x5d, 0xa0, 0x4c, 0x25, 0x33]
* [0xd5c0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
## Module: AcpiPlatformFeatures
### Boot services:
* [0xc4f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xcbe] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xe00] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x706] EFI_BOOT_SERVICES->HandleProtocol
* [0xe35] EFI_BOOT_SERVICES->HandleProtocol
* [0x31b] EFI_BOOT_SERVICES->LocateProtocol
* [0x428] EFI_BOOT_SERVICES->LocateProtocol
* [0x83e] EFI_BOOT_SERVICES->LocateProtocol
* [0xdd6] EFI_BOOT_SERVICES->LocateProtocol
* [0xfbb] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x12c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x12e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGlobalNvsAreaProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x74e1e48, 0x8132, 0x47a1, 0x8c, 0x2c, 0x3f, 0x14, 0xad, 0x9a, 0x66, 0xdc]
* [0x12b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
* [0x12d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd9035175, 0x8ce2, 0x47de, 0xa8, 0xb8, 0xcc, 0x98, 0xe5, 0xe2, 0xa8, 0x85]
* [0x12f0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
## Module: AcpiS3SaveDxe
### Boot services:
* [0x3b0] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* [0x5a0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiAcpiS3SaveProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x125f2de1, 0xfb85, 0x440c, 0xa5, 0x4c, 0x4d, 0x99, 0x35, 0x8a, 0x8d, 0x38]
## Module: AcpiSmm
### Boot services:
* [0x34c] EFI_BOOT_SERVICES->LocateProtocol
* [0x37a] EFI_BOOT_SERVICES->LocateProtocol
* [0x4ea] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x870]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x880]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x850]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3dc21d75, 0xde0e, 0x4300, 0xa0, 0xaa, 0x19, 0xc4, 0x1c, 0xc, 0xf3, 0xdf]
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
* [0x7260]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb2fa4764, 0x3b6e, 0x43d3, 0x91, 0xdf, 0x87, 0xd1, 0x5a, 0x3e, 0x56, 0x68]
* [0x7280]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xe159a956, 0x3299, 0x4ee9, 0x91, 0x76, 0x65, 0x18, 0x1a, 0x4e, 0x5e, 0x9f]
* [0x7220]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa1e37052, 0x80d9, 0x4e65, 0xa3, 0x17, 0x3e, 0x9a, 0x55, 0xc4, 0x3e, 0xc9]
* [0x7200]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x7210]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x7240]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x7250]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0x72a0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xf4f63529, 0x281e, 0x4040, 0xa3, 0x13, 0xc1, 0xd6, 0x76, 0x63, 0x84, 0xbe]
* [0x7900]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb396da3a, 0x52b2, 0x4cd6, 0xa8, 0x9a, 0x13, 0xe7, 0xc4, 0xae, 0x97, 0x90]
* [0x72d0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xffbd9ad2, 0xf1db, 0x4f92, 0xa6, 0x49, 0xeb, 0x9e, 0xed, 0xea, 0x86, 0xb5]
* [0x7290]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiStorageSecurityCommandProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc88b0b6d, 0xdfc, 0x49a7, 0x9c, 0xb4, 0x49, 0x7, 0x4b, 0x4c, 0x3a, 0x78]
* [0x7260]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb2fa4764, 0x3b6e, 0x43d3, 0x91, 0xdf, 0x87, 0xd1, 0x5a, 0x3e, 0x56, 0x68]
* [0x78e0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x1fd29be6, 0x70d0, 0x42a4, 0xa6, 0xe7, 0xe5, 0xd1, 0xe, 0x6a, 0xc3, 0x76]
* [0x7260]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb2fa4764, 0x3b6e, 0x43d3, 0x91, 0xdf, 0x87, 0xd1, 0x5a, 0x3e, 0x56, 0x68]
* [0x78d0]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5d206dd3, 0x516a, 0x47dc, 0xa1, 0xbc, 0x6d, 0xa2, 0x4, 0xaa, 0xbe, 0x8]
* [0x78e0]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x1fd29be6, 0x70d0, 0x42a4, 0xa6, 0xe7, 0xe5, 0xd1, 0xe, 0x6a, 0xc3, 0x76]
* [0x72a0]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
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
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xce6f86bb, 0xb800, 0x4c71, 0xb2, 0xd1, 0x38, 0x97, 0xa3, 0xbc, 0x1d, 0xae]
* [0x72f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x59af16b0, 0x661d, 0x4865, 0xa3, 0x81, 0x38, 0xde, 0x68, 0x38, 0x5d, 0x8d]
* [0x72e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
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
* [0x7220]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa1e37052, 0x80d9, 0x4e65, 0xa3, 0x17, 0x3e, 0x9a, 0x55, 0xc4, 0x3e, 0xc9]
* [0x7260]
	 - [service] CloseProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb2fa4764, 0x3b6e, 0x43d3, 0x91, 0xdf, 0x87, 0xd1, 0x5a, 0x3e, 0x56, 0x68]
* [0x7220]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa1e37052, 0x80d9, 0x4e65, 0xa3, 0x17, 0x3e, 0x9a, 0x55, 0xc4, 0x3e, 0xc9]
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
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
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
* [0x1480]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x67820532, 0x7613, 0x4dd3, 0x9e, 0xd7, 0x3d, 0x9b, 0xe3, 0xa7, 0xda, 0x63]
* [0x1490]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb2fa4764, 0x3b6e, 0x43d3, 0x91, 0xdf, 0x87, 0xd1, 0x5a, 0x3e, 0x56, 0x68]
* [0x14a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x14b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
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
* [0x13c3] EFI_BOOT_SERVICES->LocateProtocol
* [0x1535] EFI_BOOT_SERVICES->LocateProtocol
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
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
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
## Module: AmiHsti
### Boot services:
* [0xc65] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6ff] EFI_BOOT_SERVICES->OpenProtocol
* [0x89e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xcb6] EFI_BOOT_SERVICES->HandleProtocol
* [0x370] EFI_BOOT_SERVICES->LocateProtocol
* [0x38e] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c8] EFI_BOOT_SERVICES->LocateProtocol
* [0x3e5] EFI_BOOT_SERVICES->LocateProtocol
* [0x720] EFI_BOOT_SERVICES->LocateProtocol
* [0xa57] EFI_BOOT_SERVICES->LocateProtocol
* [0x1165] EFI_BOOT_SERVICES->LocateProtocol
* [0x15cb] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f8a] EFI_BOOT_SERVICES->LocateProtocol
* [0x22c3] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x4620]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiAdapterInformationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe5dd1403, 0xd622, 0xc24e, 0x84, 0x88, 0xc7, 0x1b, 0x17, 0xf5, 0xe8, 0x2]
* [0x4cf0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0x4620]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAdapterInformationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe5dd1403, 0xd622, 0xc24e, 0x84, 0x88, 0xc7, 0x1b, 0x17, 0xf5, 0xe8, 0x2]
* [0x4660]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x4680]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x4690]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x4650]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x4670]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
* [0x4d00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x4630]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5f87ba17, 0x957d, 0x433d, 0x9e, 0x15, 0xc0, 0xe7, 0xc8, 0x79, 0x88, 0x99]
* [0x4640]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x13a3f0f6, 0x264a, 0x3ef0, 0xf2, 0xe0, 0xde, 0xc5, 0x12, 0x34, 0x2f, 0x34]
* [0x4cb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
## Module: AmiMemoryInfoConfig
### Boot services:
* [0x581] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3d5] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x860]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6aa1f27, 0x5597, 0x4802, 0x9f, 0x63, 0xd6, 0x28, 0x36, 0x59, 0x86, 0x35]
## Module: AmiTcgNvflagSample
### Boot services:
* [0x3ac] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2f2] EFI_BOOT_SERVICES->LocateProtocol
* [0x321] EFI_BOOT_SERVICES->LocateProtocol
* [0x557] EFI_BOOT_SERVICES->LocateProtocol
* [0x586] EFI_BOOT_SERVICES->LocateProtocol
* [0x880] EFI_BOOT_SERVICES->LocateProtocol
* [0x8af] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xa70]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xe9008d70, 0x2a4e, 0x47ea, 0x8e, 0xc4, 0x72, 0xe2, 0x57, 0x67, 0xe5, 0xef]
* [0xa40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTpmMpDriverProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xde161cfe, 0x1e60, 0x42a1, 0x8c, 0xc3, 0xee, 0x7e, 0xf0, 0x73, 0x52, 0x12]
* [0xa20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf541796d, 0xa62e, 0x4954, 0xa7, 0x75, 0x95, 0x84, 0xf6, 0x1b, 0x9c, 0xdd]
## Module: AmiTcgPlatformDxe
### Boot services:
* [0xb7b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x43c] EFI_BOOT_SERVICES->OpenProtocol
* [0x3f3] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xbbb] EFI_BOOT_SERVICES->HandleProtocol
* [0x344] EFI_BOOT_SERVICES->LocateProtocol
* [0x362] EFI_BOOT_SERVICES->LocateProtocol
* [0x37f] EFI_BOOT_SERVICES->LocateProtocol
* [0x39c] EFI_BOOT_SERVICES->LocateProtocol
* [0x45c] EFI_BOOT_SERVICES->LocateProtocol
* [0x4e7] EFI_BOOT_SERVICES->LocateProtocol
* [0x6d9] EFI_BOOT_SERVICES->LocateProtocol
* [0x8fd] EFI_BOOT_SERVICES->LocateProtocol
* [0xa37] EFI_BOOT_SERVICES->LocateProtocol
* [0xb3a] EFI_BOOT_SERVICES->LocateProtocol
* [0xcea] EFI_BOOT_SERVICES->LocateProtocol
* [0xd45] EFI_BOOT_SERVICES->LocateProtocol
* [0x10c9] EFI_BOOT_SERVICES->LocateProtocol
* [0x1100] EFI_BOOT_SERVICES->LocateProtocol
* [0x1219] EFI_BOOT_SERVICES->LocateProtocol
* [0x14f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x16fe] EFI_BOOT_SERVICES->LocateProtocol
* [0x17dd] EFI_BOOT_SERVICES->LocateProtocol
* [0x19c0] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b6f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b91] EFI_BOOT_SERVICES->LocateProtocol
* [0x1bc6] EFI_BOOT_SERVICES->LocateProtocol
* [0x1c69] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d3f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1eab] EFI_BOOT_SERVICES->LocateProtocol
* [0x2010] EFI_BOOT_SERVICES->LocateProtocol
* [0x203a] EFI_BOOT_SERVICES->LocateProtocol
* [0x2971] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b36] EFI_BOOT_SERVICES->LocateProtocol
* [0x2c7f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2cb1] EFI_BOOT_SERVICES->LocateProtocol
* [0x2cd5] EFI_BOOT_SERVICES->LocateProtocol
* [0x2cfa] EFI_BOOT_SERVICES->LocateProtocol
* [0x3441] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c8e] EFI_BOOT_SERVICES->LocateProtocol
* [0x3cc8] EFI_BOOT_SERVICES->LocateProtocol
* [0x3d20] EFI_BOOT_SERVICES->LocateProtocol
* [0x413d] EFI_BOOT_SERVICES->LocateProtocol
* [0x42ed] EFI_BOOT_SERVICES->LocateProtocol
* [0x431d] EFI_BOOT_SERVICES->LocateProtocol
* [0x4342] EFI_BOOT_SERVICES->LocateProtocol
* [0x4481] EFI_BOOT_SERVICES->LocateProtocol
* [0x44a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x610a] EFI_BOOT_SERVICES->LocateProtocol
* [0x100d] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1f10] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2b9e] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3008] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x4910] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x499f] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x66c0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolumeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x389f751f, 0x1838, 0x4388, 0x83, 0x90, 0xcd, 0x81, 0x54, 0xbd, 0x27, 0xf8]
* [0x6630]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0x67b8]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8c939604, 0x700, 0x4415, 0x9d, 0x62, 0x11, 0x61, 0xdb, 0x81, 0x64, 0xa6]
* [0x66c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolumeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x389f751f, 0x1838, 0x4388, 0x83, 0x90, 0xcd, 0x81, 0x54, 0xbd, 0x27, 0xf8]
* [0x6670]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x6690]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x66a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x6660]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x6610]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf541796d, 0xa62e, 0x4954, 0xa7, 0x75, 0x95, 0x84, 0xf6, 0x1b, 0x9c, 0xdd]
* [0x6b40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6d0049, 0x61, 0x67, 0x65, 0x0, 0x45, 0x0, 0x78, 0x0, 0x65, 0x0]
* [0x67e8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTpmMpDriverProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xde161cfe, 0x1e60, 0x42a1, 0x8c, 0xc3, 0xee, 0x7e, 0xf0, 0x73, 0x52, 0x12]
* [0x6650]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
* [0x67d8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTpmMpDriverProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xde161cfe, 0x1e60, 0x42a1, 0x8c, 0xc3, 0xee, 0x7e, 0xf0, 0x73, 0x52, 0x12]
* [0x67a8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0x66f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xeb97088e, 0xcfdf, 0x49c6, 0xbe, 0x4b, 0xd9, 0x6, 0xa5, 0xb2, 0xe, 0x86]
* [0x6620]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiResetArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x27cfac88, 0x46cc, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6640]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xf2a128ff, 0x257b, 0x456e, 0x9d, 0xe8, 0x63, 0xe7, 0xc7, 0xdc, 0xdf, 0xac]
* [0x6650]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
* [0x66e0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiAcpiSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdbff9d55, 0x89b7, 0x46da, 0xbd, 0xdf, 0x67, 0x7d, 0x3d, 0xc0, 0x24, 0x1d]
## Module: AMITSE
### Boot services:
* [0x4435] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x7a62] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8c65] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x9fed] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa15b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa67b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x16d0e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x19ddc] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a1e3] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a2c6] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a838] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1b040] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2a95c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2c3ca] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2c5aa] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2ceae] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2fc01] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2fe39] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x30b67] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x30c8e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3100d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x31276] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x31390] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x706] EFI_BOOT_SERVICES->OpenProtocol
* [0x34b0] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2e8f4] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3498] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x29ae5] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2af47] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2af81] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2e8dc] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2e9a8] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xa88a] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x2a7f2] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x2a998] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x33aba] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x829] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x865] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1bb17] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x4bd3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4c1a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4c49] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4c78] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x30922] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x316a4] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3434] EFI_BOOT_SERVICES->HandleProtocol
* [0x4461] EFI_BOOT_SERVICES->HandleProtocol
* [0x7aa1] EFI_BOOT_SERVICES->HandleProtocol
* [0x8cb3] EFI_BOOT_SERVICES->HandleProtocol
* [0x9b88] EFI_BOOT_SERVICES->HandleProtocol
* [0x9c97] EFI_BOOT_SERVICES->HandleProtocol
* [0x9d07] EFI_BOOT_SERVICES->HandleProtocol
* [0xa029] EFI_BOOT_SERVICES->HandleProtocol
* [0xa066] EFI_BOOT_SERVICES->HandleProtocol
* [0xa6bf] EFI_BOOT_SERVICES->HandleProtocol
* [0xa941] EFI_BOOT_SERVICES->HandleProtocol
* [0xad86] EFI_BOOT_SERVICES->HandleProtocol
* [0xbb77] EFI_BOOT_SERVICES->HandleProtocol
* [0x1055a] EFI_BOOT_SERVICES->HandleProtocol
* [0x16d82] EFI_BOOT_SERVICES->HandleProtocol
* [0x181eb] EFI_BOOT_SERVICES->HandleProtocol
* [0x1874e] EFI_BOOT_SERVICES->HandleProtocol
* [0x19370] EFI_BOOT_SERVICES->HandleProtocol
* [0x19e1f] EFI_BOOT_SERVICES->HandleProtocol
* [0x19eaa] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a029] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a23a] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a4a0] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a87a] EFI_BOOT_SERVICES->HandleProtocol
* [0x1b067] EFI_BOOT_SERVICES->HandleProtocol
* [0x1f0ff] EFI_BOOT_SERVICES->HandleProtocol
* [0x207cc] EFI_BOOT_SERVICES->HandleProtocol
* [0x2628f] EFI_BOOT_SERVICES->HandleProtocol
* [0x2abd4] EFI_BOOT_SERVICES->HandleProtocol
* [0x2c415] EFI_BOOT_SERVICES->HandleProtocol
* [0x2c488] EFI_BOOT_SERVICES->HandleProtocol
* [0x2c54c] EFI_BOOT_SERVICES->HandleProtocol
* [0x2c5de] EFI_BOOT_SERVICES->HandleProtocol
* [0x2cf13] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d6b0] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fc47] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fe85] EFI_BOOT_SERVICES->HandleProtocol
* [0x2ff05] EFI_BOOT_SERVICES->HandleProtocol
* [0x2ff72] EFI_BOOT_SERVICES->HandleProtocol
* [0x30b2e] EFI_BOOT_SERVICES->HandleProtocol
* [0x30b99] EFI_BOOT_SERVICES->HandleProtocol
* [0x30cc0] EFI_BOOT_SERVICES->HandleProtocol
* [0x3104a] EFI_BOOT_SERVICES->HandleProtocol
* [0x312b3] EFI_BOOT_SERVICES->HandleProtocol
* [0x313cd] EFI_BOOT_SERVICES->HandleProtocol
* [0x32048] EFI_BOOT_SERVICES->HandleProtocol
* [0x32084] EFI_BOOT_SERVICES->HandleProtocol
* [0x32164] EFI_BOOT_SERVICES->HandleProtocol
* [0x32222] EFI_BOOT_SERVICES->HandleProtocol
* [0x323b6] EFI_BOOT_SERVICES->HandleProtocol
* [0x32416] EFI_BOOT_SERVICES->HandleProtocol
* [0x33b83] EFI_BOOT_SERVICES->HandleProtocol
* [0x33c0b] EFI_BOOT_SERVICES->HandleProtocol
* [0x38238] EFI_BOOT_SERVICES->HandleProtocol
* [0x38b83] EFI_BOOT_SERVICES->HandleProtocol
* [0x3bda8] EFI_BOOT_SERVICES->HandleProtocol
* [0x726] EFI_BOOT_SERVICES->LocateProtocol
* [0x4483] EFI_BOOT_SERVICES->LocateProtocol
* [0x4a40] EFI_BOOT_SERVICES->LocateProtocol
* [0x988c] EFI_BOOT_SERVICES->LocateProtocol
* [0xacb4] EFI_BOOT_SERVICES->LocateProtocol
* [0xc7f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x16cce] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ac4b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1baf1] EFI_BOOT_SERVICES->LocateProtocol
* [0x1bef3] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f14b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2031b] EFI_BOOT_SERVICES->LocateProtocol
* [0x204f1] EFI_BOOT_SERVICES->LocateProtocol
* [0x2764c] EFI_BOOT_SERVICES->LocateProtocol
* [0x29b00] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ac4b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ad6e] EFI_BOOT_SERVICES->LocateProtocol
* [0x2adda] EFI_BOOT_SERVICES->LocateProtocol
* [0x2aeed] EFI_BOOT_SERVICES->LocateProtocol
* [0x2afa7] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b02f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b0ec] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b229] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b36f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b398] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b3bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b3ee] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b550] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b56e] EFI_BOOT_SERVICES->LocateProtocol
* [0x2c6e6] EFI_BOOT_SERVICES->LocateProtocol
* [0x2c79b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ca19] EFI_BOOT_SERVICES->LocateProtocol
* [0x2cd73] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e13f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e3a0] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e455] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e59f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e65f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e74f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e78a] EFI_BOOT_SERVICES->LocateProtocol
* [0x2eb24] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ec04] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f359] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f4cf] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f536] EFI_BOOT_SERVICES->LocateProtocol
* [0x2fd74] EFI_BOOT_SERVICES->LocateProtocol
* [0x302cb] EFI_BOOT_SERVICES->LocateProtocol
* [0x30471] EFI_BOOT_SERVICES->LocateProtocol
* [0x3072b] EFI_BOOT_SERVICES->LocateProtocol
* [0x30764] EFI_BOOT_SERVICES->LocateProtocol
* [0x3080f] EFI_BOOT_SERVICES->LocateProtocol
* [0x308e1] EFI_BOOT_SERVICES->LocateProtocol
* [0x30a86] EFI_BOOT_SERVICES->LocateProtocol
* [0x30ae9] EFI_BOOT_SERVICES->LocateProtocol
* [0x30c3d] EFI_BOOT_SERVICES->LocateProtocol
* [0x30d3f] EFI_BOOT_SERVICES->LocateProtocol
* [0x30e3d] EFI_BOOT_SERVICES->LocateProtocol
* [0x30ed6] EFI_BOOT_SERVICES->LocateProtocol
* [0x30f25] EFI_BOOT_SERVICES->LocateProtocol
* [0x30f74] EFI_BOOT_SERVICES->LocateProtocol
* [0x31125] EFI_BOOT_SERVICES->LocateProtocol
* [0x3114e] EFI_BOOT_SERVICES->LocateProtocol
* [0x31d30] EFI_BOOT_SERVICES->LocateProtocol
* [0x31ec9] EFI_BOOT_SERVICES->LocateProtocol
* [0x32d2a] EFI_BOOT_SERVICES->LocateProtocol
* [0x33063] EFI_BOOT_SERVICES->LocateProtocol
* [0x33416] EFI_BOOT_SERVICES->LocateProtocol
* [0x33593] EFI_BOOT_SERVICES->LocateProtocol
* [0x336f2] EFI_BOOT_SERVICES->LocateProtocol
* [0x33733] EFI_BOOT_SERVICES->LocateProtocol
* [0x339f0] EFI_BOOT_SERVICES->LocateProtocol
* [0x404de] EFI_BOOT_SERVICES->LocateProtocol
* [0xa901] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2a838] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2a9dc] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x33b21] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x3c55] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3cb6] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3d16] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x95d8] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x9624] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xc1c1] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2e4ac] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2e834] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x2e889] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x303ba] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x30991] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x47ae0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x4a840]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x479b0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x479a0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x47b00]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2b2f68d6, 0xcd2, 0x44cf, 0x8e, 0x8b, 0xbb, 0xa2, 0xb, 0x1b, 0x5b, 0x75]
* [0x4a208]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x49de8]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x47990]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiOEMBadgingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x170e13c0, 0xbf1b, 0x4218, 0x87, 0x1d, 0x2a, 0xbd, 0xc6, 0xf8, 0x87, 0xbc]
* [0x489b8]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdd9e7534, 0x7762, 0x4698, 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa]
* [0x48798]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0x47ac0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4f860]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0x48e80]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd3431c06, 0x2b4c, 0x4337, 0x93, 0x34, 0xff, 0xd9, 0xc0, 0x55, 0x15, 0x21]
* [0x47ac0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4a840]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x479b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x479e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x47b00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2b2f68d6, 0xcd2, 0x44cf, 0x8e, 0x8b, 0xbb, 0xa2, 0xb, 0x1b, 0x5b, 0x75]
* [0x479a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x49de8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x47960]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x47990]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiOEMBadgingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x170e13c0, 0xbf1b, 0x4218, 0x87, 0x1d, 0x2a, 0xbd, 0xc6, 0xf8, 0x87, 0xbc]
* [0x49330]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xadfb62d, 0xff74, 0x484c, 0x89, 0x44, 0xf8, 0x5c, 0x4b, 0xea, 0x87, 0xa8]
* [0x489b8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdd9e7534, 0x7762, 0x4698, 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa]
* [0x4a830]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x48698]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x486b8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x487a8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x47ae0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x49800]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x30cb7768, 0xecde, 0x445a, 0xba, 0xac, 0x66, 0x54, 0x45, 0x9, 0x55, 0x22]
* [0x479c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x479f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0x47aa0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb9d4c360, 0xbcfb, 0x4f9b, 0x92, 0x98, 0x53, 0xc1, 0x36, 0x98, 0x22, 0x58]
* [0x49cb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDevicePathToTextProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8b843e20, 0x8132, 0x4852, 0x90, 0xcc, 0x55, 0x1a, 0x4e, 0x4a, 0x7f, 0x1c]
* [0x47970]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiUnicodeCollation2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa4c751fc, 0x23ae, 0x4c3e, 0x92, 0xe9, 0x49, 0x64, 0xcf, 0x63, 0xf3, 0x49]
* [0x48ea0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x96fd60f3, 0xbc8, 0x4a11, 0x84, 0xf1, 0x2e, 0xb1, 0xcb, 0x5b, 0xa5, 0xa3]
* [0x48e90]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x96fd60f3, 0xbc8, 0x4a11, 0x84, 0xf1, 0x2e, 0xb1, 0xcb, 0x5b, 0xa5, 0xa3]
* [0x47af0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x47a70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x47a80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x47a90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x47980]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiUnicodeCollationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x1d85cd7f, 0xf43d, 0x11d2, 0x9a, 0xc, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x48eb0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc7a7030c, 0xc3d8, 0x45ee, 0xbe, 0xd9, 0x5d, 0x9e, 0x76, 0x76, 0x29, 0x53]
* [0x489e8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8e008510, 0x9bb1, 0x457d, 0x9f, 0x70, 0x89, 0x7a, 0xba, 0x86, 0x5d, 0xb9]
* [0x47a40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x919383de, 0xebac, 0x4924, 0x1, 0x94, 0x52, 0x59, 0xe0, 0xd, 0x65, 0x7a]
* [0x47a20]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x45de9920, 0xcd54, 0x446a, 0xa0, 0x3c, 0x22, 0xe6, 0xfb, 0xb4, 0x51, 0xe4]
* [0x47950]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CONSOLE_CONTROL_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] [0xf42f7782, 0x12e, 0x4c12, 0x99, 0x56, 0x49, 0xf9, 0x43, 0x4, 0xf7, 0x21]
* [0x47a50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6725e645, 0x4a7f, 0x9969, 0x82, 0xec, 0xd1, 0x87, 0x21, 0xde, 0x5a, 0x57]
* [0x47a30]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x47ab0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5f87ba17, 0x957d, 0x433d, 0x9e, 0x15, 0xc0, 0xe7, 0xc8, 0x79, 0x88, 0x99]
* [0x48758]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x48778]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x48788]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb9d4c360, 0xbcfb, 0x4f9b, 0x92, 0x98, 0x53, 0xc1, 0x36, 0x98, 0x22, 0x58]
* [0x486e8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x47ae0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x48e70]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x1172381f, 0x7ae6, 0x4652, 0x8d, 0x85, 0xb6, 0x51, 0x69, 0x7b, 0xe3, 0xcf]
* [0x48e80]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd3431c06, 0x2b4c, 0x4337, 0x93, 0x34, 0xff, 0xd9, 0xc0, 0x55, 0x15, 0x21]
* [0x479d0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c1, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
## Module: AmiTxtDxe
### Boot services:
* [0x3fd] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* [0xc08]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x1c92f0ab, 0x3351, 0x1be5, 0xaf, 0xba, 0xc1, 0x25, 0x61, 0xbb, 0x32, 0xa3]
## Module: AMTbypass
### Boot services:
* [0x502] EFI_BOOT_SERVICES->LocateProtocol
* [0x337] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x750]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x45de9920, 0xcd54, 0x446a, 0xa0, 0x3c, 0x22, 0xe6, 0xfb, 0xb4, 0x51, 0xe4]
* [0x750]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x45de9920, 0xcd54, 0x446a, 0xa0, 0x3c, 0x22, 0xe6, 0xfb, 0xb4, 0x51, 0xe4]
## Module: AmtCompatiblity
### Boot services:
* [0x35d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: AMTLockKBD
### Boot services:
* [0x5a4] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x67c] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6d0] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x5e2] EFI_BOOT_SERVICES->HandleProtocol
* [0x652] EFI_BOOT_SERVICES->HandleProtocol
* [0x6a6] EFI_BOOT_SERVICES->HandleProtocol
* [0x2f7] EFI_BOOT_SERVICES->LocateProtocol
* [0x432] EFI_BOOT_SERVICES->LocateProtocol
* [0x4bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x54b] EFI_BOOT_SERVICES->LocateProtocol
* [0x74b] EFI_BOOT_SERVICES->LocateProtocol
* [0x7b5] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xef8]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c1, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xef8]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c1, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xee8]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdd9e7534, 0x7762, 0x4698, 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa]
* [0x960]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xef8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c1, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xee8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdd9e7534, 0x7762, 0x4698, 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa]
* [0x940]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x45de9920, 0xcd54, 0x446a, 0xa0, 0x3c, 0x22, 0xe6, 0xfb, 0xb4, 0x51, 0xe4]
* [0xf08]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmPowerButtonDispatchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb709efa0, 0x47a6, 0x4b41, 0xb9, 0x31, 0x12, 0xec, 0xe7, 0xa8, 0xee, 0x56]
* [0x950]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyRegion2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x70101eaf, 0x85, 0x440c, 0xb3, 0x56, 0x8e, 0xe3, 0x6f, 0xef, 0x24, 0xf0]
## Module: AmtLockPbtn
### Boot services:
* [0x2f1] EFI_BOOT_SERVICES->LocateProtocol
* [0x361] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x520]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x45de9920, 0xcd54, 0x446a, 0xa0, 0x3c, 0x22, 0xe6, 0xfb, 0xb4, 0x51, 0xe4]
* [0xa98]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3aa83745, 0x9454, 0x4f7a, 0xa7, 0xc0, 0x90, 0xdb, 0xd0, 0x2f, 0xab, 0x8e]
## Module: AMTLockUsbKBD
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x38e] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b2] EFI_BOOT_SERVICES->LocateProtocol
* [0x3e9] EFI_BOOT_SERVICES->LocateProtocol
* [0x4d7] EFI_BOOT_SERVICES->LocateProtocol
* [0x67d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xa20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xa10]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2ad8e2d2, 0x2e91, 0x4cd1, 0x95, 0xf5, 0xe7, 0x8f, 0xe5, 0xeb, 0xe3, 0x16]
* [0xa30]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x45de9920, 0xcd54, 0x446a, 0xa0, 0x3c, 0x22, 0xe6, 0xfb, 0xb4, 0x51, 0xe4]
* [0xf38]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xa50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: AmtPetAlertDxe
### Boot services:
* [0x434] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6ff] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3052] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2b16] EFI_BOOT_SERVICES->OpenProtocol
* [0x2b52] EFI_BOOT_SERVICES->OpenProtocol
* [0x4fc] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x470] EFI_BOOT_SERVICES->HandleProtocol
* [0x862] EFI_BOOT_SERVICES->HandleProtocol
* [0x8cd] EFI_BOOT_SERVICES->HandleProtocol
* [0x20d7] EFI_BOOT_SERVICES->HandleProtocol
* [0x273e] EFI_BOOT_SERVICES->HandleProtocol
* [0x28f9] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d08] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d2b] EFI_BOOT_SERVICES->HandleProtocol
* [0x2e2d] EFI_BOOT_SERVICES->HandleProtocol
* [0x2eb5] EFI_BOOT_SERVICES->HandleProtocol
* [0x2f00] EFI_BOOT_SERVICES->HandleProtocol
* [0x30a4] EFI_BOOT_SERVICES->HandleProtocol
* [0x31c] EFI_BOOT_SERVICES->LocateProtocol
* [0x33a] EFI_BOOT_SERVICES->LocateProtocol
* [0x357] EFI_BOOT_SERVICES->LocateProtocol
* [0x374] EFI_BOOT_SERVICES->LocateProtocol
* [0x391] EFI_BOOT_SERVICES->LocateProtocol
* [0x61c] EFI_BOOT_SERVICES->LocateProtocol
* [0xa7d] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f86] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3330]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0x3360]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3370]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x33e0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x56ec3091, 0x954c, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3380]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3330]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0x3330]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0x3380]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x33f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2b2f68d6, 0xcd2, 0x44cf, 0x8e, 0x8b, 0xbb, 0xa2, 0xb, 0x1b, 0x5b, 0x75]
* [0x33e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x56ec3091, 0x954c, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3370]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3360]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x33a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x33c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x33d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x3390]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x33b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
* [0x3340]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x3350]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x3400]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6725e645, 0x4a7f, 0x9969, 0x82, 0xec, 0xd1, 0x87, 0x21, 0xde, 0x5a, 0x57]
## Module: AmtSetupDxe
### Boot services:
* [0x2b5] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x370]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x919383de, 0xebac, 0x4924, 0x1, 0x94, 0x52, 0x59, 0xe0, 0xd, 0x65, 0x7a]
## Module: AmtWrapperDxe
### Boot services:
* [0x8ab] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xc9d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x15b4] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1bc6] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5473] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5644] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x59db] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5ca7] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5f60] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x60fe] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x63b1] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x66a2] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x67d5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6bc5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8618] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x869d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8c69] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x69e0] EFI_BOOT_SERVICES->OpenProtocol
* [0x8c04] EFI_BOOT_SERVICES->OpenProtocol
* [0x9206] EFI_BOOT_SERVICES->OpenProtocol
* [0x9242] EFI_BOOT_SERVICES->OpenProtocol
* [0xd45] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xa1e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xda7] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x54c5] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x5574] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xab2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8ef] EFI_BOOT_SERVICES->HandleProtocol
* [0x911] EFI_BOOT_SERVICES->HandleProtocol
* [0x97f] EFI_BOOT_SERVICES->HandleProtocol
* [0xd13] EFI_BOOT_SERVICES->HandleProtocol
* [0xe5b] EFI_BOOT_SERVICES->HandleProtocol
* [0x1bf5] EFI_BOOT_SERVICES->HandleProtocol
* [0x257b] EFI_BOOT_SERVICES->HandleProtocol
* [0x567f] EFI_BOOT_SERVICES->HandleProtocol
* [0x5965] EFI_BOOT_SERVICES->HandleProtocol
* [0x5cee] EFI_BOOT_SERVICES->HandleProtocol
* [0x5fb0] EFI_BOOT_SERVICES->HandleProtocol
* [0x661e] EFI_BOOT_SERVICES->HandleProtocol
* [0x72cd] EFI_BOOT_SERVICES->HandleProtocol
* [0x796c] EFI_BOOT_SERVICES->HandleProtocol
* [0x7a13] EFI_BOOT_SERVICES->HandleProtocol
* [0x8200] EFI_BOOT_SERVICES->HandleProtocol
* [0x8221] EFI_BOOT_SERVICES->HandleProtocol
* [0x8465] EFI_BOOT_SERVICES->HandleProtocol
* [0x8cf0] EFI_BOOT_SERVICES->HandleProtocol
* [0x8e2e] EFI_BOOT_SERVICES->HandleProtocol
* [0x8fe9] EFI_BOOT_SERVICES->HandleProtocol
* [0x93f8] EFI_BOOT_SERVICES->HandleProtocol
* [0x941b] EFI_BOOT_SERVICES->HandleProtocol
* [0x951d] EFI_BOOT_SERVICES->HandleProtocol
* [0x95a5] EFI_BOOT_SERVICES->HandleProtocol
* [0x95f0] EFI_BOOT_SERVICES->HandleProtocol
* [0xb085] EFI_BOOT_SERVICES->HandleProtocol
* [0xb17c] EFI_BOOT_SERVICES->HandleProtocol
* [0xb396] EFI_BOOT_SERVICES->HandleProtocol
* [0x304] EFI_BOOT_SERVICES->LocateProtocol
* [0x322] EFI_BOOT_SERVICES->LocateProtocol
* [0x33f] EFI_BOOT_SERVICES->LocateProtocol
* [0x35c] EFI_BOOT_SERVICES->LocateProtocol
* [0x379] EFI_BOOT_SERVICES->LocateProtocol
* [0x442] EFI_BOOT_SERVICES->LocateProtocol
* [0xf08] EFI_BOOT_SERVICES->LocateProtocol
* [0xfb3] EFI_BOOT_SERVICES->LocateProtocol
* [0xfee] EFI_BOOT_SERVICES->LocateProtocol
* [0x1012] EFI_BOOT_SERVICES->LocateProtocol
* [0x10fc] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a2b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f63] EFI_BOOT_SERVICES->LocateProtocol
* [0x4b22] EFI_BOOT_SERVICES->LocateProtocol
* [0x695e] EFI_BOOT_SERVICES->LocateProtocol
* [0x73e1] EFI_BOOT_SERVICES->LocateProtocol
* [0x880a] EFI_BOOT_SERVICES->LocateProtocol
* [0x9751] EFI_BOOT_SERVICES->LocateProtocol
* [0x9864] EFI_BOOT_SERVICES->LocateProtocol
* [0x996b] EFI_BOOT_SERVICES->LocateProtocol
* [0xc60] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xb740]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb7d0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xcc9d5c0b, 0x9010, 0x45f1, 0x99, 0x3c, 0x83, 0x27, 0x67, 0xf1, 0x67, 0x77]
* [0xb7a0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb760]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0xb7b0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0xb910]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2b2f68d6, 0xcd2, 0x44cf, 0x8e, 0x8b, 0xbb, 0xa2, 0xb, 0x1b, 0x5b, 0x75]
* [0xb790]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x56ec3091, 0x954c, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb920]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiDriverHealthProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2a534210, 0x9280, 0x41d8, 0xae, 0x79, 0xca, 0xda, 0x1, 0xa2, 0xb1, 0x27]
* [0xb790]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x56ec3091, 0x954c, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb8f0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdd9e7534, 0x7762, 0x4698, 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa]
* [0xb800]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb7d0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xcc9d5c0b, 0x9010, 0x45f1, 0x99, 0x3c, 0x83, 0x27, 0x67, 0xf1, 0x67, 0x77]
* [0xb750]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0xb7d0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xcc9d5c0b, 0x9010, 0x45f1, 0x99, 0x3c, 0x83, 0x27, 0x67, 0xf1, 0x67, 0x77]
* [0xb740]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb800]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb750]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0xb7b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0xb760]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0xb8c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb910]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2b2f68d6, 0xcd2, 0x44cf, 0x8e, 0x8b, 0xbb, 0xa2, 0xb, 0x1b, 0x5b, 0x75]
* [0xb850]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0xb840]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xb920]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverHealthProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2a534210, 0x9280, 0x41d8, 0xae, 0x79, 0xca, 0xda, 0x1, 0xa2, 0xb1, 0x27]
* [0xb8f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdd9e7534, 0x7762, 0x4698, 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa]
* [0xb790]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x56ec3091, 0x954c, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb7a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb860]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0xb880]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0xb890]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0xb830]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0xb870]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
* [0xb770]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0xb950]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd25dc167, 0xeb6a, 0x432d, 0x65, 0x91, 0xbf, 0x80, 0x29, 0xb0, 0x5, 0xbb]
* [0xb730]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x45de9920, 0xcd54, 0x446a, 0xa0, 0x3c, 0x22, 0xe6, 0xfb, 0xb4, 0x51, 0xe4]
* [0xb7e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSecurity2ArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x94ab2f58, 0x1438, 0x4ef1, 0x91, 0x52, 0x18, 0x94, 0x1a, 0x3a, 0xe, 0x68]
* [0xb780]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0xb900]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
* [0xb930]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiRamDiskProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xab38a0df, 0x6873, 0x44a9, 0x87, 0xe6, 0xd4, 0xeb, 0x56, 0x14, 0x84, 0x49]
* [0xb8e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiBootLogoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcdea2bd3, 0xfc25, 0x4c1c, 0xb9, 0x7c, 0xb3, 0x11, 0x86, 0x6, 0x49, 0x90]
* [0xb8a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb9d4c360, 0xbcfb, 0x4f9b, 0x92, 0x98, 0x53, 0xc1, 0x36, 0x98, 0x22, 0x58]
* [0xb940]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6725e645, 0x4a7f, 0x9969, 0x82, 0xec, 0xd1, 0x87, 0x21, 0xde, 0x5a, 0x57]
* [0xb7f0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
* [0xb5a0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x71202eee, 0x5f53, 0x40d9, 0xab, 0x3d, 0x9e, 0xc, 0x26, 0xd9, 0x66, 0x57]
## Module: ArpDxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x612] EFI_BOOT_SERVICES->OpenProtocol
* [0x65e] EFI_BOOT_SERVICES->OpenProtocol
* [0x832] EFI_BOOT_SERVICES->OpenProtocol
* [0x8b9] EFI_BOOT_SERVICES->OpenProtocol
* [0x8f5] EFI_BOOT_SERVICES->OpenProtocol
* [0xa69] EFI_BOOT_SERVICES->OpenProtocol
* [0xf9a] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xb24] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x568] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x96b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x9ea] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xf17] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x7fb] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x2e00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0x2e20]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0x2df0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiArpServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf44c00ee, 0x1f2c, 0x4a00, 0xaa, 0x9, 0x1c, 0x9f, 0x3e, 0x8, 0x0, 0xa3]
* [0x2e10]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4b427bb, 0xba21, 0x4f16, 0xbc, 0x4e, 0x43, 0xe4, 0x16, 0xab, 0x61, 0x9c]
* [0x2e30]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x2e40]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x2e50]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x2e30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x2e40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x2e50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x2e60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2e70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x480f8ae9, 0xc46, 0x4aa9, 0xbc, 0x89, 0xdb, 0x9f, 0xba, 0x61, 0x98, 0x6]
* [0x2e20]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0x2e20]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
## Module: AsfTable
### Boot services:
* [0x351] EFI_BOOT_SERVICES->LocateProtocol
* [0x3cf] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x470]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x45de9920, 0xcd54, 0x446a, 0xa0, 0x3c, 0x22, 0xe6, 0xfb, 0xb4, 0x51, 0xe4]
* [0x480]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
## Module: ASFVerbosity
### Boot services:
* [0x33e] EFI_BOOT_SERVICES->LocateProtocol
* [0x46e] EFI_BOOT_SERVICES->LocateProtocol
* [0x301] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x530]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5e90a50d, 0x6955, 0x4a49, 0x90, 0x32, 0xda, 0x38, 0x12, 0xf8, 0xe8, 0xe5]
* [0x520]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x45de9920, 0xcd54, 0x446a, 0xa0, 0x3c, 0x22, 0xe6, 0xfb, 0xb4, 0x51, 0xe4]
* [0x540]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xf42f3752, 0x12e, 0x4812, 0x99, 0xe6, 0x49, 0xf9, 0x43, 0x4, 0x84, 0x54]
## Module: AtaPassThru
### Boot services:
* [0x332] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x5c6] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x63e] EFI_BOOT_SERVICES->HandleProtocol
* [0x6be] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* [0x1b30]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb2fa4764, 0x3b6e, 0x43d3, 0x91, 0xdf, 0x87, 0xd1, 0x5a, 0x3e, 0x56, 0x68]
* [0x1b20]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xe159a956, 0x3299, 0x4ee9, 0x91, 0x76, 0x65, 0x18, 0x1a, 0x4e, 0x5e, 0x9f]
## Module: BdatAccessHandler
### Boot services:
* [0x2cb] EFI_BOOT_SERVICES->LocateProtocol
* [0x30a] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x830]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6aa1f27, 0x5597, 0x4802, 0x9f, 0x63, 0xd6, 0x28, 0x36, 0x59, 0x86, 0x35]
* [0x820]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
## Module: Bds
### Boot services:
* [0x836] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1294] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x171c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x179e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x184b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2461] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x28c7] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x43f2] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4432] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8507] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x883d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x936c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x9a02] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xaf4a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xb75e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xba52] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xbad9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xbbc6] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xe526] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x82c4] EFI_BOOT_SERVICES->OpenProtocol
* [0xc642] EFI_BOOT_SERVICES->OpenProtocol
* [0x1570] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1558] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1a4d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x22d7] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2379] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x661a] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x66f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1528] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb42d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xdf73] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x872] EFI_BOOT_SERVICES->HandleProtocol
* [0xabe] EFI_BOOT_SERVICES->HandleProtocol
* [0xe04] EFI_BOOT_SERVICES->HandleProtocol
* [0xfab] EFI_BOOT_SERVICES->HandleProtocol
* [0x11d5] EFI_BOOT_SERVICES->HandleProtocol
* [0x12d0] EFI_BOOT_SERVICES->HandleProtocol
* [0x1305] EFI_BOOT_SERVICES->HandleProtocol
* [0x1424] EFI_BOOT_SERVICES->HandleProtocol
* [0x1883] EFI_BOOT_SERVICES->HandleProtocol
* [0x18d9] EFI_BOOT_SERVICES->HandleProtocol
* [0x1b34] EFI_BOOT_SERVICES->HandleProtocol
* [0x2900] EFI_BOOT_SERVICES->HandleProtocol
* [0x2952] EFI_BOOT_SERVICES->HandleProtocol
* [0x2b8e] EFI_BOOT_SERVICES->HandleProtocol
* [0x2db9] EFI_BOOT_SERVICES->HandleProtocol
* [0x2e13] EFI_BOOT_SERVICES->HandleProtocol
* [0x2e5d] EFI_BOOT_SERVICES->HandleProtocol
* [0x33aa] EFI_BOOT_SERVICES->HandleProtocol
* [0x461f] EFI_BOOT_SERVICES->HandleProtocol
* [0x4650] EFI_BOOT_SERVICES->HandleProtocol
* [0x4764] EFI_BOOT_SERVICES->HandleProtocol
* [0x489e] EFI_BOOT_SERVICES->HandleProtocol
* [0x4966] EFI_BOOT_SERVICES->HandleProtocol
* [0x4e14] EFI_BOOT_SERVICES->HandleProtocol
* [0x4e7c] EFI_BOOT_SERVICES->HandleProtocol
* [0x4eb8] EFI_BOOT_SERVICES->HandleProtocol
* [0x4f7c] EFI_BOOT_SERVICES->HandleProtocol
* [0x5006] EFI_BOOT_SERVICES->HandleProtocol
* [0x523a] EFI_BOOT_SERVICES->HandleProtocol
* [0x55e0] EFI_BOOT_SERVICES->HandleProtocol
* [0x579a] EFI_BOOT_SERVICES->HandleProtocol
* [0x58a4] EFI_BOOT_SERVICES->HandleProtocol
* [0x5982] EFI_BOOT_SERVICES->HandleProtocol
* [0x59ed] EFI_BOOT_SERVICES->HandleProtocol
* [0x5d2f] EFI_BOOT_SERVICES->HandleProtocol
* [0x5df7] EFI_BOOT_SERVICES->HandleProtocol
* [0x66e3] EFI_BOOT_SERVICES->HandleProtocol
* [0x676b] EFI_BOOT_SERVICES->HandleProtocol
* [0x6864] EFI_BOOT_SERVICES->HandleProtocol
* [0x854c] EFI_BOOT_SERVICES->HandleProtocol
* [0x8881] EFI_BOOT_SERVICES->HandleProtocol
* [0x90e6] EFI_BOOT_SERVICES->HandleProtocol
* [0x91af] EFI_BOOT_SERVICES->HandleProtocol
* [0x93a8] EFI_BOOT_SERVICES->HandleProtocol
* [0x93e5] EFI_BOOT_SERVICES->HandleProtocol
* [0x95c0] EFI_BOOT_SERVICES->HandleProtocol
* [0x991a] EFI_BOOT_SERVICES->HandleProtocol
* [0x9a32] EFI_BOOT_SERVICES->HandleProtocol
* [0xa4f4] EFI_BOOT_SERVICES->HandleProtocol
* [0xaf7a] EFI_BOOT_SERVICES->HandleProtocol
* [0xb029] EFI_BOOT_SERVICES->HandleProtocol
* [0xb07a] EFI_BOOT_SERVICES->HandleProtocol
* [0xb202] EFI_BOOT_SERVICES->HandleProtocol
* [0xb4a7] EFI_BOOT_SERVICES->HandleProtocol
* [0xb543] EFI_BOOT_SERVICES->HandleProtocol
* [0xb607] EFI_BOOT_SERVICES->HandleProtocol
* [0xb79a] EFI_BOOT_SERVICES->HandleProtocol
* [0xb884] EFI_BOOT_SERVICES->HandleProtocol
* [0xb8e3] EFI_BOOT_SERVICES->HandleProtocol
* [0xbbfe] EFI_BOOT_SERVICES->HandleProtocol
* [0xbe1a] EFI_BOOT_SERVICES->HandleProtocol
* [0xc76b] EFI_BOOT_SERVICES->HandleProtocol
* [0xcd92] EFI_BOOT_SERVICES->HandleProtocol
* [0xce5d] EFI_BOOT_SERVICES->HandleProtocol
* [0xd201] EFI_BOOT_SERVICES->HandleProtocol
* [0xd459] EFI_BOOT_SERVICES->HandleProtocol
* [0xd73d] EFI_BOOT_SERVICES->HandleProtocol
* [0xd803] EFI_BOOT_SERVICES->HandleProtocol
* [0xe46c] EFI_BOOT_SERVICES->HandleProtocol
* [0xe55e] EFI_BOOT_SERVICES->HandleProtocol
* [0x3cb] EFI_BOOT_SERVICES->LocateProtocol
* [0xb15] EFI_BOOT_SERVICES->LocateProtocol
* [0xbfd] EFI_BOOT_SERVICES->LocateProtocol
* [0x166b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a2b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2394] EFI_BOOT_SERVICES->LocateProtocol
* [0x2791] EFI_BOOT_SERVICES->LocateProtocol
* [0x349e] EFI_BOOT_SERVICES->LocateProtocol
* [0x4461] EFI_BOOT_SERVICES->LocateProtocol
* [0x63cb] EFI_BOOT_SERVICES->LocateProtocol
* [0x6554] EFI_BOOT_SERVICES->LocateProtocol
* [0x7922] EFI_BOOT_SERVICES->LocateProtocol
* [0x7c5b] EFI_BOOT_SERVICES->LocateProtocol
* [0x800e] EFI_BOOT_SERVICES->LocateProtocol
* [0x818f] EFI_BOOT_SERVICES->LocateProtocol
* [0x82e4] EFI_BOOT_SERVICES->LocateProtocol
* [0x8397] EFI_BOOT_SERVICES->LocateProtocol
* [0x84c3] EFI_BOOT_SERVICES->LocateProtocol
* [0xb6e6] EFI_BOOT_SERVICES->LocateProtocol
* [0xba23] EFI_BOOT_SERVICES->LocateProtocol
* [0xbcf8] EFI_BOOT_SERVICES->LocateProtocol
* [0xbd7e] EFI_BOOT_SERVICES->LocateProtocol
* [0xbef0] EFI_BOOT_SERVICES->LocateProtocol
* [0xcdb9] EFI_BOOT_SERVICES->LocateProtocol
* [0xcfe7] EFI_BOOT_SERVICES->LocateProtocol
* [0xd68d] EFI_BOOT_SERVICES->LocateProtocol
* [0xdcf5] EFI_BOOT_SERVICES->LocateProtocol
* [0xdf27] EFI_BOOT_SERVICES->LocateProtocol
* [0xe195] EFI_BOOT_SERVICES->LocateProtocol
* [0xe34d] EFI_BOOT_SERVICES->LocateProtocol
* [0xe386] EFI_BOOT_SERVICES->LocateProtocol
* [0x6681] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xafe8] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xc654] EFI_BOOT_SERVICES->CloseProtocol
* [0x6d31] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xd53f] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xeef0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0xef00]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x119b8]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0xeee0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x119a8]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0xeed0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x56ec3091, 0x954c, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xef20]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x12bf0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0xf0c0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSioProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x215fdd18, 0xbd50, 0x4feb, 0x89, 0xb, 0x58, 0xca, 0xb, 0x47, 0x39, 0xe9]
* [0xf618]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0xef90]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiBootManagerPolicyProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfedf8e0c, 0xe147, 0x11e3, 0x99, 0x3, 0xb8, 0xe8, 0x56, 0x2c, 0xba, 0xfa]
* [0xeef0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0xef00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xf030]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xef30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xef10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0xefb0]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x934ce8da, 0x5e2a, 0x4184, 0x8a, 0x15, 0x8e, 0x8, 0x47, 0x98, 0x84, 0x31]
* [0xefd0]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xdc14e697, 0x775a, 0x4c3b, 0xa1, 0x1a, 0xed, 0xc3, 0x8e, 0x1b, 0xe3, 0xe6]
* [0xeed0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x56ec3091, 0x954c, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xef50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0xef60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2b2f68d6, 0xcd2, 0x44cf, 0x8e, 0x8b, 0xbb, 0xa2, 0xb, 0x1b, 0x5b, 0x75]
* [0xefe0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x52c78312, 0x8edc, 0x4233, 0x98, 0xf2, 0x1a, 0x1a, 0xa5, 0xe3, 0x88, 0xa5]
* [0xfbc8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0xfbe8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x10530]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xef20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xf020]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0xeeb0]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2362ea9c, 0x84e5, 0x4dff, 0x83, 0xbc, 0xb5, 0xac, 0xec, 0xb5, 0x7c, 0xbb]
* [0xf090]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBusSpecificDriverOverrideProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3bc1b285, 0x8a15, 0x4a82, 0xaa, 0xbf, 0x4d, 0x7d, 0x13, 0xfb, 0x32, 0x65]
* [0xeff0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xef40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0xef80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiS3SaveProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x125f2de1, 0xfb85, 0x440c, 0xa5, 0x4c, 0x4d, 0x99, 0x35, 0x8a, 0x8d, 0x38]
* [0x10440]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0xefc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEsrtManagementProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa340c064, 0x723c, 0x4a9c, 0xa4, 0xdd, 0xd5, 0xb4, 0x7a, 0x26, 0xfb, 0xb0]
* [0xf000]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
* [0xfc18]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0xf5d8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0xf5f8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0xf628]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0xf050]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd25dc167, 0xeb6a, 0x432d, 0x65, 0x91, 0xbf, 0x80, 0x29, 0xb0, 0x5, 0xbb]
* [0xf060]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd9035175, 0x8ce2, 0x47de, 0xa8, 0xb8, 0xcc, 0x98, 0xe5, 0xe2, 0xa8, 0x85]
* [0xf170]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0xf0b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5859cb76, 0x6bef, 0x468a, 0xbe, 0x2d, 0xb3, 0xdd, 0x1a, 0x27, 0xf0, 0x12]
* [0xf0d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2ad8e2d2, 0x2e91, 0x4cd1, 0x95, 0xf5, 0xe7, 0x8f, 0xe5, 0xeb, 0xe3, 0x16]
* [0xf040]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x45de9920, 0xcd54, 0x446a, 0xa0, 0x3c, 0x22, 0xe6, 0xfb, 0xb4, 0x51, 0xe4]
## Module: BiosExtensionLoader
### Boot services:
* [0x1a2a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1d3a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2222] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2567] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x27f9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x382] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1dbb] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x1a67] EFI_BOOT_SERVICES->HandleProtocol
* [0x1ae0] EFI_BOOT_SERVICES->HandleProtocol
* [0x1d9d] EFI_BOOT_SERVICES->HandleProtocol
* [0x225d] EFI_BOOT_SERVICES->HandleProtocol
* [0x25ac] EFI_BOOT_SERVICES->HandleProtocol
* [0x2865] EFI_BOOT_SERVICES->HandleProtocol
* [0x28a0] EFI_BOOT_SERVICES->HandleProtocol
* [0x29f8] EFI_BOOT_SERVICES->HandleProtocol
* [0x2c81] EFI_BOOT_SERVICES->HandleProtocol
* [0x320] EFI_BOOT_SERVICES->LocateProtocol
* [0xbb7] EFI_BOOT_SERVICES->LocateProtocol
* [0xf5c] EFI_BOOT_SERVICES->LocateProtocol
* [0x10ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x10d4] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b35] EFI_BOOT_SERVICES->LocateProtocol
* [0x31c1] EFI_BOOT_SERVICES->LocateProtocol
* [0x31e8] EFI_BOOT_SERVICES->LocateProtocol
* [0x3250] EFI_BOOT_SERVICES->LocateProtocol
* [0x3307] EFI_BOOT_SERVICES->LocateProtocol
* [0x33ff] EFI_BOOT_SERVICES->LocateProtocol
* [0x348d] EFI_BOOT_SERVICES->LocateProtocol
* [0x3618] EFI_BOOT_SERVICES->LocateProtocol
* [0x371a] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3ac0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3ab0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x3b00]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiAtaPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x1d3de7f0, 0x807, 0x424f, 0xaa, 0x69, 0x11, 0xa5, 0x4e, 0x19, 0xa4, 0x6f]
* [0x3af0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x52c78312, 0x8edc, 0x4233, 0x98, 0xf2, 0x1a, 0x1a, 0xa5, 0xe3, 0x88, 0xa5]
* [0x3ae0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3b10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3ac0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3ab0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x3b00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAtaPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x1d3de7f0, 0x807, 0x424f, 0xaa, 0x69, 0x11, 0xa5, 0x4e, 0x19, 0xa4, 0x6f]
* [0x3af0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x52c78312, 0x8edc, 0x4233, 0x98, 0xf2, 0x1a, 0x1a, 0xa5, 0xe3, 0x88, 0xa5]
* [0x3ae0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3ad0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0x3a70]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x3b50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd25dc167, 0xeb6a, 0x432d, 0x65, 0x91, 0xbf, 0x80, 0x29, 0xb0, 0x5, 0xbb]
* [0x3a90]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x1ab1829, 0xcecd, 0x4cfa, 0xa1, 0x8c, 0xea, 0x75, 0xd6, 0x6f, 0x3e, 0x74]
* [0x3ab0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x3b20]
	 - [service] LocateProtocol
	 - [protocol_name] gPlatformSeCHookProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbc52476e, 0xf67e, 0x4301, 0xb2, 0x62, 0x36, 0x9c, 0x48, 0x78, 0xaa, 0xc2]
* [0x3b30]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb42b8d12, 0x2acb, 0x499a, 0xa9, 0x20, 0xdd, 0x5b, 0xe6, 0xcf, 0x9, 0xb1]
* [0x3b40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8d9b3387, 0x73db, 0x456f, 0x88, 0x9d, 0x6f, 0xfe, 0x90, 0x82, 0x64, 0x9]
* [0x3a80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6725e645, 0x4a7f, 0x9969, 0x82, 0xec, 0xd1, 0x87, 0x21, 0xde, 0x5a, 0x57]
## Module: BootGuardDxe
### Boot services:
* [0x422] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x600]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xdbc9fd21, 0xfad8, 0x45b0, 0x9e, 0x78, 0x27, 0x15, 0x88, 0x67, 0xcc, 0x93]
## Module: BootScriptExecutorDxe
### Boot services:
* [0x3a09] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x482] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x4b3] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1144] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1232] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x38f6] EFI_BOOT_SERVICES->HandleProtocol
* [0x3923] EFI_BOOT_SERVICES->HandleProtocol
* [0x4db] EFI_BOOT_SERVICES->LocateProtocol
* [0xc44] EFI_BOOT_SERVICES->LocateProtocol
* [0xd2c] EFI_BOOT_SERVICES->LocateProtocol
* [0xdf7] EFI_BOOT_SERVICES->LocateProtocol
* [0xf71] EFI_BOOT_SERVICES->LocateProtocol
* [0x119b] EFI_BOOT_SERVICES->LocateProtocol
* [0x42bb] EFI_BOOT_SERVICES->LocateProtocol
* [0xed0] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x68e0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x68b0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x47b7fa8c, 0xf4bd, 0x4af6, 0x82, 0x0, 0x33, 0x30, 0x86, 0xf0, 0xd2, 0xc8]
* [0x6890]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x68e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x6820]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xfa20568b, 0x548b, 0x4b2b, 0x81, 0xef, 0x1b, 0xa0, 0x8d, 0x4a, 0x3c, 0xec]
* [0x6880]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc68ed8e2, 0x9dc6, 0x4cbd, 0x9d, 0x94, 0xdb, 0x65, 0xac, 0xc5, 0xc3, 0x32]
* [0x6860]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeMmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x60ff8964, 0xe906, 0x41d0, 0xaf, 0xed, 0xf2, 0x41, 0xe9, 0x74, 0xe0, 0x8e]
* [0x68a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x6870]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
* [0x6860]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiDxeMmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x60ff8964, 0xe906, 0x41d0, 0xaf, 0xed, 0xf2, 0x41, 0xe9, 0x74, 0xe0, 0x8e]
## Module: CapsuleRuntimeDxe
### Boot services:
* [0x106b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1625] EFI_BOOT_SERVICES->LocateProtocol
* [0x16e9] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2050]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
* [0x2050]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
## Module: CmosDxe
### Boot services:
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
* [0x6b5] EFI_BOOT_SERVICES->LocateProtocol
* [0xcd0] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2600]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x25f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x9851740c, 0x22e0, 0x440d, 0x90, 0x90, 0xef, 0x2d, 0x71, 0xc2, 0x51, 0xc9]
* [0x2cf8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x9851740c, 0x22e0, 0x440d, 0x90, 0x90, 0xef, 0x2d, 0x71, 0xc2, 0x51, 0xc9]
## Module: CmosSmm
### Boot services:
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a1] EFI_BOOT_SERVICES->LocateProtocol
* [0x474] EFI_BOOT_SERVICES->LocateProtocol
* [0x66a] EFI_BOOT_SERVICES->LocateProtocol
* [0x22a5] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2900]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2930]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x2e98]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2920]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: ConSplitter
### Boot services:
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
* [0xc6f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4585] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4597] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x447] EFI_BOOT_SERVICES->HandleProtocol
* [0x53a] EFI_BOOT_SERVICES->HandleProtocol
* [0xdcb] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a73] EFI_BOOT_SERVICES->HandleProtocol
* [0x2d48] EFI_BOOT_SERVICES->HandleProtocol
* [0x2e7e] EFI_BOOT_SERVICES->HandleProtocol
* [0x23ff] EFI_BOOT_SERVICES->LocateProtocol
* [0x4674] EFI_BOOT_SERVICES->LocateProtocol
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
* [0x49c9] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x4cc0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4ca0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c1, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4cb0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdd9e7534, 0x7762, 0x4698, 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa]
* [0x4cd0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xadfb62d, 0xff74, 0x484c, 0x89, 0x44, 0xf8, 0x5c, 0x4b, 0xea, 0x87, 0xa8]
* [0x4ce0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8d59d32b, 0xc655, 0x4ae9, 0x9b, 0x15, 0xf2, 0x59, 0x4, 0x99, 0x2a, 0x43]
* [0x4c90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31878c87, 0xb75, 0x11d5, 0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x4d20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x4d10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4d40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4d00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x5288]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x4cc0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4ca0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c1, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4cd0]
	 - [service] CloseProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xadfb62d, 0xff74, 0x484c, 0x89, 0x44, 0xf8, 0x5c, 0x4b, 0xea, 0x87, 0xa8]
* [0x4cb0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdd9e7534, 0x7762, 0x4698, 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa]
* [0x4c90]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31878c87, 0xb75, 0x11d5, 0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x4ce0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8d59d32b, 0xc655, 0x4ae9, 0x9b, 0x15, 0xf2, 0x59, 0x4, 0x99, 0x2a, 0x43]
## Module: CpuDxe
### Boot services:
* [0x1636] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2238]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3fdda605, 0xa76e, 0x4f46, 0xad, 0x29, 0x12, 0xf4, 0x53, 0x1b, 0x3d, 0x8]
## Module: CpuInitDxe
### Boot services:
* [0xab9] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xc56] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x11bb] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2d69] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb3f] EFI_BOOT_SERVICES->LocateProtocol
* [0x246e] EFI_BOOT_SERVICES->LocateProtocol
* [0x26a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a76] EFI_BOOT_SERVICES->LocateProtocol
* [0x4df9] EFI_BOOT_SERVICES->LocateProtocol
* [0x5131] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x56f0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26baccb1, 0x6f42, 0x11d4, 0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
* [0x56e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMetronomeArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26baccb2, 0x6f42, 0x11d4, 0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
* [0x5710]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMmControlProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x843dc720, 0xab1e, 0x42cb, 0x93, 0x57, 0x8a, 0x0, 0x78, 0xf3, 0x56, 0x1b]
* [0x5720]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xe223cf65, 0xf6ce, 0x4122, 0xb3, 0xaf, 0x4b, 0xd1, 0x8a, 0xff, 0x40, 0xa1]
* [0x56f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26baccb1, 0x6f42, 0x11d4, 0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
* [0x5740]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xab5a4df4, 0xf0d7, 0x49a8, 0xbf, 0x5c, 0xf2, 0x5d, 0xa0, 0x4c, 0x25, 0x33]
## Module: CpuIo2Dxe
### Boot services:
* [0x2b5] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: CpuIo2Smm
### Boot services:
* [0x2d3] EFI_BOOT_SERVICES->LocateProtocol
* [0x34d] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x7d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x910]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
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
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1338]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xe50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: CrbDxe
### Boot services:
* [0x3de] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
* [0x424] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x990]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x980]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x67269263, 0xaf1, 0x45dd, 0x93, 0xc8, 0x29, 0x99, 0x21, 0xd0, 0xe1, 0xe9]
## Module: CrbSmi
### Boot services:
* [0x34c] EFI_BOOT_SERVICES->LocateProtocol
* [0x381] EFI_BOOT_SERVICES->LocateProtocol
* [0x454] EFI_BOOT_SERVICES->LocateProtocol
* [0x4ee] EFI_BOOT_SERVICES->LocateProtocol
* [0x6d3] EFI_BOOT_SERVICES->LocateProtocol
* [0x879] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xd80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xdb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x1298]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xda0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: CryptoDXE
### Boot services:
* [0x12d1] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: CryptoPkgTest
### Boot services:
* [0x31b] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* [0xb08]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x840b0034, 0x6f90, 0x4af5, 0x9a, 0xc4, 0xa1, 0x32, 0x7b, 0x7a, 0x66, 0x69]
## Module: CryptoSMM
### Boot services:
* [0x1582] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x380] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b5] EFI_BOOT_SERVICES->LocateProtocol
* [0x147c] EFI_BOOT_SERVICES->LocateProtocol
* [0x17f1] EFI_BOOT_SERVICES->LocateProtocol
* [0x15ab] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xcb60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xcb80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0xd0f8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xcb90]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: CsmBlockIo
### Boot services:
* [0x3b8] EFI_BOOT_SERVICES->OpenProtocol
* [0x40a] EFI_BOOT_SERVICES->OpenProtocol
* [0x43c] EFI_BOOT_SERVICES->OpenProtocol
* [0x47b] EFI_BOOT_SERVICES->OpenProtocol
* [0x5f8] EFI_BOOT_SERVICES->OpenProtocol
* [0x62c] EFI_BOOT_SERVICES->OpenProtocol
* [0x66e] EFI_BOOT_SERVICES->OpenProtocol
* [0xb4a] EFI_BOOT_SERVICES->OpenProtocol
* [0xca8] EFI_BOOT_SERVICES->OpenProtocol
* [0xcef] EFI_BOOT_SERVICES->OpenProtocol
* [0xd63] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x342] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa9e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x381] EFI_BOOT_SERVICES->LocateProtocol
* [0x59b] EFI_BOOT_SERVICES->LocateProtocol
* [0x5bf] EFI_BOOT_SERVICES->LocateProtocol
* [0x6c7] EFI_BOOT_SERVICES->LocateProtocol
* [0x3df] EFI_BOOT_SERVICES->CloseProtocol
* [0x4cc] EFI_BOOT_SERVICES->CloseProtocol
* [0x8b7] EFI_BOOT_SERVICES->CloseProtocol
* [0x8d5] EFI_BOOT_SERVICES->CloseProtocol
* [0xbd0] EFI_BOOT_SERVICES->CloseProtocol
* [0xbee] EFI_BOOT_SERVICES->CloseProtocol
* [0xd21] EFI_BOOT_SERVICES->CloseProtocol
* [0xdac] EFI_BOOT_SERVICES->CloseProtocol
* [0xdfa] EFI_BOOT_SERVICES->CloseProtocol
* [0xe1d] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x2850]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2e18]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5d206dd3, 0x516a, 0x47dc, 0xa1, 0xbc, 0x6d, 0xa2, 0x4, 0xaa, 0xbe, 0x8]
* [0x2820]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa1e37052, 0x80d9, 0x4e65, 0xa3, 0x17, 0x3e, 0x9a, 0x55, 0xc4, 0x3e, 0xc9]
* [0x27e0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x2800]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x27d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x27f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8e008510, 0x9bb1, 0x457d, 0x9f, 0x70, 0x89, 0x7a, 0xba, 0x86, 0x5d, 0xb9]
* [0x2830]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacy8259ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x38321dba, 0x4fe0, 0x4e17, 0x8a, 0xec, 0x41, 0x30, 0x55, 0xea, 0xed, 0xc1]
* [0x2850]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x27e0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
## Module: CsmDxe
### Boot services:
* [0x1f85] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2397] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2aa1] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2e51] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2fa0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x37b6] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3a58] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3f54] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5567] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5e6f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x68f5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6a58] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x7f1d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x9dbd] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x36d7] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x413] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x36bf] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x59c5] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x59f7] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7028] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x9a2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x832d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8d59] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xcae] EFI_BOOT_SERVICES->HandleProtocol
* [0x1fbd] EFI_BOOT_SERVICES->HandleProtocol
* [0x23cc] EFI_BOOT_SERVICES->HandleProtocol
* [0x2ad8] EFI_BOOT_SERVICES->HandleProtocol
* [0x2dbd] EFI_BOOT_SERVICES->HandleProtocol
* [0x2e0b] EFI_BOOT_SERVICES->HandleProtocol
* [0x2eb3] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fdf] EFI_BOOT_SERVICES->HandleProtocol
* [0x3061] EFI_BOOT_SERVICES->HandleProtocol
* [0x37ea] EFI_BOOT_SERVICES->HandleProtocol
* [0x3ab3] EFI_BOOT_SERVICES->HandleProtocol
* [0x3fa5] EFI_BOOT_SERVICES->HandleProtocol
* [0x3fe5] EFI_BOOT_SERVICES->HandleProtocol
* [0x400e] EFI_BOOT_SERVICES->HandleProtocol
* [0x4053] EFI_BOOT_SERVICES->HandleProtocol
* [0x5088] EFI_BOOT_SERVICES->HandleProtocol
* [0x50e1] EFI_BOOT_SERVICES->HandleProtocol
* [0x5597] EFI_BOOT_SERVICES->HandleProtocol
* [0x5878] EFI_BOOT_SERVICES->HandleProtocol
* [0x5ead] EFI_BOOT_SERVICES->HandleProtocol
* [0x65ab] EFI_BOOT_SERVICES->HandleProtocol
* [0x6662] EFI_BOOT_SERVICES->HandleProtocol
* [0x6929] EFI_BOOT_SERVICES->HandleProtocol
* [0x6b2a] EFI_BOOT_SERVICES->HandleProtocol
* [0x6e5d] EFI_BOOT_SERVICES->HandleProtocol
* [0x6f0e] EFI_BOOT_SERVICES->HandleProtocol
* [0x7316] EFI_BOOT_SERVICES->HandleProtocol
* [0x7575] EFI_BOOT_SERVICES->HandleProtocol
* [0x7f58] EFI_BOOT_SERVICES->HandleProtocol
* [0x80db] EFI_BOOT_SERVICES->HandleProtocol
* [0x9df8] EFI_BOOT_SERVICES->HandleProtocol
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
* [0x5d8] EFI_BOOT_SERVICES->LocateProtocol
* [0x602] EFI_BOOT_SERVICES->LocateProtocol
* [0x62c] EFI_BOOT_SERVICES->LocateProtocol
* [0x656] EFI_BOOT_SERVICES->LocateProtocol
* [0xf2d] EFI_BOOT_SERVICES->LocateProtocol
* [0x20a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x20de] EFI_BOOT_SERVICES->LocateProtocol
* [0x210e] EFI_BOOT_SERVICES->LocateProtocol
* [0x2488] EFI_BOOT_SERVICES->LocateProtocol
* [0x2579] EFI_BOOT_SERVICES->LocateProtocol
* [0x48f9] EFI_BOOT_SERVICES->LocateProtocol
* [0x5a8f] EFI_BOOT_SERVICES->LocateProtocol
* [0x5bf4] EFI_BOOT_SERVICES->LocateProtocol
* [0x6339] EFI_BOOT_SERVICES->LocateProtocol
* [0x6e08] EFI_BOOT_SERVICES->LocateProtocol
* [0x7db4] EFI_BOOT_SERVICES->LocateProtocol
* [0x813b] EFI_BOOT_SERVICES->LocateProtocol
* [0x81b7] EFI_BOOT_SERVICES->LocateProtocol
* [0x86b5] EFI_BOOT_SERVICES->LocateProtocol
* [0x892b] EFI_BOOT_SERVICES->LocateProtocol
* [0x93fc] EFI_BOOT_SERVICES->LocateProtocol
* [0x9c46] EFI_BOOT_SERVICES->LocateProtocol
* [0xa42b] EFI_BOOT_SERVICES->LocateProtocol
* [0x504a] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x9f4] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xa46] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x5991] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x8377] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xc550]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc4f0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0xc5a0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0xc560]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSioProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x215fdd18, 0xbd50, 0x4feb, 0x89, 0xb, 0x58, 0xca, 0xb, 0x47, 0x39, 0xe9]
* [0xc580]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSerialIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbb25cf6f, 0xf1d4, 0x11d2, 0x9a, 0xc, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0xfd]
* [0xc650]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3ea824d1, 0x81e3, 0x4ff5, 0xbd, 0x43, 0xbb, 0x9c, 0x65, 0xdf, 0x7c, 0x46]
* [0xc630]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x9400d59b, 0xe9c, 0x4f6c, 0xb5, 0x9a, 0xfc, 0x20, 0x0, 0x9d, 0xb9, 0xec]
* [0xc4a0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiLegacyBiosPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x783658a3, 0x4172, 0x4421, 0xa2, 0x99, 0xe0, 0x9, 0x7, 0x9c, 0xc, 0xb4]
* [0xd228]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xcbbee336, 0x2682, 0x4cd6, 0x81, 0x8b, 0xa, 0xd, 0x96, 0x7e, 0x5a, 0x67]
* [0xc630]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x9400d59b, 0xe9c, 0x4f6c, 0xb5, 0x9a, 0xfc, 0x20, 0x0, 0x9d, 0xb9, 0xec]
* [0xc570]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc550]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc4f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0xd4a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0xc590]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31878c87, 0xb75, 0x11d5, 0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xc670]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc560]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSioProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x215fdd18, 0xbd50, 0x4feb, 0x89, 0xb, 0x58, 0xca, 0xb, 0x47, 0x39, 0xe9]
* [0xc5c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0xc6b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0xc470]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2362ea9c, 0x84e5, 0x4dff, 0x83, 0xbc, 0xb5, 0xac, 0xec, 0xb5, 0x7c, 0xbb]
* [0xc490]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0xc5f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc6c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xc4e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyRegion2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x70101eaf, 0x85, 0x440c, 0xb3, 0x56, 0x8e, 0xe3, 0x6f, 0xef, 0x24, 0xf0]
* [0xc4a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x783658a3, 0x4172, 0x4421, 0xa2, 0x99, 0xe0, 0x9, 0x7, 0x9c, 0xc, 0xb4]
* [0xc5d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacy8259ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x38321dba, 0x4fe0, 0x4e17, 0x8a, 0xec, 0x41, 0x30, 0x55, 0xea, 0xed, 0xc1]
* [0xc5e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyInterruptProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31ce593d, 0x108a, 0x485d, 0xad, 0xb2, 0x78, 0xf2, 0x1f, 0x29, 0x66, 0xbe]
* [0xc530]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTimerArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26baccb3, 0x6f42, 0x11d4, 0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
* [0xc520]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3fdda605, 0xa76e, 0x4f46, 0xad, 0x29, 0x12, 0xf4, 0x53, 0x1b, 0x3d, 0x8]
* [0xc5b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x67820532, 0x7613, 0x4dd3, 0x9e, 0xd7, 0x3d, 0x9b, 0xe3, 0xa7, 0xda, 0x63]
* [0xc640]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2ad8e2d2, 0x2e91, 0x4cd1, 0x95, 0xf5, 0xe7, 0x8f, 0xe5, 0xeb, 0xe3, 0x16]
* [0xc500]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8e008510, 0x9bb1, 0x457d, 0x9f, 0x70, 0x89, 0x7a, 0xba, 0x86, 0x5d, 0xb9]
* [0xc6a0]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CONSOLE_CONTROL_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] [0xf42f7782, 0x12e, 0x4c12, 0x99, 0x56, 0x49, 0xf9, 0x43, 0x4, 0xf7, 0x21]
* [0xc490]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0xc690]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xdc14e697, 0x775a, 0x4c3b, 0xa1, 0x1a, 0xed, 0xc3, 0x8e, 0x1b, 0xe3, 0xe6]
* [0xd0e8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0xc680]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x4fc0733f, 0x6fd2, 0x491b, 0xa8, 0x90, 0x53, 0x74, 0x52, 0x1b, 0xf4, 0x8f]
* [0xc4f0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0xc510]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xdbc9fd21, 0xfad8, 0x45b0, 0x9e, 0x78, 0x27, 0x15, 0x88, 0x67, 0xcc, 0x93]
* [0xc610]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xf42a009d, 0x977f, 0x4f08, 0x94, 0x40, 0xbc, 0xa5, 0xa3, 0xbe, 0xd9, 0xaf]
* [0xc4f0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0xd208]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2df1e051, 0x906d, 0x4eff, 0x86, 0x9d, 0x24, 0xe6, 0x53, 0x78, 0xfb, 0x9e]
## Module: CsmVideo
### Boot services:
* [0x52b] EFI_BOOT_SERVICES->OpenProtocol
* [0x62c] EFI_BOOT_SERVICES->OpenProtocol
* [0x816] EFI_BOOT_SERVICES->OpenProtocol
* [0x85e] EFI_BOOT_SERVICES->OpenProtocol
* [0xbf5] EFI_BOOT_SERVICES->OpenProtocol
* [0xd15] EFI_BOOT_SERVICES->OpenProtocol
* [0xd52] EFI_BOOT_SERVICES->OpenProtocol
* [0xe53] EFI_BOOT_SERVICES->OpenProtocol
* [0x28aa] EFI_BOOT_SERVICES->OpenProtocol
* [0x28da] EFI_BOOT_SERVICES->OpenProtocol
* [0x294a] EFI_BOOT_SERVICES->OpenProtocol
* [0x2982] EFI_BOOT_SERVICES->OpenProtocol
* [0x2bae] EFI_BOOT_SERVICES->OpenProtocol
* [0x2bd2] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x124f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xb48] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xdfd] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xe1e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x35b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3c2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3e6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb0d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xbb7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc7c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2b4d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5f0] EFI_BOOT_SERVICES->HandleProtocol
* [0x2912] EFI_BOOT_SERVICES->HandleProtocol
* [0x4f1] EFI_BOOT_SERVICES->LocateProtocol
* [0x653] EFI_BOOT_SERVICES->LocateProtocol
* [0x14e7] EFI_BOOT_SERVICES->LocateProtocol
* [0x593] EFI_BOOT_SERVICES->CloseProtocol
* [0x7a4] EFI_BOOT_SERVICES->CloseProtocol
* [0x8ca] EFI_BOOT_SERVICES->CloseProtocol
* [0xd95] EFI_BOOT_SERVICES->CloseProtocol
* [0x29c9] EFI_BOOT_SERVICES->CloseProtocol
* [0x2bf5] EFI_BOOT_SERVICES->CloseProtocol
* [0x2c13] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x39c0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x39d0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiVgaMiniPortProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc7735a2f, 0x88f5, 0x4882, 0xae, 0x63, 0xfa, 0xac, 0x8c, 0x8b, 0x86, 0xb3]
* [0x39f0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x39f0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3a20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3970]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x39a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiEdidOverrideProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x48ecb431, 0xfb72, 0x45c0, 0xa9, 0x22, 0xf4, 0x58, 0xfe, 0x4, 0xb, 0xd5]
* [0x39c0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x39d0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiVgaMiniPortProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc7735a2f, 0x88f5, 0x4882, 0xae, 0x63, 0xfa, 0xac, 0x8c, 0x8b, 0x86, 0xb3]
## Module: DataHubDxe
### Boot services:
* empty
### Protocols:
* empty
## Module: DcScreen
### Boot services:
* [0x653] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xb78] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x69c] EFI_BOOT_SERVICES->HandleProtocol
* [0x7aa] EFI_BOOT_SERVICES->HandleProtocol
* [0x837] EFI_BOOT_SERVICES->HandleProtocol
* [0x58f] EFI_BOOT_SERVICES->LocateProtocol
* [0xb3f] EFI_BOOT_SERVICES->LocateProtocol
* [0xcac] EFI_BOOT_SERVICES->LocateProtocol
* [0xf2e] EFI_BOOT_SERVICES->LocateProtocol
* [0x1134] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2e90]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0x2e90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0x2e80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2ad8e2d2, 0x2e91, 0x4cd1, 0x95, 0xf5, 0xe7, 0x8f, 0xe5, 0xeb, 0xe3, 0x16]
* [0x28f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x4fc0733f, 0x6fd2, 0x491b, 0xa8, 0x90, 0x53, 0x74, 0x52, 0x1b, 0xf4, 0x8f]
## Module: DevicePathDxe
### Boot services:
* [0x304] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: Dhcp4Dxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5a0] EFI_BOOT_SERVICES->OpenProtocol
* [0x856] EFI_BOOT_SERVICES->OpenProtocol
* [0xa07] EFI_BOOT_SERVICES->OpenProtocol
* [0xc74] EFI_BOOT_SERVICES->OpenProtocol
* [0xd63] EFI_BOOT_SERVICES->OpenProtocol
* [0x3520] EFI_BOOT_SERVICES->OpenProtocol
* [0x3eba] EFI_BOOT_SERVICES->OpenProtocol
* [0x506e] EFI_BOOT_SERVICES->OpenProtocol
* [0x50bd] EFI_BOOT_SERVICES->OpenProtocol
* [0x5dbb] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xa9a] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xe04] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xc9b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x565] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8f0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc17] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x98b] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x3e37] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xdda] EFI_BOOT_SERVICES->CloseProtocol
* [0xe9f] EFI_BOOT_SERVICES->CloseProtocol
* [0x3783] EFI_BOOT_SERVICES->CloseProtocol
* [0x3b35] EFI_BOOT_SERVICES->CloseProtocol
* [0x511b] EFI_BOOT_SERVICES->CloseProtocol
* [0x5213] EFI_BOOT_SERVICES->CloseProtocol
* [0x5252] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x67a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x83f01464, 0x99bd, 0x45e5, 0xb3, 0x83, 0xaf, 0x63, 0x5, 0xd8, 0xe9, 0xe6]
* [0x6790]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9d9a39d8, 0xbd42, 0x4a73, 0xa4, 0xd5, 0x8e, 0xe9, 0x4b, 0xe1, 0x13, 0x80]
* [0x67c0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0x67b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0x6800]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6810]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6820]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x6790]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDhcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9d9a39d8, 0xbd42, 0x4a73, 0xa4, 0xd5, 0x8e, 0xe9, 0x4b, 0xe1, 0x13, 0x80]
* [0x67b0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0x6800]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6810]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6820]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x6830]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x67f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x480f8ae9, 0xc46, 0x4aa9, 0xbc, 0x89, 0xdb, 0x9f, 0xba, 0x61, 0x98, 0x6]
* [0x67c0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0x67c0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0x67e0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
## Module: Dhcp6Dxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x92c] EFI_BOOT_SERVICES->OpenProtocol
* [0x972] EFI_BOOT_SERVICES->OpenProtocol
* [0xac7] EFI_BOOT_SERVICES->OpenProtocol
* [0xc6c] EFI_BOOT_SERVICES->OpenProtocol
* [0xd4a] EFI_BOOT_SERVICES->OpenProtocol
* [0x1e56] EFI_BOOT_SERVICES->OpenProtocol
* [0x594c] EFI_BOOT_SERVICES->OpenProtocol
* [0x599b] EFI_BOOT_SERVICES->OpenProtocol
* [0x65eb] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xb4d] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xe0b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xc93] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x568] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9c0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc27] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x69c] EFI_BOOT_SERVICES->HandleProtocol
* [0x6635] EFI_BOOT_SERVICES->HandleProtocol
* [0x66a5] EFI_BOOT_SERVICES->HandleProtocol
* [0x6d53] EFI_BOOT_SERVICES->HandleProtocol
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0xa4b] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x1dd3] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xdc0] EFI_BOOT_SERVICES->CloseProtocol
* [0x59f5] EFI_BOOT_SERVICES->CloseProtocol
* [0x5aef] EFI_BOOT_SERVICES->CloseProtocol
* [0x5b2e] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x6e90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x66ed4721, 0x3c98, 0x4d3e, 0x81, 0xe3, 0xd0, 0x3d, 0xd3, 0x9a, 0x72, 0x54]
* [0x6eb0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9fb9a8a1, 0x2f4a, 0x43a6, 0x88, 0x9c, 0xd0, 0xf7, 0xb6, 0xc4, 0x7a, 0xd5]
* [0x6ea0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
* [0x6ec0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
* [0x6f20]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6f30]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6f40]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x6eb0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDhcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9fb9a8a1, 0x2f4a, 0x43a6, 0x88, 0x9c, 0xd0, 0xf7, 0xb6, 0xc4, 0x7a, 0xd5]
* [0x6ec0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
* [0x6f20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6f30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6f40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x6f50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6ed0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp6ConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x937fe521, 0x95ae, 0x4d1a, 0x89, 0x29, 0x48, 0xbc, 0xd9, 0xa, 0xd3, 0x1a]
* [0x6f60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6f10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6f00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x480f8ae9, 0xc46, 0x4aa9, 0xbc, 0x89, 0xdb, 0x9f, 0xba, 0x61, 0x98, 0x6]
* [0x6ea0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
* [0x6ea0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
* [0x6ef0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
## Module: DiskIoDxe
### Boot services:
* [0x35e] EFI_BOOT_SERVICES->OpenProtocol
* [0x3eb] EFI_BOOT_SERVICES->OpenProtocol
* [0x42b] EFI_BOOT_SERVICES->OpenProtocol
* [0x5f1] EFI_BOOT_SERVICES->OpenProtocol
* [0x62b] EFI_BOOT_SERVICES->OpenProtocol
* [0x686] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x6a1] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x31b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x50a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x51c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x381] EFI_BOOT_SERVICES->CloseProtocol
* [0x581] EFI_BOOT_SERVICES->CloseProtocol
* [0x737] EFI_BOOT_SERVICES->CloseProtocol
* [0x760] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x21c0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x21d0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa77b2472, 0xe282, 0x4e9f, 0xa2, 0x45, 0xc2, 0xc0, 0xe2, 0x7b, 0xbc, 0xc1]
* [0x21a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xce345171, 0xba0b, 0x11d2, 0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x21b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x151c8eae, 0x7f2c, 0x472c, 0x9e, 0x54, 0x98, 0x28, 0x19, 0x4f, 0x6a, 0x88]
* [0x21c0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x21d0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiBlockIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa77b2472, 0xe282, 0x4e9f, 0xa2, 0x45, 0xc2, 0xc0, 0xe2, 0x7b, 0xbc, 0xc1]
## Module: DnsDxe
### Boot services:
* [0x748] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xc25] EFI_BOOT_SERVICES->OpenProtocol
* [0xc61] EFI_BOOT_SERVICES->OpenProtocol
* [0xd6f] EFI_BOOT_SERVICES->OpenProtocol
* [0xe61] EFI_BOOT_SERVICES->OpenProtocol
* [0xe9d] EFI_BOOT_SERVICES->OpenProtocol
* [0xfab] EFI_BOOT_SERVICES->OpenProtocol
* [0x35ca] EFI_BOOT_SERVICES->OpenProtocol
* [0x3650] EFI_BOOT_SERVICES->OpenProtocol
* [0x5203] EFI_BOOT_SERVICES->OpenProtocol
* [0x52b3] EFI_BOOT_SERVICES->OpenProtocol
* [0x58f0] EFI_BOOT_SERVICES->OpenProtocol
* [0x5ffb] EFI_BOOT_SERVICES->OpenProtocol
* [0x6095] EFI_BOOT_SERVICES->OpenProtocol
* [0x7f9b] EFI_BOOT_SERVICES->OpenProtocol
* [0x7fe7] EFI_BOOT_SERVICES->OpenProtocol
* [0x7eb] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x834] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x87d] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xde8] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1024] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xb63] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xb9d] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xcdf] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xf1b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x7b19] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x309] EFI_BOOT_SERVICES->HandleProtocol
* [0x783] EFI_BOOT_SERVICES->HandleProtocol
* [0x80d] EFI_BOOT_SERVICES->HandleProtocol
* [0x856] EFI_BOOT_SERVICES->HandleProtocol
* [0x52de] EFI_BOOT_SERVICES->HandleProtocol
* [0x8031] EFI_BOOT_SERVICES->HandleProtocol
* [0x80a1] EFI_BOOT_SERVICES->HandleProtocol
* [0x8abf] EFI_BOOT_SERVICES->HandleProtocol
* [0x2ec] EFI_BOOT_SERVICES->LocateProtocol
* [0x357e] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x3607] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x82db] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x57a7] EFI_BOOT_SERVICES->CloseProtocol
* [0x57f4] EFI_BOOT_SERVICES->CloseProtocol
* [0x5ab2] EFI_BOOT_SERVICES->CloseProtocol
* [0x6045] EFI_BOOT_SERVICES->CloseProtocol
* [0x60db] EFI_BOOT_SERVICES->CloseProtocol
* [0x620b] EFI_BOOT_SERVICES->CloseProtocol
* [0x624a] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x8be0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb625b186, 0xe063, 0x44f7, 0x89, 0x5, 0x6a, 0x74, 0xdc, 0x6f, 0x52, 0xb4]
* [0x8c00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x83f01464, 0x99bd, 0x45e5, 0xb3, 0x83, 0xaf, 0x63, 0x5, 0xd8, 0xe9, 0xe6]
* [0x8c70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7f1647c8, 0xb76e, 0x44b2, 0xa5, 0x65, 0xf7, 0xf, 0xf1, 0x9c, 0xd1, 0x9e]
* [0x8c90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x66ed4721, 0x3c98, 0x4d3e, 0x81, 0xe3, 0xd0, 0x3d, 0xd3, 0x9a, 0x72, 0x54]
* [0x8c80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xca37bc1f, 0xa327, 0x4ae9, 0x82, 0x8a, 0x8c, 0x40, 0xd8, 0x50, 0x6a, 0x17]
* [0x8bf0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xae3d28cc, 0xe05b, 0x4fa1, 0xa0, 0x11, 0x7e, 0xb5, 0x5a, 0x3f, 0x14, 0x1]
* [0x8c60]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0x8c30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0x8cc0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
* [0x8c10]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0x8ca0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
* [0x8cf0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x8d00]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x8d10]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x8be0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDns4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb625b186, 0xe063, 0x44f7, 0x89, 0x5, 0x6a, 0x74, 0xdc, 0x6f, 0x52, 0xb4]
* [0x8c70]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDns6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7f1647c8, 0xb76e, 0x44b2, 0xa5, 0x65, 0xf7, 0xf, 0xf1, 0x9c, 0xd1, 0x9e]
* [0x8d20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x8cf0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x8d00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x8d10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x8c40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp4Config2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b446ed1, 0xe30b, 0x4faa, 0x87, 0x1a, 0x36, 0x54, 0xec, 0xa3, 0x60, 0x80]
* [0x8d30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x8ce0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x8cd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x480f8ae9, 0xc46, 0x4aa9, 0xbc, 0x89, 0xdb, 0x9f, 0xba, 0x61, 0x98, 0x6]
* [0x8ca0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
* [0x8c10]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0x8c30]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0x8c60]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0x8cc0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
* [0x8c10]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0x8ca0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
## Module: DpcDxe
### Boot services:
* [0x2f2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: Dptf
### Boot services:
* [0x39b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x60f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3cd] EFI_BOOT_SERVICES->HandleProtocol
* [0x641] EFI_BOOT_SERVICES->HandleProtocol
* [0x482] EFI_BOOT_SERVICES->LocateProtocol
* [0x6f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x7db] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x8a0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x8a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x8b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
* [0x8c0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
## Module: DxeBoardConfigInit
### Boot services:
* [0xdb3] EFI_BOOT_SERVICES->HandleProtocol
* [0x1690] EFI_BOOT_SERVICES->HandleProtocol
* [0x1f23] EFI_BOOT_SERVICES->HandleProtocol
* [0x3f3] EFI_BOOT_SERVICES->LocateProtocol
* [0x5e3] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2ae0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd9035175, 0x8ce2, 0x47de, 0xa8, 0xb8, 0xcc, 0x98, 0xe5, 0xe2, 0xa8, 0x85]
* [0x2af0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
## Module: DxeCore
### Boot services:
* [0x1278d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x12870] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1946] EFI_BOOT_SERVICES->HandleProtocol
* [0xff38] EFI_BOOT_SERVICES->HandleProtocol
* [0x1002a] EFI_BOOT_SERVICES->HandleProtocol
* [0x10239] EFI_BOOT_SERVICES->HandleProtocol
* [0x102ef] EFI_BOOT_SERVICES->HandleProtocol
* [0x127ce] EFI_BOOT_SERVICES->HandleProtocol
* [0x128ab] EFI_BOOT_SERVICES->HandleProtocol
* [0x12d9e] EFI_BOOT_SERVICES->LocateProtocol
* [0x12f16] EFI_BOOT_SERVICES->LocateProtocol
* [0x12f34] EFI_BOOT_SERVICES->LocateProtocol
* [0xdfce] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x135a8] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x135fa] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x19770]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x19780]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x19770]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x196f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x19710]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFile2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4006c0c1, 0xfcb3, 0x403e, 0x99, 0x6d, 0x4a, 0x6c, 0x87, 0x24, 0xe0, 0x6d]
* [0x19700]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x56ec3091, 0x954c, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x198d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf541796d, 0xa62e, 0x4954, 0xa7, 0x75, 0x95, 0x84, 0xf6, 0x1b, 0x9c, 0xdd]
* [0x19978]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x78092548, 0x48cf, 0x449b, 0x9b, 0xdb, 0xf6, 0x38, 0x49, 0x85, 0x64, 0x60]
* [0x19978]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x78092548, 0x48cf, 0x449b, 0x9b, 0xdb, 0xf6, 0x38, 0x49, 0x85, 0x64, 0x60]
* [0x198d0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf541796d, 0xa62e, 0x4954, 0xa7, 0x75, 0x95, 0x84, 0xf6, 0x1b, 0x9c, 0xdd]
## Module: DxeOverClock
### Boot services:
* [0x726] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x650] EFI_BOOT_SERVICES->LocateProtocol
* [0x6a6] EFI_BOOT_SERVICES->LocateProtocol
* [0x74c] EFI_BOOT_SERVICES->LocateProtocol
* [0x889] EFI_BOOT_SERVICES->LocateProtocol
* [0x9cd] EFI_BOOT_SERVICES->LocateProtocol
* [0xb34] EFI_BOOT_SERVICES->LocateProtocol
* [0xc14] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b5f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1cab] EFI_BOOT_SERVICES->LocateProtocol
* [0x1de3] EFI_BOOT_SERVICES->LocateProtocol
* [0x6f6] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x838] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2000]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb42b8d12, 0x2acb, 0x499a, 0xa9, 0x20, 0xdd, 0x5b, 0xe6, 0xcf, 0x9, 0xb1]
* [0x1ff0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd4d2f201, 0x50e8, 0x4d45, 0x8e, 0x5, 0xfd, 0x49, 0xa8, 0x2a, 0x15, 0x69]
* [0x2020]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x2010]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x92c7d0bb, 0x679e, 0x479d, 0x87, 0x8d, 0xd4, 0xb8, 0x29, 0x68, 0x57, 0x8b]
* [0x2030]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd9035175, 0x8ce2, 0x47de, 0xa8, 0xb8, 0xcc, 0x98, 0xe5, 0xe2, 0xa8, 0x85]
* [0x2060]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8d9b3387, 0x73db, 0x456f, 0x88, 0x9d, 0x6f, 0xfe, 0x90, 0x82, 0x64, 0x9]
* [0x1ff0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd4d2f201, 0x50e8, 0x4d45, 0x8e, 0x5, 0xfd, 0x49, 0xa8, 0x2a, 0x15, 0x69]
* [0x2050]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xf2a128ff, 0x257b, 0x456e, 0x9d, 0xe8, 0x63, 0xe7, 0xc7, 0xdc, 0xdf, 0xac]
## Module: EbcDxe
### Boot services:
* [0x368] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x56f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5cd] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x421] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4f8] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x3c9] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x3a0] EFI_BOOT_SERVICES->HandleProtocol
* [0x5a4] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* empty
## Module: EnglishDxe
### Boot services:
* [0x3b8] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: EsrtDxe
### Boot services:
* [0x68e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x36a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x7c5] EFI_BOOT_SERVICES->HandleProtocol
* [0xaed] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x14c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareManagementProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x86c77a67, 0xb97, 0x4633, 0xa1, 0x87, 0x49, 0x10, 0x4d, 0x6, 0x85, 0xc7]
* [0x14e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
## Module: ExportHiiDb
### Boot services:
* empty
### Protocols:
* empty
## Module: FastBootOption
### Boot services:
* empty
### Protocols:
* empty
## Module: FastBootRuntime
### Boot services:
* [0x148c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1155] EFI_BOOT_SERVICES->LocateProtocol
* [0x11bf] EFI_BOOT_SERVICES->LocateProtocol
* [0x120e] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2598]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x302cb4f, 0xaf05, 0x4a16, 0x99, 0xa9, 0x31, 0xad, 0xcf, 0x87, 0x8, 0x90]
* [0x2010]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x25d8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiVariableArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x1e5668e2, 0x8481, 0x11d4, 0xbc, 0xf1, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
* [0x25d8]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiVariableArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x1e5668e2, 0x8481, 0x11d4, 0xbc, 0xf1, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
## Module: Fat
### Boot services:
* [0x18f3] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1960] EFI_BOOT_SERVICES->OpenProtocol
* [0x5e52] EFI_BOOT_SERVICES->OpenProtocol
* [0x14a3] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x61b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1432] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5a9] EFI_BOOT_SERVICES->HandleProtocol
* [0x5e74] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x2c0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xce345171, 0xba0b, 0x11d2, 0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x350]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2c0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xce345171, 0xba0b, 0x11d2, 0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
## Module: FirmwareVersionInfoDxe
### Boot services:
* [0x397] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3ca] EFI_BOOT_SERVICES->HandleProtocol
* [0xe7b] EFI_BOOT_SERVICES->LocateProtocol
* [0xfdb] EFI_BOOT_SERVICES->LocateProtocol
* [0xf8d] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x1340]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x1340]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x13a0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
* [0x1390]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3583ff6, 0xcb36, 0x4940, 0x94, 0x7e, 0xb9, 0xb3, 0x9f, 0x4a, 0xfa, 0xf7]
## Module: FlashDriver
### Boot services:
* [0x108a] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1183] EFI_BOOT_SERVICES->LocateProtocol
* [0x120a] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x6030]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x755b6596, 0x6896, 0x4ba3, 0xb3, 0xdd, 0x1c, 0x62, 0x9f, 0xd1, 0xea, 0x88]
* [0x6040]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
## Module: FlashDriverSmm
### Boot services:
* [0x660] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x3a8] EFI_BOOT_SERVICES->LocateProtocol
* [0x3dd] EFI_BOOT_SERVICES->LocateProtocol
* [0x46b] EFI_BOOT_SERVICES->LocateProtocol
* [0x4c9] EFI_BOOT_SERVICES->LocateProtocol
* [0x685] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x6aa] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x4630]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xecb867ab, 0x8df4, 0x492d, 0x81, 0x50, 0xa7, 0xfd, 0x1b, 0x9b, 0x5a, 0x75]
* [0x4640]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x4650]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x4f10]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
## Module: FlashSmiDxe
### Boot services:
* [0x11ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x11e2] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a57] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a9e] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d01] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x3030]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x3020]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc68ed8e2, 0x9dc6, 0x4cbd, 0x9d, 0x94, 0xdb, 0x65, 0xac, 0xc5, 0xc3, 0x32]
* [0x3010]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x755b6596, 0x6896, 0x4ba3, 0xb3, 0xdd, 0x1c, 0x62, 0x9f, 0xd1, 0xea, 0x88]
## Module: FlashSmiSmm
### Boot services:
* [0x2c2] EFI_BOOT_SERVICES->LocateProtocol
* [0x57c] EFI_BOOT_SERVICES->LocateProtocol
* [0x745] EFI_BOOT_SERVICES->LocateProtocol
* [0x82d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xbd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xbc0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xecb867ab, 0x8df4, 0x492d, 0x81, 0x50, 0xa7, 0xfd, 0x1b, 0x9b, 0x5a, 0x75]
* [0xc00]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
* [0x10e8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
## Module: GBT_SleepSMI
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x458] EFI_BOOT_SERVICES->LocateProtocol
* [0x727] EFI_BOOT_SERVICES->LocateProtocol
* [0x8cd] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xc60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1168]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xc80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: GenericSio
### Boot services:
* [0x11b4] EFI_BOOT_SERVICES->OpenProtocol
* [0x1217] EFI_BOOT_SERVICES->OpenProtocol
* [0x1248] EFI_BOOT_SERVICES->OpenProtocol
* [0x2550] EFI_BOOT_SERVICES->OpenProtocol
* [0x29dd] EFI_BOOT_SERVICES->OpenProtocol
* [0x2a73] EFI_BOOT_SERVICES->OpenProtocol
* [0x2d9c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xd0c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2513] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
* [0x71f] EFI_BOOT_SERVICES->LocateProtocol
* [0x7af] EFI_BOOT_SERVICES->LocateProtocol
* [0x3541] EFI_BOOT_SERVICES->LocateProtocol
* [0x4361] EFI_BOOT_SERVICES->LocateProtocol
* [0x44d8] EFI_BOOT_SERVICES->LocateProtocol
* [0x5406] EFI_BOOT_SERVICES->LocateProtocol
* [0x11ea] EFI_BOOT_SERVICES->CloseProtocol
* [0x13b4] EFI_BOOT_SERVICES->CloseProtocol
* [0x2a36] EFI_BOOT_SERVICES->CloseProtocol
* [0x2d48] EFI_BOOT_SERVICES->CloseProtocol
* [0x2e7b] EFI_BOOT_SERVICES->CloseProtocol
* [0x3acf] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x56f0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x5700]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x5720]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x5690]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x4250cec2, 0xdddb, 0x400b, 0x8c, 0x62, 0xcf, 0x98, 0x64, 0xf6, 0xd1, 0x54]
* [0x5670]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x9d36f7ef, 0x6078, 0x4419, 0x8c, 0x46, 0x2b, 0xbd, 0xb0, 0xe0, 0xc7, 0xb3]
* [0x56c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc68ed8e2, 0x9dc6, 0x4cbd, 0x9d, 0x94, 0xdb, 0x65, 0xac, 0xc5, 0xc3, 0x32]
* [0x5cb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xeb97088e, 0xcfdf, 0x49c6, 0xbe, 0x4b, 0xd9, 0x6, 0xa5, 0xb2, 0xe, 0x86]
* [0x5c58]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x5730]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x4fc0733f, 0x6fd2, 0x491b, 0xa8, 0x90, 0x53, 0x74, 0x52, 0x1b, 0xf4, 0x8f]
* [0x56f0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x5700]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x5710]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiVariableWriteArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6441f818, 0x6362, 0x4e44, 0xb5, 0x70, 0x7d, 0xba, 0x31, 0xdd, 0x24, 0x53]
## Module: GopDebugDxe
### Boot services:
* [0x338] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* [0x470]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiDebugPortDevicePathGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xeba4e8d2, 0x3858, 0x41ec, 0xa2, 0x81, 0x26, 0x47, 0xba, 0x96, 0x60, 0xd0]
## Module: GraphicsConsole
### Boot services:
* [0x68b] EFI_BOOT_SERVICES->OpenProtocol
* [0x6d9] EFI_BOOT_SERVICES->OpenProtocol
* [0x810] EFI_BOOT_SERVICES->OpenProtocol
* [0xa0f] EFI_BOOT_SERVICES->OpenProtocol
* [0xa79] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x3a3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x956] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x6f9] EFI_BOOT_SERVICES->LocateProtocol
* [0x83b] EFI_BOOT_SERVICES->LocateProtocol
* [0x20b2] EFI_BOOT_SERVICES->LocateProtocol
* [0x23eb] EFI_BOOT_SERVICES->LocateProtocol
* [0x6ae] EFI_BOOT_SERVICES->CloseProtocol
* [0x977] EFI_BOOT_SERVICES->CloseProtocol
* [0xa41] EFI_BOOT_SERVICES->CloseProtocol
* [0xa9c] EFI_BOOT_SERVICES->CloseProtocol
* [0x34a] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x3070]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x3040]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3060]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3080]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x3660]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x3070]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x3060]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x3090]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
## Module: HardwareSignatureEntry
### Boot services:
* [0x763] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x13b1] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x344] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7b3] EFI_BOOT_SERVICES->HandleProtocol
* [0x1480] EFI_BOOT_SERVICES->HandleProtocol
* [0x18d0] EFI_BOOT_SERVICES->LocateProtocol
* [0x1973] EFI_BOOT_SERVICES->LocateProtocol
* [0x1dcd] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x24a8]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x43169678, 0x506c, 0x46fe, 0xb3, 0x2a, 0xfc, 0xb3, 0x1, 0xf7, 0x4f, 0xbd]
## Module: HddAcousticDynamicSetup
### Boot services:
* [0x693] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1b44] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x732] EFI_BOOT_SERVICES->OpenProtocol
* [0xae7] EFI_BOOT_SERVICES->OpenProtocol
* [0xb81] EFI_BOOT_SERVICES->OpenProtocol
* [0xced] EFI_BOOT_SERVICES->OpenProtocol
* [0x1012] EFI_BOOT_SERVICES->OpenProtocol
* [0x1dc9] EFI_BOOT_SERVICES->OpenProtocol
* [0x377e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x6e4] EFI_BOOT_SERVICES->HandleProtocol
* [0x7d9] EFI_BOOT_SERVICES->HandleProtocol
* [0xaa9] EFI_BOOT_SERVICES->HandleProtocol
* [0xc9c] EFI_BOOT_SERVICES->HandleProtocol
* [0xda8] EFI_BOOT_SERVICES->HandleProtocol
* [0xfc3] EFI_BOOT_SERVICES->HandleProtocol
* [0x10c8] EFI_BOOT_SERVICES->HandleProtocol
* [0x1d8c] EFI_BOOT_SERVICES->HandleProtocol
* [0x36fe] EFI_BOOT_SERVICES->HandleProtocol
* [0x324] EFI_BOOT_SERVICES->LocateProtocol
* [0x342] EFI_BOOT_SERVICES->LocateProtocol
* [0x35f] EFI_BOOT_SERVICES->LocateProtocol
* [0x37c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3f3] EFI_BOOT_SERVICES->LocateProtocol
* [0x1df0] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f52] EFI_BOOT_SERVICES->LocateProtocol
* [0x309e] EFI_BOOT_SERVICES->LocateProtocol
* [0x33d7] EFI_BOOT_SERVICES->LocateProtocol
* [0x1eef] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x5100]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0x5140]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x5110]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb2fa4764, 0x3b6e, 0x43d3, 0x91, 0xdf, 0x87, 0xd1, 0x5a, 0x3e, 0x56, 0x68]
* [0x5120]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xe159a956, 0x3299, 0x4ee9, 0x91, 0x76, 0x65, 0x18, 0x1a, 0x4e, 0x5e, 0x9f]
* [0x56c8]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0x5150]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x5100]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0x5130]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x57c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x5900]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x50f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x5180]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x5190]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x5160]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x56d8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x51a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb9d4c360, 0xbcfb, 0x4f9b, 0x92, 0x98, 0x53, 0xc1, 0x36, 0x98, 0x22, 0x58]
* [0x5688]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
## Module: HddSmart
### Boot services:
* [0x402] EFI_BOOT_SERVICES->OpenProtocol
* [0xf47] EFI_BOOT_SERVICES->OpenProtocol
* [0x4d3] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1253] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x324] EFI_BOOT_SERVICES->LocateProtocol
* [0x342] EFI_BOOT_SERVICES->LocateProtocol
* [0x35f] EFI_BOOT_SERVICES->LocateProtocol
* [0x37c] EFI_BOOT_SERVICES->LocateProtocol
* [0x427] EFI_BOOT_SERVICES->LocateProtocol
* [0xb35] EFI_BOOT_SERVICES->LocateProtocol
* [0x23ae] EFI_BOOT_SERVICES->LocateProtocol
* [0x26e7] EFI_BOOT_SERVICES->LocateProtocol
* [0x306c] EFI_BOOT_SERVICES->LocateProtocol
* [0x8b1] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x3d58]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0x3700]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xffbd9ad2, 0xf1db, 0x4f92, 0xa6, 0x49, 0xeb, 0x9e, 0xed, 0xea, 0x86, 0xb5]
* [0x3740]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x3760]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x3770]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x3730]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x3d68]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x3710]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0x3d18]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x3800]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x3720]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xdbc9fd21, 0xfad8, 0x45b0, 0x9e, 0x78, 0x27, 0x15, 0x88, 0x67, 0xcc, 0x93]
## Module: HeciInit
### Boot services:
* [0x4ce] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x30f] EFI_BOOT_SERVICES->LocateProtocol
* [0x4fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x6ce] EFI_BOOT_SERVICES->LocateProtocol
* [0x9fa] EFI_BOOT_SERVICES->LocateProtocol
* [0xaa9] EFI_BOOT_SERVICES->LocateProtocol
* [0x158e] EFI_BOOT_SERVICES->LocateProtocol
* [0x169f] EFI_BOOT_SERVICES->LocateProtocol
* [0x583] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2cf0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0x2cb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3583ff6, 0xcb36, 0x4940, 0x94, 0x7e, 0xb9, 0xb3, 0x9f, 0x4a, 0xfa, 0xf7]
* [0x2c90]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x2cd0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xa0b5dc52, 0x4f34, 0x3990, 0xd4, 0x91, 0x10, 0x8b, 0xe8, 0xba, 0x75, 0x42]
* [0x2ce0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8d9b3387, 0x73db, 0x456f, 0x88, 0x9d, 0x6f, 0xfe, 0x90, 0x82, 0x64, 0x9]
* [0x2cb0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3583ff6, 0xcb36, 0x4940, 0x94, 0x7e, 0xb9, 0xb3, 0x9f, 0x4a, 0xfa, 0xf7]
## Module: HiiDatabase
### Boot services:
* [0x42ba] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xce48] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8d3f] EFI_BOOT_SERVICES->OpenProtocol
* [0x8da9] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x3f6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x43e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8ca6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xdfb6] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xe00a] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x3ffa] EFI_BOOT_SERVICES->HandleProtocol
* [0x4305] EFI_BOOT_SERVICES->HandleProtocol
* [0x4832] EFI_BOOT_SERVICES->HandleProtocol
* [0x85f6] EFI_BOOT_SERVICES->HandleProtocol
* [0xce8a] EFI_BOOT_SERVICES->HandleProtocol
* [0x14d5f] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* [0x15090]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiHiiConfigAccessProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x330d4706, 0xf2a0, 0x4e4f, 0xa3, 0x69, 0xb6, 0x6f, 0xa8, 0xd5, 0x43, 0x85]
* [0x150b0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x15000]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x348c4d62, 0xbfbd, 0x4882, 0x9e, 0xce, 0xc8, 0xb, 0xb1, 0xc4, 0x78, 0x3b]
* [0x15090]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiHiiConfigAccessProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x330d4706, 0xf2a0, 0x4e4f, 0xa3, 0x69, 0xb6, 0x6f, 0xa8, 0xd5, 0x43, 0x85]
* [0x15030]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x150b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
## Module: HpetTimerDxe
### Boot services:
* [0xa7a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x805] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xe10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26baccb1, 0x6f42, 0x11d4, 0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
## Module: HstiSiliconDxe
### Boot services:
* [0x37e5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x364] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x955] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x53d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3836] EFI_BOOT_SERVICES->HandleProtocol
* [0x32d] EFI_BOOT_SERVICES->LocateProtocol
* [0x7d6] EFI_BOOT_SERVICES->LocateProtocol
* [0xe28] EFI_BOOT_SERVICES->LocateProtocol
* [0x104c] EFI_BOOT_SERVICES->LocateProtocol
* [0x15ce] EFI_BOOT_SERVICES->LocateProtocol
* [0x44da] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x46e0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiAdapterInformationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe5dd1403, 0xd622, 0xc24e, 0x84, 0x88, 0xc7, 0x1b, 0x17, 0xf5, 0xe8, 0x2]
* [0x4680]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x1b05de41, 0xc93b, 0x4bb4, 0xad, 0x47, 0x2a, 0x78, 0xac, 0xf, 0xc9, 0xe4]
* [0x46b0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xf500be6, 0xece4, 0x4ed8, 0x90, 0x81, 0x9a, 0xa9, 0xa5, 0x23, 0xfb, 0x7b]
* [0x46e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAdapterInformationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe5dd1403, 0xd622, 0xc24e, 0x84, 0x88, 0xc7, 0x1b, 0x17, 0xf5, 0xe8, 0x2]
* [0x46a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xeca27516, 0x306c, 0x4e28, 0x8c, 0x94, 0x4e, 0x52, 0x10, 0x96, 0x69, 0x5e]
* [0x4690]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3fdda605, 0xa76e, 0x4f46, 0xad, 0x29, 0x12, 0xf4, 0x53, 0x1b, 0x3d, 0x8]
* [0x46d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc7d289, 0x1347, 0x4de0, 0xbf, 0x42, 0xe, 0x26, 0x9d, 0xe, 0xf3, 0x4a]
* [0x46c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTrEEProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x607f766c, 0x7455, 0x42be, 0x93, 0xb, 0xe4, 0xd7, 0x6d, 0xb2, 0x72, 0xf]
## Module: HttpBootDxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8c9] EFI_BOOT_SERVICES->OpenProtocol
* [0x8f9] EFI_BOOT_SERVICES->OpenProtocol
* [0x929] EFI_BOOT_SERVICES->OpenProtocol
* [0x980] EFI_BOOT_SERVICES->OpenProtocol
* [0xa02] EFI_BOOT_SERVICES->OpenProtocol
* [0xa3d] EFI_BOOT_SERVICES->OpenProtocol
* [0xb25] EFI_BOOT_SERVICES->OpenProtocol
* [0xb5f] EFI_BOOT_SERVICES->OpenProtocol
* [0xcad] EFI_BOOT_SERVICES->OpenProtocol
* [0xd32] EFI_BOOT_SERVICES->OpenProtocol
* [0xd78] EFI_BOOT_SERVICES->OpenProtocol
* [0xe75] EFI_BOOT_SERVICES->OpenProtocol
* [0xea5] EFI_BOOT_SERVICES->OpenProtocol
* [0xed5] EFI_BOOT_SERVICES->OpenProtocol
* [0xf2c] EFI_BOOT_SERVICES->OpenProtocol
* [0xfae] EFI_BOOT_SERVICES->OpenProtocol
* [0xfe9] EFI_BOOT_SERVICES->OpenProtocol
* [0x10d1] EFI_BOOT_SERVICES->OpenProtocol
* [0x1137] EFI_BOOT_SERVICES->OpenProtocol
* [0x1171] EFI_BOOT_SERVICES->OpenProtocol
* [0x12bf] EFI_BOOT_SERVICES->OpenProtocol
* [0x1342] EFI_BOOT_SERVICES->OpenProtocol
* [0x1388] EFI_BOOT_SERVICES->OpenProtocol
* [0x18e5] EFI_BOOT_SERVICES->OpenProtocol
* [0x1d6d] EFI_BOOT_SERVICES->OpenProtocol
* [0x23df] EFI_BOOT_SERVICES->OpenProtocol
* [0x911f] EFI_BOOT_SERVICES->OpenProtocol
* [0x916b] EFI_BOOT_SERVICES->OpenProtocol
* [0xbabe] EFI_BOOT_SERVICES->OpenProtocol
* [0xbafa] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xe02] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1412] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xa80] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x102c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x65b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x737] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x858] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x41e1] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xc72] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1284] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x40a3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8a61] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4478] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x44a7] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x457] EFI_BOOT_SERVICES->HandleProtocol
* [0x17f2] EFI_BOOT_SERVICES->HandleProtocol
* [0x85cb] EFI_BOOT_SERVICES->HandleProtocol
* [0x91b5] EFI_BOOT_SERVICES->HandleProtocol
* [0x9225] EFI_BOOT_SERVICES->HandleProtocol
* [0x92b8] EFI_BOOT_SERVICES->HandleProtocol
* [0x9308] EFI_BOOT_SERVICES->HandleProtocol
* [0xb6e6] EFI_BOOT_SERVICES->HandleProtocol
* [0xb8a1] EFI_BOOT_SERVICES->HandleProtocol
* [0xbcb0] EFI_BOOT_SERVICES->HandleProtocol
* [0xbcd3] EFI_BOOT_SERVICES->HandleProtocol
* [0xbdd5] EFI_BOOT_SERVICES->HandleProtocol
* [0xbe5d] EFI_BOOT_SERVICES->HandleProtocol
* [0xbea8] EFI_BOOT_SERVICES->HandleProtocol
* [0x4bc] EFI_BOOT_SERVICES->LocateProtocol
* [0x4da] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f7] EFI_BOOT_SERVICES->LocateProtocol
* [0x514] EFI_BOOT_SERVICES->LocateProtocol
* [0x531] EFI_BOOT_SERVICES->LocateProtocol
* [0x3519] EFI_BOOT_SERVICES->LocateProtocol
* [0x35af] EFI_BOOT_SERVICES->LocateProtocol
* [0x375d] EFI_BOOT_SERVICES->LocateProtocol
* [0x8c63] EFI_BOOT_SERVICES->LocateProtocol
* [0xb1a8] EFI_BOOT_SERVICES->LocateProtocol
* [0x1459] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x1493] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x14dd] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x1517] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x6a7] EFI_BOOT_SERVICES->CloseProtocol
* [0x701] EFI_BOOT_SERVICES->CloseProtocol
* [0x78b] EFI_BOOT_SERVICES->CloseProtocol
* [0x7c8] EFI_BOOT_SERVICES->CloseProtocol
* [0x822] EFI_BOOT_SERVICES->CloseProtocol
* [0x1a3f] EFI_BOOT_SERVICES->CloseProtocol
* [0x1fe8] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0xc130]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9d9a39d8, 0xbd42, 0x4a73, 0xa4, 0xd5, 0x8e, 0xe9, 0x4b, 0xe1, 0x13, 0x80]
* [0xc110]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHttpServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbdc8e6af, 0xd9bc, 0x4379, 0xa7, 0x2a, 0xe0, 0xc4, 0xe7, 0x5d, 0xae, 0x1c]
* [0xc0f0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc020]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xecebcb00, 0xd9c8, 0x11e4, 0xaf, 0x3d, 0x8c, 0xdc, 0xd4, 0x26, 0xc9, 0x73]
* [0xc1d0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiNetworkInterfaceIdentifierProtocolGuid_31
	 - [protocol_place] edk2_guids
	 - [guid] [0x1aced566, 0x76ed, 0x4218, 0xbc, 0x81, 0x76, 0x7f, 0x1f, 0x97, 0x7a, 0x89]
* [0xc140]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0xc150]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4Config2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b446ed1, 0xe30b, 0x4faa, 0x87, 0x1a, 0x36, 0x54, 0xec, 0xa3, 0x60, 0x80]
* [0xc100]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x56ec3091, 0x954c, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc160]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9fb9a8a1, 0x2f4a, 0x43a6, 0x88, 0x9c, 0xd0, 0xf7, 0xb6, 0xc4, 0x7a, 0xd5]
* [0xc170]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
* [0xc1b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2c8759d5, 0x5c2d, 0x66ef, 0x92, 0x5f, 0xb6, 0x6c, 0x10, 0x19, 0x57, 0xe2]
* [0xc1c0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x937fe521, 0x95ae, 0x4d1a, 0x89, 0x29, 0x48, 0xbc, 0xd9, 0xa, 0xd3, 0x1a]
* [0xc190]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xca37bc1f, 0xa327, 0x4ae9, 0x82, 0x8a, 0x8c, 0x40, 0xd8, 0x50, 0x6a, 0x17]
* [0xc120]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHttpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7a59b29b, 0x910b, 0x4171, 0x82, 0x42, 0xa8, 0x5a, 0xd, 0xf2, 0x5b, 0x5b]
* [0xc200]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0xc230]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xc240]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0xc020]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xecebcb00, 0xd9c8, 0x11e4, 0xaf, 0x3d, 0x8c, 0xdc, 0xd4, 0x26, 0xc9, 0x73]
* [0xc020]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xecebcb00, 0xd9c8, 0x11e4, 0xaf, 0x3d, 0x8c, 0xdc, 0xd4, 0x26, 0xc9, 0x73]
* [0xc0f0]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc200]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0xc230]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xc240]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0xc2c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc1c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp6ConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x937fe521, 0x95ae, 0x4d1a, 0x89, 0x29, 0x48, 0xbc, 0xd9, 0xa, 0xd3, 0x1a]
* [0xc0f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc290]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xc2b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0xc2a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0xc310]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0xc300]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2b2f68d6, 0xcd2, 0x44cf, 0x8e, 0x8b, 0xbb, 0xa2, 0xb, 0x1b, 0x5b, 0x75]
* [0xc100]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x56ec3091, 0x954c, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc2e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc2d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc250]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0xc270]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0xc280]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0xc220]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0xc260]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
* [0xc320]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0xc210]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0xc1e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiRamDiskProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xab38a0df, 0x6873, 0x44a9, 0x87, 0xe6, 0xd4, 0xeb, 0x56, 0x14, 0x84, 0x49]
* [0xc2f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
* [0xc120]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiHttpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7a59b29b, 0x910b, 0x4171, 0x82, 0x42, 0xa8, 0x5a, 0xd, 0xf2, 0x5b, 0x5b]
* [0xc140]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0xc170]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
* [0xc140]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0xc020]
	 - [service] CloseProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xecebcb00, 0xd9c8, 0x11e4, 0xaf, 0x3d, 0x8c, 0xdc, 0xd4, 0x26, 0xc9, 0x73]
* [0xc1b0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2c8759d5, 0x5c2d, 0x66ef, 0x92, 0x5f, 0xb6, 0x6c, 0x10, 0x19, 0x57, 0xe2]
* [0xc170]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
* [0xc190]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDns6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xca37bc1f, 0xa327, 0x4ae9, 0x82, 0x8a, 0x8c, 0x40, 0xd8, 0x50, 0x6a, 0x17]
* [0xc120]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiHttpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7a59b29b, 0x910b, 0x4171, 0x82, 0x42, 0xa8, 0x5a, 0xd, 0xf2, 0x5b, 0x5b]
## Module: HttpDxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa42] EFI_BOOT_SERVICES->OpenProtocol
* [0xb70] EFI_BOOT_SERVICES->OpenProtocol
* [0x78f] EFI_BOOT_SERVICES->OpenProtocol
* [0x8c9] EFI_BOOT_SERVICES->OpenProtocol
* [0xbdc] EFI_BOOT_SERVICES->OpenProtocol
* [0x2b41] EFI_BOOT_SERVICES->OpenProtocol
* [0x2b81] EFI_BOOT_SERVICES->OpenProtocol
* [0x2bef] EFI_BOOT_SERVICES->OpenProtocol
* [0x2c2f] EFI_BOOT_SERVICES->OpenProtocol
* [0x2c66] EFI_BOOT_SERVICES->OpenProtocol
* [0x3ebb] EFI_BOOT_SERVICES->OpenProtocol
* [0x4256] EFI_BOOT_SERVICES->OpenProtocol
* [0x490b] EFI_BOOT_SERVICES->OpenProtocol
* [0x4957] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xb13] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x5e6] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x811] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4725] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x3dbf] EFI_BOOT_SERVICES->HandleProtocol
* [0x416e] EFI_BOOT_SERVICES->HandleProtocol
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x4eb] EFI_BOOT_SERVICES->LocateProtocol
* [0x6c8] EFI_BOOT_SERVICES->LocateProtocol
* [0x5930] EFI_BOOT_SERVICES->LocateProtocol
* [0x977] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x9c5] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x638] EFI_BOOT_SERVICES->CloseProtocol
* [0x67c] EFI_BOOT_SERVICES->CloseProtocol
* [0x2cb0] EFI_BOOT_SERVICES->CloseProtocol
* [0x2cd3] EFI_BOOT_SERVICES->CloseProtocol
* [0x2d17] EFI_BOOT_SERVICES->CloseProtocol
* [0x2d3f] EFI_BOOT_SERVICES->CloseProtocol
* [0x2d62] EFI_BOOT_SERVICES->CloseProtocol
* [0x2da6] EFI_BOOT_SERVICES->CloseProtocol
* [0x2eb8] EFI_BOOT_SERVICES->CloseProtocol
* [0x2edf] EFI_BOOT_SERVICES->CloseProtocol
* [0x2f27] EFI_BOOT_SERVICES->CloseProtocol
* [0x2f53] EFI_BOOT_SERVICES->CloseProtocol
* [0x2f7a] EFI_BOOT_SERVICES->CloseProtocol
* [0x2fc2] EFI_BOOT_SERVICES->CloseProtocol
* [0x4055] EFI_BOOT_SERVICES->CloseProtocol
* [0x43b3] EFI_BOOT_SERVICES->CloseProtocol
* [0x53a] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x5f80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHttpServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbdc8e6af, 0xd9bc, 0x4379, 0xa7, 0x2a, 0xe0, 0xc4, 0xe7, 0x5d, 0xae, 0x1c]
* [0x5fb0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x720665, 0x67eb, 0x4a99, 0xba, 0xf7, 0xd3, 0xc3, 0x3a, 0x1c, 0x7c, 0xc9]
* [0x5fd0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xec20eb79, 0x6c1a, 0x4664, 0x9a, 0xd, 0xd2, 0xe4, 0xcc, 0x16, 0xd6, 0x64]
* [0x6000]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xae3d28cc, 0xe05b, 0x4fa1, 0xa0, 0x11, 0x7e, 0xb5, 0x5a, 0x3f, 0x14, 0x1]
* [0x6020]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDns6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xca37bc1f, 0xa327, 0x4ae9, 0x82, 0x8a, 0x8c, 0x40, 0xd8, 0x50, 0x6a, 0x17]
* [0x6050]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6060]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6070]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x5f80]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiHttpServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbdc8e6af, 0xd9bc, 0x4379, 0xa7, 0x2a, 0xe0, 0xc4, 0xe7, 0x5d, 0xae, 0x1c]
* [0x6050]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6060]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6070]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x6080]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6030]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp4Config2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b446ed1, 0xe30b, 0x4faa, 0x87, 0x1a, 0x36, 0x54, 0xec, 0xa3, 0x60, 0x80]
* [0x6040]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp6ConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x937fe521, 0x95ae, 0x4d1a, 0x89, 0x29, 0x48, 0xbc, 0xd9, 0xa, 0xd3, 0x1a]
* [0x6090]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x480f8ae9, 0xc46, 0x4aa9, 0xbc, 0x89, 0xdb, 0x9f, 0xba, 0x61, 0x98, 0x6]
* [0x5fa0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHttpUtilitiesProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3e35c163, 0x4074, 0x45dd, 0x43, 0x1e, 0x23, 0x98, 0x9d, 0xd8, 0x6b, 0x32]
* [0x5fc0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiTcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x65530bc7, 0xa359, 0x410f, 0xb0, 0x10, 0x5a, 0xad, 0xc7, 0xec, 0x2b, 0x62]
* [0x5fe0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiTcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x46e44855, 0xbd60, 0x4ab7, 0xab, 0xd, 0xa6, 0x79, 0xb9, 0x44, 0x7d, 0x77]
* [0x5fc0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiTcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x65530bc7, 0xa359, 0x410f, 0xb0, 0x10, 0x5a, 0xad, 0xc7, 0xec, 0x2b, 0x62]
* [0x5fe0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiTcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x46e44855, 0xbd60, 0x4ab7, 0xab, 0xd, 0xa6, 0x79, 0xb9, 0x44, 0x7d, 0x77]
* [0x5fb0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiTcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x720665, 0x67eb, 0x4a99, 0xba, 0xf7, 0xd3, 0xc3, 0x3a, 0x1c, 0x7c, 0xc9]
* [0x5fd0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiTcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xec20eb79, 0x6c1a, 0x4664, 0x9a, 0xd, 0xd2, 0xe4, 0xcc, 0x16, 0xd6, 0x64]
* [0x6000]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDns4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xae3d28cc, 0xe05b, 0x4fa1, 0xa0, 0x11, 0x7e, 0xb5, 0x5a, 0x3f, 0x14, 0x1]
* [0x6020]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDns6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xca37bc1f, 0xa327, 0x4ae9, 0x82, 0x8a, 0x8c, 0x40, 0xd8, 0x50, 0x6a, 0x17]
* [0x5fa0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiHttpUtilitiesProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3e35c163, 0x4074, 0x45dd, 0x43, 0x1e, 0x23, 0x98, 0x9d, 0xd8, 0x6b, 0x32]
## Module: HttpUtilitiesDxe
### Boot services:
* [0x2d3] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x316] EFI_BOOT_SERVICES->OpenProtocol
* [0x340] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x3d2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x398] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* [0xe20]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiHttpUtilitiesProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3e35c163, 0x4074, 0x45dd, 0x43, 0x1e, 0x23, 0x98, 0x9d, 0xd8, 0x6b, 0x32]
* [0xe20]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHttpUtilitiesProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3e35c163, 0x4074, 0x45dd, 0x43, 0x1e, 0x23, 0x98, 0x9d, 0xd8, 0x6b, 0x32]
* [0xe30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
## Module: IccPlatformDxe
### Boot services:
* empty
### Protocols:
* empty
## Module: IdeBusBoard
### Boot services:
* [0x2cf] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* [0x440]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6737f69b, 0xb8cc, 0x45bc, 0x93, 0x27, 0xcc, 0xf5, 0xee, 0xf7, 0xc, 0xde]
## Module: IdeBusSrc
### Boot services:
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
* [0x1119] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x16fd] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x35e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1137] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1969] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x12eb] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x130a] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x148e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x14d6] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x39d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xd0c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xe0f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5f22] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x656a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x10f9] EFI_BOOT_SERVICES->HandleProtocol
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
* [0x716d] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x45f] EFI_BOOT_SERVICES->CloseProtocol
* [0x51d] EFI_BOOT_SERVICES->CloseProtocol
* [0x128a] EFI_BOOT_SERVICES->CloseProtocol
* [0x1658] EFI_BOOT_SERVICES->CloseProtocol
* [0x16e5] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x75d0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xe159a956, 0x3299, 0x4ee9, 0x91, 0x76, 0x65, 0x18, 0x1a, 0x4e, 0x5e, 0x9f]
* [0x76c0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x7600]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x7610]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x7640]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xf4f63529, 0x281e, 0x4040, 0xa3, 0x13, 0xc1, 0xd6, 0x76, 0x63, 0x84, 0xbe]
* [0x7660]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xffbd9ad2, 0xf1db, 0x4f92, 0xa6, 0x49, 0xeb, 0x9e, 0xed, 0xea, 0x86, 0xb5]
* [0x7680]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiStorageSecurityCommandProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc88b0b6d, 0xdfc, 0x49a7, 0x9c, 0xb4, 0x49, 0x7, 0x4b, 0x4c, 0x3a, 0x78]
* [0x7d34]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x552d6e65, 0x53, 0x0, 0x0, 0x0, 0x0, 0x0, 0x50, 0x0, 0x43, 0x0]
* [0x75d0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xe159a956, 0x3299, 0x4ee9, 0x91, 0x76, 0x65, 0x18, 0x1a, 0x4e, 0x5e, 0x9f]
* [0x76b0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6737f69b, 0xb8cc, 0x45bc, 0x93, 0x27, 0xcc, 0xf5, 0xee, 0xf7, 0xc, 0xde]
* [0x75d0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xe159a956, 0x3299, 0x4ee9, 0x91, 0x76, 0x65, 0x18, 0x1a, 0x4e, 0x5e, 0x9f]
* [0x76b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6737f69b, 0xb8cc, 0x45bc, 0x93, 0x27, 0xcc, 0xf5, 0xee, 0xf7, 0xc, 0xde]
* [0x7690]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6734411, 0x2dda, 0x4632, 0xa5, 0x92, 0x92, 0xf, 0x24, 0xd6, 0xed, 0x21]
* [0x76a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xfc50878, 0x1633, 0x432a, 0xbd, 0xe4, 0x84, 0x13, 0x57, 0xfc, 0x15, 0xe9]
* [0x7620]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xce6f86bb, 0xb800, 0x4c71, 0xb2, 0xd1, 0x38, 0x97, 0xa3, 0xbc, 0x1d, 0xae]
* [0x7c80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x10e9d800, 0x53b7, 0x4845, 0x9d, 0xff, 0x30, 0xd1, 0x8a, 0x95, 0x6d, 0x53]
* [0x7670]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x59af16b0, 0x661d, 0x4865, 0xa3, 0x81, 0x38, 0xde, 0x68, 0x38, 0x5d, 0x8d]
* [0x7650]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x9401bd4f, 0x1a00, 0x4990, 0xab, 0x56, 0xda, 0xf0, 0xe4, 0xe3, 0x48, 0xde]
* [0x7c90]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5578ae16, 0xf1c9, 0x4e8f, 0xb1, 0x29, 0xba, 0x7, 0xf8, 0xfc, 0xf8, 0x4a]
* [0x7c08]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x75d0]
	 - [service] CloseProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xe159a956, 0x3299, 0x4ee9, 0x91, 0x76, 0x65, 0x18, 0x1a, 0x4e, 0x5e, 0x9f]
## Module: IntegratedTouch
### Boot services:
* [0x2c9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xc92] EFI_BOOT_SERVICES->OpenProtocol
* [0xcd6] EFI_BOOT_SERVICES->OpenProtocol
* [0x1043] EFI_BOOT_SERVICES->OpenProtocol
* [0x138e] EFI_BOOT_SERVICES->OpenProtocol
* [0x334] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x38b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1092] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x10bc] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x10dd] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x4b0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4d3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xbc0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xbed] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xe31] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x439] EFI_BOOT_SERVICES->HandleProtocol
* [0x586] EFI_BOOT_SERVICES->LocateProtocol
* [0x64f] EFI_BOOT_SERVICES->LocateProtocol
* [0xf82] EFI_BOOT_SERVICES->LocateProtocol
* [0x18ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x196f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1aaa] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b71] EFI_BOOT_SERVICES->LocateProtocol
* [0x1c83] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d57] EFI_BOOT_SERVICES->LocateProtocol
* [0xd20] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x1eb0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2b12e46f, 0x3c24, 0x47ff, 0x8b, 0x89, 0xc0, 0x60, 0x2c, 0x1c, 0x61, 0x42]
* [0x1e90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x1e50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8d59d32b, 0xc655, 0x4ae9, 0x9b, 0x15, 0xf2, 0x59, 0x4, 0x99, 0x2a, 0x43]
* [0x1ee0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x1e80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x1e90]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
## Module: IntelGigabitLan
### Boot services:
* [0x1f634] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2631f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4443e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a81d] EFI_BOOT_SERVICES->OpenProtocol
* [0x1f683] EFI_BOOT_SERVICES->OpenProtocol
* [0x25f4c] EFI_BOOT_SERVICES->OpenProtocol
* [0x26017] EFI_BOOT_SERVICES->OpenProtocol
* [0x260e9] EFI_BOOT_SERVICES->OpenProtocol
* [0x261be] EFI_BOOT_SERVICES->OpenProtocol
* [0x26280] EFI_BOOT_SERVICES->OpenProtocol
* [0x2638c] EFI_BOOT_SERVICES->OpenProtocol
* [0x27ec7] EFI_BOOT_SERVICES->OpenProtocol
* [0x27f1f] EFI_BOOT_SERVICES->OpenProtocol
* [0x44497] EFI_BOOT_SERVICES->OpenProtocol
* [0x1f36e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x231ef] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1a6ed] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1a7a7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1a7df] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1a52f] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a594] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a5b2] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a5cf] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a5ec] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f262] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f288] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f2ae] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f2d4] EFI_BOOT_SERVICES->LocateProtocol
* [0x45fab] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f86d] EFI_BOOT_SERVICES->CloseProtocol
* [0x25f97] EFI_BOOT_SERVICES->CloseProtocol
* [0x26063] EFI_BOOT_SERVICES->CloseProtocol
* [0x26135] EFI_BOOT_SERVICES->CloseProtocol
* [0x2620a] EFI_BOOT_SERVICES->CloseProtocol
* [0x262bf] EFI_BOOT_SERVICES->CloseProtocol
* [0x2641c] EFI_BOOT_SERVICES->CloseProtocol
* [0x27ef7] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x1010]
	 - [service] LocateHandleBuffer
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x51dd8b21, 0xad8d, 0x48e9, 0xbc, 0x3f, 0x24, 0xf4, 0x67, 0x22, 0xc7, 0x48]
* [0x2a0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x3b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x1b48]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPlatformToDriverConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x642cd590, 0x8059, 0x4c0a, 0xa9, 0x58, 0xc5, 0xec, 0x7, 0xd2, 0x3c, 0x4b]
* [0x1010]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x51dd8b21, 0xad8d, 0x48e9, 0xbc, 0x3f, 0x24, 0xf4, 0x67, 0x22, 0xc7, 0x48]
* [0x2b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x1d58]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xe3161450, 0xad0f, 0x11d9, 0x96, 0x69, 0x8, 0x0, 0x20, 0xc, 0x9a, 0x66]
* [0x2a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x3b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x300]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x2e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x330]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x2c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb9d4c360, 0xbcfb, 0x4f9b, 0x92, 0x98, 0x53, 0xc1, 0x36, 0x98, 0x22, 0x58]
* [0x1b48]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPlatformToDriverConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x642cd590, 0x8059, 0x4c0a, 0xa9, 0x58, 0xc5, 0xec, 0x7, 0xd2, 0x3c, 0x4b]
* [0x1010]
	 - [service] CloseProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x51dd8b21, 0xad8d, 0x48e9, 0xbc, 0x3f, 0x24, 0xf4, 0x67, 0x22, 0xc7, 0x48]
* [0x2b0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
## Module: IntelGigabitLanDxe
### Boot services:
* [0x443] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* empty
## Module: Ip4Dxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x691] EFI_BOOT_SERVICES->OpenProtocol
* [0x6c1] EFI_BOOT_SERVICES->OpenProtocol
* [0x922] EFI_BOOT_SERVICES->OpenProtocol
* [0xc29] EFI_BOOT_SERVICES->OpenProtocol
* [0xee6] EFI_BOOT_SERVICES->OpenProtocol
* [0x19f4] EFI_BOOT_SERVICES->OpenProtocol
* [0x25ae] EFI_BOOT_SERVICES->OpenProtocol
* [0x2d5c] EFI_BOOT_SERVICES->OpenProtocol
* [0x3372] EFI_BOOT_SERVICES->OpenProtocol
* [0x483c] EFI_BOOT_SERVICES->OpenProtocol
* [0x961c] EFI_BOOT_SERVICES->OpenProtocol
* [0xc01f] EFI_BOOT_SERVICES->OpenProtocol
* [0xc06b] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xd9d] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x10ce] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x9740] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x633] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc94] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x95d6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x457] EFI_BOOT_SERVICES->HandleProtocol
* [0x9509] EFI_BOOT_SERVICES->HandleProtocol
* [0xb1b3] EFI_BOOT_SERVICES->HandleProtocol
* [0xc0b5] EFI_BOOT_SERVICES->HandleProtocol
* [0xc125] EFI_BOOT_SERVICES->HandleProtocol
* [0xc200] EFI_BOOT_SERVICES->HandleProtocol
* [0xc250] EFI_BOOT_SERVICES->HandleProtocol
* [0x4bc] EFI_BOOT_SERVICES->LocateProtocol
* [0x4da] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f7] EFI_BOOT_SERVICES->LocateProtocol
* [0x514] EFI_BOOT_SERVICES->LocateProtocol
* [0x531] EFI_BOOT_SERVICES->LocateProtocol
* [0x6be2] EFI_BOOT_SERVICES->LocateProtocol
* [0xb88f] EFI_BOOT_SERVICES->LocateProtocol
* [0xe14] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xe55] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xe92] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x252b] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xb05] EFI_BOOT_SERVICES->CloseProtocol
* [0x1974] EFI_BOOT_SERVICES->CloseProtocol
* [0x1a7a] EFI_BOOT_SERVICES->CloseProtocol
* [0x1b9a] EFI_BOOT_SERVICES->CloseProtocol
* [0x2655] EFI_BOOT_SERVICES->CloseProtocol
* [0x31fd] EFI_BOOT_SERVICES->CloseProtocol
* [0x4962] EFI_BOOT_SERVICES->CloseProtocol
* [0x9705] EFI_BOOT_SERVICES->CloseProtocol
* [0xb26f] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xd850]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0xd870]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiArpServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf44c00ee, 0x1f2c, 0x4a00, 0xaa, 0x9, 0x1c, 0x9f, 0x3e, 0x8, 0x0, 0xa3]
* [0xd860]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0xd830]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc51711e7, 0xb4bf, 0x404a, 0xbf, 0xb8, 0xa, 0x4, 0x8e, 0xf1, 0xff, 0xe4]
* [0xd890]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4b427bb, 0xba21, 0x4f16, 0xbc, 0x4e, 0x43, 0xe4, 0x16, 0xab, 0x61, 0x9c]
* [0xd840]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x41d94cd2, 0x35b6, 0x455a, 0x82, 0x58, 0xd4, 0xe5, 0x13, 0x34, 0xaa, 0xdd]
* [0xd8b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0xd8f0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0xd910]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xd920]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0xd830]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiIp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc51711e7, 0xb4bf, 0x404a, 0xbf, 0xb8, 0xa, 0x4, 0x8e, 0xf1, 0xff, 0xe4]
* [0xd8f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0xd910]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xd920]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0xd970]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xd8e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xd980]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xd850]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0xd860]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0xd930]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0xd950]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0xd960]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0xd900]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0xd940]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
* [0xd8c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiIpSec2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa3979e64, 0xace8, 0x4ddc, 0xbc, 0x7, 0x4d, 0x66, 0xb8, 0xfd, 0x9, 0x77]
* [0xd860]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0xd890]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4b427bb, 0xba21, 0x4f16, 0xbc, 0x4e, 0x43, 0xe4, 0x16, 0xab, 0x61, 0x9c]
* [0xd8b0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0xd860]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0xd890]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4b427bb, 0xba21, 0x4f16, 0xbc, 0x4e, 0x43, 0xe4, 0x16, 0xab, 0x61, 0x9c]
* [0xd8b0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0xd850]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
## Module: Ip6Dxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x691] EFI_BOOT_SERVICES->OpenProtocol
* [0x6c1] EFI_BOOT_SERVICES->OpenProtocol
* [0x9aa] EFI_BOOT_SERVICES->OpenProtocol
* [0xdb8] EFI_BOOT_SERVICES->OpenProtocol
* [0xe0f] EFI_BOOT_SERVICES->OpenProtocol
* [0xfb7] EFI_BOOT_SERVICES->OpenProtocol
* [0x12f6] EFI_BOOT_SERVICES->OpenProtocol
* [0x738e] EFI_BOOT_SERVICES->OpenProtocol
* [0x811a] EFI_BOOT_SERVICES->OpenProtocol
* [0x81e0] EFI_BOOT_SERVICES->OpenProtocol
* [0xa1ed] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x2da7] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x30b2] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x317c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x386d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x3bee] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x13df] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x633] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1022] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x457] EFI_BOOT_SERVICES->HandleProtocol
* [0x203f] EFI_BOOT_SERVICES->HandleProtocol
* [0xf6e9] EFI_BOOT_SERVICES->HandleProtocol
* [0xf759] EFI_BOOT_SERVICES->HandleProtocol
* [0xf834] EFI_BOOT_SERVICES->HandleProtocol
* [0xf884] EFI_BOOT_SERVICES->HandleProtocol
* [0x10987] EFI_BOOT_SERVICES->HandleProtocol
* [0x4bc] EFI_BOOT_SERVICES->LocateProtocol
* [0x4da] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f7] EFI_BOOT_SERVICES->LocateProtocol
* [0x514] EFI_BOOT_SERVICES->LocateProtocol
* [0x531] EFI_BOOT_SERVICES->LocateProtocol
* [0x5e39] EFI_BOOT_SERVICES->LocateProtocol
* [0x120c] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x1277] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x730b] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x968] EFI_BOOT_SERVICES->CloseProtocol
* [0xa1ad] EFI_BOOT_SERVICES->CloseProtocol
* [0xedbf] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x10ad0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0x10af0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiArpServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf44c00ee, 0x1f2c, 0x4a00, 0xaa, 0x9, 0x1c, 0x9f, 0x3e, 0x8, 0x0, 0xa3]
* [0x10ae0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0x10b00]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xec835dd3, 0xfe0f, 0x617b, 0xa6, 0x21, 0xb3, 0x50, 0xc3, 0xe1, 0x33, 0x88]
* [0x10b10]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2c8759d5, 0x5c2d, 0x66ef, 0x92, 0x5f, 0xb6, 0x6c, 0x10, 0x19, 0x57, 0xe2]
* [0x10b30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9fb9a8a1, 0x2f4a, 0x43a6, 0x88, 0x9c, 0xd0, 0xf7, 0xb6, 0xc4, 0x7a, 0xd5]
* [0x10b40]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
* [0x10b70]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x10b90]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x10ba0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x10b70]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x10b90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x10ba0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x10bf0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x10c00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x10ad0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0x10ae0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0x10b60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x10bb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x10bd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x10be0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x10b80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x10bc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
* [0x10b50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiIpSec2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa3979e64, 0xace8, 0x4ddc, 0xbc, 0x7, 0x4d, 0x66, 0xb8, 0xfd, 0x9, 0x77]
* [0x10ae0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0x10b40]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
* [0x10ae0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0x10b40]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
## Module: KbcEmul
### Boot services:
* [0x2dd] EFI_BOOT_SERVICES->LocateProtocol
* [0x3bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x4c4] EFI_BOOT_SERVICES->LocateProtocol
* [0x562] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d1d] EFI_BOOT_SERVICES->LocateProtocol
* [0x50b] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1114] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1aa7] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2280]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2888]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x22e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2ad8e2d2, 0x2e91, 0x4cd1, 0x95, 0xf5, 0xe7, 0x8f, 0xe5, 0xeb, 0xe3, 0x16]
* [0x2300]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
* [0x2e38]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
## Module: KbcEmulDxe
### Boot services:
* [0x389] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x358] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x850]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x68b81e51, 0x2583, 0x4582, 0x95, 0xdb, 0xc5, 0x72, 0x32, 0x36, 0xc4, 0xf1]
* [0x840]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xad61f191, 0xae5f, 0x4c0e, 0xb9, 0xfa, 0xe8, 0x69, 0xd2, 0x88, 0xc6, 0x4f]
## Module: LegacyInterrupt
### Boot services:
* [0x2d5] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: LegacySmmSredir
### Boot services:
* [0x2c2] EFI_BOOT_SERVICES->LocateProtocol
* [0x54f] EFI_BOOT_SERVICES->LocateProtocol
* [0x600] EFI_BOOT_SERVICES->LocateProtocol
* [0x727] EFI_BOOT_SERVICES->LocateProtocol
* [0x8cd] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xc40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1178]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xc80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: LegacySredir
### Boot services:
* [0xea8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xfdb] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1802] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x377] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1237] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xede] EFI_BOOT_SERVICES->HandleProtocol
* [0x1036] EFI_BOOT_SERVICES->HandleProtocol
* [0x14f3] EFI_BOOT_SERVICES->HandleProtocol
* [0x15e2] EFI_BOOT_SERVICES->HandleProtocol
* [0x188d] EFI_BOOT_SERVICES->HandleProtocol
* [0x1974] EFI_BOOT_SERVICES->HandleProtocol
* [0x313] EFI_BOOT_SERVICES->LocateProtocol
* [0x46b] EFI_BOOT_SERVICES->LocateProtocol
* [0x7ca] EFI_BOOT_SERVICES->LocateProtocol
* [0x9f1] EFI_BOOT_SERVICES->LocateProtocol
* [0xa9f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1bb1] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x1d50]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x1d80]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xa062cf1f, 0x8473, 0x4aa3, 0x87, 0x93, 0x60, 0xb, 0xc4, 0xff, 0xa9, 0xa9]
* [0x1d40]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x50dc5c90, 0x1d33, 0x4fd6, 0x87, 0xe5, 0x6, 0x3b, 0x1d, 0xfa, 0x21, 0x70]
* [0x1d50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x1d60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x1da0]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x51e9b4f9, 0x555d, 0x476c, 0x8b, 0xb5, 0xbd, 0x18, 0xd9, 0xa6, 0x88, 0x78]
* [0x1d70]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8e008510, 0x9bb1, 0x457d, 0x9f, 0x70, 0x89, 0x7a, 0xba, 0x86, 0x5d, 0xb9]
* [0x1d90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x1d80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xa062cf1f, 0x8473, 0x4aa3, 0x87, 0x93, 0x60, 0xb, 0xc4, 0xff, 0xa9, 0xa9]
## Module: MeFwDowngrade
### Boot services:
* [0x376] EFI_BOOT_SERVICES->LocateProtocol
* [0x447] EFI_BOOT_SERVICES->LocateProtocol
* [0x51d] EFI_BOOT_SERVICES->LocateProtocol
* [0x7f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x8bb] EFI_BOOT_SERVICES->LocateProtocol
* [0x921] EFI_BOOT_SERVICES->LocateProtocol
* [0x948] EFI_BOOT_SERVICES->LocateProtocol
* [0x9b0] EFI_BOOT_SERVICES->LocateProtocol
* [0xa51] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1020]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x1030]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xa0b5dc52, 0x4f34, 0x3990, 0xd4, 0x91, 0x10, 0x8b, 0xe8, 0xba, 0x75, 0x42]
* [0x1060]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8d9b3387, 0x73db, 0x456f, 0x88, 0x9d, 0x6f, 0xfe, 0x90, 0x82, 0x64, 0x9]
* [0x1040]
	 - [service] LocateProtocol
	 - [protocol_name] gPlatformSeCHookProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbc52476e, 0xf67e, 0x4301, 0xb2, 0x62, 0x36, 0x9c, 0x48, 0x78, 0xaa, 0xc2]
* [0x1050]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb42b8d12, 0x2acb, 0x499a, 0xa9, 0x20, 0xdd, 0x5b, 0xe6, 0xcf, 0x9, 0xb1]
## Module: MePlatformReset
### Boot services:
* [0x18fc] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1048] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x192c] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a31] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a58] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ac0] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b7b] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x20d0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gPchResetCallbackProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3a3300ab, 0xc929, 0x487d, 0xab, 0x34, 0x15, 0x9b, 0xc1, 0x35, 0x62, 0xc0]
* [0x20d0]
	 - [service] HandleProtocol
	 - [protocol_name] gPchResetCallbackProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3a3300ab, 0xc929, 0x487d, 0xab, 0x34, 0x15, 0x9b, 0xc1, 0x35, 0x62, 0xc0]
* [0x2080]
	 - [service] LocateProtocol
	 - [protocol_name] gPlatformSeCHookProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbc52476e, 0xf67e, 0x4301, 0xb2, 0x62, 0x36, 0x9c, 0x48, 0x78, 0xaa, 0xc2]
* [0x2090]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x20a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb42b8d12, 0x2acb, 0x499a, 0xa9, 0x20, 0xdd, 0x5b, 0xe6, 0xcf, 0x9, 0xb1]
* [0x20b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8d9b3387, 0x73db, 0x456f, 0x88, 0x9d, 0x6f, 0xfe, 0x90, 0x82, 0x64, 0x9]
## Module: MeSmbiosDxe
### Boot services:
* [0x4a0] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xa20]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
## Module: MicrocodeUpdate
### Boot services:
* [0x318] EFI_BOOT_SERVICES->LocateProtocol
* [0x353] EFI_BOOT_SERVICES->LocateProtocol
* [0x38d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x4290]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x4260]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
## Module: MnpDxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5c2] EFI_BOOT_SERVICES->OpenProtocol
* [0x6d2] EFI_BOOT_SERVICES->OpenProtocol
* [0x8b1] EFI_BOOT_SERVICES->OpenProtocol
* [0x8e5] EFI_BOOT_SERVICES->OpenProtocol
* [0xb2f] EFI_BOOT_SERVICES->OpenProtocol
* [0xc23] EFI_BOOT_SERVICES->OpenProtocol
* [0x10e8] EFI_BOOT_SERVICES->OpenProtocol
* [0x1530] EFI_BOOT_SERVICES->OpenProtocol
* [0x1ff3] EFI_BOOT_SERVICES->OpenProtocol
* [0x20d0] EFI_BOOT_SERVICES->OpenProtocol
* [0x2166] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x834] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x972] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xb94] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xc8d] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x15e3] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x163f] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x568] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x734] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xaee] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1585] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x21c7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x4f63] EFI_BOOT_SERVICES->HandleProtocol
* [0x582d] EFI_BOOT_SERVICES->HandleProtocol
* [0x589d] EFI_BOOT_SERVICES->HandleProtocol
* [0x5930] EFI_BOOT_SERVICES->HandleProtocol
* [0x5980] EFI_BOOT_SERVICES->HandleProtocol
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x204a] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x5e5] EFI_BOOT_SERVICES->CloseProtocol
* [0xc70] EFI_BOOT_SERVICES->CloseProtocol
* [0x1328] EFI_BOOT_SERVICES->CloseProtocol
* [0x161b] EFI_BOOT_SERVICES->CloseProtocol
* [0x2015] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x61e0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6200]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiVlanConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9e23d768, 0xd2f3, 0x4366, 0x9f, 0xc3, 0x3a, 0x7a, 0xba, 0x86, 0x43, 0x74]
* [0x61d0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0x61f0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0x6210]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6220]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6230]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6240]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x6220]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6230]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6240]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x6250]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6210]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x61e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x61d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0x61f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0x6260]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x480f8ae9, 0xc46, 0x4aa9, 0xbc, 0x89, 0xdb, 0x9f, 0xba, 0x61, 0x98, 0x6]
* [0x61d0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0x61e0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x61d0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0x6200]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiVlanConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9e23d768, 0xd2f3, 0x4366, 0x9f, 0xc3, 0x3a, 0x7a, 0xba, 0x86, 0x43, 0x74]
## Module: MouseDriver
### Boot services:
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
* [0x3f04] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x115d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3cec] EFI_BOOT_SERVICES->LocateProtocol
* [0x1337] EFI_BOOT_SERVICES->CloseProtocol
* [0x1506] EFI_BOOT_SERVICES->CloseProtocol
* [0x15d6] EFI_BOOT_SERVICES->CloseProtocol
* [0x17d7] EFI_BOOT_SERVICES->CloseProtocol
* [0x11bc] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1216] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3f5e] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x5000]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiEdidDiscoveredProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x1c0c34f6, 0xd380, 0x41fa, 0xa0, 0x49, 0x8a, 0xd0, 0x6c, 0x1a, 0x66, 0xaa]
* [0x5050]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x5020]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31878c87, 0xb75, 0x11d5, 0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x5030]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8d59d32b, 0xc655, 0x4ae9, 0x9b, 0x15, 0xf2, 0x59, 0x4, 0x99, 0x2a, 0x43]
* [0x5040]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x5020]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31878c87, 0xb75, 0x11d5, 0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x5000]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiEdidDiscoveredProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x1c0c34f6, 0xd380, 0x41fa, 0xa0, 0x49, 0x8a, 0xd0, 0x6c, 0x1a, 0x66, 0xaa]
* [0x5030]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8d59d32b, 0xc655, 0x4ae9, 0x9b, 0x15, 0xf2, 0x59, 0x4, 0x99, 0x2a, 0x43]
* [0x5020]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31878c87, 0xb75, 0x11d5, 0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x5030]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8d59d32b, 0xc655, 0x4ae9, 0x9b, 0x15, 0xf2, 0x59, 0x4, 0x99, 0x2a, 0x43]
* [0x5040]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
## Module: Mtftp4Dxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5a0] EFI_BOOT_SERVICES->OpenProtocol
* [0x75a] EFI_BOOT_SERVICES->OpenProtocol
* [0x939] EFI_BOOT_SERVICES->OpenProtocol
* [0x1082] EFI_BOOT_SERVICES->OpenProtocol
* [0x3b51] EFI_BOOT_SERVICES->OpenProtocol
* [0x46f6] EFI_BOOT_SERVICES->OpenProtocol
* [0x4745] EFI_BOOT_SERVICES->OpenProtocol
* [0x6067] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xa09] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x565] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x7d0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x8b9] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xfff] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x11c8] EFI_BOOT_SERVICES->CloseProtocol
* [0x47a3] EFI_BOOT_SERVICES->CloseProtocol
* [0x489b] EFI_BOOT_SERVICES->CloseProtocol
* [0x48da] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x68e0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x83f01464, 0x99bd, 0x45e5, 0xb3, 0x83, 0xaf, 0x63, 0x5, 0xd8, 0xe9, 0xe6]
* [0x68d0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2fe800be, 0x8f01, 0x4aa6, 0x94, 0x6b, 0xd7, 0x13, 0x88, 0xe1, 0x83, 0x3f]
* [0x68f0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x78247c57, 0x63db, 0x4708, 0x99, 0xc2, 0xa8, 0xb4, 0xa9, 0xa6, 0x1f, 0x6b]
* [0x6900]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0x6940]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6950]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6960]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x68d0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiMtftp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2fe800be, 0x8f01, 0x4aa6, 0x94, 0x6b, 0xd7, 0x13, 0x88, 0xe1, 0x83, 0x3f]
* [0x6940]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6950]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6960]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x6970]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6930]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x480f8ae9, 0xc46, 0x4aa9, 0xbc, 0x89, 0xdb, 0x9f, 0xba, 0x61, 0x98, 0x6]
* [0x6900]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0x6900]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0x6920]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
## Module: Mtftp6Dxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x7ec] EFI_BOOT_SERVICES->OpenProtocol
* [0x832] EFI_BOOT_SERVICES->OpenProtocol
* [0x9b4] EFI_BOOT_SERVICES->OpenProtocol
* [0xbc3] EFI_BOOT_SERVICES->OpenProtocol
* [0xcb3] EFI_BOOT_SERVICES->OpenProtocol
* [0x1032] EFI_BOOT_SERVICES->OpenProtocol
* [0x266a] EFI_BOOT_SERVICES->OpenProtocol
* [0x385d] EFI_BOOT_SERVICES->OpenProtocol
* [0x41e2] EFI_BOOT_SERVICES->OpenProtocol
* [0x4231] EFI_BOOT_SERVICES->OpenProtocol
* [0x5dab] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xa84] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xdb1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xbe9] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x568] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8a8] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb7b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x935] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x25e7] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xd29] EFI_BOOT_SERVICES->CloseProtocol
* [0xd59] EFI_BOOT_SERVICES->CloseProtocol
* [0xd88] EFI_BOOT_SERVICES->CloseProtocol
* [0x1f1c] EFI_BOOT_SERVICES->CloseProtocol
* [0x428f] EFI_BOOT_SERVICES->CloseProtocol
* [0x4387] EFI_BOOT_SERVICES->CloseProtocol
* [0x43c6] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x6a70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x66ed4721, 0x3c98, 0x4d3e, 0x81, 0xe3, 0xd0, 0x3d, 0xd3, 0x9a, 0x72, 0x54]
* [0x6a90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd9760ff3, 0x3cca, 0x4267, 0x80, 0xf9, 0x75, 0x27, 0xfa, 0xfa, 0x42, 0x23]
* [0x6a80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
* [0x6aa0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbf0a78ba, 0xec29, 0x49cf, 0xa1, 0xc9, 0x7a, 0xe5, 0x4e, 0xab, 0x6a, 0x51]
* [0x6ae0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6af0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6b00]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x6a90]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiMtftp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd9760ff3, 0x3cca, 0x4267, 0x80, 0xf9, 0x75, 0x27, 0xfa, 0xfa, 0x42, 0x23]
* [0x6aa0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiMtftp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbf0a78ba, 0xec29, 0x49cf, 0xa1, 0xc9, 0x7a, 0xe5, 0x4e, 0xab, 0x6a, 0x51]
* [0x6ae0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6af0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6b00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x6b10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6ad0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x480f8ae9, 0xc46, 0x4aa9, 0xbc, 0x89, 0xdb, 0x9f, 0xba, 0x61, 0x98, 0x6]
* [0x6a80]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
* [0x6a80]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
* [0x6ac0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
## Module: Mxm30Nbci
### Boot services:
* [0x55f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x82e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x954] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x59a] EFI_BOOT_SERVICES->HandleProtocol
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a9] EFI_BOOT_SERVICES->LocateProtocol
* [0x3cf] EFI_BOOT_SERVICES->LocateProtocol
* [0x7a9] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x27f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x27d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x27e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8e008510, 0x9bb1, 0x457d, 0x9f, 0x70, 0x89, 0x7a, 0xba, 0x86, 0x5d, 0xb9]
* [0x27d0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
## Module: NbDxe
### Boot services:
* [0x314] EFI_BOOT_SERVICES->LocateProtocol
* [0x433] EFI_BOOT_SERVICES->LocateProtocol
* [0x450] EFI_BOOT_SERVICES->LocateProtocol
* [0x634] EFI_BOOT_SERVICES->LocateProtocol
* [0x7af] EFI_BOOT_SERVICES->LocateProtocol
* [0x836] EFI_BOOT_SERVICES->LocateProtocol
* [0x120b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1760] EFI_BOOT_SERVICES->LocateProtocol
* [0x617] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1851] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x3970]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x38f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x3900]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0x43d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x783658a3, 0x4172, 0x4421, 0xa2, 0x99, 0xe0, 0x9, 0x7, 0x9c, 0xc, 0xb4]
* [0x3950]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
* [0x3930]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3dc21d75, 0xde0e, 0x4300, 0xa0, 0xaa, 0x19, 0xc4, 0x1c, 0xc, 0xf3, 0xdf]
* [0x3e98]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x3930]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3dc21d75, 0xde0e, 0x4300, 0xa0, 0xaa, 0x19, 0xc4, 0x1c, 0xc, 0xf3, 0xdf]
## Module: NbSmi
### Boot services:
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a1] EFI_BOOT_SERVICES->LocateProtocol
* [0x474] EFI_BOOT_SERVICES->LocateProtocol
* [0x6eb] EFI_BOOT_SERVICES->LocateProtocol
* [0xa3f] EFI_BOOT_SERVICES->LocateProtocol
* [0xc4d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2da0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2dd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x32b8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2dc0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: NetworkStackSetupScreen
### Boot services:
* empty
### Protocols:
* empty
## Module: NTFS
### Boot services:
* [0x431] EFI_BOOT_SERVICES->OpenProtocol
* [0x54a] EFI_BOOT_SERVICES->OpenProtocol
* [0x5a8] EFI_BOOT_SERVICES->OpenProtocol
* [0x60a] EFI_BOOT_SERVICES->OpenProtocol
* [0x64b] EFI_BOOT_SERVICES->OpenProtocol
* [0x729] EFI_BOOT_SERVICES->OpenProtocol
* [0x3566] EFI_BOOT_SERVICES->OpenProtocol
* [0x765] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x402] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa33] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
* [0x697] EFI_BOOT_SERVICES->LocateProtocol
* [0x57b] EFI_BOOT_SERVICES->CloseProtocol
* [0x66e] EFI_BOOT_SERVICES->CloseProtocol
* [0x6d1] EFI_BOOT_SERVICES->CloseProtocol
* [0x788] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x4c60]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4670]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xce345171, 0xba0b, 0x11d2, 0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4c80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4cf0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4690]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x4680]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiUnicodeCollationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x1d85cd7f, 0xf43d, 0x11d2, 0x9a, 0xc, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x4670]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xce345171, 0xba0b, 0x11d2, 0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
## Module: Nvme
### Boot services:
* [0x310d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3529] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3bb] EFI_BOOT_SERVICES->OpenProtocol
* [0x496] EFI_BOOT_SERVICES->OpenProtocol
* [0x62d] EFI_BOOT_SERVICES->OpenProtocol
* [0xa06] EFI_BOOT_SERVICES->OpenProtocol
* [0xb4a] EFI_BOOT_SERVICES->OpenProtocol
* [0xb9e] EFI_BOOT_SERVICES->OpenProtocol
* [0xc61] EFI_BOOT_SERVICES->OpenProtocol
* [0xcb4] EFI_BOOT_SERVICES->OpenProtocol
* [0xe10] EFI_BOOT_SERVICES->OpenProtocol
* [0xe5a] EFI_BOOT_SERVICES->OpenProtocol
* [0xea4] EFI_BOOT_SERVICES->OpenProtocol
* [0xf6e] EFI_BOOT_SERVICES->OpenProtocol
* [0xfbc] EFI_BOOT_SERVICES->OpenProtocol
* [0x1393] EFI_BOOT_SERVICES->OpenProtocol
* [0x1f86] EFI_BOOT_SERVICES->OpenProtocol
* [0x2032] EFI_BOOT_SERVICES->OpenProtocol
* [0x4038] EFI_BOOT_SERVICES->OpenProtocol
* [0x914] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x932] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xabf] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xc88] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xcdb] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xcfd] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xef2] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xf44] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xf92] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xfe0] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x33b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x750] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x79a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa58] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1a53] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1ff4] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2c20] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2c8e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8f4] EFI_BOOT_SERVICES->HandleProtocol
* [0x3147] EFI_BOOT_SERVICES->HandleProtocol
* [0x3598] EFI_BOOT_SERVICES->HandleProtocol
* [0x7c3] EFI_BOOT_SERVICES->LocateProtocol
* [0x828] EFI_BOOT_SERVICES->LocateProtocol
* [0x871] EFI_BOOT_SERVICES->LocateProtocol
* [0x959] EFI_BOOT_SERVICES->LocateProtocol
* [0x21ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x2275] EFI_BOOT_SERVICES->LocateProtocol
* [0xae2] EFI_BOOT_SERVICES->CloseProtocol
* [0xc2c] EFI_BOOT_SERVICES->CloseProtocol
* [0x101d] EFI_BOOT_SERVICES->CloseProtocol
* [0x380] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x5480]
	 - [service] LocateHandleBuffer
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xafa4cf3f, 0xaf71, 0x4c30, 0xa4, 0xfb, 0x29, 0x10, 0xe7, 0x71, 0xf9, 0xb0]
* [0x5450]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x55a8]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x52c78312, 0x8edc, 0x4233, 0x98, 0xf2, 0x1a, 0x1a, 0xa5, 0xe3, 0x88, 0xa5]
* [0x5490]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x4b215191, 0x9a25, 0x43fd, 0x86, 0xb5, 0x74, 0xe7, 0xaf, 0x72, 0x33, 0x15]
* [0x5480]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xafa4cf3f, 0xaf71, 0x4c30, 0xa4, 0xfb, 0x29, 0x10, 0xe7, 0x71, 0xf9, 0xb0]
* [0x54a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x5470]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x54e0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0x5510]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xf4f63529, 0x281e, 0x4040, 0xa3, 0x13, 0xc1, 0xd6, 0x76, 0x63, 0x84, 0xbe]
* [0x55c8]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb396da3a, 0x52b2, 0x4cd6, 0xa8, 0x9a, 0x13, 0xe7, 0xc4, 0xae, 0x97, 0x90]
* [0x5530]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xffbd9ad2, 0xf1db, 0x4f92, 0xa6, 0x49, 0xeb, 0x9e, 0xed, 0xea, 0x86, 0xb5]
* [0x5480]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xafa4cf3f, 0xaf71, 0x4c30, 0xa4, 0xfb, 0x29, 0x10, 0xe7, 0x71, 0xf9, 0xb0]
* [0x5520]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x9401bd4f, 0x1a00, 0x4990, 0xab, 0x56, 0xda, 0xf0, 0xe4, 0xe3, 0x48, 0xde]
* [0x54f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xce6f86bb, 0xb800, 0x4c71, 0xb2, 0xd1, 0x38, 0x97, 0xa3, 0xbc, 0x1d, 0xae]
* [0x55b8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x734aa01d, 0x95ec, 0x45b7, 0xa2, 0x3a, 0x2d, 0x86, 0xd8, 0xfd, 0xeb, 0xb6]
* [0x5550]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x7f955a3e, 0xafb5, 0x4122, 0xb9, 0x25, 0x4b, 0x11, 0x71, 0xf6, 0x93, 0xf5]
* [0x54d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc68ed8e2, 0x9dc6, 0x4cbd, 0x9d, 0x94, 0xdb, 0x65, 0xac, 0xc5, 0xc3, 0x32]
* [0x54c0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd4e79dae, 0xaafc, 0x4382, 0x95, 0x40, 0x3e, 0x3f, 0xa4, 0x2d, 0x42, 0x55]
* [0x5450]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x55d8]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3aa83745, 0x9454, 0x4f7a, 0xa7, 0xc0, 0x90, 0xdb, 0xd0, 0x2f, 0xab, 0x8e]
## Module: NvmeDynamicSetup
### Boot services:
* [0x491] EFI_BOOT_SERVICES->OpenProtocol
* [0x324] EFI_BOOT_SERVICES->LocateProtocol
* [0x342] EFI_BOOT_SERVICES->LocateProtocol
* [0x35f] EFI_BOOT_SERVICES->LocateProtocol
* [0x37c] EFI_BOOT_SERVICES->LocateProtocol
* [0x4b1] EFI_BOOT_SERVICES->LocateProtocol
* [0x52b] EFI_BOOT_SERVICES->LocateProtocol
* [0x18f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x1c2f] EFI_BOOT_SERVICES->LocateProtocol
* [0x464] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x3030]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0x29d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x2a40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x2a50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x2a20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x3040]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x2ff0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
## Module: NvmeInt13
### Boot services:
* [0x38c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2cf] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x690]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd4e79dae, 0xaafc, 0x4382, 0x95, 0x40, 0x3e, 0x3f, 0xa4, 0x2d, 0x42, 0x55]
* [0x680]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8e008510, 0x9bb1, 0x457d, 0x9f, 0x70, 0x89, 0x7a, 0xba, 0x86, 0x5d, 0xb9]
## Module: NvmeSmm
### Boot services:
* [0x2e2] EFI_BOOT_SERVICES->LocateProtocol
* [0xced] EFI_BOOT_SERVICES->LocateProtocol
* [0xd8c] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x1e30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
## Module: NvramDxe
### Boot services:
* [0x4497] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1ac8] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1b51] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1be0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x44cd] EFI_BOOT_SERVICES->HandleProtocol
* [0x114d] EFI_BOOT_SERVICES->LocateProtocol
* [0x1209] EFI_BOOT_SERVICES->LocateProtocol
* [0x1bab] EFI_BOOT_SERVICES->LocateProtocol
* [0x6044] EFI_BOOT_SERVICES->LocateProtocol
* [0x755c] EFI_BOOT_SERVICES->LocateProtocol
* [0x7695] EFI_BOOT_SERVICES->LocateProtocol
* [0x8a2b] EFI_BOOT_SERVICES->LocateProtocol
* [0x7709] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x8689] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xb120]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0xb120]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0xb190]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xb140]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc68ed8e2, 0x9dc6, 0x4cbd, 0x9d, 0x94, 0xdb, 0x65, 0xac, 0xc5, 0xc3, 0x32]
* [0xb130]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x755b6596, 0x6896, 0x4ba3, 0xb3, 0xdd, 0x1c, 0x62, 0x9f, 0xd1, 0xea, 0x88]
* [0xba00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0xb1a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
* [0xb1d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5f87ba17, 0x957d, 0x433d, 0x9e, 0x15, 0xc0, 0xe7, 0xc8, 0x79, 0x88, 0x99]
* [0xb418]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3aa83745, 0x9454, 0x4f7a, 0xa7, 0xc0, 0x90, 0xdb, 0xd0, 0x2f, 0xab, 0x8e]
## Module: NvramSmm
### Boot services:
* [0x2d27] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2d5d] EFI_BOOT_SERVICES->HandleProtocol
* [0x37f] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b4] EFI_BOOT_SERVICES->LocateProtocol
* [0x484] EFI_BOOT_SERVICES->LocateProtocol
* [0x4c4] EFI_BOOT_SERVICES->LocateProtocol
* [0x6570] EFI_BOOT_SERVICES->LocateProtocol
* [0x66a9] EFI_BOOT_SERVICES->LocateProtocol
* [0x6791] EFI_BOOT_SERVICES->LocateProtocol
* [0x984] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x9a7] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x9ca] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x7559] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x9630]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x9630]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x9670]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x96a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x9f00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x9690]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
* [0x9ec0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x9918]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3aa83745, 0x9454, 0x4f7a, 0xa7, 0xc0, 0x90, 0xdb, 0xd0, 0x2f, 0xab, 0x8e]
## Module: OA2
### Boot services:
* [0x385] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3ba] EFI_BOOT_SERVICES->HandleProtocol
* [0x949] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* empty
## Module: OA3
### Boot services:
* [0x341] EFI_BOOT_SERVICES->LocateProtocol
* [0x70a] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xa40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xa30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
## Module: OA3_SMM
### Boot services:
* [0x2c2] EFI_BOOT_SERVICES->LocateProtocol
* [0x717] EFI_BOOT_SERVICES->LocateProtocol
* [0x939] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xc40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1158]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xc60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: Ofbd
### Boot services:
* [0x387] EFI_BOOT_SERVICES->LocateProtocol
* [0x3bc] EFI_BOOT_SERVICES->LocateProtocol
* [0x48c] EFI_BOOT_SERVICES->LocateProtocol
* [0x678] EFI_BOOT_SERVICES->LocateProtocol
* [0x70c] EFI_BOOT_SERVICES->LocateProtocol
* [0x863] EFI_BOOT_SERVICES->LocateProtocol
* [0xa2d] EFI_BOOT_SERVICES->LocateProtocol
* [0x1fa5] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x55f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x5630]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x5e78]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x5620]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: OpalSecurity
### Boot services:
* [0x312] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* empty
## Module: OverclockInterface
### Boot services:
* [0x64b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x680] EFI_BOOT_SERVICES->HandleProtocol
* [0x60d] EFI_BOOT_SERVICES->LocateProtocol
* [0x8cd] EFI_BOOT_SERVICES->LocateProtocol
* [0x91e] EFI_BOOT_SERVICES->LocateProtocol
* [0x1cc3] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1ea0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x1ea0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x1e40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
* [0x1e50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb42b8d12, 0x2acb, 0x499a, 0xa9, 0x20, 0xdd, 0x5b, 0xe6, 0xcf, 0x9, 0xb1]
* [0x1e70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGlobalNvsAreaProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x74e1e48, 0x8132, 0x47a1, 0x8c, 0x2c, 0x3f, 0x14, 0xad, 0x9a, 0x66, 0xdc]
* [0x1eb0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8d9b3387, 0x73db, 0x456f, 0x88, 0x9d, 0x6f, 0xfe, 0x90, 0x82, 0x64, 0x9]
## Module: OverClockSmiHandler
### Boot services:
* [0x267f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2798] EFI_BOOT_SERVICES->LocateProtocol
* [0x2830] EFI_BOOT_SERVICES->LocateProtocol
* [0x299d] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a7d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2e90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGlobalNvsAreaProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x74e1e48, 0x8132, 0x47a1, 0x8c, 0x2c, 0x3f, 0x14, 0xad, 0x9a, 0x66, 0xdc]
* [0x2eb0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd9035175, 0x8ce2, 0x47de, 0xa8, 0xb8, 0xcc, 0x98, 0xe5, 0xe2, 0xa8, 0x85]
* [0x2e60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2ed0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
* [0x33b8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
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
* [0x1350] EFI_BOOT_SERVICES->OpenProtocol
* [0x954] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x999] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x31b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x12ed] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1314] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3d7] EFI_BOOT_SERVICES->CloseProtocol
* [0x42c] EFI_BOOT_SERVICES->CloseProtocol
* [0x72e] EFI_BOOT_SERVICES->CloseProtocol
* [0x74c] EFI_BOOT_SERVICES->CloseProtocol
* [0x76a] EFI_BOOT_SERVICES->CloseProtocol
* [0x7ec] EFI_BOOT_SERVICES->CloseProtocol
* [0x80a] EFI_BOOT_SERVICES->CloseProtocol
* [0x828] EFI_BOOT_SERVICES->CloseProtocol
* [0x8dc] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x2de0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xce345171, 0xba0b, 0x11d2, 0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2dd0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2db0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2dc0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa77b2472, 0xe282, 0x4e9f, 0xa2, 0x45, 0xc2, 0xc0, 0xe2, 0x7b, 0xbc, 0xc1]
* [0x2df0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDiskIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x151c8eae, 0x7f2c, 0x472c, 0x9e, 0x54, 0x98, 0x28, 0x19, 0x4f, 0x6a, 0x88]
* [0x2de0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xce345171, 0xba0b, 0x11d2, 0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2dd0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2df0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDiskIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x151c8eae, 0x7f2c, 0x472c, 0x9e, 0x54, 0x98, 0x28, 0x19, 0x4f, 0x6a, 0x88]
## Module: PauseKey
### Boot services:
* [0x3fc] EFI_BOOT_SERVICES->OpenProtocol
* [0x525] EFI_BOOT_SERVICES->HandleProtocol
* [0x324] EFI_BOOT_SERVICES->LocateProtocol
* [0x342] EFI_BOOT_SERVICES->LocateProtocol
* [0x35f] EFI_BOOT_SERVICES->LocateProtocol
* [0x37c] EFI_BOOT_SERVICES->LocateProtocol
* [0x421] EFI_BOOT_SERVICES->LocateProtocol
* [0x5ca] EFI_BOOT_SERVICES->LocateProtocol
* [0xee6] EFI_BOOT_SERVICES->LocateProtocol
* [0x121f] EFI_BOOT_SERVICES->LocateProtocol
* [0x4cc] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2730]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0x20f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdd9e7534, 0x7762, 0x4698, 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa]
* [0x2120]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x2140]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x2150]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x2110]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x2740]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x2100]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0x26f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x20f0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdd9e7534, 0x7762, 0x4698, 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa]
## Module: PcdDxe
### Boot services:
* [0x368] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3a3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x24ba] EFI_BOOT_SERVICES->HandleProtocol
* [0x24e7] EFI_BOOT_SERVICES->HandleProtocol
* [0x2311] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ec] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2640]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2650]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x2630]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
* [0x2630]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
## Module: PchInitDxe
### Boot services:
* [0x979] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x99b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa37] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x14ae] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2c9e] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fc] EFI_BOOT_SERVICES->LocateProtocol
* [0x49b5] EFI_BOOT_SERVICES->LocateProtocol
* [0x775f] EFI_BOOT_SERVICES->LocateProtocol
* [0xa92] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x86b0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x10fe7e3b, 0xdbe5, 0x4cfa, 0x90, 0x25, 0x40, 0x2, 0xcf, 0xdd, 0xbb, 0x89]
* [0x86d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x8710]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0x86c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
* [0x8720]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xeb97088e, 0xcfdf, 0x49c6, 0xbe, 0x4b, 0xd9, 0x6, 0xa5, 0xb2, 0xe, 0x86]
* [0x86e0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiPciEnumerationCompleteProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x30cfe3e7, 0x3de1, 0x4586, 0xbe, 0x20, 0xde, 0xab, 0xa1, 0xb3, 0xb7, 0x93]
## Module: PchInitSmm
### Boot services:
* [0x139b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x39a] EFI_BOOT_SERVICES->LocateProtocol
* [0x70d] EFI_BOOT_SERVICES->LocateProtocol
* [0x7d9] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x47c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x47d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x4750]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2e058b2b, 0xedc1, 0x4431, 0x87, 0xd9, 0xc6, 0xc4, 0xea, 0x10, 0x2b, 0xe3]
## Module: PchResetRuntime
### Boot services:
* [0x16b0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1086] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x16e0] EFI_BOOT_SERVICES->HandleProtocol
* [0x17e5] EFI_BOOT_SERVICES->LocateProtocol
* [0x180c] EFI_BOOT_SERVICES->LocateProtocol
* [0x1874] EFI_BOOT_SERVICES->LocateProtocol
* [0x192f] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2060]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gPchResetCallbackProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3a3300ab, 0xc929, 0x487d, 0xab, 0x34, 0x15, 0x9b, 0xc1, 0x35, 0x62, 0xc0]
* [0x2060]
	 - [service] HandleProtocol
	 - [protocol_name] gPchResetCallbackProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3a3300ab, 0xc929, 0x487d, 0xab, 0x34, 0x15, 0x9b, 0xc1, 0x35, 0x62, 0xc0]
* [0x2080]
	 - [service] LocateProtocol
	 - [protocol_name] gPlatformSeCHookProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbc52476e, 0xf67e, 0x4301, 0xb2, 0x62, 0x36, 0x9c, 0x48, 0x78, 0xaa, 0xc2]
* [0x2090]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x20a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb42b8d12, 0x2acb, 0x499a, 0xa9, 0x20, 0xdd, 0x5b, 0xe6, 0xcf, 0x9, 0xb1]
* [0x20b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8d9b3387, 0x73db, 0x456f, 0x88, 0x9d, 0x6f, 0xfe, 0x90, 0x82, 0x64, 0x9]
## Module: PchSerialGpio
### Boot services:
* [0x369] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: PchSmbusDxe
### Boot services:
* [0x52f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: PchSmbusSmm
### Boot services:
* [0x2b1] EFI_BOOT_SERVICES->LocateProtocol
* [0x479] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xeb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
## Module: PchSmiDispatcher
### Boot services:
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x39a] EFI_BOOT_SERVICES->LocateProtocol
* [0x67b] EFI_BOOT_SERVICES->LocateProtocol
* [0x540] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x576] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x599] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x5bc] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x5df] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x602] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x6b7] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x6dc] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x71f] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x74e] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x5740]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x5810]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x7460]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0x5858]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x0, 0x0, 0x0, 0x50, 0x52, 0x4f, 0x54, 0x0, 0x0, 0x0, 0x0]
* [0x7428]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0x6948]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
## Module: PchSpiRuntime
### Boot services:
* [0x127b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: PchSpiSmm
### Boot services:
* [0x29d] EFI_BOOT_SERVICES->LocateProtocol
* [0x39d] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x1030]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
## Module: PciBus
### Boot services:
* [0x75cd] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xc4b4] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x78b4] EFI_BOOT_SERVICES->OpenProtocol
* [0x9f95] EFI_BOOT_SERVICES->OpenProtocol
* [0xa273] EFI_BOOT_SERVICES->OpenProtocol
* [0xa5b1] EFI_BOOT_SERVICES->OpenProtocol
* [0xa610] EFI_BOOT_SERVICES->OpenProtocol
* [0xdcd] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xa438] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xaa53] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x45f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9be0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9d7b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9dab] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9f44] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa8de] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1cb9] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x847a] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x7571] EFI_BOOT_SERVICES->HandleProtocol
* [0x7682] EFI_BOOT_SERVICES->HandleProtocol
* [0x77e0] EFI_BOOT_SERVICES->HandleProtocol
* [0x78de] EFI_BOOT_SERVICES->HandleProtocol
* [0xc4f9] EFI_BOOT_SERVICES->HandleProtocol
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
* [0x76b1] EFI_BOOT_SERVICES->LocateProtocol
* [0x76d5] EFI_BOOT_SERVICES->LocateProtocol
* [0x76f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x79a7] EFI_BOOT_SERVICES->LocateProtocol
* [0x904f] EFI_BOOT_SERVICES->LocateProtocol
* [0x94e8] EFI_BOOT_SERVICES->LocateProtocol
* [0x9510] EFI_BOOT_SERVICES->LocateProtocol
* [0xa6af] EFI_BOOT_SERVICES->LocateProtocol
* [0xa709] EFI_BOOT_SERVICES->LocateProtocol
* [0xa72f] EFI_BOOT_SERVICES->LocateProtocol
* [0xaf22] EFI_BOOT_SERVICES->LocateProtocol
* [0xb020] EFI_BOOT_SERVICES->LocateProtocol
* [0xc07e] EFI_BOOT_SERVICES->LocateProtocol
* [0xa34b] EFI_BOOT_SERVICES->CloseProtocol
* [0xa5e7] EFI_BOOT_SERVICES->CloseProtocol
* [0xa636] EFI_BOOT_SERVICES->CloseProtocol
* [0xa98e] EFI_BOOT_SERVICES->CloseProtocol
* [0x4ad] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xdd10]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciHostBridgeResourceAllocationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcf8034be, 0x6768, 0x4d8b, 0xb7, 0x39, 0x7c, 0xce, 0x68, 0x3a, 0x9f, 0xbe]
* [0xde10]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0xdd20]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xdd30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xdd20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xdd30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xde10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0xddf0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xdda0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7d75280, 0x27d4, 0x4d69, 0x90, 0xd0, 0x56, 0x43, 0xe2, 0x38, 0xb3, 0x41]
* [0xddb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciOverrideProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb5b35764, 0x460c, 0x4a06, 0x99, 0xfc, 0x77, 0xa1, 0x7c, 0x1b, 0x5c, 0xeb]
* [0xdd40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiIncompatiblePciDeviceSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xeb23f55a, 0x7863, 0x4ac2, 0x8d, 0x3d, 0x95, 0x65, 0x35, 0xde, 0x3, 0x75]
* [0xdd90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciHotPlugInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xaa0e8bc1, 0xdabc, 0x46b0, 0xa8, 0x44, 0x37, 0xb8, 0x16, 0x9b, 0x2b, 0xea]
* [0xdd80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDecompressProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd8117cfe, 0x94a6, 0x11d4, 0x9a, 0x3a, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xdd60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x542d6248, 0x4198, 0x4960, 0x9f, 0x59, 0x23, 0x84, 0x64, 0x6d, 0x63, 0xb4]
* [0xddc0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xdc14e697, 0x775a, 0x4c3b, 0xa1, 0x1a, 0xed, 0xc3, 0x8e, 0x1b, 0xe3, 0xe6]
* [0xdd50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0xde20]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xec63428d, 0x66ca, 0x4bf9, 0x82, 0xae, 0x84, 0xf, 0x6d, 0x5c, 0x23, 0x5]
* [0xdd70]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xea4b0675, 0x1f36, 0x4abe, 0xbb, 0x3a, 0x6d, 0x60, 0x76, 0xa, 0x2, 0xa2]
* [0xdde0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeMmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x60ff8964, 0xe906, 0x41d0, 0xaf, 0xed, 0xf2, 0x41, 0xe9, 0x74, 0xe0, 0x8e]
* [0xe798]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0xde00]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x4fc0733f, 0x6fd2, 0x491b, 0xa8, 0x90, 0x53, 0x74, 0x52, 0x1b, 0xf4, 0x8f]
* [0xdd20]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xdd30]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xdde0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiDxeMmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x60ff8964, 0xe906, 0x41d0, 0xaf, 0xed, 0xf2, 0x41, 0xe9, 0x74, 0xe0, 0x8e]
## Module: PciDxeInit
### Boot services:
* [0x80a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x304] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x84c] EFI_BOOT_SERVICES->HandleProtocol
* [0x3ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x4e6] EFI_BOOT_SERVICES->LocateProtocol
* [0x50c] EFI_BOOT_SERVICES->LocateProtocol
* [0x739] EFI_BOOT_SERVICES->LocateProtocol
* [0x9fe] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e57] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3170]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x3170]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x3160]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x3180]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x542d6248, 0x4198, 0x4960, 0x9f, 0x59, 0x23, 0x84, 0x64, 0x6d, 0x63, 0xb4]
* [0x3190]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xdc14e697, 0x775a, 0x4c3b, 0xa1, 0x1a, 0xed, 0xc3, 0x8e, 0x1b, 0xe3, 0xe6]
* [0x31a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd9035175, 0x8ce2, 0x47de, 0xa8, 0xb8, 0xcc, 0x98, 0xe5, 0xe2, 0xa8, 0x85]
* [0x3130]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x4fc0733f, 0x6fd2, 0x491b, 0xa8, 0x90, 0x53, 0x74, 0x52, 0x1b, 0xf4, 0x8f]
* [0x3150]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
## Module: PciDynamicSetup
### Boot services:
* [0x290b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2e94] EFI_BOOT_SERVICES->OpenProtocol
* [0x305a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x295e] EFI_BOOT_SERVICES->HandleProtocol
* [0x2e5f] EFI_BOOT_SERVICES->HandleProtocol
* [0x2fcc] EFI_BOOT_SERVICES->HandleProtocol
* [0x344] EFI_BOOT_SERVICES->LocateProtocol
* [0x362] EFI_BOOT_SERVICES->LocateProtocol
* [0x37f] EFI_BOOT_SERVICES->LocateProtocol
* [0x39c] EFI_BOOT_SERVICES->LocateProtocol
* [0x2eb8] EFI_BOOT_SERVICES->LocateProtocol
* [0x39b2] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ceb] EFI_BOOT_SERVICES->LocateProtocol
* [0x48be] EFI_BOOT_SERVICES->LocateProtocol
* [0x3181] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x5a60]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x5fe8]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0x5a60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x60e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x62d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x5a80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x5aa0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x5ab0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x5a70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x5ff8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x5fa8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x5a50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x4fc0733f, 0x6fd2, 0x491b, 0xa8, 0x90, 0x53, 0x74, 0x52, 0x1b, 0xf4, 0x8f]
* [0x62c0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x71202eee, 0x5f53, 0x40d9, 0xab, 0x3d, 0x9e, 0xc, 0x26, 0xd9, 0x66, 0x57]
## Module: PcieSataController
### Boot services:
* [0x1059] EFI_BOOT_SERVICES->OpenProtocol
* [0x10ba] EFI_BOOT_SERVICES->OpenProtocol
* [0x11e0] EFI_BOOT_SERVICES->OpenProtocol
* [0x1379] EFI_BOOT_SERVICES->OpenProtocol
* [0x20d8] EFI_BOOT_SERVICES->OpenProtocol
* [0x2137] EFI_BOOT_SERVICES->OpenProtocol
* [0x23bc] EFI_BOOT_SERVICES->OpenProtocol
* [0x28b6] EFI_BOOT_SERVICES->OpenProtocol
* [0x28ee] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x44d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x49a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1647] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x277f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1ad7] EFI_BOOT_SERVICES->HandleProtocol
* [0x1b75] EFI_BOOT_SERVICES->HandleProtocol
* [0x1c35] EFI_BOOT_SERVICES->HandleProtocol
* [0x1877] EFI_BOOT_SERVICES->LocateProtocol
* [0x19f5] EFI_BOOT_SERVICES->LocateProtocol
* [0x1ab2] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e76] EFI_BOOT_SERVICES->LocateProtocol
* [0x1082] EFI_BOOT_SERVICES->CloseProtocol
* [0x113f] EFI_BOOT_SERVICES->CloseProtocol
* [0x1212] EFI_BOOT_SERVICES->CloseProtocol
* [0x16c4] EFI_BOOT_SERVICES->CloseProtocol
* [0x20ff] EFI_BOOT_SERVICES->CloseProtocol
* [0x21bc] EFI_BOOT_SERVICES->CloseProtocol
* [0x2259] EFI_BOOT_SERVICES->CloseProtocol
* [0x2832] EFI_BOOT_SERVICES->CloseProtocol
* [0x2920] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x2fc0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2f90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa1e37052, 0x80d9, 0x4e65, 0xa3, 0x17, 0x3e, 0x9a, 0x55, 0xc4, 0x3e, 0xc9]
* [0x2f80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x2fa0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2acb6627, 0xdf02, 0x4e23, 0xb4, 0xf9, 0x6a, 0x93, 0xfa, 0x6e, 0x9d, 0xa6]
* [0x2fc0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2f80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x3750]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc68ed8e2, 0x9dc6, 0x4cbd, 0x9d, 0x94, 0xdb, 0x65, 0xac, 0xc5, 0xc3, 0x32]
* [0x35b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x2fd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0x2fc0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2f90]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIdeControllerInitProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa1e37052, 0x80d9, 0x4e65, 0xa3, 0x17, 0x3e, 0x9a, 0x55, 0xc4, 0x3e, 0xc9]
* [0x2f80]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
## Module: PciHostBridge
### Boot services:
* [0x987] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xbf2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2f0] EFI_BOOT_SERVICES->LocateProtocol
* [0x80c] EFI_BOOT_SERVICES->LocateProtocol
* [0xba0] EFI_BOOT_SERVICES->LocateProtocol
* [0xbbd] EFI_BOOT_SERVICES->LocateProtocol
* [0x1166] EFI_BOOT_SERVICES->LocateProtocol
* [0x1301] EFI_BOOT_SERVICES->LocateProtocol
* [0x26ae] EFI_BOOT_SERVICES->LocateProtocol
* [0x1355] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x48c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x48a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3dc21d75, 0xde0e, 0x4300, 0xa0, 0xaa, 0x19, 0xc4, 0x1c, 0xc, 0xf3, 0xdf]
* [0x4850]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuIo2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xad61f191, 0xae5f, 0x4c0e, 0xb9, 0xfa, 0xe8, 0x69, 0xd2, 0x88, 0xc6, 0x4f]
* [0x4890]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6aa1f27, 0x5597, 0x4802, 0x9f, 0x63, 0xd6, 0x28, 0x36, 0x59, 0x86, 0x35]
* [0x48b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x4fc0733f, 0x6fd2, 0x491b, 0xa8, 0x90, 0x53, 0x74, 0x52, 0x1b, 0xf4, 0x8f]
* [0x48a0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3dc21d75, 0xde0e, 0x4300, 0xa0, 0xaa, 0x19, 0xc4, 0x1c, 0xc, 0xf3, 0xdf]
## Module: PciOutOfResourceSetupPage
### Boot services:
* [0x1201] EFI_BOOT_SERVICES->OpenProtocol
* [0x1158] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x10d9] EFI_BOOT_SERVICES->HandleProtocol
* [0x11cb] EFI_BOOT_SERVICES->HandleProtocol
* [0xa76] EFI_BOOT_SERVICES->LocateProtocol
* [0xdaf] EFI_BOOT_SERVICES->LocateProtocol
* [0x1225] EFI_BOOT_SERVICES->LocateProtocol
* [0x37d] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2078]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0x22c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2170]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2038]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x2088]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x22b0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xdbc9fd21, 0xfad8, 0x45b0, 0x9e, 0x78, 0x27, 0x15, 0x88, 0x67, 0xcc, 0x93]
## Module: PciPort
### Boot services:
* [0x47d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xc80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
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
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xe90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0xe80]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
## Module: PiSmmCommunicationSmm
### Boot services:
* [0x34f] EFI_BOOT_SERVICES->LocateProtocol
* [0x37d] EFI_BOOT_SERVICES->LocateProtocol
* [0x5c7] EFI_BOOT_SERVICES->LocateProtocol
* [0x6bf] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x9a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x9c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x990]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
* [0x9b0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
## Module: PiSmmCore
### Boot services:
* [0x1baf] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x19c6] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x614] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1684] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1968] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x12a3] EFI_BOOT_SERVICES->HandleProtocol
* [0x1c6d] EFI_BOOT_SERVICES->HandleProtocol
* [0x1c95] EFI_BOOT_SERVICES->HandleProtocol
* [0x1e0f] EFI_BOOT_SERVICES->HandleProtocol
* [0x125c] EFI_BOOT_SERVICES->LocateProtocol
* [0x1282] EFI_BOOT_SERVICES->LocateProtocol
* [0x3756] EFI_BOOT_SERVICES->LocateProtocol
* [0x4233] EFI_BOOT_SERVICES->LocateProtocol
* [0x4380] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x43a5] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x6100]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x85f8]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x72617453, 0x4974, 0x616d, 0x67, 0x65, 0x3a, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0x6110]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x60f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSecurity2ArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x94ab2f58, 0x1438, 0x4ef1, 0x91, 0x52, 0x18, 0x94, 0x1a, 0x3a, 0xe, 0x68]
* [0x60e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSecurityArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa46423e3, 0x4617, 0x49f1, 0xb9, 0xff, 0xd1, 0xbf, 0xa9, 0x11, 0x58, 0x39]
* [0x6140]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0xa2f8]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0xa320]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
## Module: PiSmmCpuDxeSmm
### Boot services:
* [0x162c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x378] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a6] EFI_BOOT_SERVICES->LocateProtocol
* [0xfef] EFI_BOOT_SERVICES->LocateProtocol
* [0x112f] EFI_BOOT_SERVICES->LocateProtocol
* [0x428f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1652] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x1688] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x8f30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x8ed0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x8ee0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3fdda605, 0xa76e, 0x4f46, 0xad, 0x29, 0x12, 0xf4, 0x53, 0x1b, 0x3d, 0x8]
* [0x8f40]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
* [0xa600]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
## Module: PiSmmIpl
### Boot services:
* [0x1642] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x20e7] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1680] EFI_BOOT_SERVICES->HandleProtocol
* [0x35b8] EFI_BOOT_SERVICES->HandleProtocol
* [0x14cd] EFI_BOOT_SERVICES->LocateProtocol
* [0x1545] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b12] EFI_BOOT_SERVICES->LocateProtocol
* [0x1edf] EFI_BOOT_SERVICES->LocateProtocol
* [0x1efc] EFI_BOOT_SERVICES->LocateProtocol
* [0x201b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2152] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x40f0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x40f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x40d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeMmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x60ff8964, 0xe906, 0x41d0, 0xaf, 0xed, 0xf2, 0x41, 0xe9, 0x74, 0xe0, 0x8e]
* [0x40b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26eeb3de, 0xb689, 0x492e, 0x80, 0xf0, 0xbe, 0x8b, 0xd7, 0xda, 0x4b, 0xa7]
* [0x40a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x40c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMmControlProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x843dc720, 0xab1e, 0x42cb, 0x93, 0x57, 0x8a, 0x0, 0x78, 0xf3, 0x56, 0x1b]
* [0x40e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26baccb1, 0x6f42, 0x11d4, 0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
## Module: PlatformInfoDxe
### Boot services:
* [0x3af] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4ef] EFI_BOOT_SERVICES->LocateProtocol
* [0x3f4] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xae0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd9035175, 0x8ce2, 0x47de, 0xa8, 0xb8, 0xcc, 0x98, 0xe5, 0xe2, 0xa8, 0x85]
* [0xb00]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
* [0xaf0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiVariableWriteArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6441f818, 0x6362, 0x4e44, 0xb5, 0x70, 0x7d, 0xba, 0x31, 0xdd, 0x24, 0x53]
## Module: PlatformInitDxe
### Boot services:
* [0x179d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x17d8] EFI_BOOT_SERVICES->HandleProtocol
* [0x332] EFI_BOOT_SERVICES->LocateProtocol
* [0x36f] EFI_BOOT_SERVICES->LocateProtocol
* [0x84d] EFI_BOOT_SERVICES->LocateProtocol
* [0x8f8] EFI_BOOT_SERVICES->LocateProtocol
* [0xab9] EFI_BOOT_SERVICES->LocateProtocol
* [0xb18] EFI_BOOT_SERVICES->LocateProtocol
* [0xc6a] EFI_BOOT_SERVICES->LocateProtocol
* [0xe3f] EFI_BOOT_SERVICES->LocateProtocol
* [0xea9] EFI_BOOT_SERVICES->LocateProtocol
* [0xee8] EFI_BOOT_SERVICES->LocateProtocol
* [0xff0] EFI_BOOT_SERVICES->LocateProtocol
* [0x1096] EFI_BOOT_SERVICES->LocateProtocol
* [0x10d7] EFI_BOOT_SERVICES->LocateProtocol
* [0x1139] EFI_BOOT_SERVICES->LocateProtocol
* [0x146f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1cd7] EFI_BOOT_SERVICES->LocateProtocol
* [0x2087] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ed7] EFI_BOOT_SERVICES->LocateProtocol
* [0x308d] EFI_BOOT_SERVICES->LocateProtocol
* [0x33bf] EFI_BOOT_SERVICES->LocateProtocol
* [0xf35] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x13a4] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x39c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x3a10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0x3a30]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x3980]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd4d2f201, 0x50e8, 0x4d45, 0x8e, 0x5, 0xfd, 0x49, 0xa8, 0x2a, 0x15, 0x69]
* [0x39a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
* [0x3990]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xe223cf65, 0xf6ce, 0x4122, 0xb3, 0xaf, 0x4b, 0xd1, 0x8a, 0xff, 0x40, 0xa1]
* [0x39d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6aa1f27, 0x5597, 0x4802, 0x9f, 0x63, 0xd6, 0x28, 0x36, 0x59, 0x86, 0x35]
* [0x39e0]
	 - [service] LocateProtocol
	 - [protocol_name] gPlatformGOPPolicyGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xec2e931b, 0x3281, 0x48a5, 0x81, 0x7, 0xdf, 0x8a, 0x8b, 0xed, 0x3c, 0x5d]
* [0x39b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd9035175, 0x8ce2, 0x47de, 0xa8, 0xb8, 0xcc, 0x98, 0xe5, 0xe2, 0xa8, 0x85]
* [0x3a00]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
* [0x3a20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3583ff6, 0xcb36, 0x4940, 0x94, 0x7e, 0xb9, 0xb3, 0x9f, 0x4a, 0xfa, 0xf7]
* [0x3a40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8d9b3387, 0x73db, 0x456f, 0x88, 0x9d, 0x6f, 0xfe, 0x90, 0x82, 0x64, 0x9]
* [0x4908]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0x39f0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xdbc9fd21, 0xfad8, 0x45b0, 0x9e, 0x78, 0x27, 0x15, 0x88, 0x67, 0xcc, 0x93]
## Module: PlatformSetup
### Boot services:
* [0x1195] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x30f] EFI_BOOT_SERVICES->LocateProtocol
* [0x5be] EFI_BOOT_SERVICES->LocateProtocol
* [0xfc4] EFI_BOOT_SERVICES->LocateProtocol
* [0xfdf] EFI_BOOT_SERVICES->LocateProtocol
* [0xffc] EFI_BOOT_SERVICES->LocateProtocol
* [0x13e7] EFI_BOOT_SERVICES->LocateProtocol
* [0x1840] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x1b70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0x1af0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3fdda605, 0xa76e, 0x4f46, 0xad, 0x29, 0x12, 0xf4, 0x53, 0x1b, 0x3d, 0x8]
* [0x1ae0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x1b30]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd9035175, 0x8ce2, 0x47de, 0xa8, 0xb8, 0xcc, 0x98, 0xe5, 0xe2, 0xa8, 0x85]
* [0x1b50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6aa1f27, 0x5597, 0x4802, 0x9f, 0x63, 0xd6, 0x28, 0x36, 0x59, 0x86, 0x35]
* [0x1b60]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
## Module: PolicyInitDxe
### Boot services:
* [0x3f4] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4bc] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4fa] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x63e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc0e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x308] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d5b] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3e60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x3e70]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
## Module: PostReport
### Boot services:
* [0xde5] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x374] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xe52] EFI_BOOT_SERVICES->HandleProtocol
* [0xedb] EFI_BOOT_SERVICES->HandleProtocol
* [0x390] EFI_BOOT_SERVICES->LocateProtocol
* [0x5de] EFI_BOOT_SERVICES->LocateProtocol
* [0x83e] EFI_BOOT_SERVICES->LocateProtocol
* [0x8d2] EFI_BOOT_SERVICES->LocateProtocol
* [0xc1b] EFI_BOOT_SERVICES->LocateProtocol
* [0xdb3] EFI_BOOT_SERVICES->LocateProtocol
* [0x1644] EFI_BOOT_SERVICES->LocateProtocol
* [0x16c3] EFI_BOOT_SERVICES->LocateProtocol
* [0x1743] EFI_BOOT_SERVICES->LocateProtocol
* [0x1761] EFI_BOOT_SERVICES->LocateProtocol
* [0x18a1] EFI_BOOT_SERVICES->LocateProtocol
* [0x1992] EFI_BOOT_SERVICES->LocateProtocol
* [0x19fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x1a15] EFI_BOOT_SERVICES->LocateProtocol
* [0x2254] EFI_BOOT_SERVICES->LocateProtocol
* [0x2319] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2be0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x31c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0x2bc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDataHubProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xae80d021, 0x618e, 0x11d4, 0xbc, 0xd7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
* [0x2c00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3583ff6, 0xcb36, 0x4940, 0x94, 0x7e, 0xb9, 0xb3, 0x9f, 0x4a, 0xfa, 0xf7]
* [0x2bf0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x903dd14, 0x2ca0, 0x458a, 0xb5, 0xeb, 0xc, 0xc, 0xa3, 0xd, 0x78, 0x5c]
* [0x31a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2ad8e2d2, 0x2e91, 0x4cd1, 0x95, 0xf5, 0xe7, 0x8f, 0xe5, 0xeb, 0xe3, 0x16]
* [0x2bd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x31d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x387225ff, 0x5e97, 0x4ef0, 0x86, 0x9d, 0xd, 0x73, 0x5d, 0x84, 0xf5, 0xea]
* [0x31b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0x3128]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
## Module: PowerButton
### Boot services:
* [0x300] EFI_BOOT_SERVICES->LocateProtocol
* [0x335] EFI_BOOT_SERVICES->LocateProtocol
* [0x408] EFI_BOOT_SERVICES->LocateProtocol
* [0x4a8] EFI_BOOT_SERVICES->LocateProtocol
* [0x57d] EFI_BOOT_SERVICES->LocateProtocol
* [0x76d] EFI_BOOT_SERVICES->LocateProtocol
* [0x855] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xd30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xd70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x1258]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xd60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: PowerMgmtDxe
### Boot services:
* [0x77c] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3cd] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x7b4] EFI_BOOT_SERVICES->HandleProtocol
* [0x312] EFI_BOOT_SERVICES->LocateProtocol
* [0x405] EFI_BOOT_SERVICES->LocateProtocol
* [0x1487] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x16c0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x16c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x16e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0x16b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xab5a4df4, 0xf0d7, 0x49a8, 0xbf, 0x5c, 0xf2, 0x5d, 0xa0, 0x4c, 0x25, 0x33]
* [0x16d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xeb97088e, 0xcfdf, 0x49c6, 0xbe, 0x4b, 0xd9, 0x6, 0xa5, 0xb2, 0xe, 0x86]
## Module: PowerMgmtSmm
### Boot services:
* [0x32f] EFI_BOOT_SERVICES->LocateProtocol
* [0x35d] EFI_BOOT_SERVICES->LocateProtocol
* [0x464] EFI_BOOT_SERVICES->LocateProtocol
* [0x833] EFI_BOOT_SERVICES->LocateProtocol
* [0x160e] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1c00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1c50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x1c40]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xab5a4df4, 0xf0d7, 0x49a8, 0xbf, 0x5c, 0xf2, 0x5d, 0xa0, 0x4c, 0x25, 0x33]
## Module: Ps2Main
### Boot services:
* [0x6f0] EFI_BOOT_SERVICES->OpenProtocol
* [0xa03] EFI_BOOT_SERVICES->OpenProtocol
* [0x2dd3] EFI_BOOT_SERVICES->OpenProtocol
* [0x2e79] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xdcb] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x2f22] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x342] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xb82] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x7cb] EFI_BOOT_SERVICES->LocateProtocol
* [0x8a4] EFI_BOOT_SERVICES->LocateProtocol
* [0x2227] EFI_BOOT_SERVICES->LocateProtocol
* [0x250d] EFI_BOOT_SERVICES->LocateProtocol
* [0x252f] EFI_BOOT_SERVICES->LocateProtocol
* [0x317e] EFI_BOOT_SERVICES->LocateProtocol
* [0x31b5] EFI_BOOT_SERVICES->LocateProtocol
* [0x3edc] EFI_BOOT_SERVICES->LocateProtocol
* [0x791] EFI_BOOT_SERVICES->CloseProtocol
* [0xbab] EFI_BOOT_SERVICES->CloseProtocol
* [0xdf7] EFI_BOOT_SERVICES->CloseProtocol
* [0x2e20] EFI_BOOT_SERVICES->CloseProtocol
* [0x2ea5] EFI_BOOT_SERVICES->CloseProtocol
* [0x2f4a] EFI_BOOT_SERVICES->CloseProtocol
* [0x4011] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x4280]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x42a0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31878c87, 0xb75, 0x11d5, 0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x42e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x4300]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb295bd1c, 0x63e3, 0x48e3, 0xb2, 0x65, 0xf7, 0xdf, 0xa2, 0x7, 0x1, 0x23]
* [0x42f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacy8259ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x38321dba, 0x4fe0, 0x4e17, 0x8a, 0xec, 0x41, 0x30, 0x55, 0xea, 0xed, 0xc1]
* [0x42d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26baccb1, 0x6f42, 0x11d4, 0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
* [0x4838]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x4280]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
## Module: RaidDriver
### Boot services:
* [0x8dff] EFI_BOOT_SERVICES->OpenProtocol
* [0x906e] EFI_BOOT_SERVICES->OpenProtocol
* [0x90c3] EFI_BOOT_SERVICES->OpenProtocol
* [0x92cb] EFI_BOOT_SERVICES->OpenProtocol
* [0x5478] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x8850] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x98f7] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x9aab] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x9ad9] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x9b0c] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xf75d] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x53b4] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x7675] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x7de5] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8568] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8800] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8f49] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x928c] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9316] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xf6b7] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xfd9b] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x22a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x293d] EFI_BOOT_SERVICES->LocateProtocol
* [0x299f] EFI_BOOT_SERVICES->LocateProtocol
* [0x29fb] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a5a] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a77] EFI_BOOT_SERVICES->LocateProtocol
* [0x88f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x8970] EFI_BOOT_SERVICES->LocateProtocol
* [0x89ee] EFI_BOOT_SERVICES->LocateProtocol
* [0x8a6a] EFI_BOOT_SERVICES->LocateProtocol
* [0x8cda] EFI_BOOT_SERVICES->LocateProtocol
* [0x8fc7] EFI_BOOT_SERVICES->LocateProtocol
* [0x8fff] EFI_BOOT_SERVICES->LocateProtocol
* [0x9092] EFI_BOOT_SERVICES->LocateProtocol
* [0x94b8] EFI_BOOT_SERVICES->LocateProtocol
* [0x94eb] EFI_BOOT_SERVICES->LocateProtocol
* [0xb242] EFI_BOOT_SERVICES->LocateProtocol
* [0x99dc] EFI_BOOT_SERVICES->CloseProtocol
* [0x9a76] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x2ffa0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiAcpiSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdbff9d55, 0x89b7, 0x46da, 0xbd, 0xdf, 0x67, 0x7d, 0x3d, 0xc0, 0x24, 0x1d]
* [0x30010]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x30140]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb9d4c360, 0xbcfb, 0x4f9b, 0x92, 0x98, 0x53, 0xc1, 0x36, 0x98, 0x22, 0x58]
* [0x2ff60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x301d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x30160]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x2ff50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x2ff40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
* [0x30070]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x2ffc0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
* [0x2ffa0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdbff9d55, 0x89b7, 0x46da, 0xbd, 0xdf, 0x67, 0x7d, 0x3d, 0xc0, 0x24, 0x1d]
* [0x30170]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x30100]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x30010]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
## Module: ReFlash
### Boot services:
* [0xab0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4338] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x345d] EFI_BOOT_SERVICES->OpenProtocol
* [0xf65] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2aea] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xaeb] EFI_BOOT_SERVICES->HandleProtocol
* [0x2a6a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3427] EFI_BOOT_SERVICES->HandleProtocol
* [0x4373] EFI_BOOT_SERVICES->HandleProtocol
* [0x340] EFI_BOOT_SERVICES->LocateProtocol
* [0x8e1] EFI_BOOT_SERVICES->LocateProtocol
* [0xd26] EFI_BOOT_SERVICES->LocateProtocol
* [0x10f8] EFI_BOOT_SERVICES->LocateProtocol
* [0x113c] EFI_BOOT_SERVICES->LocateProtocol
* [0x1db4] EFI_BOOT_SERVICES->LocateProtocol
* [0x240a] EFI_BOOT_SERVICES->LocateProtocol
* [0x2743] EFI_BOOT_SERVICES->LocateProtocol
* [0x2cae] EFI_BOOT_SERVICES->LocateProtocol
* [0x2e2b] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f75] EFI_BOOT_SERVICES->LocateProtocol
* [0x30bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x30ff] EFI_BOOT_SERVICES->LocateProtocol
* [0x3248] EFI_BOOT_SERVICES->LocateProtocol
* [0x3289] EFI_BOOT_SERVICES->LocateProtocol
* [0x3481] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x5150]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x57a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0x5150]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x5af8]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x5170]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x5120]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x755b6596, 0x6896, 0x4ba3, 0xb3, 0xdd, 0x1c, 0x62, 0x9f, 0xd1, 0xea, 0x88]
* [0x5160]
	 - [service] LocateProtocol
	 - [protocol_name] gEsrtManagementProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa340c064, 0x723c, 0x4a9c, 0xa4, 0xdd, 0xd5, 0xb4, 0x7a, 0x26, 0xfb, 0xb0]
* [0x59c0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0x5140]
	 - [service] LocateProtocol
	 - [protocol_name] EFI_CONSOLE_CONTROL_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] [0xf42f7782, 0x12e, 0x4c12, 0x99, 0x56, 0x49, 0xf9, 0x43, 0x4, 0xf7, 0x21]
* [0x5760]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x5780]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x5790]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb9d4c360, 0xbcfb, 0x4f9b, 0x92, 0x98, 0x53, 0xc1, 0x36, 0x98, 0x22, 0x58]
* [0x57b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
## Module: RomLayoutDxe
### Boot services:
* [0x548] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x953] EFI_BOOT_SERVICES->HandleProtocol
* [0x522] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xa98]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3aa83745, 0x9454, 0x4f7a, 0xa7, 0xc0, 0x90, 0xdb, 0xd0, 0x2f, 0xab, 0x8e]
## Module: RstOneClickEnable
### Boot services:
* empty
### Protocols:
* empty
## Module: RTCWakeup
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x4ec] EFI_BOOT_SERVICES->LocateProtocol
* [0x5c8] EFI_BOOT_SERVICES->LocateProtocol
* [0x831] EFI_BOOT_SERVICES->LocateProtocol
* [0x919] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xcd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x11d8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xcf0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: RuntimeDxe
### Boot services:
* [0x1356] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1257] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* [0x2040]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
## Module: RuntimeSmm
### Boot services:
* [0x3fd] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x497] EFI_BOOT_SERVICES->LocateProtocol
* [0x63d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x9c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xec8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x9e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: S3SaveStateDxe
### Boot services:
* [0x47e] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x4af] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x24f8] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x261b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x38b] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1e50] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f38] EFI_BOOT_SERVICES->LocateProtocol
* [0x202a] EFI_BOOT_SERVICES->LocateProtocol
* [0x2148] EFI_BOOT_SERVICES->LocateProtocol
* [0x2289] EFI_BOOT_SERVICES->LocateProtocol
* [0x2387] EFI_BOOT_SERVICES->LocateProtocol
* [0x2584] EFI_BOOT_SERVICES->LocateProtocol
* [0x2d33] EFI_BOOT_SERVICES->LocateProtocol
* [0x2547] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2f10]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x47b7fa8c, 0xf4bd, 0x4af6, 0x82, 0x0, 0x33, 0x30, 0x86, 0xf0, 0xd2, 0xc8]
* [0x2eb0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0x2ee0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc68ed8e2, 0x9dc6, 0x4cbd, 0x9d, 0x94, 0xdb, 0x65, 0xac, 0xc5, 0xc3, 0x32]
* [0x2f00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeMmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x60ff8964, 0xe906, 0x41d0, 0xaf, 0xed, 0xf2, 0x41, 0xe9, 0x74, 0xe0, 0x8e]
* [0x2ef0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2ed0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
* [0x2f00]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiDxeMmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x60ff8964, 0xe906, 0x41d0, 0xaf, 0xed, 0xf2, 0x41, 0xe9, 0x74, 0xe0, 0x8e]
## Module: SaInitDxe
### Boot services:
* [0x728] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8f3] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1caf] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2314] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2669] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2a40] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3119] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x557] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xbb2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x30b2] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x75d] EFI_BOOT_SERVICES->HandleProtocol
* [0x925] EFI_BOOT_SERVICES->HandleProtocol
* [0x1ce1] EFI_BOOT_SERVICES->HandleProtocol
* [0x2356] EFI_BOOT_SERVICES->HandleProtocol
* [0x269b] EFI_BOOT_SERVICES->HandleProtocol
* [0x2a6b] EFI_BOOT_SERVICES->HandleProtocol
* [0x315d] EFI_BOOT_SERVICES->HandleProtocol
* [0x320] EFI_BOOT_SERVICES->LocateProtocol
* [0x350] EFI_BOOT_SERVICES->LocateProtocol
* [0x6ea] EFI_BOOT_SERVICES->LocateProtocol
* [0x9be] EFI_BOOT_SERVICES->LocateProtocol
* [0xb20] EFI_BOOT_SERVICES->LocateProtocol
* [0x1039] EFI_BOOT_SERVICES->LocateProtocol
* [0x1c86] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e4a] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e8f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1eaf] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f2f] EFI_BOOT_SERVICES->LocateProtocol
* [0x249a] EFI_BOOT_SERVICES->LocateProtocol
* [0x272f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2900] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b0c] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b67] EFI_BOOT_SERVICES->LocateProtocol
* [0x2bea] EFI_BOOT_SERVICES->LocateProtocol
* [0x2d58] EFI_BOOT_SERVICES->LocateProtocol
* [0x2d92] EFI_BOOT_SERVICES->LocateProtocol
* [0x8dce] EFI_BOOT_SERVICES->LocateProtocol
* [0x46a] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x508] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x91a0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x9180]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x91e0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x603df7ca, 0x1ba8, 0x4c12, 0xa9, 0x8a, 0x49, 0x6d, 0xfe, 0x77, 0xeb, 0xdf]
* [0x91a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x9180]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x91f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0x9170]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x9120]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
* [0x9140]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6aa1f27, 0x5597, 0x4802, 0x9f, 0x63, 0xd6, 0x28, 0x36, 0x59, 0x86, 0x35]
* [0x91d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x1861e089, 0xcaa3, 0x473e, 0x84, 0x32, 0xdc, 0x1f, 0x94, 0xc6, 0xc1, 0xa6]
* [0x91b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x91c0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x651b7ebd, 0xce13, 0x41d0, 0x82, 0xe5, 0xa0, 0x63, 0xab, 0xbe, 0x9b, 0xb6]
* [0x9130]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3dc21d75, 0xde0e, 0x4300, 0xa0, 0xaa, 0x19, 0xc4, 0x1c, 0xc, 0xf3, 0xdf]
* [0x9150]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26baccb1, 0x6f42, 0x11d4, 0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
* [0x9160]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiPciEnumerationCompleteProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x30cfe3e7, 0x3de1, 0x4586, 0xbe, 0x20, 0xde, 0xab, 0xa1, 0xb3, 0xb7, 0x93]
## Module: SaLateInitSmm
### Boot services:
* [0x5d6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x34c] EFI_BOOT_SERVICES->LocateProtocol
* [0x37a] EFI_BOOT_SERVICES->LocateProtocol
* [0x582] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2410]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2420]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x23e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6aa1f27, 0x5597, 0x4802, 0x9f, 0x63, 0xd6, 0x28, 0x36, 0x59, 0x86, 0x35]
## Module: SataController
### Boot services:
* [0x363] EFI_BOOT_SERVICES->OpenProtocol
* [0x3b6] EFI_BOOT_SERVICES->OpenProtocol
* [0x54d] EFI_BOOT_SERVICES->OpenProtocol
* [0x742] EFI_BOOT_SERVICES->OpenProtocol
* [0xc0a] EFI_BOOT_SERVICES->OpenProtocol
* [0x779] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x31b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x6bd] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x38a] EFI_BOOT_SERVICES->CloseProtocol
* [0x406] EFI_BOOT_SERVICES->CloseProtocol
* [0x411] EFI_BOOT_SERVICES->CloseProtocol
* [0x6e8] EFI_BOOT_SERVICES->CloseProtocol
* [0x79c] EFI_BOOT_SERVICES->CloseProtocol
* [0xc2c] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x1170]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x1180]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x1160]
	 - [service] OpenProtocol
	 - [protocol_name] gSataControllerDriverGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbb929da9, 0x68f7, 0x4035, 0xb2, 0x2c, 0xa3, 0xbb, 0x3f, 0x23, 0xda, 0x55]
* [0x1170]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x1180]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
## Module: SaveMemoryConfig
### Boot services:
* [0x45c] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x5b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
## Module: SavePegConfig
### Boot services:
* [0x489] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x620]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
## Module: SbDxe
### Boot services:
* [0x10da] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2045] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4a6] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4da] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x88d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xdb0] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1474] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x830] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1497] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x110f] EFI_BOOT_SERVICES->HandleProtocol
* [0x12bd] EFI_BOOT_SERVICES->HandleProtocol
* [0x1550] EFI_BOOT_SERVICES->HandleProtocol
* [0x1f3f] EFI_BOOT_SERVICES->HandleProtocol
* [0x2083] EFI_BOOT_SERVICES->HandleProtocol
* [0x20b1] EFI_BOOT_SERVICES->HandleProtocol
* [0x2f0] EFI_BOOT_SERVICES->LocateProtocol
* [0x74c] EFI_BOOT_SERVICES->LocateProtocol
* [0x771] EFI_BOOT_SERVICES->LocateProtocol
* [0xae4] EFI_BOOT_SERVICES->LocateProtocol
* [0xdec] EFI_BOOT_SERVICES->LocateProtocol
* [0xec5] EFI_BOOT_SERVICES->LocateProtocol
* [0x19aa] EFI_BOOT_SERVICES->LocateProtocol
* [0x32a0] EFI_BOOT_SERVICES->LocateProtocol
* [0x34b5] EFI_BOOT_SERVICES->LocateProtocol
* [0x3395] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x5e20]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x5e50]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x5e00]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x17706d27, 0x83fe, 0x4770, 0x87, 0x5f, 0x4c, 0xef, 0x4c, 0xb8, 0xf6, 0x3d]
* [0x6a90]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiWatchdogTimerArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x665e3ff5, 0x46cc, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6a80]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5d206dd3, 0x516a, 0x47dc, 0xa1, 0xbc, 0x6d, 0xa2, 0x4, 0xaa, 0xbe, 0x8]
* [0x5e20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x5dc0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x5e30]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xf2a128ff, 0x257b, 0x456e, 0x9d, 0xe8, 0x63, 0xe7, 0xc7, 0xdc, 0xdf, 0xac]
* [0x5e50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x5e40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x5da0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x5d90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0x5dd0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiTableProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xffe06bdd, 0x6107, 0x46a6, 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c]
* [0x5df0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2e058b2b, 0xedc1, 0x4431, 0x87, 0xd9, 0xc6, 0xc4, 0xea, 0x10, 0x2b, 0xe3]
* [0x5e10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGlobalNvsAreaProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x74e1e48, 0x8132, 0x47a1, 0x8c, 0x2c, 0x3f, 0x14, 0xad, 0x9a, 0x66, 0xdc]
* [0x6838]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x67a8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xeb97088e, 0xcfdf, 0x49c6, 0xbe, 0x4b, 0xd9, 0x6, 0xa5, 0xb2, 0xe, 0x86]
## Module: SbRun
### Boot services:
* [0x155d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x15df] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x111a] EFI_BOOT_SERVICES->LocateProtocol
* [0x16b0] EFI_BOOT_SERVICES->LocateProtocol
* [0x17e9] EFI_BOOT_SERVICES->LocateProtocol
* [0x14f2] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x40c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x46a8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x40a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
* [0x4090]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiResetArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x27cfac88, 0x46cc, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
## Module: SbRunSmm
### Boot services:
* [0x378] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x480] EFI_BOOT_SERVICES->LocateProtocol
* [0x8b7] EFI_BOOT_SERVICES->LocateProtocol
* [0x13c4] EFI_BOOT_SERVICES->LocateProtocol
* [0x14fd] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2950]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2980]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x2f08]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2f48]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x2970]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: SdioDriver
### Boot services:
* [0x3f2] EFI_BOOT_SERVICES->OpenProtocol
* [0x4c7] EFI_BOOT_SERVICES->OpenProtocol
* [0x51a] EFI_BOOT_SERVICES->OpenProtocol
* [0x635] EFI_BOOT_SERVICES->OpenProtocol
* [0x66e] EFI_BOOT_SERVICES->OpenProtocol
* [0x6c7] EFI_BOOT_SERVICES->OpenProtocol
* [0x9ff] EFI_BOOT_SERVICES->OpenProtocol
* [0xa80] EFI_BOOT_SERVICES->OpenProtocol
* [0xb24] EFI_BOOT_SERVICES->OpenProtocol
* [0xcd6] EFI_BOOT_SERVICES->OpenProtocol
* [0xcff] EFI_BOOT_SERVICES->OpenProtocol
* [0xd27] EFI_BOOT_SERVICES->OpenProtocol
* [0xf99] EFI_BOOT_SERVICES->OpenProtocol
* [0x13a3] EFI_BOOT_SERVICES->OpenProtocol
* [0xb45] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xb81] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xca3] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x87d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xe5f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x356] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xf60] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xfff] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x103d] EFI_BOOT_SERVICES->LocateProtocol
* [0x16d6] EFI_BOOT_SERVICES->LocateProtocol
* [0x4ee] EFI_BOOT_SERVICES->CloseProtocol
* [0x57e] EFI_BOOT_SERVICES->CloseProtocol
* [0x694] EFI_BOOT_SERVICES->CloseProtocol
* [0x990] EFI_BOOT_SERVICES->CloseProtocol
* [0xa49] EFI_BOOT_SERVICES->CloseProtocol
* [0xc50] EFI_BOOT_SERVICES->CloseProtocol
* [0xc6e] EFI_BOOT_SERVICES->CloseProtocol
* [0xc88] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x40f0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x94c69847, 0xa0cf, 0x4635, 0xaa, 0x23, 0xd2, 0x66, 0x7b, 0xd7, 0xf7, 0x91]
* [0x40c0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x40b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x40d0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x40d0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x40c0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x40f0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x94c69847, 0xa0cf, 0x4635, 0xaa, 0x23, 0xd2, 0x66, 0x7b, 0xd7, 0xf7, 0x91]
* [0x40e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x9708adb2, 0x28b1, 0x46f7, 0x9a, 0x6c, 0xe7, 0x44, 0x97, 0xfa, 0x66, 0x79]
* [0x4110]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMmCommunicationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc68ed8e2, 0x9dc6, 0x4cbd, 0x9d, 0x94, 0xdb, 0x65, 0xac, 0xc5, 0xc3, 0x32]
* [0x40c0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x40b0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
## Module: SdioInt13
### Boot services:
* [0x39d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2df] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x7f0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x9708adb2, 0x28b1, 0x46f7, 0x9a, 0x6c, 0xe7, 0x44, 0x97, 0xfa, 0x66, 0x79]
* [0x7e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8e008510, 0x9bb1, 0x457d, 0x9f, 0x70, 0x89, 0x7a, 0xba, 0x86, 0x5d, 0xb9]
## Module: SdioSmm
### Boot services:
* [0x2e2] EFI_BOOT_SERVICES->LocateProtocol
* [0x4c1] EFI_BOOT_SERVICES->LocateProtocol
* [0x555] EFI_BOOT_SERVICES->LocateProtocol
* [0xb05] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1860]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1d88]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1890]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: SecFlashUpdDXE
### Boot services:
* [0x1170] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2000]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3aa83745, 0x9454, 0x4f7a, 0xa7, 0xc0, 0x90, 0xdb, 0xd0, 0x2f, 0xab, 0x8e]
## Module: SecSMIFlash
### Boot services:
* [0xf12] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xf55] EFI_BOOT_SERVICES->HandleProtocol
* [0x36f] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a3] EFI_BOOT_SERVICES->LocateProtocol
* [0x473] EFI_BOOT_SERVICES->LocateProtocol
* [0x1171] EFI_BOOT_SERVICES->LocateProtocol
* [0x13c6] EFI_BOOT_SERVICES->LocateProtocol
* [0x152f] EFI_BOOT_SERVICES->LocateProtocol
* [0x23ed] EFI_BOOT_SERVICES->LocateProtocol
* [0x1479] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x31a0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x31a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x31b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x31e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x3758]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x3190]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xecb867ab, 0x8df4, 0x492d, 0x81, 0x50, 0xa7, 0xfd, 0x1b, 0x9b, 0x5a, 0x75]
* [0x31d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: SecureBootDXE
### Boot services:
* [0x12e1] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1322] EFI_BOOT_SERVICES->HandleProtocol
* [0x193a] EFI_BOOT_SERVICES->LocateProtocol
* [0x1c73] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3020]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x3020]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x35c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
## Module: SecureEraseDxe
### Boot services:
* [0xcfe] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1a1a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x21ba] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x98e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xa7c] EFI_BOOT_SERVICES->HandleProtocol
* [0xabc] EFI_BOOT_SERVICES->HandleProtocol
* [0x1a80] EFI_BOOT_SERVICES->HandleProtocol
* [0x1b09] EFI_BOOT_SERVICES->HandleProtocol
* [0x2268] EFI_BOOT_SERVICES->HandleProtocol
* [0x304] EFI_BOOT_SERVICES->LocateProtocol
* [0x322] EFI_BOOT_SERVICES->LocateProtocol
* [0x33f] EFI_BOOT_SERVICES->LocateProtocol
* [0x35c] EFI_BOOT_SERVICES->LocateProtocol
* [0x379] EFI_BOOT_SERVICES->LocateProtocol
* [0x561] EFI_BOOT_SERVICES->LocateProtocol
* [0x5c2] EFI_BOOT_SERVICES->LocateProtocol
* [0x6c2] EFI_BOOT_SERVICES->LocateProtocol
* [0x8d0] EFI_BOOT_SERVICES->LocateProtocol
* [0x21f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a4f] EFI_BOOT_SERVICES->LocateProtocol
* [0xa28] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x42b0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4270]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x52c78312, 0x8edc, 0x4233, 0x98, 0xf2, 0x1a, 0x1a, 0xa5, 0xe3, 0x88, 0xa5]
* [0x4260]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiAtaPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x1d3de7f0, 0x807, 0x424f, 0xaa, 0x69, 0x11, 0xa5, 0x4e, 0x19, 0xa4, 0x6f]
* [0x4c60]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0x4290]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x42b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4270]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiNvmExpressPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x52c78312, 0x8edc, 0x4233, 0x98, 0xf2, 0x1a, 0x1a, 0xa5, 0xe3, 0x88, 0xa5]
* [0x4310]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x4260]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAtaPassThruProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x1d3de7f0, 0x807, 0x424f, 0xaa, 0x69, 0x11, 0xa5, 0x4e, 0x19, 0xa4, 0x6f]
* [0x42d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x42f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x4300]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x42c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x42e0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
* [0x4280]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x42a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x919383de, 0xebac, 0x4924, 0x1, 0x94, 0x52, 0x59, 0xe0, 0xd, 0x65, 0x7a]
## Module: SecurityStubDxe
### Boot services:
* [0xe22] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x2de] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x622] EFI_BOOT_SERVICES->HandleProtocol
* [0xb31] EFI_BOOT_SERVICES->HandleProtocol
* [0x4734] EFI_BOOT_SERVICES->HandleProtocol
* [0x482b] EFI_BOOT_SERVICES->HandleProtocol
* [0x4a44] EFI_BOOT_SERVICES->HandleProtocol
* [0x4afa] EFI_BOOT_SERVICES->HandleProtocol
* [0x36c] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x3f4] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x8fb0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0x6a60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6a80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x6ab0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6aa0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFile2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4006c0c1, 0xfcb3, 0x403e, 0x99, 0x6d, 0x4a, 0x6c, 0x87, 0x24, 0xe0, 0x6d]
* [0x6a90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x56ec3091, 0x954c, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6af0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiDxeMmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x60ff8964, 0xe906, 0x41d0, 0xaf, 0xed, 0xf2, 0x41, 0xe9, 0x74, 0xe0, 0x8e]
* [0x6a30]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3aa83745, 0x9454, 0x4f7a, 0xa7, 0xc0, 0x90, 0xdb, 0xd0, 0x2f, 0xab, 0x8e]
## Module: SerialIo
### Boot services:
* [0x40a] EFI_BOOT_SERVICES->OpenProtocol
* [0x4a9] EFI_BOOT_SERVICES->OpenProtocol
* [0x59d] EFI_BOOT_SERVICES->OpenProtocol
* [0x64e] EFI_BOOT_SERVICES->OpenProtocol
* [0x688] EFI_BOOT_SERVICES->OpenProtocol
* [0x996] EFI_BOOT_SERVICES->OpenProtocol
* [0xb2a] EFI_BOOT_SERVICES->OpenProtocol
* [0xb81] EFI_BOOT_SERVICES->OpenProtocol
* [0xc8d] EFI_BOOT_SERVICES->OpenProtocol
* [0x10d0] EFI_BOOT_SERVICES->OpenProtocol
* [0x11ec] EFI_BOOT_SERVICES->OpenProtocol
* [0x1ff2] EFI_BOOT_SERVICES->OpenProtocol
* [0x71a] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xdc6] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x126e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x33f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1069] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1739] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x839] EFI_BOOT_SERVICES->HandleProtocol
* [0x4d0] EFI_BOOT_SERVICES->CloseProtocol
* [0x5c4] EFI_BOOT_SERVICES->CloseProtocol
* [0x6d0] EFI_BOOT_SERVICES->CloseProtocol
* [0xcbb] EFI_BOOT_SERVICES->CloseProtocol
* [0xcd9] EFI_BOOT_SERVICES->CloseProtocol
* [0xcf7] EFI_BOOT_SERVICES->CloseProtocol
* [0x1165] EFI_BOOT_SERVICES->CloseProtocol
* [0x1188] EFI_BOOT_SERVICES->CloseProtocol
* [0x11ab] EFI_BOOT_SERVICES->CloseProtocol
* [0x1236] EFI_BOOT_SERVICES->CloseProtocol
* [0x2066] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x2d80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSerialIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbb25cf6f, 0xf1d4, 0x11d2, 0x9a, 0xc, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0xfd]
* [0x2db0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x50dc5c90, 0x1d33, 0x4fd6, 0x87, 0xe5, 0x6, 0x3b, 0x1d, 0xfa, 0x21, 0x70]
* [0x2d60]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x51e9b4f9, 0x555d, 0x476c, 0x8b, 0xb5, 0xbd, 0x18, 0xd9, 0xa6, 0x88, 0x78]
* [0x2dc0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2da0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x2dc0]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2db0]
	 - [service] CloseProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x50dc5c90, 0x1d33, 0x4fd6, 0x87, 0xe5, 0x6, 0x3b, 0x1d, 0xfa, 0x21, 0x70]
* [0x2d60]
	 - [service] CloseProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x51e9b4f9, 0x555d, 0x476c, 0x8b, 0xb5, 0xbd, 0x18, 0xd9, 0xa6, 0x88, 0x78]
* [0x2da0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x2dc0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
## Module: SerialOverLan
### Boot services:
* [0x3fb] EFI_BOOT_SERVICES->OpenProtocol
* [0x461] EFI_BOOT_SERVICES->OpenProtocol
* [0x629] EFI_BOOT_SERVICES->OpenProtocol
* [0x66d] EFI_BOOT_SERVICES->OpenProtocol
* [0x72c] EFI_BOOT_SERVICES->OpenProtocol
* [0xb1f] EFI_BOOT_SERVICES->OpenProtocol
* [0xc7a] EFI_BOOT_SERVICES->OpenProtocol
* [0xd11] EFI_BOOT_SERVICES->OpenProtocol
* [0x1d03] EFI_BOOT_SERVICES->OpenProtocol
* [0x87f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xcd8] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x35a] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xae3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1717] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xbf5] EFI_BOOT_SERVICES->HandleProtocol
* [0x3a8] EFI_BOOT_SERVICES->LocateProtocol
* [0x6b7] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x438] EFI_BOOT_SERVICES->CloseProtocol
* [0x5ba] EFI_BOOT_SERVICES->CloseProtocol
* [0xb45] EFI_BOOT_SERVICES->CloseProtocol
* [0xb63] EFI_BOOT_SERVICES->CloseProtocol
* [0xc18] EFI_BOOT_SERVICES->CloseProtocol
* [0xc36] EFI_BOOT_SERVICES->CloseProtocol
* [0xcaa] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x2520]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2500]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x2510]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSerialIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbb25cf6f, 0xf1d4, 0x11d2, 0x9a, 0xc, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0xfd]
* [0x2520]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2520]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2550]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd25dc167, 0xeb6a, 0x432d, 0x65, 0x91, 0xbf, 0x80, 0x29, 0xb0, 0x5, 0xbb]
* [0x2500]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x2520]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x2500]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
## Module: SetTimerPeriodDxe
### Boot services:
* [0x331] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x4a0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTimerArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26baccb3, 0x6f42, 0x11d4, 0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
## Module: Setup
### Boot services:
* [0x1f33] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4d72] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5297] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5b96] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5d93] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x7b24] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x973f] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x9869] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xb154] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xd289] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xf2d2] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1541e] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x15963] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4f67] EFI_BOOT_SERVICES->OpenProtocol
* [0x535f] EFI_BOOT_SERVICES->OpenProtocol
* [0x53ca] EFI_BOOT_SERVICES->OpenProtocol
* [0x5546] EFI_BOOT_SERVICES->OpenProtocol
* [0x575a] EFI_BOOT_SERVICES->OpenProtocol
* [0x57e0] EFI_BOOT_SERVICES->OpenProtocol
* [0x5929] EFI_BOOT_SERVICES->OpenProtocol
* [0x59bf] EFI_BOOT_SERVICES->OpenProtocol
* [0x5b19] EFI_BOOT_SERVICES->OpenProtocol
* [0x6003] EFI_BOOT_SERVICES->OpenProtocol
* [0xf3c1] EFI_BOOT_SERVICES->OpenProtocol
* [0x154fe] EFI_BOOT_SERVICES->OpenProtocol
* [0x15534] EFI_BOOT_SERVICES->OpenProtocol
* [0x1559a] EFI_BOOT_SERVICES->OpenProtocol
* [0x15753] EFI_BOOT_SERVICES->OpenProtocol
* [0x157fd] EFI_BOOT_SERVICES->OpenProtocol
* [0x15a53] EFI_BOOT_SERVICES->OpenProtocol
* [0x15a9b] EFI_BOOT_SERVICES->OpenProtocol
* [0x15b80] EFI_BOOT_SERVICES->OpenProtocol
* [0x5bd8] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x5de6] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0xd12] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8845] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc30] EFI_BOOT_SERVICES->HandleProtocol
* [0xc5c] EFI_BOOT_SERVICES->HandleProtocol
* [0x1f84] EFI_BOOT_SERVICES->HandleProtocol
* [0x4db6] EFI_BOOT_SERVICES->HandleProtocol
* [0x52e1] EFI_BOOT_SERVICES->HandleProtocol
* [0x7bc4] EFI_BOOT_SERVICES->HandleProtocol
* [0x9781] EFI_BOOT_SERVICES->HandleProtocol
* [0x98b2] EFI_BOOT_SERVICES->HandleProtocol
* [0x9914] EFI_BOOT_SERVICES->HandleProtocol
* [0xb19a] EFI_BOOT_SERVICES->HandleProtocol
* [0xbfdb] EFI_BOOT_SERVICES->HandleProtocol
* [0xd30d] EFI_BOOT_SERVICES->HandleProtocol
* [0xd5a0] EFI_BOOT_SERVICES->HandleProtocol
* [0xf32f] EFI_BOOT_SERVICES->HandleProtocol
* [0xf46c] EFI_BOOT_SERVICES->HandleProtocol
* [0x1545e] EFI_BOOT_SERVICES->HandleProtocol
* [0x15680] EFI_BOOT_SERVICES->HandleProtocol
* [0x159a8] EFI_BOOT_SERVICES->HandleProtocol
* [0x35c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c2] EFI_BOOT_SERVICES->LocateProtocol
* [0x3df] EFI_BOOT_SERVICES->LocateProtocol
* [0x3fc] EFI_BOOT_SERVICES->LocateProtocol
* [0x419] EFI_BOOT_SERVICES->LocateProtocol
* [0xbe0] EFI_BOOT_SERVICES->LocateProtocol
* [0xc04] EFI_BOOT_SERVICES->LocateProtocol
* [0x1108] EFI_BOOT_SERVICES->LocateProtocol
* [0x4651] EFI_BOOT_SERVICES->LocateProtocol
* [0x49e3] EFI_BOOT_SERVICES->LocateProtocol
* [0x7f00] EFI_BOOT_SERVICES->LocateProtocol
* [0x8348] EFI_BOOT_SERVICES->LocateProtocol
* [0x8496] EFI_BOOT_SERVICES->LocateProtocol
* [0x8e20] EFI_BOOT_SERVICES->LocateProtocol
* [0x9fc3] EFI_BOOT_SERVICES->LocateProtocol
* [0xa195] EFI_BOOT_SERVICES->LocateProtocol
* [0xa1d5] EFI_BOOT_SERVICES->LocateProtocol
* [0xad1e] EFI_BOOT_SERVICES->LocateProtocol
* [0xaee6] EFI_BOOT_SERVICES->LocateProtocol
* [0xb70d] EFI_BOOT_SERVICES->LocateProtocol
* [0xba5a] EFI_BOOT_SERVICES->LocateProtocol
* [0xcd1e] EFI_BOOT_SERVICES->LocateProtocol
* [0xdf59] EFI_BOOT_SERVICES->LocateProtocol
* [0xe0e3] EFI_BOOT_SERVICES->LocateProtocol
* [0xe3d1] EFI_BOOT_SERVICES->LocateProtocol
* [0xe54b] EFI_BOOT_SERVICES->LocateProtocol
* [0xe572] EFI_BOOT_SERVICES->LocateProtocol
* [0xeb46] EFI_BOOT_SERVICES->LocateProtocol
* [0xeb6a] EFI_BOOT_SERVICES->LocateProtocol
* [0xee45] EFI_BOOT_SERVICES->LocateProtocol
* [0xeea8] EFI_BOOT_SERVICES->LocateProtocol
* [0xeef8] EFI_BOOT_SERVICES->LocateProtocol
* [0xefb7] EFI_BOOT_SERVICES->LocateProtocol
* [0x106ff] EFI_BOOT_SERVICES->LocateProtocol
* [0x11bca] EFI_BOOT_SERVICES->LocateProtocol
* [0x11e97] EFI_BOOT_SERVICES->LocateProtocol
* [0x12256] EFI_BOOT_SERVICES->LocateProtocol
* [0x123d3] EFI_BOOT_SERVICES->LocateProtocol
* [0x12520] EFI_BOOT_SERVICES->LocateProtocol
* [0x12562] EFI_BOOT_SERVICES->LocateProtocol
* [0x126aa] EFI_BOOT_SERVICES->LocateProtocol
* [0x126eb] EFI_BOOT_SERVICES->LocateProtocol
* [0x1415b] EFI_BOOT_SERVICES->LocateProtocol
* [0x14639] EFI_BOOT_SERVICES->LocateProtocol
* [0x14660] EFI_BOOT_SERVICES->LocateProtocol
* [0x146c8] EFI_BOOT_SERVICES->LocateProtocol
* [0x1477d] EFI_BOOT_SERVICES->LocateProtocol
* [0x148a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x1495d] EFI_BOOT_SERVICES->LocateProtocol
* [0x14a1b] EFI_BOOT_SERVICES->LocateProtocol
* [0x14ac5] EFI_BOOT_SERVICES->LocateProtocol
* [0x14bd1] EFI_BOOT_SERVICES->LocateProtocol
* [0x14cef] EFI_BOOT_SERVICES->LocateProtocol
* [0x14e40] EFI_BOOT_SERVICES->LocateProtocol
* [0x14f8b] EFI_BOOT_SERVICES->LocateProtocol
* [0x14fed] EFI_BOOT_SERVICES->LocateProtocol
* [0x15f11] EFI_BOOT_SERVICES->LocateProtocol
* [0x5c1a] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x5e22] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x13f34] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x18ec8]
	 - [service] LocateHandleBuffer
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x51e9b4f9, 0x555d, 0x476c, 0x8b, 0xb5, 0xbd, 0x18, 0xd9, 0xa6, 0x88, 0x78]
* [0x18040]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x18000]
	 - [service] LocateHandleBuffer
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x94c69847, 0xa0cf, 0x4635, 0xaa, 0x23, 0xd2, 0x66, 0x7b, 0xd7, 0xf7, 0x91]
* [0x18010]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x18020]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x17ec0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x17fd0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x17ff0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x18e38]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2362ea9c, 0x84e5, 0x4dff, 0x83, 0xbc, 0xb5, 0xac, 0xec, 0xb5, 0x7c, 0xbb]
* [0x17fc0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x17fb0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x17fe0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiEdidDiscoveredProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x1c0c34f6, 0xd380, 0x41fa, 0xa0, 0x49, 0x8a, 0xd0, 0x6c, 0x1a, 0x66, 0xaa]
* [0x18040]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x18200]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiGopDisplayBrightnessProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6ff23f1d, 0x877c, 0x4b1b, 0x93, 0xfc, 0xf1, 0x42, 0xb2, 0xee, 0xa6, 0xa7]
* [0x18210]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xf51dd33a, 0xe57f, 0x4020, 0xb4, 0x66, 0xf4, 0xc1, 0x71, 0xc6, 0xe4, 0xf7]
* [0x17e80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0x17eb0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbc62157e, 0x3e33, 0x4fec, 0x99, 0x20, 0x2d, 0x3b, 0x36, 0xd7, 0x50, 0xdf]
* [0x18ec8]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x51e9b4f9, 0x555d, 0x476c, 0x8b, 0xb5, 0xbd, 0x18, 0xd9, 0xa6, 0x88, 0x78]
* [0x18040]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x18000]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x94c69847, 0xa0cf, 0x4635, 0xaa, 0x23, 0xd2, 0x66, 0x7b, 0xd7, 0xf7, 0x91]
* [0x17ec0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x17f10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskInfoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd432a67f, 0x14dc, 0x484b, 0xb3, 0xbb, 0x3f, 0x2, 0x91, 0x84, 0x93, 0x27]
* [0x18010]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x18020]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x18060]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x17e90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x17ea0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x17ee0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x18070]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x18080]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
* [0x17fa0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd4d2f201, 0x50e8, 0x4d45, 0x8e, 0x5, 0xfd, 0x49, 0xa8, 0x2a, 0x15, 0x69]
* [0x18dd8]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x1c92f0ab, 0x3351, 0x1be5, 0xaf, 0xba, 0xc1, 0x25, 0x61, 0xbb, 0x32, 0xa3]
* [0x17f20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3583ff6, 0xcb36, 0x4940, 0x94, 0x7e, 0xb9, 0xb3, 0x9f, 0x4a, 0xfa, 0xf7]
* [0x17f50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd9035175, 0x8ce2, 0x47de, 0xa8, 0xb8, 0xcc, 0x98, 0xe5, 0xe2, 0xa8, 0x85]
* [0x180a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3c7bc880, 0x41f8, 0x4869, 0xae, 0xfc, 0x87, 0xa, 0x3e, 0xd2, 0x82, 0x99]
* [0x17f60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x984eb4e9, 0x5a95, 0x41de, 0xaa, 0xd0, 0x53, 0x66, 0x8c, 0xa5, 0x13, 0xc0]
* [0x18030]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5f87ba17, 0x957d, 0x433d, 0x9e, 0x15, 0xc0, 0xe7, 0xc8, 0x79, 0x88, 0x99]
* [0x18330]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x17ef0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0x17f70]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x92c7d0bb, 0x679e, 0x479d, 0x87, 0x8d, 0xd4, 0xb8, 0x29, 0x68, 0x57, 0x8b]
* [0x17d60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd84beff0, 0x159a, 0x4b60, 0x9a, 0xb9, 0xac, 0x5c, 0x47, 0x4b, 0xd3, 0xb1]
* [0x180b0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb42b8d12, 0x2acb, 0x499a, 0xa9, 0x20, 0xdd, 0x5b, 0xe6, 0xcf, 0x9, 0xb1]
* [0x17f90]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x919383de, 0xebac, 0x4924, 0x1, 0x94, 0x52, 0x59, 0xe0, 0xd, 0x65, 0x7a]
* [0x18050]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
* [0x18310]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x18340]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb9d4c360, 0xbcfb, 0x4f9b, 0x92, 0x98, 0x53, 0xc1, 0x36, 0x98, 0x22, 0x58]
* [0x18090]
	 - [service] LocateProtocol
	 - [protocol_name] gPlatformSeCHookProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbc52476e, 0xf67e, 0x4301, 0xb2, 0x62, 0x36, 0x9c, 0x48, 0x78, 0xaa, 0xc2]
* [0x180c0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8d9b3387, 0x73db, 0x456f, 0x88, 0x9d, 0x6f, 0xfe, 0x90, 0x82, 0x64, 0x9]
* [0x180d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiFormBrowser2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xb9d4c360, 0xbcfb, 0x4f9b, 0x92, 0x98, 0x53, 0xc1, 0x36, 0x98, 0x22, 0x58]
* [0x17d60]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd84beff0, 0x159a, 0x4b60, 0x9a, 0xb9, 0xac, 0x5c, 0x47, 0x4b, 0xd3, 0xb1]
## Module: SgTpvAcpiS3Save
### Boot services:
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
* [0x560] EFI_BOOT_SERVICES->LocateProtocol
* [0x584] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2c20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2c00]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3dc21d75, 0xde0e, 0x4300, 0xa0, 0xaa, 0x19, 0xc4, 0x1c, 0xc, 0xf3, 0xdf]
* [0x2c10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
## Module: SgTpvAcpiTables
### Boot services:
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
* [0x3e3] EFI_BOOT_SERVICES->LocateProtocol
* [0xbec] EFI_BOOT_SERVICES->LocateProtocol
* [0xf78] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3630]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x35f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3dc21d75, 0xde0e, 0x4300, 0xa0, 0xaa, 0x19, 0xc4, 0x1c, 0xc, 0xf3, 0xdf]
* [0x3620]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdbff9d55, 0x89b7, 0x46da, 0xbd, 0xdf, 0x67, 0x7d, 0x3d, 0xc0, 0x24, 0x1d]
## Module: SgTpvDxe
### Boot services:
* [0x2f0] EFI_BOOT_SERVICES->LocateProtocol
* [0x397] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x1070]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1060]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6aa1f27, 0x5597, 0x4802, 0x9f, 0x63, 0xd6, 0x28, 0x36, 0x59, 0x86, 0x35]
## Module: Shell_Full
### Boot services:
* [0x65662] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x66ffe] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x67687] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x67863] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x80bb8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x87fd0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8a299] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8a9e0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x8af45] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa1d4b] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xad6ef] EFI_BOOT_SERVICES->LocateHandleBuffer
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
* [0x896d9] EFI_BOOT_SERVICES->OpenProtocol
* [0x8970d] EFI_BOOT_SERVICES->OpenProtocol
* [0x8b30a] EFI_BOOT_SERVICES->OpenProtocol
* [0x96eaf] EFI_BOOT_SERVICES->OpenProtocol
* [0x99cd4] EFI_BOOT_SERVICES->OpenProtocol
* [0x99d04] EFI_BOOT_SERVICES->OpenProtocol
* [0x9af72] EFI_BOOT_SERVICES->OpenProtocol
* [0x9afaa] EFI_BOOT_SERVICES->OpenProtocol
* [0x9b069] EFI_BOOT_SERVICES->OpenProtocol
* [0x9b1b9] EFI_BOOT_SERVICES->OpenProtocol
* [0xa4740] EFI_BOOT_SERVICES->OpenProtocol
* [0xa479c] EFI_BOOT_SERVICES->OpenProtocol
* [0x65785] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x65d7b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x65de5] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x66d2d] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x66d96] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6cd30] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6cd4f] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6cd6b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x6d38b] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x66cf6] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x67cbd] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x6ebc1] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x67084] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x67dcb] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x7ab7c] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x96c43] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x65819] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x6833d] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x6835b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x659eb] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x93ce1] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
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
* [0x9bf06] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0xa09f2] EFI_BOOT_SERVICES->ReinstallProtocolInterface
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
* [0x84f3a] EFI_BOOT_SERVICES->HandleProtocol
* [0x86510] EFI_BOOT_SERVICES->HandleProtocol
* [0x87f9c] EFI_BOOT_SERVICES->HandleProtocol
* [0x88008] EFI_BOOT_SERVICES->HandleProtocol
* [0x8804b] EFI_BOOT_SERVICES->HandleProtocol
* [0x8a376] EFI_BOOT_SERVICES->HandleProtocol
* [0x8a575] EFI_BOOT_SERVICES->HandleProtocol
* [0x8a7dd] EFI_BOOT_SERVICES->HandleProtocol
* [0x8a8d8] EFI_BOOT_SERVICES->HandleProtocol
* [0x8afa1] EFI_BOOT_SERVICES->HandleProtocol
* [0x8afd2] EFI_BOOT_SERVICES->HandleProtocol
* [0x96d01] EFI_BOOT_SERVICES->HandleProtocol
* [0x96e46] EFI_BOOT_SERVICES->HandleProtocol
* [0x9beeb] EFI_BOOT_SERVICES->HandleProtocol
* [0xa0df8] EFI_BOOT_SERVICES->HandleProtocol
* [0xa1d0a] EFI_BOOT_SERVICES->HandleProtocol
* [0xa1d88] EFI_BOOT_SERVICES->HandleProtocol
* [0xad6ae] EFI_BOOT_SERVICES->HandleProtocol
* [0xad72c] EFI_BOOT_SERVICES->HandleProtocol
* [0x685b8] EFI_BOOT_SERVICES->LocateProtocol
* [0x80b2f] EFI_BOOT_SERVICES->LocateProtocol
* [0x84190] EFI_BOOT_SERVICES->LocateProtocol
* [0x8a0da] EFI_BOOT_SERVICES->LocateProtocol
* [0x8a9aa] EFI_BOOT_SERVICES->LocateProtocol
* [0x902ef] EFI_BOOT_SERVICES->LocateProtocol
* [0x93c20] EFI_BOOT_SERVICES->LocateProtocol
* [0xa113a] EFI_BOOT_SERVICES->LocateProtocol
* [0xa14c6] EFI_BOOT_SERVICES->LocateProtocol
* [0xa1796] EFI_BOOT_SERVICES->LocateProtocol
* [0xa1b1b] EFI_BOOT_SERVICES->LocateProtocol
* [0xaaf3a] EFI_BOOT_SERVICES->LocateProtocol
* [0xab790] EFI_BOOT_SERVICES->LocateProtocol
* [0xac2ed] EFI_BOOT_SERVICES->LocateProtocol
* [0xb1ea8] EFI_BOOT_SERVICES->LocateProtocol
* [0xb22e3] EFI_BOOT_SERVICES->LocateProtocol
* [0xb2bb6] EFI_BOOT_SERVICES->LocateProtocol
* [0x672e0] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x690b0] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x8a2fc] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x812f9] EFI_BOOT_SERVICES->CloseProtocol
* [0x8e5ba] EFI_BOOT_SERVICES->CloseProtocol
* [0x9b113] EFI_BOOT_SERVICES->CloseProtocol
* [0x65cad] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x54e64]
	 - [service] LocateHandleBuffer
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xa, 0x73, 0x74, 0x61, 0x0, 0x72, 0x0, 0x74, 0x0, 0x75, 0x0]
* [0x400]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0x3e0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiHiiConfigAccessProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x330d4706, 0xf2a0, 0x4e4f, 0xa3, 0x69, 0xb6, 0x6f, 0xa8, 0xd5, 0x43, 0x85]
* [0x3a0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiIp4ConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3b95aa31, 0x3793, 0x434b, 0x86, 0x67, 0xc8, 0x7, 0x8, 0x92, 0xe0, 0x5e]
* [0x350]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31878c87, 0xb75, 0x11d5, 0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x555b0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x0, 0x0, 0x0, 0x25, 0x0, 0x2a, 0x0, 0x61, 0x0, 0x25, 0x0]
* [0x560]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x5a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x540]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDriverConfigurationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772b, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x4e0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDriverConfiguration2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbfd7dc1d, 0x24f1, 0x40d9, 0x82, 0xe7, 0x2e, 0x9, 0xbb, 0x6b, 0x4e, 0xbe]
* [0x520]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDriverDiagnosticsProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x784924f, 0xe296, 0x11d4, 0x9a, 0x49, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x510]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDriverDiagnostics2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4d330321, 0x25f, 0x4aac, 0x90, 0xd8, 0x5e, 0xd9, 0x0, 0x17, 0x3b, 0x63]
* [0x580]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x420]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc51711e7, 0xb4bf, 0x404a, 0xbf, 0xb8, 0xa, 0x4, 0x8e, 0xf1, 0xff, 0xe4]
* [0x430]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x41d94cd2, 0x35b6, 0x455a, 0x82, 0x58, 0xd4, 0xe5, 0x13, 0x34, 0xaa, 0xdd]
* [0x572f0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x4e0025, 0xa, 0x0, 0x77, 0x0, 0x72, 0x0, 0x69, 0x0, 0x74, 0x0]
* [0x54d50]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiShellEnvironment2Guid
	 - [protocol_place] edk2_guids
	 - [guid] [0x47c7b221, 0xc42a, 0x11d2, 0x8e, 0x57, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x470]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x460]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c1, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x580]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x98f0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiShellInterfaceGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x47c7b223, 0xc42a, 0x11d2, 0x8e, 0x57, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb8120]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0x8dd0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6d5c0, 0x0, 0x0, 0x24, 0x3b, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0x54d50]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiShellEnvironment2Guid
	 - [protocol_place] edk2_guids
	 - [guid] [0x47c7b221, 0xc42a, 0x11d2, 0x8e, 0x57, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x98f0]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiShellInterfaceGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x47c7b223, 0xc42a, 0x11d2, 0x8e, 0x57, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x8dd0]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6d5c0, 0x0, 0x0, 0x24, 0x3b, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0x460]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c1, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x470]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x530]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb8148]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0x5a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x580]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x54e64]
	 - [service] HandleProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xa, 0x73, 0x74, 0x61, 0x0, 0x72, 0x0, 0x74, 0x0, 0x75, 0x0]
* [0x98f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiShellInterfaceGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x47c7b223, 0xc42a, 0x11d2, 0x8e, 0x57, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x54d50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiShellEnvironment2Guid
	 - [protocol_place] edk2_guids
	 - [guid] [0x47c7b221, 0xc42a, 0x11d2, 0x8e, 0x57, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x590]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPeiIdeBlockIoPpiGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b22, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x5b0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolumeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x389f751f, 0x1838, 0x4388, 0x83, 0x90, 0xcd, 0x81, 0x54, 0xbd, 0x27, 0xf8]
* [0x5c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x530]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x600]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDebugMaskProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4c8a2451, 0xc207, 0x405b, 0x96, 0x94, 0x99, 0xea, 0x13, 0x25, 0x13, 0x41]
* [0x3f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSerialIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbb25cf6f, 0xf1d4, 0x11d2, 0x9a, 0xc, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0xfd]
* [0x410]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0x5e0]
	 - [service] HandleProtocol
	 - [protocol_name] EFI_NIC_IP4_CONFIG_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] [0xdca3d4d, 0x12da, 0x4728, 0xbf, 0x7e, 0x86, 0xce, 0xb9, 0x28, 0xd0, 0x67]
* [0x3a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp4ConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3b95aa31, 0x3793, 0x434b, 0x86, 0x67, 0xc8, 0x7, 0x8, 0x92, 0xe0, 0x5e]
* [0x380]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x350]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31878c87, 0xb75, 0x11d5, 0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x340]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiCpuArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x26baccb1, 0x6f42, 0x11d4, 0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
* [0x3b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x390]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDecompressProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd8117cfe, 0x94a6, 0x11d4, 0x9a, 0x3a, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x380]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x400]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0x430]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x41d94cd2, 0x35b6, 0x455a, 0x82, 0x58, 0xd4, 0xe5, 0x13, 0x34, 0xaa, 0xdd]
## Module: SiInitDxe
### Boot services:
* [0x115d] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1240] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1199] EFI_BOOT_SERVICES->HandleProtocol
* [0x127c] EFI_BOOT_SERVICES->HandleProtocol
* [0x1353] EFI_BOOT_SERVICES->HandleProtocol
* [0x332] EFI_BOOT_SERVICES->LocateProtocol
* [0x369] EFI_BOOT_SERVICES->LocateProtocol
* [0x42c] EFI_BOOT_SERVICES->LocateProtocol
* [0x5d4] EFI_BOOT_SERVICES->LocateProtocol
* [0x5fa] EFI_BOOT_SERVICES->LocateProtocol
* [0x164b] EFI_BOOT_SERVICES->LocateProtocol
* [0x17e5] EFI_BOOT_SERVICES->LocateProtocol
* [0x29e4] EFI_BOOT_SERVICES->LocateProtocol
* [0x3c0] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2d30]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiDriverSupportedEfiVersionProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5c198761, 0x16a8, 0x4e69, 0x97, 0x2c, 0x89, 0xd6, 0x79, 0x54, 0xf8, 0x1d]
* [0x2d40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x2d00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x2d30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverSupportedEfiVersionProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5c198761, 0x16a8, 0x4e69, 0x97, 0x2c, 0x89, 0xd6, 0x79, 0x54, 0xf8, 0x1d]
* [0x2d10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0x2ce0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3583ff6, 0xcb36, 0x4940, 0x94, 0x7e, 0xb9, 0xb3, 0x9f, 0x4a, 0xfa, 0xf7]
* [0x2d20]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6aa1f27, 0x5597, 0x4802, 0x9f, 0x63, 0xd6, 0x28, 0x36, 0x59, 0x86, 0x35]
* [0x2d60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0x2d50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x1ab1829, 0xcecd, 0x4cfa, 0xa1, 0x8c, 0xea, 0x75, 0xd6, 0x6f, 0x3e, 0x74]
* [0x2ce0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3583ff6, 0xcb36, 0x4940, 0x94, 0x7e, 0xb9, 0xb3, 0x9f, 0x4a, 0xfa, 0xf7]
## Module: SioDxeInit
### Boot services:
* [0x304] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3ad] EFI_BOOT_SERVICES->LocateProtocol
* [0x47d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xa00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
## Module: SleepSmi
### Boot services:
* [0x36c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a1] EFI_BOOT_SERVICES->LocateProtocol
* [0x474] EFI_BOOT_SERVICES->LocateProtocol
* [0x53f] EFI_BOOT_SERVICES->LocateProtocol
* [0x7e2] EFI_BOOT_SERVICES->LocateProtocol
* [0xb11] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3380]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x33b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x3908]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x33a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: Smbios
### Boot services:
* [0xd60] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x3fec] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x431e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4344] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xa43] EFI_BOOT_SERVICES->HandleProtocol
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ef9] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x47b0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x47c0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3583ff6, 0xcb36, 0x4940, 0x94, 0x7e, 0xb9, 0xb3, 0x9f, 0x4a, 0xfa, 0xf7]
* [0x47e0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5e90a50d, 0x6955, 0x4a49, 0x90, 0x32, 0xda, 0x38, 0x12, 0xf8, 0xe8, 0xe5]
* [0x5500]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x47f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x47d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x903dd14, 0x2ca0, 0x458a, 0xb5, 0xeb, 0xc, 0xc, 0xa3, 0xd, 0x78, 0x5c]
## Module: SmbiosBoard
### Boot services:
* [0x35e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2e5] EFI_BOOT_SERVICES->LocateProtocol
* [0x3fd] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x620]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x903dd14, 0x2ca0, 0x458a, 0xb5, 0xeb, 0xc, 0xc, 0xa3, 0xd, 0x78, 0x5c]
* [0x630]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
## Module: SmbiosDmiEdit
### Boot services:
* [0x36f] EFI_BOOT_SERVICES->LocateProtocol
* [0x3a3] EFI_BOOT_SERVICES->LocateProtocol
* [0x473] EFI_BOOT_SERVICES->LocateProtocol
* [0x55b] EFI_BOOT_SERVICES->LocateProtocol
* [0x626] EFI_BOOT_SERVICES->LocateProtocol
* [0x65e] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ef5] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x33f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x3450]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x39e8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x3400]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xddfb5557, 0x3e2e, 0x4569, 0xb4, 0x59, 0xbe, 0xff, 0xe1, 0x89, 0xb8, 0xb0]
* [0x3440]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: SmbiosGetFlashData
### Boot services:
* [0x3f0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x317] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x42e] EFI_BOOT_SERVICES->HandleProtocol
### Protocols:
* empty
## Module: SmbiosMisc
### Boot services:
* [0x2ca] EFI_BOOT_SERVICES->LocateProtocol
* [0x33c] EFI_BOOT_SERVICES->LocateProtocol
* [0x35a] EFI_BOOT_SERVICES->LocateProtocol
* [0x377] EFI_BOOT_SERVICES->LocateProtocol
* [0x394] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b1] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x780]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3583ff6, 0xcb36, 0x4940, 0x94, 0x7e, 0xb9, 0xb3, 0x9f, 0x4a, 0xfa, 0xf7]
* [0x7b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x790]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x7d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x7a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x7c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
## Module: SmbiosUpdateData
### Boot services:
* [0x32d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x309] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x690]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x67269263, 0xaf1, 0x45dd, 0x93, 0xc8, 0x29, 0x99, 0x21, 0xd0, 0xe1, 0xe9]
* [0x680]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5e90a50d, 0x6955, 0x4a49, 0x90, 0x32, 0xda, 0x38, 0x12, 0xf8, 0xe8, 0xe5]
## Module: SmiFlash
### Boot services:
* [0xd37] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xd74] EFI_BOOT_SERVICES->HandleProtocol
* [0x35b] EFI_BOOT_SERVICES->LocateProtocol
* [0x397] EFI_BOOT_SERVICES->LocateProtocol
* [0x1034] EFI_BOOT_SERVICES->LocateProtocol
* [0x10c8] EFI_BOOT_SERVICES->LocateProtocol
* [0x1157] EFI_BOOT_SERVICES->LocateProtocol
* [0x11f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x134b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e45] EFI_BOOT_SERVICES->LocateProtocol
* [0x1250] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x4a60]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x4a60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x4a30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x5648]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x4a70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x4a50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xecb867ab, 0x8df4, 0x492d, 0x81, 0x50, 0xa7, 0xfd, 0x1b, 0x9b, 0x5a, 0x75]
* [0x4ab0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: SmiFlashDxe
### Boot services:
* empty
### Protocols:
* empty
## Module: SmiVariable
### Boot services:
* [0x2c2] EFI_BOOT_SERVICES->LocateProtocol
* [0x883] EFI_BOOT_SERVICES->LocateProtocol
* [0xaa5] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xda0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x12b8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xdc0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: SmmAccess
### Boot services:
* [0x4d5] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x33d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x900]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
## Module: SmmControl
### Boot services:
* [0x116b] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: SmmGenericSio
### Boot services:
* [0x36f] EFI_BOOT_SERVICES->LocateProtocol
* [0x39d] EFI_BOOT_SERVICES->LocateProtocol
* [0x110b] EFI_BOOT_SERVICES->LocateProtocol
* [0x119f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1399] EFI_BOOT_SERVICES->LocateProtocol
* [0x150d] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1b70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1b90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x2178]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1b50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x7576cc89, 0x8fa3, 0x4cad, 0xba, 0x2, 0x61, 0x19, 0xb4, 0x6e, 0xd4, 0x4a]
* [0x1ba0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: SmmLockBox
### Boot services:
* [0x463] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x330] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xd00]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiLockBoxProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbd445d79, 0xb7ad, 0x4f04, 0x9a, 0xd8, 0x29, 0xbd, 0x20, 0x40, 0xeb, 0x3c]
* [0xd10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
## Module: SmmPcieSataController
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x4eb] EFI_BOOT_SERVICES->LocateProtocol
* [0x57d] EFI_BOOT_SERVICES->LocateProtocol
* [0x6c9] EFI_BOOT_SERVICES->LocateProtocol
* [0x7a6] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xb80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1098]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xba0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: SmmPciRbIo
### Boot services:
* [0x361] EFI_BOOT_SERVICES->LocateProtocol
* [0x395] EFI_BOOT_SERVICES->LocateProtocol
* [0x1155] EFI_BOOT_SERVICES->LocateProtocol
* [0x11e6] EFI_BOOT_SERVICES->LocateProtocol
* [0x1260] EFI_BOOT_SERVICES->LocateProtocol
* [0x13ed] EFI_BOOT_SERVICES->LocateProtocol
* [0x12b2] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x1c60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1c90]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x2198]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1c50]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x6fce3bb9, 0x9742, 0x4cfd, 0x8e, 0x9e, 0x39, 0xf9, 0x8d, 0xca, 0x32, 0x71]
* [0x1c80]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
* [0x1c40]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiSmmPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8bc1714d, 0xffcb, 0x41c3, 0x89, 0xdc, 0x6c, 0x74, 0xd0, 0x6d, 0x98, 0xea]
## Module: SmmPlatform
### Boot services:
* [0x149f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x14e7] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x34c] EFI_BOOT_SERVICES->LocateProtocol
* [0x37a] EFI_BOOT_SERVICES->LocateProtocol
* [0x17a0] EFI_BOOT_SERVICES->LocateProtocol
* [0x17d0] EFI_BOOT_SERVICES->LocateProtocol
* [0x1800] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b2f] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x3278]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
* [0x2c50]
	 - [service] ReinstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x70eeecbe, 0x727a, 0x4244, 0x90, 0x4c, 0xdb, 0x6b, 0xf0, 0x5, 0x53, 0x92]
* [0x2ca0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2d10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x2c80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGlobalNvsAreaProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x74e1e48, 0x8132, 0x47a1, 0x8c, 0x2c, 0x3f, 0x14, 0xad, 0x9a, 0x66, 0xdc]
* [0x2c70]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xab5a4df4, 0xf0d7, 0x49a8, 0xbf, 0x5c, 0xf2, 0x5d, 0xa0, 0x4c, 0x25, 0x33]
* [0x2c60]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x3dc21d75, 0xde0e, 0x4300, 0xa0, 0xaa, 0x19, 0xc4, 0x1c, 0xc, 0xf3, 0xdf]
* [0x2d00]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
## Module: SmmS3SaveState
### Boot services:
* [0x54e] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x57f] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x218c] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x22af] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x39c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3ca] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f8d] EFI_BOOT_SERVICES->LocateProtocol
* [0x2218] EFI_BOOT_SERVICES->LocateProtocol
* [0x29c7] EFI_BOOT_SERVICES->LocateProtocol
* [0x2fe] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x21db] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2bc0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSmmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x47b7fa8c, 0xf4bd, 0x4af6, 0x82, 0x0, 0x33, 0x30, 0x86, 0xf0, 0xd2, 0xc8]
* [0x2b80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x2ba0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x2bb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDxeMmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x60ff8964, 0xe906, 0x41d0, 0xaf, 0xed, 0xf2, 0x41, 0xe9, 0x74, 0xe0, 0x8e]
* [0x2b90]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
* [0x2bb0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiDxeMmReadyToLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x60ff8964, 0xe906, 0x41d0, 0xaf, 0xed, 0xf2, 0x41, 0xe9, 0x74, 0xe0, 0x8e]
## Module: SmramSaveInfoHandlerSmm
### Boot services:
* [0x303] EFI_BOOT_SERVICES->LocateProtocol
* [0x331] EFI_BOOT_SERVICES->LocateProtocol
* [0x447] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x790]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x7a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
* [0x780]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xe223cf65, 0xf6ce, 0x4122, 0xb3, 0xaf, 0x4b, 0xd1, 0x8a, 0xff, 0x40, 0xa1]
## Module: SnpDxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x1dbe] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6b1] EFI_BOOT_SERVICES->OpenProtocol
* [0x6e9] EFI_BOOT_SERVICES->OpenProtocol
* [0x809] EFI_BOOT_SERVICES->OpenProtocol
* [0x873] EFI_BOOT_SERVICES->OpenProtocol
* [0x8aa] EFI_BOOT_SERVICES->OpenProtocol
* [0x1021] EFI_BOOT_SERVICES->OpenProtocol
* [0x25fa] EFI_BOOT_SERVICES->OpenProtocol
* [0x265a] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1059] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xb6e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xf0f] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x548] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x46c] EFI_BOOT_SERVICES->HandleProtocol
* [0x1df6] EFI_BOOT_SERVICES->HandleProtocol
* [0x75e] EFI_BOOT_SERVICES->CloseProtocol
* [0x8d5] EFI_BOOT_SERVICES->CloseProtocol
* [0xf89] EFI_BOOT_SERVICES->CloseProtocol
* [0xfad] EFI_BOOT_SERVICES->CloseProtocol
* [0x10b3] EFI_BOOT_SERVICES->CloseProtocol
* [0x10d1] EFI_BOOT_SERVICES->CloseProtocol
* [0x261c] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x4e90]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x4ea0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4eb0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiNetworkInterfaceIdentifierProtocolGuid_31
	 - [protocol_place] edk2_guids
	 - [guid] [0x1aced566, 0x76ed, 0x4218, 0xbc, 0x81, 0x76, 0x7f, 0x1f, 0x97, 0x7a, 0x89]
* [0x4e80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x4e90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x4ec0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x4ed0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x4ee0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x4e90]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x4ec0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x4ed0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x4ee0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x4ef0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4e90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x4eb0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiNetworkInterfaceIdentifierProtocolGuid_31
	 - [protocol_place] edk2_guids
	 - [guid] [0x1aced566, 0x76ed, 0x4218, 0xbc, 0x81, 0x76, 0x7f, 0x1f, 0x97, 0x7a, 0x89]
* [0x4ea0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x4e90]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
## Module: SoftKbd
### Boot services:
* [0x1341] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x13b1] EFI_BOOT_SERVICES->OpenProtocol
* [0x12ae] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x5878] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x5724] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x137c] EFI_BOOT_SERVICES->HandleProtocol
* [0x1606] EFI_BOOT_SERVICES->HandleProtocol
* [0x162f] EFI_BOOT_SERVICES->HandleProtocol
* [0x1422] EFI_BOOT_SERVICES->LocateProtocol
* [0x1480] EFI_BOOT_SERVICES->LocateProtocol
* [0x14b4] EFI_BOOT_SERVICES->LocateProtocol
* [0x168f] EFI_BOOT_SERVICES->LocateProtocol
* [0x16ba] EFI_BOOT_SERVICES->LocateProtocol
* [0x16e5] EFI_BOOT_SERVICES->LocateProtocol
* [0x1b6b] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d36] EFI_BOOT_SERVICES->LocateProtocol
* [0x34a8] EFI_BOOT_SERVICES->LocateProtocol
* [0x52c6] EFI_BOOT_SERVICES->LocateProtocol
* [0x62e0] EFI_BOOT_SERVICES->LocateProtocol
* [0x63b6] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x7010]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x7030]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x16460]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x96fd60f3, 0xbc8, 0x4a11, 0x84, 0xf1, 0x2e, 0xb1, 0xcb, 0x5b, 0xa5, 0xa3]
* [0x7010]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleTextOutProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c2, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x7030]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x7050]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0x7030]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0x16470]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc7a7030c, 0xc3d8, 0x45ee, 0xbe, 0xd9, 0x5d, 0x9e, 0x76, 0x76, 0x29, 0x53]
* [0x7040]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x16480]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x9dd0a4dc, 0xefa3, 0x4caf, 0xa0, 0x1e, 0x28, 0x95, 0xb, 0x1, 0x17, 0x74]
* [0x16490]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x890df583, 0xd14, 0x4c82, 0x99, 0x6d, 0xe5, 0xea, 0xe8, 0xca, 0x90, 0x5e]
* [0x7060]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb295bd1c, 0x63e3, 0x48e3, 0xb2, 0x65, 0xf7, 0xdf, 0xa2, 0x7, 0x1, 0x23]
## Module: StatusCodeDxe
### Boot services:
* [0x1bfc] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1c81] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1e3e] EFI_BOOT_SERVICES->LocateProtocol
* [0x2438] EFI_BOOT_SERVICES->LocateProtocol
* [0x24f9] EFI_BOOT_SERVICES->LocateProtocol
* [0x256e] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x4060]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
* [0x4050]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDataHubProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xae80d021, 0x618e, 0x11d4, 0xbc, 0xd7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
* [0x4618]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x4060]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
* [0x4050]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiDataHubProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xae80d021, 0x618e, 0x11d4, 0xbc, 0xd7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81]
## Module: StatusCodeSmm
### Boot services:
* [0x2dd] EFI_BOOT_SERVICES->LocateProtocol
* [0x7a7] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x7d1] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x7f4] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x2540]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
## Module: Tcg2Dxe
### Boot services:
* [0x6979] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x6e1f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x5ccb] EFI_BOOT_SERVICES->HandleProtocol
* [0x383] EFI_BOOT_SERVICES->LocateProtocol
* [0x773] EFI_BOOT_SERVICES->LocateProtocol
* [0x88e] EFI_BOOT_SERVICES->LocateProtocol
* [0xf6b] EFI_BOOT_SERVICES->LocateProtocol
* [0x107f] EFI_BOOT_SERVICES->LocateProtocol
* [0x2195] EFI_BOOT_SERVICES->LocateProtocol
* [0x3107] EFI_BOOT_SERVICES->LocateProtocol
* [0x392e] EFI_BOOT_SERVICES->LocateProtocol
* [0x395d] EFI_BOOT_SERVICES->LocateProtocol
* [0x4b6c] EFI_BOOT_SERVICES->LocateProtocol
* [0x4b9b] EFI_BOOT_SERVICES->LocateProtocol
* [0x5a19] EFI_BOOT_SERVICES->LocateProtocol
* [0x5c3b] EFI_BOOT_SERVICES->LocateProtocol
* [0x64c6] EFI_BOOT_SERVICES->LocateProtocol
* [0x6506] EFI_BOOT_SERVICES->LocateProtocol
* [0x6a86] EFI_BOOT_SERVICES->LocateProtocol
* [0xcd68] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ee2] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x6d56] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xde00]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xde70]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xeb97088e, 0xcfdf, 0x49c6, 0xbe, 0x4b, 0xd9, 0x6, 0xa5, 0xb2, 0xe, 0x86]
* [0xde60]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiAcpiSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdbff9d55, 0x89b7, 0x46da, 0xbd, 0xdf, 0x67, 0x7d, 0x3d, 0xc0, 0x24, 0x1d]
* [0xddf0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiResetArchProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x27cfac88, 0x46cc, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
## Module: TcgDxe
### Boot services:
* [0x1863] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1889] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1c2e] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1ec6] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2e02] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x2e62] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1085] EFI_BOOT_SERVICES->HandleProtocol
* [0x10a8] EFI_BOOT_SERVICES->HandleProtocol
* [0x3e1] EFI_BOOT_SERVICES->LocateProtocol
* [0xd23] EFI_BOOT_SERVICES->LocateProtocol
* [0xd47] EFI_BOOT_SERVICES->LocateProtocol
* [0xe92] EFI_BOOT_SERVICES->LocateProtocol
* [0x10cb] EFI_BOOT_SERVICES->LocateProtocol
* [0x10ef] EFI_BOOT_SERVICES->LocateProtocol
* [0x1500] EFI_BOOT_SERVICES->LocateProtocol
* [0x169a] EFI_BOOT_SERVICES->LocateProtocol
* [0x17a8] EFI_BOOT_SERVICES->LocateProtocol
* [0x1e64] EFI_BOOT_SERVICES->LocateProtocol
* [0x2aee] EFI_BOOT_SERVICES->LocateProtocol
* [0x2ce5] EFI_BOOT_SERVICES->LocateProtocol
* [0x2d02] EFI_BOOT_SERVICES->LocateProtocol
* [0x2b41] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x55a0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] EFI_TCG_PLATFORM_PROTOCOL_GUID
	 - [protocol_place] edk_guids
	 - [guid] [0x8c4c9a41, 0xbf56, 0x4627, 0x9e, 0xa, 0xc8, 0x38, 0x6d, 0x66, 0x11, 0x5c]
* [0x5560]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x320bdc39, 0x3fa0, 0x4ba9, 0xbf, 0x2d, 0xb3, 0x3f, 0x72, 0xba, 0x9c, 0xa1]
* [0x5570]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x5590]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xce345171, 0xba0b, 0x11d2, 0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x5550]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf541796d, 0xa62e, 0x4954, 0xa7, 0x75, 0x95, 0x84, 0xf6, 0x1b, 0x9c, 0xdd]
* [0x5540]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTpmMpDriverProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xde161cfe, 0x1e60, 0x42a1, 0x8c, 0xc3, 0xee, 0x7e, 0xf0, 0x73, 0x52, 0x12]
* [0x5580]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdbff9d55, 0x89b7, 0x46da, 0xbd, 0xdf, 0x67, 0x7d, 0x3d, 0xc0, 0x24, 0x1d]
* [0x5580]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiAcpiSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdbff9d55, 0x89b7, 0x46da, 0xbd, 0xdf, 0x67, 0x7d, 0x3d, 0xc0, 0x24, 0x1d]
## Module: TcgDxeplatform
### Boot services:
* [0x392] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x5c0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8c939604, 0x700, 0x4415, 0x9d, 0x62, 0x11, 0x61, 0xdb, 0x81, 0x64, 0xa6]
## Module: TcgLegacy
### Boot services:
* [0x520] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x680] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x560] EFI_BOOT_SERVICES->HandleProtocol
* [0x6c0] EFI_BOOT_SERVICES->HandleProtocol
* [0x981] EFI_BOOT_SERVICES->LocateProtocol
* [0x9a9] EFI_BOOT_SERVICES->LocateProtocol
* [0x9d4] EFI_BOOT_SERVICES->LocateProtocol
* [0xc03] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xf20]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0xf20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0xf50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTcgProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf541796d, 0xa62e, 0x4954, 0xa7, 0x75, 0x95, 0x84, 0xf6, 0x1b, 0x9c, 0xdd]
* [0xf10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
* [0xf30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyRegion2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x70101eaf, 0x85, 0x440c, 0xb3, 0x56, 0x8e, 0xe3, 0x6f, 0xef, 0x24, 0xf0]
## Module: TcgPlatformSetupPolicy
### Boot services:
* [0xc7f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x6d0] EFI_BOOT_SERVICES->LocateProtocol
* [0xcda] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xdf0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xdbc9fd21, 0xfad8, 0x45b0, 0x9e, 0x78, 0x27, 0x15, 0x88, 0x67, 0xcc, 0x93]
## Module: TcgSmm
### Boot services:
* [0x32c] EFI_BOOT_SERVICES->LocateProtocol
* [0x35a] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1270]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x12a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
## Module: TcoSmi
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x401] EFI_BOOT_SERVICES->LocateProtocol
* [0x56b] EFI_BOOT_SERVICES->LocateProtocol
* [0x711] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xab0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xfb8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xad0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: TcpDxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x6d9] EFI_BOOT_SERVICES->OpenProtocol
* [0x718] EFI_BOOT_SERVICES->OpenProtocol
* [0xa53] EFI_BOOT_SERVICES->OpenProtocol
* [0xba1] EFI_BOOT_SERVICES->OpenProtocol
* [0xbdd] EFI_BOOT_SERVICES->OpenProtocol
* [0xc81] EFI_BOOT_SERVICES->OpenProtocol
* [0xcbd] EFI_BOOT_SERVICES->OpenProtocol
* [0xd8d] EFI_BOOT_SERVICES->OpenProtocol
* [0xdc3] EFI_BOOT_SERVICES->OpenProtocol
* [0x1014] EFI_BOOT_SERVICES->OpenProtocol
* [0x104c] EFI_BOOT_SERVICES->OpenProtocol
* [0x1c4f] EFI_BOOT_SERVICES->OpenProtocol
* [0x4366] EFI_BOOT_SERVICES->OpenProtocol
* [0x43ec] EFI_BOOT_SERVICES->OpenProtocol
* [0x5a6d] EFI_BOOT_SERVICES->OpenProtocol
* [0x7363] EFI_BOOT_SERVICES->OpenProtocol
* [0x73a6] EFI_BOOT_SERVICES->OpenProtocol
* [0x73d9] EFI_BOOT_SERVICES->OpenProtocol
* [0x749f] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1b65] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x4038] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x75c6] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7732] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x5c0] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xb1f] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x5953] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x5a8e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x904] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x58e4] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9e79] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0xa0e7] EFI_BOOT_SERVICES->HandleProtocol
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x9d9] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x431a] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x43a3] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xdeb] EFI_BOOT_SERVICES->CloseProtocol
* [0x1d26] EFI_BOOT_SERVICES->CloseProtocol
* [0x7477] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0xacf0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xec20eb79, 0x6c1a, 0x4664, 0x9a, 0xd, 0xd2, 0xe4, 0xcc, 0x16, 0xd6, 0x64]
* [0xacb0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x720665, 0x67eb, 0x4a99, 0xba, 0xf7, 0xd3, 0xc3, 0x3a, 0x1c, 0x7c, 0xc9]
* [0xac90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc51711e7, 0xb4bf, 0x404a, 0xbf, 0xb8, 0xa, 0x4, 0x8e, 0xf1, 0xff, 0xe4]
* [0xacd0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xec835dd3, 0xfe0f, 0x617b, 0xa6, 0x21, 0xb3, 0x50, 0xc3, 0xe1, 0x33, 0x88]
* [0xac70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xaca0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x65530bc7, 0xa359, 0x410f, 0xb0, 0x10, 0x5a, 0xad, 0xc7, 0xec, 0x2b, 0x62]
* [0xace0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiTcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x46e44855, 0xbd60, 0x4ab7, 0xab, 0xd, 0xa6, 0x79, 0xb9, 0x44, 0x7d, 0x77]
* [0xad10]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0xad20]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xad30]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0xac70]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xad10]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0xad20]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xad30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0xad40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xad50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp4Config2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b446ed1, 0xe30b, 0x4faa, 0x87, 0x1a, 0x36, 0x54, 0xec, 0xa3, 0x60, 0x80]
* [0xad00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x480f8ae9, 0xc46, 0x4aa9, 0xbc, 0x89, 0xdb, 0x9f, 0xba, 0x61, 0x98, 0x6]
* [0xacc0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2c8759d5, 0x5c2d, 0x66ef, 0x92, 0x5f, 0xb6, 0x6c, 0x10, 0x19, 0x57, 0xe2]
* [0xac80]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x41d94cd2, 0x35b6, 0x455a, 0x82, 0x58, 0xd4, 0xe5, 0x13, 0x34, 0xaa, 0xdd]
* [0xac70]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xac80]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x41d94cd2, 0x35b6, 0x455a, 0x82, 0x58, 0xd4, 0xe5, 0x13, 0x34, 0xaa, 0xdd]
* [0xacc0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2c8759d5, 0x5c2d, 0x66ef, 0x92, 0x5f, 0xb6, 0x6c, 0x10, 0x19, 0x57, 0xe2]
## Module: TerminalSrc
### Boot services:
* [0x1d02] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5bf] EFI_BOOT_SERVICES->OpenProtocol
* [0x618] EFI_BOOT_SERVICES->OpenProtocol
* [0x8b3] EFI_BOOT_SERVICES->OpenProtocol
* [0xab7] EFI_BOOT_SERVICES->OpenProtocol
* [0xcb8] EFI_BOOT_SERVICES->OpenProtocol
* [0x1025] EFI_BOOT_SERVICES->OpenProtocol
* [0x1085] EFI_BOOT_SERVICES->OpenProtocol
* [0x1167] EFI_BOOT_SERVICES->OpenProtocol
* [0x142f] EFI_BOOT_SERVICES->OpenProtocol
* [0x1572] EFI_BOOT_SERVICES->OpenProtocol
* [0x1685] EFI_BOOT_SERVICES->OpenProtocol
* [0x176f] EFI_BOOT_SERVICES->OpenProtocol
* [0x17cb] EFI_BOOT_SERVICES->OpenProtocol
* [0x18ca] EFI_BOOT_SERVICES->OpenProtocol
* [0x192f] EFI_BOOT_SERVICES->OpenProtocol
* [0x1dba] EFI_BOOT_SERVICES->OpenProtocol
* [0x1954] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0xda2] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x124b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x353] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xc86] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xf02] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1be3] EFI_BOOT_SERVICES->LocateProtocol
* [0x1f27] EFI_BOOT_SERVICES->LocateProtocol
* [0x2361] EFI_BOOT_SERVICES->LocateProtocol
* [0x1d3d] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x5e5] EFI_BOOT_SERVICES->CloseProtocol
* [0x63e] EFI_BOOT_SERVICES->CloseProtocol
* [0xe3d] EFI_BOOT_SERVICES->CloseProtocol
* [0xfb8] EFI_BOOT_SERVICES->CloseProtocol
* [0xfe1] EFI_BOOT_SERVICES->CloseProtocol
* [0x1f7d] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x5640]
	 - [service] LocateHandleBuffer
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x50dc5c90, 0x1d33, 0x4fd6, 0x87, 0xe5, 0x6, 0x3b, 0x1d, 0xfa, 0x21, 0x70]
* [0x55f0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSerialIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbb25cf6f, 0xf1d4, 0x11d2, 0x9a, 0xc, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0xfd]
* [0x5650]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x55b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c1, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x5630]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0x55a0]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x51e9b4f9, 0x555d, 0x476c, 0x8b, 0xb5, 0xbd, 0x18, 0xd9, 0xa6, 0x88, 0x78]
* [0x5640]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x50dc5c90, 0x1d33, 0x4fd6, 0x87, 0xe5, 0x6, 0x3b, 0x1d, 0xfa, 0x21, 0x70]
* [0x5620]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdbff9d55, 0x89b7, 0x46da, 0xbd, 0xdf, 0x67, 0x7d, 0x3d, 0xc0, 0x24, 0x1d]
* [0x6e78]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiPciRootBridgeIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2f707ebb, 0x4a1a, 0x11d4, 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x5640]
	 - [service] OpenProtocolInformation
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x50dc5c90, 0x1d33, 0x4fd6, 0x87, 0xe5, 0x6, 0x3b, 0x1d, 0xfa, 0x21, 0x70]
* [0x55f0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiSerialIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbb25cf6f, 0xf1d4, 0x11d2, 0x9a, 0xc, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0xfd]
* [0x5620]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiAcpiSupportProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdbff9d55, 0x89b7, 0x46da, 0xbd, 0xdf, 0x67, 0x7d, 0x3d, 0xc0, 0x24, 0x1d]
## Module: TimestampDxe
### Boot services:
* [0x2ff] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
### Protocols:
* empty
## Module: TouchInputFilterDriver
### Boot services:
* [0x2c9] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x84e] EFI_BOOT_SERVICES->OpenProtocol
* [0x88c] EFI_BOOT_SERVICES->OpenProtocol
* [0x8bc] EFI_BOOT_SERVICES->OpenProtocol
* [0xb1b] EFI_BOOT_SERVICES->OpenProtocol
* [0xcc2] EFI_BOOT_SERVICES->OpenProtocol
* [0x334] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x38b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xb4e] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x4b0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4d3] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x9ef] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x439] EFI_BOOT_SERVICES->HandleProtocol
* [0xa25] EFI_BOOT_SERVICES->HandleProtocol
* [0x76e] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1290]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2599ed9d, 0x61ee, 0x4e32, 0x92, 0x57, 0x9c, 0x7c, 0xd, 0x9c, 0x40, 0xa3]
* [0x1260]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8d59d32b, 0xc655, 0x4ae9, 0x9b, 0x15, 0xf2, 0x59, 0x4, 0x99, 0x2a, 0x43]
* [0x1220]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x91b1d27b, 0xe126, 0x48d1, 0x82, 0x34, 0xd2, 0x8b, 0x81, 0xc8, 0x83, 0x62]
* [0x12c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x1260]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8d59d32b, 0xc655, 0x4ae9, 0x9b, 0x15, 0xf2, 0x59, 0x4, 0x99, 0x2a, 0x43]
* [0x1290]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2599ed9d, 0x61ee, 0x4e32, 0x92, 0x57, 0x9c, 0x7c, 0xd, 0x9c, 0x40, 0xa3]
## Module: Tpm20Acpi
### Boot services:
* [0x425] EFI_BOOT_SERVICES->LocateProtocol
* [0x4fe] EFI_BOOT_SERVICES->LocateProtocol
* [0xa22] EFI_BOOT_SERVICES->LocateProtocol
* [0x39f] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x48d] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xe08]
	 - [service] LocateProtocol
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
* [0xdb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiAcpiSdtProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xeb97088e, 0xcfdf, 0x49c6, 0xbe, 0x4b, 0xd9, 0x6, 0xa5, 0xb2, 0xe, 0x86]
* [0xdc0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xdbc9fd21, 0xfad8, 0x45b0, 0x9e, 0x78, 0x27, 0x15, 0x88, 0x67, 0xcc, 0x93]
* [0xe08]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
## Module: Tpm20PlatformDxe
### Boot services:
* [0xead] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x4e1c] EFI_BOOT_SERVICES->OpenProtocol
* [0x1029] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x9e6] EFI_BOOT_SERVICES->HandleProtocol
* [0xa16] EFI_BOOT_SERVICES->HandleProtocol
* [0xf14] EFI_BOOT_SERVICES->HandleProtocol
* [0x344] EFI_BOOT_SERVICES->LocateProtocol
* [0x362] EFI_BOOT_SERVICES->LocateProtocol
* [0x37f] EFI_BOOT_SERVICES->LocateProtocol
* [0x39c] EFI_BOOT_SERVICES->LocateProtocol
* [0x3b9] EFI_BOOT_SERVICES->LocateProtocol
* [0x410] EFI_BOOT_SERVICES->LocateProtocol
* [0x58b] EFI_BOOT_SERVICES->LocateProtocol
* [0x603] EFI_BOOT_SERVICES->LocateProtocol
* [0x808] EFI_BOOT_SERVICES->LocateProtocol
* [0xd90] EFI_BOOT_SERVICES->LocateProtocol
* [0x1522] EFI_BOOT_SERVICES->LocateProtocol
* [0x17ab] EFI_BOOT_SERVICES->LocateProtocol
* [0x2544] EFI_BOOT_SERVICES->LocateProtocol
* [0x2a37] EFI_BOOT_SERVICES->LocateProtocol
* [0x2f79] EFI_BOOT_SERVICES->LocateProtocol
* [0x3454] EFI_BOOT_SERVICES->LocateProtocol
* [0x4502] EFI_BOOT_SERVICES->LocateProtocol
* [0x4961] EFI_BOOT_SERVICES->LocateProtocol
* [0x49f4] EFI_BOOT_SERVICES->LocateProtocol
* [0x4e4d] EFI_BOOT_SERVICES->LocateProtocol
* [0x4fb3] EFI_BOOT_SERVICES->LocateProtocol
* [0x50d7] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x525c] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x52ca] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x6e60]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiHiiPackageListProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a1ee763, 0xd47a, 0x43b4, 0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc]
* [0x6e30]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6e40]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDiskIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xce345171, 0xba0b, 0x11d2, 0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6e90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x6eb0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0x6ec0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0x6ed0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0x6ea0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0x6e50]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
* [0x6e80]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiTrEEProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x607f766c, 0x7455, 0x42be, 0x93, 0xb, 0xe4, 0xd7, 0x6d, 0xb2, 0x72, 0xf]
* [0x6f20]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0x6f10]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xdbc9fd21, 0xfad8, 0x45b0, 0x9e, 0x78, 0x27, 0x15, 0x88, 0x67, 0xcc, 0x93]
* [0x6e70]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEdkiiVariableLockProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xcd3d0a05, 0x9e24, 0x437c, 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38]
## Module: TpmClearOnRollbackSmm
### Boot services:
* [0x5f0] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x62b] EFI_BOOT_SERVICES->HandleProtocol
* [0x34c] EFI_BOOT_SERVICES->LocateProtocol
* [0x381] EFI_BOOT_SERVICES->LocateProtocol
* [0x4cb] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x12a0]
	 - [service] LocateHandleBuffer
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x12a0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiFirmwareVolume2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x220e73b6, 0x6bdb, 0x4413, 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a]
* [0x1280]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1290]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmAccess2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc2702b74, 0x800c, 0x4131, 0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac]
## Module: TxtDxe
### Boot services:
* [0x2fc] EFI_BOOT_SERVICES->LocateProtocol
* [0x391] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x19a0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiS3SaveStateProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe857caf6, 0xc046, 0x45dc, 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87]
* [0x1990]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMpServiceProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3fdda605, 0xa76e, 0x4f46, 0xad, 0x29, 0x12, 0xf4, 0x53, 0x1b, 0x3d, 0x8]
## Module: Udp4Dxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x649] EFI_BOOT_SERVICES->OpenProtocol
* [0x685] EFI_BOOT_SERVICES->OpenProtocol
* [0x821] EFI_BOOT_SERVICES->OpenProtocol
* [0xf06] EFI_BOOT_SERVICES->OpenProtocol
* [0x30cf] EFI_BOOT_SERVICES->OpenProtocol
* [0x3112] EFI_BOOT_SERVICES->OpenProtocol
* [0x3145] EFI_BOOT_SERVICES->OpenProtocol
* [0x320b] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3332] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x349e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x8f2] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x576] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x710] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x7a2] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xe83] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x31e3] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x6290]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x83f01464, 0x99bd, 0x45e5, 0xb3, 0x83, 0xaf, 0x63, 0x5, 0xd8, 0xe9, 0xe6]
* [0x62a0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xc51711e7, 0xb4bf, 0x404a, 0xbf, 0xb8, 0xa, 0x4, 0x8e, 0xf1, 0xff, 0xe4]
* [0x62b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0x6300]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6310]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6320]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x6300]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x6310]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x6320]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x6330]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x62f0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x480f8ae9, 0xc46, 0x4aa9, 0xbc, 0x89, 0xdb, 0x9f, 0xba, 0x61, 0x98, 0x6]
* [0x62c0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x41d94cd2, 0x35b6, 0x455a, 0x82, 0x58, 0xd4, 0xe5, 0x13, 0x34, 0xaa, 0xdd]
* [0x62d0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2c8759d5, 0x5c2d, 0x66ef, 0x92, 0x5f, 0xb6, 0x6c, 0x10, 0x19, 0x57, 0xe2]
## Module: Udp6Dxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x5ed] EFI_BOOT_SERVICES->OpenProtocol
* [0x629] EFI_BOOT_SERVICES->OpenProtocol
* [0x808] EFI_BOOT_SERVICES->OpenProtocol
* [0xf3e] EFI_BOOT_SERVICES->OpenProtocol
* [0x2def] EFI_BOOT_SERVICES->OpenProtocol
* [0x2e32] EFI_BOOT_SERVICES->OpenProtocol
* [0x2e65] EFI_BOOT_SERVICES->OpenProtocol
* [0x2f2b] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3052] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x31be] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x8e0] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x576] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x69f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x48d] EFI_BOOT_SERVICES->HandleProtocol
* [0x470] EFI_BOOT_SERVICES->LocateProtocol
* [0x789] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0xebb] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x2f03] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0x6070]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x66ed4721, 0x3c98, 0x4d3e, 0x81, 0xe3, 0xd0, 0x3d, 0xd3, 0x9a, 0x72, 0x54]
* [0x6060]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xec835dd3, 0xfe0f, 0x617b, 0xa6, 0x21, 0xb3, 0x50, 0xc3, 0xe1, 0x33, 0x88]
* [0x6080]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
* [0x60c0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x60d0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x60e0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x60c0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0x60d0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0x60e0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0x60f0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x60b0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiDpcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x480f8ae9, 0xc46, 0x4aa9, 0xbc, 0x89, 0xdb, 0x9f, 0xba, 0x61, 0x98, 0x6]
* [0x6050]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2c8759d5, 0x5c2d, 0x66ef, 0x92, 0x5f, 0xb6, 0x6c, 0x10, 0x19, 0x57, 0xe2]
* [0x6050]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2c8759d5, 0x5c2d, 0x66ef, 0x92, 0x5f, 0xb6, 0x6c, 0x10, 0x19, 0x57, 0xe2]
## Module: UefiPxeBcDxe
### Boot services:
* [0x2c8] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0xa05a] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x102c] EFI_BOOT_SERVICES->OpenProtocol
* [0x1088] EFI_BOOT_SERVICES->OpenProtocol
* [0x10e4] EFI_BOOT_SERVICES->OpenProtocol
* [0x1140] EFI_BOOT_SERVICES->OpenProtocol
* [0x1199] EFI_BOOT_SERVICES->OpenProtocol
* [0x11f2] EFI_BOOT_SERVICES->OpenProtocol
* [0x13d7] EFI_BOOT_SERVICES->OpenProtocol
* [0x1539] EFI_BOOT_SERVICES->OpenProtocol
* [0x16fd] EFI_BOOT_SERVICES->OpenProtocol
* [0x1761] EFI_BOOT_SERVICES->OpenProtocol
* [0x17c5] EFI_BOOT_SERVICES->OpenProtocol
* [0x1829] EFI_BOOT_SERVICES->OpenProtocol
* [0x1a83] EFI_BOOT_SERVICES->OpenProtocol
* [0x1e74] EFI_BOOT_SERVICES->OpenProtocol
* [0x1ec8] EFI_BOOT_SERVICES->OpenProtocol
* [0x1f06] EFI_BOOT_SERVICES->OpenProtocol
* [0x1b6f] EFI_BOOT_SERVICES->OpenProtocol
* [0x1b9b] EFI_BOOT_SERVICES->OpenProtocol
* [0x1c28] EFI_BOOT_SERVICES->OpenProtocol
* [0x1cf2] EFI_BOOT_SERVICES->OpenProtocol
* [0x1d2f] EFI_BOOT_SERVICES->OpenProtocol
* [0x209f] EFI_BOOT_SERVICES->OpenProtocol
* [0x7caa] EFI_BOOT_SERVICES->OpenProtocol
* [0xbf5b] EFI_BOOT_SERVICES->OpenProtocol
* [0xbfa7] EFI_BOOT_SERVICES->OpenProtocol
* [0x368] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x3fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xae4] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0xdfe] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1f98] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1de0] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x805c] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x1396] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1a42] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1d5c] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7e9a] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x9fcb] EFI_BOOT_SERVICES->ProtocolsPerHandle
* [0x678] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xabf] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xdd9] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x7ecd] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x803d] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x1363] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1a0f] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xbbd5] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x300] EFI_BOOT_SERVICES->HandleProtocol
* [0x38a] EFI_BOOT_SERVICES->HandleProtocol
* [0x3d3] EFI_BOOT_SERVICES->HandleProtocol
* [0x457] EFI_BOOT_SERVICES->HandleProtocol
* [0xeaa] EFI_BOOT_SERVICES->HandleProtocol
* [0x1272] EFI_BOOT_SERVICES->HandleProtocol
* [0x1910] EFI_BOOT_SERVICES->HandleProtocol
* [0x4237] EFI_BOOT_SERVICES->HandleProtocol
* [0x7e48] EFI_BOOT_SERVICES->HandleProtocol
* [0xb8c3] EFI_BOOT_SERVICES->HandleProtocol
* [0xbff1] EFI_BOOT_SERVICES->HandleProtocol
* [0xc061] EFI_BOOT_SERVICES->HandleProtocol
* [0xc0f4] EFI_BOOT_SERVICES->HandleProtocol
* [0xc144] EFI_BOOT_SERVICES->HandleProtocol
* [0x4bc] EFI_BOOT_SERVICES->LocateProtocol
* [0x4da] EFI_BOOT_SERVICES->LocateProtocol
* [0x4f7] EFI_BOOT_SERVICES->LocateProtocol
* [0x514] EFI_BOOT_SERVICES->LocateProtocol
* [0x531] EFI_BOOT_SERVICES->LocateProtocol
* [0x480f] EFI_BOOT_SERVICES->LocateProtocol
* [0x48a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x6b9] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x6f7] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x735] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x76f] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x7a9] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x7f1] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x82f] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x869] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x8a3] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x7835] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x79a4] EFI_BOOT_SERVICES->OpenProtocolInformation
* [0x7fe7] EFI_BOOT_SERVICES->OpenProtocolInformation
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
* [0x7d32] EFI_BOOT_SERVICES->CloseProtocol
### Protocols:
* [0xdb50]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0xdb30]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x78247c57, 0x63db, 0x4708, 0x99, 0xc2, 0xa8, 0xb4, 0xa9, 0xa6, 0x1f, 0x6b]
* [0xdb10]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0xda90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4b427bb, 0xba21, 0x4f16, 0xbc, 0x4e, 0x43, 0xe4, 0x16, 0xab, 0x61, 0x9c]
* [0xdab0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x41d94cd2, 0x35b6, 0x455a, 0x82, 0x58, 0xd4, 0xe5, 0x13, 0x34, 0xaa, 0xdd]
* [0xda00]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb95e9fda, 0x26de, 0x48d2, 0x88, 0x7, 0x1f, 0x91, 0x7, 0xac, 0x5e, 0x3a]
* [0xdbb0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
* [0xdb90]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbf0a78ba, 0xec29, 0x49cf, 0xa1, 0xc9, 0x7a, 0xe5, 0x4e, 0xab, 0x6a, 0x51]
* [0xdb70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
* [0xdae0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2c8759d5, 0x5c2d, 0x66ef, 0x92, 0x5f, 0xb6, 0x6c, 0x10, 0x19, 0x57, 0xe2]
* [0xdbe0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiLoadFileProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x56ec3091, 0x954c, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xdb80]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiMtftp6ServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd9760ff3, 0x3cca, 0x4267, 0x80, 0xf9, 0x75, 0x27, 0xfa, 0xfa, 0x42, 0x23]
* [0xda60]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xda70]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiNetworkInterfaceIdentifierProtocolGuid_31
	 - [protocol_place] edk2_guids
	 - [guid] [0x1aced566, 0x76ed, 0x4218, 0xbc, 0x81, 0x76, 0x7f, 0x1f, 0x97, 0x7a, 0x89]
* [0xdc50]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0xdc70]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xdc80]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0xdca0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xda00]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb95e9fda, 0x26de, 0x48d2, 0x88, 0x7, 0x1f, 0x91, 0x7, 0xac, 0x5e, 0x3a]
* [0xdbc0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiPxeBaseCodeCallbackProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x245dca21, 0xfb7b, 0x11d3, 0x8f, 0x1, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xda60]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xda00]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb95e9fda, 0x26de, 0x48d2, 0x88, 0x7, 0x1f, 0x91, 0x7, 0xac, 0x5e, 0x3a]
* [0xdbc0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiPxeBaseCodeCallbackProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x245dca21, 0xfb7b, 0x11d3, 0x8f, 0x1, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xdc50]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDriverBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x18a031ab, 0xb443, 0x4d1a, 0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71]
* [0xdc70]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentNameProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x107a772c, 0xd5e1, 0x11d4, 0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xdc80]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiComponentName2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x6a7a5cff, 0xe8d9, 0x4f70, 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14]
* [0xdc90]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiLoadedImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b1b31a1, 0x9562, 0x11d2, 0x8e, 0x3f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xdbf0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiAdapterInformationProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe5dd1403, 0xd622, 0xc24e, 0x84, 0x88, 0xc7, 0x1b, 0x17, 0xf5, 0xe8, 0x2]
* [0xdac0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp4Config2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x5b446ed1, 0xe30b, 0x4faa, 0x87, 0x1a, 0x36, 0x54, 0xec, 0xa3, 0x60, 0x80]
* [0xdaf0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiIp6ConfigProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x937fe521, 0x95ae, 0x4d1a, 0x89, 0x29, 0x48, 0xbc, 0xd9, 0xa, 0xd3, 0x1a]
* [0xdbc0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPxeBaseCodeCallbackProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x245dca21, 0xfb7b, 0x11d3, 0x8f, 0x1, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xda60]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xdca0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiSimpleNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xa19832b9, 0xac25, 0x11d3, 0x9a, 0x2d, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xdcc0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkServiceBindingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf36ff770, 0xa7e1, 0x42cf, 0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c]
* [0xdcb0]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiManagedNetworkProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x7ab33a91, 0xace5, 0x4326, 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16]
* [0xdc10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiStringProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xfd96974, 0x23aa, 0x4cdc, 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a]
* [0xdc30]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiDatabaseProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xef9fc172, 0xa1b2, 0x4693, 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42]
* [0xdc40]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiConfigRoutingProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x587e72d7, 0xcc50, 0x4f79, 0x82, 0x9, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0xf]
* [0xdc00]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiFontProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe9ca4775, 0x8657, 0x47fc, 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24]
* [0xdc20]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiHiiImageProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31a6406a, 0x6bdf, 0x4e46, 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20]
* [0xdce0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8a91b1e1, 0x56c7, 0x4adc, 0xab, 0xeb, 0x1c, 0x2c, 0xa1, 0x72, 0x9e, 0xff]
* [0xdc60]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiGraphicsOutputProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9042a9de, 0x23dc, 0x4a38, 0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a]
* [0xda90]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4b427bb, 0xba21, 0x4f16, 0xbc, 0x4e, 0x43, 0xe4, 0x16, 0xab, 0x61, 0x9c]
* [0xdab0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x41d94cd2, 0x35b6, 0x455a, 0x82, 0x58, 0xd4, 0xe5, 0x13, 0x34, 0xaa, 0xdd]
* [0xdb10]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0xdb50]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0xdb30]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiMtftp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x78247c57, 0x63db, 0x4708, 0x99, 0xc2, 0xa8, 0xb4, 0xa9, 0xa6, 0x1f, 0x6b]
* [0xdae0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2c8759d5, 0x5c2d, 0x66ef, 0x92, 0x5f, 0xb6, 0x6c, 0x10, 0x19, 0x57, 0xe2]
* [0xdb70]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
* [0xdbb0]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
* [0xdb90]
	 - [service] OpenProtocolInformation
	 - [protocol_name] gEfiMtftp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbf0a78ba, 0xec29, 0x49cf, 0xa1, 0xc9, 0x7a, 0xe5, 0x4e, 0xab, 0x6a, 0x51]
* [0xda90]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiArpProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4b427bb, 0xba21, 0x4f16, 0xbc, 0x4e, 0x43, 0xe4, 0x16, 0xab, 0x61, 0x9c]
* [0xdab0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x41d94cd2, 0x35b6, 0x455a, 0x82, 0x58, 0xd4, 0xe5, 0x13, 0x34, 0xaa, 0xdd]
* [0xdb10]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3ad9df29, 0x4501, 0x478d, 0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0xe, 0x50, 0xf3]
* [0xdb30]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiMtftp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x78247c57, 0x63db, 0x4708, 0x99, 0xc2, 0xa8, 0xb4, 0xa9, 0xa6, 0x1f, 0x6b]
* [0xdb50]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp4ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8a219718, 0x4ef5, 0x4761, 0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56]
* [0xda00]
	 - [service] CloseProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb95e9fda, 0x26de, 0x48d2, 0x88, 0x7, 0x1f, 0x91, 0x7, 0xac, 0x5e, 0x3a]
* [0xdae0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiIp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2c8759d5, 0x5c2d, 0x66ef, 0x92, 0x5f, 0xb6, 0x6c, 0x10, 0x19, 0x57, 0xe2]
* [0xdb70]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUdp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4f948815, 0xb4b9, 0x43cb, 0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55]
* [0xdb90]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiMtftp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xbf0a78ba, 0xec29, 0x49cf, 0xa1, 0xc9, 0x7a, 0xe5, 0x4e, 0xab, 0x6a, 0x51]
* [0xdbb0]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDhcp6ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x87c8bad7, 0x595, 0x4053, 0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b]
## Module: Uhcd
### Boot services:
* [0xbe2] EFI_BOOT_SERVICES->OpenProtocol
* [0xc9f] EFI_BOOT_SERVICES->OpenProtocol
* [0xd0d] EFI_BOOT_SERVICES->OpenProtocol
* [0xdcf] EFI_BOOT_SERVICES->OpenProtocol
* [0xffe] EFI_BOOT_SERVICES->OpenProtocol
* [0x103b] EFI_BOOT_SERVICES->OpenProtocol
* [0x1f2f] EFI_BOOT_SERVICES->OpenProtocol
* [0x2028] EFI_BOOT_SERVICES->OpenProtocol
* [0x3e26] EFI_BOOT_SERVICES->OpenProtocol
* [0x43f6] EFI_BOOT_SERVICES->OpenProtocol
* [0x468f] EFI_BOOT_SERVICES->OpenProtocol
* [0x470d] EFI_BOOT_SERVICES->OpenProtocol
* [0x4942] EFI_BOOT_SERVICES->OpenProtocol
* [0x497c] EFI_BOOT_SERVICES->OpenProtocol
* [0x85df] EFI_BOOT_SERVICES->OpenProtocol
* [0x8696] EFI_BOOT_SERVICES->OpenProtocol
* [0x87aa] EFI_BOOT_SERVICES->OpenProtocol
* [0x89da] EFI_BOOT_SERVICES->OpenProtocol
* [0x8a9c] EFI_BOOT_SERVICES->OpenProtocol
* [0x8c63] EFI_BOOT_SERVICES->OpenProtocol
* [0x8c99] EFI_BOOT_SERVICES->OpenProtocol
* [0x8d82] EFI_BOOT_SERVICES->OpenProtocol
* [0x93db] EFI_BOOT_SERVICES->OpenProtocol
* [0xa289] EFI_BOOT_SERVICES->OpenProtocol
* [0xa2bb] EFI_BOOT_SERVICES->OpenProtocol
* [0x8da9] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x93fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x632] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x6df] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x829] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x16c2] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x4b7e] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x73e0] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x7405] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x805a] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x8fcf] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x9395] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x10ac] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x4021] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x87fe] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x8e14] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0xa337] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
* [0x8af] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x3dbe] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x4643] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x88de] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8997] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x8b80] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0xa22d] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
* [0x1946] EFI_BOOT_SERVICES->HandleProtocol
* [0x442f] EFI_BOOT_SERVICES->HandleProtocol
* [0x981] EFI_BOOT_SERVICES->LocateProtocol
* [0x9fb] EFI_BOOT_SERVICES->LocateProtocol
* [0xb45] EFI_BOOT_SERVICES->LocateProtocol
* [0x45a5] EFI_BOOT_SERVICES->LocateProtocol
* [0x4b15] EFI_BOOT_SERVICES->LocateProtocol
* [0x9995] EFI_BOOT_SERVICES->LocateProtocol
* [0xac94] EFI_BOOT_SERVICES->LocateProtocol
* [0xc27] EFI_BOOT_SERVICES->CloseProtocol
* [0xcc2] EFI_BOOT_SERVICES->CloseProtocol
* [0xd5c] EFI_BOOT_SERVICES->CloseProtocol
* [0xdf1] EFI_BOOT_SERVICES->CloseProtocol
* [0xe52] EFI_BOOT_SERVICES->CloseProtocol
* [0xf63] EFI_BOOT_SERVICES->CloseProtocol
* [0xf81] EFI_BOOT_SERVICES->CloseProtocol
* [0x1132] EFI_BOOT_SERVICES->CloseProtocol
* [0x1155] EFI_BOOT_SERVICES->CloseProtocol
* [0x3fde] EFI_BOOT_SERVICES->CloseProtocol
* [0x46d5] EFI_BOOT_SERVICES->CloseProtocol
* [0x4821] EFI_BOOT_SERVICES->CloseProtocol
* [0x8602] EFI_BOOT_SERVICES->CloseProtocol
* [0x870d] EFI_BOOT_SERVICES->CloseProtocol
* [0x8751] EFI_BOOT_SERVICES->CloseProtocol
* [0x8841] EFI_BOOT_SERVICES->CloseProtocol
* [0x89fd] EFI_BOOT_SERVICES->CloseProtocol
* [0x8b43] EFI_BOOT_SERVICES->CloseProtocol
* [0x8e46] EFI_BOOT_SERVICES->CloseProtocol
* [0x93a] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x9d0] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0xaef3] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0xb310]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0xb360]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb2c0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUsbHcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf5089266, 0x1aa0, 0x4953, 0x97, 0xd8, 0x56, 0x2f, 0x8a, 0x73, 0xb5, 0x19]
* [0xb300]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUsb2HcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3e745226, 0x9818, 0x45b6, 0xa2, 0xac, 0xd7, 0xcd, 0xe, 0x8b, 0xa2, 0xbc]
* [0xb370]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2b2f68d6, 0xcd2, 0x44cf, 0x8e, 0x8b, 0xbb, 0xa2, 0xb, 0x1b, 0x5b, 0x75]
* [0xb380]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xc558]
	 - [service] OpenProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x1fede521, 0x31c, 0x4bc5, 0x80, 0x50, 0xf3, 0xd6, 0x16, 0x1e, 0x2e, 0x92]
* [0xb3d0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8d59d32b, 0xc655, 0x4ae9, 0x9b, 0x15, 0xf2, 0x59, 0x4, 0x99, 0x2a, 0x43]
* [0xb3b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31878c87, 0xb75, 0x11d5, 0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xb390]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextInProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x387477c1, 0x69c7, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb2b0]
	 - [service] OpenProtocol
	 - [protocol_name] gEfiSimpleTextInputExProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdd9e7534, 0x7762, 0x4698, 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa]
* [0xb3d0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8d59d32b, 0xc655, 0x4ae9, 0x9b, 0x15, 0xf2, 0x59, 0x4, 0x99, 0x2a, 0x43]
* [0xb3b0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31878c87, 0xb75, 0x11d5, 0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xb2e0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5859cb76, 0x6bef, 0x468a, 0xbe, 0x2d, 0xb3, 0xdd, 0x1a, 0x27, 0xf0, 0x12]
* [0xb300]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiUsb2HcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3e745226, 0x9818, 0x45b6, 0xa2, 0xac, 0xd7, 0xcd, 0xe, 0x8b, 0xa2, 0xbc]
* [0xb380]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb3d0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiAbsolutePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x8d59d32b, 0xc655, 0x4ae9, 0x9b, 0x15, 0xf2, 0x59, 0x4, 0x99, 0x2a, 0x43]
* [0xb3b0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gEfiSimplePointerProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x31878c87, 0xb75, 0x11d5, 0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d]
* [0xb310]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0xb370]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2b2f68d6, 0xcd2, 0x44cf, 0x8e, 0x8b, 0xbb, 0xa2, 0xb, 0x1b, 0x5b, 0x75]
* [0xb3c0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x783658a3, 0x4172, 0x4421, 0xa2, 0x99, 0xe0, 0x9, 0x7, 0x9c, 0xc, 0xb4]
* [0xb350]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x68b81e51, 0x2583, 0x4582, 0x95, 0xdb, 0xc5, 0x72, 0x32, 0x36, 0xc4, 0xf1]
* [0xb3f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x9400d59b, 0xe9c, 0x4f6c, 0xb5, 0x9a, 0xfc, 0x20, 0x0, 0x9d, 0xb9, 0xec]
* [0xb2f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2ad8e2d2, 0x2e91, 0x4cd1, 0x95, 0xf5, 0xe7, 0x8f, 0xe5, 0xeb, 0xe3, 0x16]
* [0xb330]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiMmControlProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x843dc720, 0xab1e, 0x42cb, 0x93, 0x57, 0x8a, 0x0, 0x78, 0xf3, 0x56, 0x1b]
* [0xb3e0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb295bd1c, 0x63e3, 0x48e3, 0xb2, 0x65, 0xf7, 0xdf, 0xa2, 0x7, 0x1, 0x23]
* [0xb918]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0xb310]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0xb360]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiDevicePathProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x9576e91, 0x6d3f, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0xb300]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUsb2HcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3e745226, 0x9818, 0x45b6, 0xa2, 0xac, 0xd7, 0xcd, 0xe, 0x8b, 0xa2, 0xbc]
* [0xb370]
	 - [service] CloseProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2b2f68d6, 0xcd2, 0x44cf, 0x8e, 0x8b, 0xbb, 0xa2, 0xb, 0x1b, 0x5b, 0x75]
* [0xb310]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiPciIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x4cf5b200, 0x68b8, 0x4ca5, 0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a]
* [0xb3c0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiLegacyBiosPlatformProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x783658a3, 0x4172, 0x4421, 0xa2, 0x99, 0xe0, 0x9, 0x7, 0x9c, 0xc, 0xb4]
* [0xcbf0]
	 - [service] RegisterProtocolNotify
	 - [protocol_name] gEfiTpmDeviceInstanceNoneGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
## Module: UpdateMemoryRecord
### Boot services:
* [0x2f6] EFI_BOOT_SERVICES->LocateProtocol
* [0x314] EFI_BOOT_SERVICES->LocateProtocol
* [0x33b] EFI_BOOT_SERVICES->LocateProtocol
* [0x358] EFI_BOOT_SERVICES->LocateProtocol
* [0x373] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xde0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5e90a50d, 0x6955, 0x4a49, 0x90, 0x32, 0xda, 0x38, 0x12, 0xf8, 0xe8, 0xe5]
* [0xdf0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x67269263, 0xaf1, 0x45dd, 0x93, 0xc8, 0x29, 0x99, 0x21, 0xd0, 0xe1, 0xe9]
* [0xe00]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xd4d2f201, 0x50e8, 0x4d45, 0x8e, 0x5, 0xfd, 0x49, 0xa8, 0x2a, 0x15, 0x69]
* [0xe10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmbusHcProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xe49d33ed, 0x513d, 0x4634, 0xb6, 0x98, 0x6f, 0x55, 0xaa, 0x75, 0x1c, 0x1b]
* [0xe20]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xc6aa1f27, 0x5597, 0x4802, 0x9f, 0x63, 0xd6, 0x28, 0x36, 0x59, 0x86, 0x35]
## Module: UsbInt13
### Boot services:
* [0x8ef] EFI_BOOT_SERVICES->LocateHandleBuffer
* [0x927] EFI_BOOT_SERVICES->HandleProtocol
* [0x96a] EFI_BOOT_SERVICES->HandleProtocol
* [0x31d] EFI_BOOT_SERVICES->LocateProtocol
* [0x402] EFI_BOOT_SERVICES->LocateProtocol
* [0x611] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x1020]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiUsbIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x2b2f68d6, 0xcd2, 0x44cf, 0x8e, 0x8b, 0xbb, 0xa2, 0xb, 0x1b, 0x5b, 0x75]
* [0x1030]
	 - [service] HandleProtocol
	 - [protocol_name] gEfiBlockIoProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x964e5b21, 0x6459, 0x11d2, 0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b]
* [0x1010]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2ad8e2d2, 0x2e91, 0x4cd1, 0x95, 0xf5, 0xe7, 0x8f, 0xe5, 0xeb, 0xe3, 0x16]
* [0x1000]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x8e008510, 0x9bb1, 0x457d, 0x9f, 0x70, 0x89, 0x7a, 0xba, 0x86, 0x5d, 0xb9]
* [0xff0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiLegacyBiosProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xdb9a1e3d, 0x45cb, 0x4abb, 0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d]
## Module: UsbRtSmm
### Boot services:
* [0x5956] EFI_BOOT_SERVICES->OpenProtocol
* [0x20b3] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2214] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x23c1] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x55af] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x1768d] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x5744] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x57e3] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x350] EFI_BOOT_SERVICES->LocateProtocol
* [0xac7] EFI_BOOT_SERVICES->LocateProtocol
* [0xdc5] EFI_BOOT_SERVICES->LocateProtocol
* [0xe70] EFI_BOOT_SERVICES->LocateProtocol
* [0x5237] EFI_BOOT_SERVICES->LocateProtocol
* [0x19779] EFI_BOOT_SERVICES->LocateProtocol
* [0x103b] EFI_BOOT_SERVICES->RegisterProtocolNotify
* [0x583b] EFI_BOOT_SERVICES->RegisterProtocolNotify
### Protocols:
* [0x1a440]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1a958]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1a3a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2ad8e2d2, 0x2e91, 0x4cd1, 0x95, 0xf5, 0xe7, 0x8f, 0xe5, 0xeb, 0xe3, 0x16]
* [0x1a3c0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x5859cb76, 0x6bef, 0x468a, 0xbe, 0x2d, 0xb3, 0xdd, 0x1a, 0x27, 0xf0, 0x12]
* [0x1a470]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: UsbS5Wakeup
### Boot services:
* [0x7eb] EFI_BOOT_SERVICES->ReinstallProtocolInterface
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0xf6f] EFI_BOOT_SERVICES->LocateProtocol
* [0x1003] EFI_BOOT_SERVICES->LocateProtocol
* [0x1325] EFI_BOOT_SERVICES->LocateProtocol
* [0x140d] EFI_BOOT_SERVICES->LocateProtocol
* [0xda7] EFI_BOOT_SERVICES->OpenProtocolInformation
### Protocols:
* [0x17d0]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1cd8]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x17a0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x2ad8e2d2, 0x2e91, 0x4cd1, 0x95, 0xf5, 0xe7, 0x8f, 0xe5, 0xeb, 0xe3, 0x16]
* [0x17f0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: UsbWorkaroundDxe
### Boot services:
* [0x1184] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x124e] EFI_BOOT_SERVICES->LocateProtocol
* [0x1354] EFI_BOOT_SERVICES->LocateProtocol
* [0x1415] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x2598]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gPchResetCallbackProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3a3300ab, 0xc929, 0x487d, 0xab, 0x34, 0x15, 0x9b, 0xc1, 0x35, 0x62, 0xc0]
* [0x2538]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiStatusCodeRuntimeProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xd2b2b828, 0x826, 0x48a7, 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0]
* [0x2000]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: VerifyFwBootGuard
### Boot services:
* [0x2bd] EFI_BOOT_SERVICES->LocateProtocol
* [0x67b] EFI_BOOT_SERVICES->LocateProtocol
* [0x7d3] EFI_BOOT_SERVICES->LocateProtocol
* [0x9ed] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0xd10]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0x1218]
	 - [service] LocateProtocol
	 - [protocol_name] gEfiSmmBase2ProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0xf4ccbfb7, 0xf6e0, 0x47fd, 0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91]
* [0xd30]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x36232936, 0xe76, 0x31c8, 0xa1, 0x3a, 0x3a, 0xf2, 0xfc, 0x1c, 0x39, 0x32]
## Module: WdtAppDxe
### Boot services:
* [0x3c2] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x2f8] EFI_BOOT_SERVICES->LocateProtocol
* [0x408] EFI_BOOT_SERVICES->LocateProtocol
* [0x4d1] EFI_BOOT_SERVICES->LocateProtocol
* [0x557] EFI_BOOT_SERVICES->LocateProtocol
### Protocols:
* [0x5e0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0x92c7d0bb, 0x679e, 0x479d, 0x87, 0x8d, 0xd4, 0xb8, 0x29, 0x68, 0x57, 0x8b]
* [0x5d0]
	 - [service] LocateProtocol
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb42b8d12, 0x2acb, 0x499a, 0xa9, 0x20, 0xdd, 0x5b, 0xe6, 0xcf, 0x9, 0xb1]
* [0x5f0]
	 - [service] LocateProtocol
	 - [protocol_name] gPcdProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x11b34006, 0xd85b, 0x4d0a, 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7]
## Module: WdtDxe
### Boot services:
* [0x3de] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x400] EFI_BOOT_SERVICES->UninstallProtocolInterface
* [0x381] EFI_BOOT_SERVICES->InstallProtocolInterface
* [0x3a4] EFI_BOOT_SERVICES->InstallProtocolInterface
### Protocols:
* [0x6e0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb42b8d12, 0x2acb, 0x499a, 0xa9, 0x20, 0xdd, 0x5b, 0xe6, 0xcf, 0x9, 0xb1]
* [0x6f0]
	 - [service] UninstallProtocolInterface
	 - [protocol_name] gPchResetCallbackProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3a3300ab, 0xc929, 0x487d, 0xab, 0x34, 0x15, 0x9b, 0xc1, 0x35, 0x62, 0xc0]
* [0x6e0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] ProprietaryProtocol
	 - [protocol_place] unknown
	 - [guid] [0xb42b8d12, 0x2acb, 0x499a, 0xa9, 0x20, 0xdd, 0x5b, 0xe6, 0xcf, 0x9, 0xb1]
* [0x6f0]
	 - [service] InstallProtocolInterface
	 - [protocol_name] gPchResetCallbackProtocolGuid
	 - [protocol_place] edk2_guids
	 - [guid] [0x3a3300ab, 0xc929, 0x487d, 0xab, 0x34, 0x15, 0x9b, 0xc1, 0x35, 0x62, 0xc0]
