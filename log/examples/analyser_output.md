*Example №1*

```
Python>analyser = Analyser()
Python>analyser.help()
Methods:
 * analyser.get_boot_services()
   - check: analyser.gBServices[<service_name>]
 * analyser.get_protocols()
   - check: analyser.Protocols['All']
 * analyser.get_prot_names()
   - check: analyser.Protocols['All']
Commands:
 * analyser.list_boot_services()
 * analyser.list_protocols()
 * analyser.make_comments()
 * analyser.make_names()
 * analyser.set_types()
 * analyser.print_all()
 * analyser.analyse_all()
Python>analyser.print_all()
Boot services:
+------------+-------------------------------------+
| Address    | Service                             |
+------------+-------------------------------------+
| 0x00065662 | LocateHandleBuffer                  |
| 0x00067863 | LocateHandleBuffer                  |
| 0x000678bc | OpenProtocol                        |
| 0x00065785 | UninstallProtocolInterface          |
| 0x00065d7b | UninstallProtocolInterface          |
| 0x00065de5 | UninstallProtocolInterface          |
| 0x00066d2d | UninstallProtocolInterface          |
| 0x00066d96 | UninstallProtocolInterface          |
| 0x0006d38b | UninstallProtocolInterface          |
| 0x00066cf6 | InstallProtocolInterface            |
| 0x00067cbd | InstallProtocolInterface            |
| 0x0006ebc1 | InstallProtocolInterface            |
| 0x00067dcb | ProtocolsPerHandle                  |
| 0x00065819 | UninstallMultipleProtocolInterfaces |
| 0x000659eb | InstallMultipleProtocolInterfaces   |
| 0x00065791 | ReinstallProtocolInterface          |
| 0x00066e09 | ReinstallProtocolInterface          |
| 0x00066e44 | ReinstallProtocolInterface          |
| 0x0006cfe7 | ReinstallProtocolInterface          |
| 0x0006d048 | ReinstallProtocolInterface          |
| 0x0006d145 | ReinstallProtocolInterface          |
| 0x0006d183 | ReinstallProtocolInterface          |
| 0x0006ec23 | ReinstallProtocolInterface          |
| 0x0007274e | ReinstallProtocolInterface          |
| 0x0007287e | ReinstallProtocolInterface          |
| 0x00072987 | ReinstallProtocolInterface          |
| 0x00072a3a | ReinstallProtocolInterface          |
| 0x000a09f2 | ReinstallProtocolInterface          |
| 0x0006534e | HandleProtocol                      |
| 0x00065abb | HandleProtocol                      |
| 0x00065b7f | HandleProtocol                      |
| 0x00065bac | HandleProtocol                      |
| 0x000677ee | HandleProtocol                      |
| 0x00067977 | HandleProtocol                      |
| 0x00067b2d | HandleProtocol                      |
| 0x00067b69 | HandleProtocol                      |
| 0x00067c30 | HandleProtocol                      |
| 0x00067ccb | HandleProtocol                      |
| 0x00067d10 | HandleProtocol                      |
| 0x0006ce41 | HandleProtocol                      |
| 0x0006ce7a | HandleProtocol                      |
| 0x0006d1ba | HandleProtocol                      |
| 0x0006ebfe | HandleProtocol                      |
| 0x000a0df8 | HandleProtocol                      |
| 0x000690b0 | OpenProtocolInformation             |
| 0x00065cad | RegisterProtocolNotify              |
+------------+-------------------------------------+
Protocols:
+-------------------------------------+----------------------------------+------------+-------------------------------------+----------------+
| GUID                                | Protocol name                    | Address    | Service                             | Protocol place |
+-------------------------------------+----------------------------------+------------+-------------------------------------+----------------+
| 47C7B221-C42A-11D2-8E5700A0C969723B | gEfiShellEnvironment2Guid        | 0x00054d50 | UninstallProtocolInterface          | edk2_guids     |
| 47C7B223-C42A-11D2-8E5700A0C969723B | gEfiShellInterfaceGuid           | 0x000098f0 | UninstallProtocolInterface          | edk2_guids     |
| 0FD96974-23AA-4CDC-B9CB98D17750322A | gEfiHiiStringProtocolGuid        | 0x00000490 | UninstallMultipleProtocolInterfaces | edk2_guids     |
| 47C7B221-C42A-11D2-8E5700A0C969723B | gEfiShellEnvironment2Guid        | 0x00054d50 | ReinstallProtocolInterface          | edk2_guids     |
| 47C7B223-C42A-11D2-8E5700A0C969723B | gEfiShellInterfaceGuid           | 0x000098f0 | ReinstallProtocolInterface          | edk2_guids     |
| 0006D5C0-0000-0000-243B070000000000 | ProprietaryProtocol              | 0x00008dd0 | ReinstallProtocolInterface          | unknown        |
| 387477C1-69C7-11D2-8E3900A0C969723B | gEfiSimpleTextInProtocolGuid     | 0x00000460 | ReinstallProtocolInterface          | edk2_guids     |
| 387477C2-69C7-11D2-8E3900A0C969723B | gEfiSimpleTextOutProtocolGuid    | 0x00000470 | ReinstallProtocolInterface          | edk2_guids     |
| 5B1B31A1-9562-11D2-8E3F00A0C969723B | gEfiLoadedImageProtocolGuid      | 0x000005a0 | HandleProtocol                      | edk2_guids     |
| 09576E91-6D3F-11D2-8E3900A0C969723B | gEfiDevicePathProtocolGuid       | 0x00000580 | HandleProtocol                      | edk2_guids     |
| 47C7B223-C42A-11D2-8E5700A0C969723B | gEfiShellInterfaceGuid           | 0x000098f0 | HandleProtocol                      | edk2_guids     |
| 47C7B221-C42A-11D2-8E5700A0C969723B | gEfiShellEnvironment2Guid        | 0x00054d50 | HandleProtocol                      | edk2_guids     |
| 964E5B22-6459-11D2-8E3900A0C969723B | gEfiSimpleFileSystemProtocolGuid | 0x00000590 | HandleProtocol                      | edk2_guids     |
+-------------------------------------+----------------------------------+------------+-------------------------------------+----------------+
```

