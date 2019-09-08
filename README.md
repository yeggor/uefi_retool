# [UEFI_RETool](https://yeggor.github.io/UEFI_RETool/)

A tool for finding proprietary protocols in UEFI firmware and UEFI modules analysing

## `ida_plugin`

[IDA plugin for UEFI analysis](https://github.com/yeggor/UEFI_RETool/tree/master/ida_plugin)

## `ida_plugin\uefi_analyser\analyser.py`

A script for simplifying reverse engineering of UEFI firmware modules with IDA Pro

Usage:

 * Open the UEFI module in IDA Pro
 * Run `pip install -r requirements.txt`
 * Run script from IDA
 * Run following commands in output window:

```
    Python>analyser = Analyser()
    Python>analyser.help()
```

```
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
```

 * Then run the necessary command from the list

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

*In result*

 * Before analysis:

    ![before_analysis](https://github.com/yeggor/UEFI_RETool/blob/master/img/before_analysis.png)

 * After analysis:

    ![after_analysis](https://github.com/yeggor/UEFI_RETool/blob/master/img/after_analysis.png)

## `r2_uefi_re\analyser.py`

A script with similar functionality based on r2pipe

Usage:

* Run `pip install -r requirements.txt`
* Run `python r2_uefi_re\analyser.py -h`

```
UEFI_RETool
A tool for UEFI module analysis with radare2
usage: python analyser.py [-h] module

UEFI module analyser

positional arguments:
  module      path to UEFI module

optional arguments:
  -h, --help  show this help message and exit
```
```
>python r2_uefi_re\analyser.py modules\DxeMain.efi
UEFI_RETool
A tool for UEFI module analysis with radare2
Boot services:
┌─────────┬──────────────────────────┐
│ Address │ Service                  │
├─────────┼──────────────────────────┤
│ 0x15fef │ LocateHandleBuffer       │
│ 0x1c30f │ OpenProtocol             │
│ 0x1bec7 │ OpenProtocol             │
│ 0x1603c │ OpenProtocol             │
│ 0x1c9af │ InstallProtocolInterface │
│ 0x1c2dd │ HandleProtocol           │
│ 0x1c33a │ HandleProtocol           │
│ 0x1bf98 │ HandleProtocol           │
│ 0x1c9fd │ HandleProtocol           │
│ 0x1be95 │ HandleProtocol           │
│ 0x1bef2 │ HandleProtocol           │
│ 0x12f2f │ LocateProtocol           │
│ 0x1c7b0 │ LocateProtocol           │
│ 0x1c744 │ LocateProtocol           │
└─────────┴──────────────────────────┘
Protocols:
┌────────────────────────────────────────────────────────────────────┬───────────────────────────────┬─────────┬──────────────────────────┬────────────────┐
│ GUID                                                               │ Protocol name                 │ Address │ Service                  │ Protocol place │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────┼─────────┼──────────────────────────┼────────────────┤
│ [0x18a031ab-0xb443-0x4d1a-0xa5-0xc0-0xc-0x9-0x26-0x1e-0x9f-0x71]   │ gEfiDriverBindingProtocolGuid │ 0x11410 │ LocateHandleBuffer       │ edk2_guids     │
│ [0x18a031ab-0xb443-0x4d1a-0xa5-0xc0-0xc-0x9-0x26-0x1e-0x9f-0x71]   │ gEfiDriverBindingProtocolGuid │ 0x11410 │ OpenProtocol             │ edk2_guids     │
│ [0x83485340-0x30ec-0x8b48-0x44-0x24-0x60-0x4d-0x8b-0xd1-0x4d-0x8b] │ ProprietaryProtocol           │ 0x1c6d4 │ InstallProtocolInterface │ unknown        │
│ [0x5b1b31a1-0x9562-0x11d2-0x8e-0x3f-0x0-0xa0-0xc9-0x69-0x72-0x3b]  │ gEfiLoadedImageProtocolGuid   │ 0x11440 │ HandleProtocol           │ edk2_guids     │
│ [0x9576e91-0x6d3f-0x11d2-0x8e-0x39-0x0-0xa0-0xc9-0x69-0x72-0x3b]   │ gEfiDevicePathProtocolGuid    │ 0x11400 │ HandleProtocol           │ edk2_guids     │
│ [0x26baccb1-0x6f42-0x11d4-0xbc-0xe7-0x0-0x80-0xc7-0x3c-0x88-0x81]  │ gEfiCpuArchProtocolGuid       │ 0x11520 │ LocateProtocol           │ edk2_guids     │
│ [0xffecffff-0x923c-0x14d2-0x9e-0x3f-0x22-0xa0-0xc9-0x69-0x56-0x3b] │ EFI_PERFORMANCE_PROTOCOL_GUID │ 0x11650 │ LocateProtocol           │ edk_guids      │
└────────────────────────────────────────────────────────────────────┴───────────────────────────────┴─────────┴──────────────────────────┴────────────────┘

```

## `analyse_fw_ida.py`

A script for finding proprietary protocols in UEFI firmware with IDA Pro

Usage:

 * Copy `ida_plugin\uefi_analyser` directory to IDA plugins directory
 * Edit `config.json` file
    - "PE_DIR" is a folder that contains all executable images from the UEFI firmware file
    - "DUMP_DIR" is a folder that contains all components from the firmware filesystem
    - "IDA_PATH" and "IDA64_PATH" are paths to IDA Pro executable files
 * Run `pip install -r requirements.txt`
 * Run `python analyse_fw_ida.py -h` command to display the help message

```
UEFI_RETool
A tool for UEFI firmware analysis with IDA Pro
usage: python analyse_fw_ida.py [-h] [--all] [--pp_guids] [--get_efi_images]
                                [--update_edk2_guids EDK2_PATH]
                                firmware_path

positional arguments:
  firmware_path         path to UEFI firmware for analysis

optional arguments:
  -h, --help            show this help message and exit
  --all                 analyse of all UEFI firmware modules and output of
                        information to .\log\ida_log_all.md file (example:
                        python analyse_fw_ida.py --all <firmware_path>)
  --pp_guids            analyse all UEFI firmware modules and save a table
                        with proprietry protocols to .\log\ida_pp_guids.md
                        file (example: python analyse_fw_ida.py --pp_guids
                        <firmware_path>)
  --get_efi_images      get all executable images from UEFI firmware (images
                        are stored in .\modules directory, example: python
                        analyse_fw_ida.py --get_efi_images <firmware_path>)
  --update_edk2_guids EDK2_PATH
                        update list of GUIDs from EDK2 (example: git clone
                        https://github.com/tianocore/edk2, python
                        analyse_fw_ida.py --update_edk2_guids edk2)
```

*Examples of logs can be viewed at the following links: [log_all](https://github.com/yeggor/UEFI_RETool/blob/master/log/examples/ida_log_all_tpx1c.md), [log_pp_guids](https://github.com/yeggor/UEFI_RETool/blob/master/log/examples/ida_log_pp_guids_tpx1c.md)*

## `analyse_fw_r2.py`

A similar script for UEFI firmware analysis with radare2

Usage:
 * Run `pip install -r requirements.txt`
 * Run `python analyse_fw_r2.py -h` command to display the help message

```
UEFI_RETool
A tool for UEFI firmware analysis with radare2
usage: python analyse_fw_r2.py [-h] [--all] [--pp_guids] [--pp_guids_num]
                               [--get_efi_images]
                               [--update_edk2_guids EDK2_PATH]
                               firmware_path

positional arguments:
  firmware_path         path to UEFI firmware for analysis

optional arguments:
  -h, --help            show this help message and exit
  --all                 analyse of all UEFI firmware modules and output of
                        information to .\log\r2_log_all.md file (example:
                        python analyse_fw_r2.py --all <firmware_path>)
  --pp_guids            analyse all UEFI firmware modules and save a table
                        with proprietary protocols to .\log\r2_pp_guids.md
                        file (example: python analyse_fw_r2.py --pp_guids
                        <firmware_path>)
  --pp_guids_num        analyse all UEFI firmware modules and get number of
                        proprietary protocols (example: python
                        analyse_fw_r2.py --pp_guids_num <firmware_path>)
  --get_efi_images      get all executable images from UEFI firmware (images
                        are stored in .\modules directory, example: python
                        analyse_fw_r2.py --get_efi_images <firmware_path>)
  --update_edk2_guids EDK2_PATH
                        update list of GUIDs from EDK2 (example: git clone
                        https://github.com/tianocore/edk2, python
                        analyse_fw_r2.py --update_edk2_guids edk2)
```

## Additional tools

 * `tools\get_efi_images.py` is a script that gets all PE-images from the firmware file
 * `tools\update_edk2_guids.py` is a script that updates protocol GUIDs list from the `conf` directory

## Similar works

 * [ida-efiutils](https://github.com/snare/ida-efiutils)
 * [EFISwissKnife](https://github.com/gdbinit/EFISwissKnife)

## Contributors

 * yeggor (vasilenko.yegor@gmail.com)
 * p41l (philka9498@gmail.com)