*Example №2*

```
Python>analyser.analyse_all()
Comments:
[ 0x00065662 ] EFI_BOOT_SERVICES->LocateHandleBuffer
[ 0x00067863 ] EFI_BOOT_SERVICES->LocateHandleBuffer
[ 0x000678bc ] EFI_BOOT_SERVICES->OpenProtocol
[ 0x00065785 ] EFI_BOOT_SERVICES->UninstallProtocolInterface
[ 0x00065d7b ] EFI_BOOT_SERVICES->UninstallProtocolInterface
[ 0x00065de5 ] EFI_BOOT_SERVICES->UninstallProtocolInterface
[ 0x00066d2d ] EFI_BOOT_SERVICES->UninstallProtocolInterface
[ 0x00066d96 ] EFI_BOOT_SERVICES->UninstallProtocolInterface
[ 0x0006d38b ] EFI_BOOT_SERVICES->UninstallProtocolInterface
[ 0x00066cf6 ] EFI_BOOT_SERVICES->InstallProtocolInterface
[ 0x00067cbd ] EFI_BOOT_SERVICES->InstallProtocolInterface
[ 0x0006ebc1 ] EFI_BOOT_SERVICES->InstallProtocolInterface
[ 0x00067dcb ] EFI_BOOT_SERVICES->ProtocolsPerHandle
[ 0x00065819 ] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
[ 0x000659eb ] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
[ 0x00065791 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x00066e09 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x00066e44 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x0006cfe7 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x0006d048 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x0006d145 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x0006d183 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x0006ec23 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x0007274e ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x0007287e ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x00072987 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x00072a3a ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x000a09f2 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
[ 0x0006534e ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x00065abb ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x00065b7f ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x00065bac ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x000677ee ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x00067977 ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x00067b2d ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x00067b69 ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x00067c30 ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x00067ccb ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x00067d10 ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x0006ce41 ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x0006ce7a ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x0006d1ba ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x0006ebfe ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x000a0df8 ] EFI_BOOT_SERVICES->HandleProtocol
[ 0x000690b0 ] EFI_BOOT_SERVICES->OpenProtocolInformation
[ 0x00065cad ] EFI_BOOT_SERVICES->RegisterProtocolNotify
Names:
[ 0x00054d50 ] gEfiShellEnvironment2Guid_0x54d50
[ 0x000098f0 ] gEfiShellInterfaceGuid_0x98f0
[ 0x00000490 ] gEfiHiiStringProtocolGuid_0x490
[ 0x00054d50 ] gEfiShellEnvironment2Guid_0x54d50
[ 0x000098f0 ] gEfiShellInterfaceGuid_0x98f0
[ 0x00008dd0 ] ProprietaryProtocol_0x8dd0
[ 0x00000460 ] gEfiSimpleTextInProtocolGuid_0x460
[ 0x00000470 ] gEfiSimpleTextOutProtocolGuid_0x470
[ 0x000005a0 ] gEfiLoadedImageProtocolGuid_0x5a0
[ 0x00000580 ] gEfiDevicePathProtocolGuid_0x580
[ 0x000098f0 ] gEfiShellInterfaceGuid_0x98f0
[ 0x00054d50 ] gEfiShellEnvironment2Guid_0x54d50
[ 0x00000590 ] gEfiSimpleFileSystemProtocolGuid_0x590
[ 0x00054d50 ] gEfiShellEnvironment2Guid_0x54d50
[ 0x000098f0 ] gEfiShellInterfaceGuid_0x98f0
[ 0x00000490 ] gEfiHiiStringProtocolGuid_0x490
[ 0x00054d50 ] gEfiShellEnvironment2Guid_0x54d50
[ 0x000098f0 ] gEfiShellInterfaceGuid_0x98f0
[ 0x00008dd0 ] ProprietaryProtocol_0x8dd0
[ 0x00000460 ] gEfiSimpleTextInProtocolGuid_0x460
[ 0x00000470 ] gEfiSimpleTextOutProtocolGuid_0x470
[ 0x000005a0 ] gEfiLoadedImageProtocolGuid_0x5a0
[ 0x00000580 ] gEfiDevicePathProtocolGuid_0x580
[ 0x000098f0 ] gEfiShellInterfaceGuid_0x98f0
[ 0x00054d50 ] gEfiShellEnvironment2Guid_0x54d50
[ 0x00000590 ] gEfiSimpleFileSystemProtocolGuid_0x590
Types:
[ 0x00065662 ] EFI_BOOT_SERVICES->LocateHandleBuffer
	 address: 0x000b8120
	 message: type successfully applied
[ 0x00067863 ] EFI_BOOT_SERVICES->LocateHandleBuffer
	 address: 0x000b8130
	 message: type successfully applied
[ 0x000678bc ] EFI_BOOT_SERVICES->OpenProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x00065785 ] EFI_BOOT_SERVICES->UninstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x00065de5 ] EFI_BOOT_SERVICES->UninstallProtocolInterface
	 address: 0x000b8120
	 message: type already applied
[ 0x00066d2d ] EFI_BOOT_SERVICES->UninstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x00066d96 ] EFI_BOOT_SERVICES->UninstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x0006d38b ] EFI_BOOT_SERVICES->UninstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x00066cf6 ] EFI_BOOT_SERVICES->InstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x00067cbd ] EFI_BOOT_SERVICES->InstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x0006ebc1 ] EFI_BOOT_SERVICES->InstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x00067dcb ] EFI_BOOT_SERVICES->ProtocolsPerHandle
	 address: 0x000b8120
	 message: type already applied
[ 0x00065819 ] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
	 address: 0x000b8130
	 message: type already applied
[ 0x000659eb ] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
	 address: 0x000b8130
	 message: type already applied
[ 0x00065791 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x00066e09 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x00066e44 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x0006d048 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x0006d145 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x0006d183 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x0006ec23 ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x0007274e ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x0007287e ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x00072a3a ] EFI_BOOT_SERVICES->ReinstallProtocolInterface
	 address: 0x000b8130
	 message: type already applied
[ 0x0006534e ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x00065abb ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x00065b7f ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x00065bac ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x000677ee ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x00067b2d ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x00067b69 ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x00067c30 ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x00067ccb ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x00067d10 ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x0006ce41 ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x0006ce7a ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x0006d1ba ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x0006ebfe ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x000a0df8 ] EFI_BOOT_SERVICES->HandleProtocol
	 address: 0x000b8130
	 message: type already applied
[ 0x000690b0 ] EFI_BOOT_SERVICES->OpenProtocolInformation
	 address: 0x000b8120
	 message: type already applied
```
