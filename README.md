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
| 0x000002c8 | LocateHandleBuffer                  |
| 0x000005a0 | OpenProtocol                        |
| 0x00000856 | OpenProtocol                        |
| 0x00000a07 | OpenProtocol                        |
| 0x00000c74 | OpenProtocol                        |
| 0x00000d63 | OpenProtocol                        |
| 0x00003520 | OpenProtocol                        |
| 0x00003eba | OpenProtocol                        |
| 0x0000506e | OpenProtocol                        |
| 0x000050bd | OpenProtocol                        |
| 0x00005dbb | OpenProtocol                        |
| 0x00000368 | UninstallProtocolInterface          |
| 0x000003b1 | UninstallProtocolInterface          |
| 0x000003fa | UninstallProtocolInterface          |
| 0x00000a9a | UninstallProtocolInterface          |
| 0x00000e04 | UninstallProtocolInterface          |
| 0x00000c9b | UninstallMultipleProtocolInterfaces |
| 0x00000565 | InstallMultipleProtocolInterfaces   |
| 0x000008f0 | InstallMultipleProtocolInterfaces   |
| 0x00000c17 | InstallMultipleProtocolInterfaces   |
| 0x00000300 | HandleProtocol                      |
| 0x0000038a | HandleProtocol                      |
| 0x000003d3 | HandleProtocol                      |
| 0x0000048d | HandleProtocol                      |
| 0x00000470 | LocateProtocol                      |
| 0x0000098b | OpenProtocolInformation             |
| 0x00003e37 | OpenProtocolInformation             |
| 0x00000dda | CloseProtocol                       |
| 0x00000e9f | CloseProtocol                       |
| 0x00003783 | CloseProtocol                       |
| 0x00003b35 | CloseProtocol                       |
| 0x0000511b | CloseProtocol                       |
| 0x00005213 | CloseProtocol                       |
| 0x00005252 | CloseProtocol                       |
+------------+-------------------------------------+
Protocols:
+--------------------------------------------+-------------------------------------+------------+-------------------------------------+----------------+
| GUID                                       | Protocol name                       | Address    | Service                             | Protocol place |
+--------------------------------------------+-------------------------------------+------------+-------------------------------------+----------------+
| 6414F083-BD99-E545-B3-83-AF-63-00-D8-E9-E6 | gEfiUdp4ServiceBindingProtocolGuid  | 0x000067a0 | OpenProtocol                        | edk2_guids     |
| D8399A9D-42BD-734A-A4-D5-8E-E9-4B-E1-13-80 | gEfiDhcp4ServiceBindingProtocolGuid | 0x00006790 | OpenProtocol                        | edk2_guids     |
| 29DFD93A-0145-8D47-B1-F8-7F-7F-E7-00-50-F3 | gEfiUdp4ProtocolGuid                | 0x000067c0 | OpenProtocol                        | edk2_guids     |
| 1897218A-F54E-6147-91-C8-C0-F0-4B-DA-9E-56 | gEfiDhcp4ProtocolGuid               | 0x000067b0 | OpenProtocol                        | edk2_guids     |
| AB31A018-43B4-1A4D-A5-C0-00-00-26-1E-9F-71 | gEfiDriverBindingProtocolGuid       | 0x00006800 | UninstallProtocolInterface          | edk2_guids     |
| 2C777A10-E1D5-D411-9A-46-00-90-27-3F-C1-4D | gEfiComponentNameProtocolGuid       | 0x00006810 | UninstallProtocolInterface          | edk2_guids     |
| FF5C7A6A-D9E8-704F-BA-DA-75-AB-30-25-CE-14 | gEfiComponentName2ProtocolGuid      | 0x00006820 | UninstallProtocolInterface          | edk2_guids     |
| D8399A9D-42BD-734A-A4-D5-8E-E9-4B-E1-13-80 | gEfiDhcp4ServiceBindingProtocolGuid | 0x00006790 | UninstallProtocolInterface          | edk2_guids     |
| 1897218A-F54E-6147-91-C8-C0-F0-4B-DA-9E-56 | gEfiDhcp4ProtocolGuid               | 0x000067b0 | UninstallProtocolInterface          | edk2_guids     |
| 1897218A-F54E-6147-91-C8-C0-F0-4B-DA-9E-56 | gEfiDhcp4ProtocolGuid               | 0x000067b0 | UninstallMultipleProtocolInterfaces | edk2_guids     |
| 1897218A-F54E-6147-91-C8-C0-F0-4B-DA-9E-56 | gEfiDhcp4ProtocolGuid               | 0x000067b0 | InstallMultipleProtocolInterfaces   | edk2_guids     |
| AB31A018-43B4-1A4D-A5-C0-00-00-26-1E-9F-71 | gEfiDriverBindingProtocolGuid       | 0x00006800 | HandleProtocol                      | edk2_guids     |
| 2C777A10-E1D5-D411-9A-46-00-90-27-3F-C1-4D | gEfiComponentNameProtocolGuid       | 0x00006810 | HandleProtocol                      | edk2_guids     |
| FF5C7A6A-D9E8-704F-BA-DA-75-AB-30-25-CE-14 | gEfiComponentName2ProtocolGuid      | 0x00006820 | HandleProtocol                      | edk2_guids     |
| A1311B5B-6295-D211-8E-3F-00-A0-C9-69-72-3B | gEfiLoadedImageProtocolGuid         | 0x00006830 | HandleProtocol                      | edk2_guids     |
| 29DFD93A-0145-8D47-B1-F8-7F-7F-E7-00-50-F3 | gEfiUdp4ProtocolGuid                | 0x000067c0 | OpenProtocolInformation             | edk2_guids     |
| 29DFD93A-0145-8D47-B1-F8-7F-7F-E7-00-50-F3 | gEfiUdp4ProtocolGuid                | 0x000067c0 | CloseProtocol                       | edk2_guids     |
| 1588944F-B9B4-CB43-8A-33-90-E0-60-B3-49-55 | gEfiUdp6ProtocolGuid                | 0x000067e0 | CloseProtocol                       | edk2_guids     |
+--------------------------------------------+-------------------------------------+------------+-------------------------------------+----------------+
```

*Example №2*

```
Python>analyser.analyse_all()
Comments:
[0x000002c8] EFI_BOOT_SERVICES->LocateHandleBuffer
[0x000005a0] EFI_BOOT_SERVICES->OpenProtocol
[0x00000856] EFI_BOOT_SERVICES->OpenProtocol
[0x00000a07] EFI_BOOT_SERVICES->OpenProtocol
[0x00000c74] EFI_BOOT_SERVICES->OpenProtocol
[0x00000d63] EFI_BOOT_SERVICES->OpenProtocol
[0x00003520] EFI_BOOT_SERVICES->OpenProtocol
[0x00003eba] EFI_BOOT_SERVICES->OpenProtocol
[0x0000506e] EFI_BOOT_SERVICES->OpenProtocol
[0x000050bd] EFI_BOOT_SERVICES->OpenProtocol
[0x00005dbb] EFI_BOOT_SERVICES->OpenProtocol
[0x00000368] EFI_BOOT_SERVICES->UninstallProtocolInterface
[0x000003b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
[0x000003fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
[0x00000a9a] EFI_BOOT_SERVICES->UninstallProtocolInterface
[0x00000e04] EFI_BOOT_SERVICES->UninstallProtocolInterface
[0x00000c9b] EFI_BOOT_SERVICES->UninstallMultipleProtocolInterfaces
[0x00000565] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
[0x000008f0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
[0x00000c17] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
[0x00000300] EFI_BOOT_SERVICES->HandleProtocol
[0x0000038a] EFI_BOOT_SERVICES->HandleProtocol
[0x000003d3] EFI_BOOT_SERVICES->HandleProtocol
[0x0000048d] EFI_BOOT_SERVICES->HandleProtocol
[0x00000470] EFI_BOOT_SERVICES->LocateProtocol
[0x0000098b] EFI_BOOT_SERVICES->OpenProtocolInformation
[0x00003e37] EFI_BOOT_SERVICES->OpenProtocolInformation
[0x00000dda] EFI_BOOT_SERVICES->CloseProtocol
[0x00000e9f] EFI_BOOT_SERVICES->CloseProtocol
[0x00003783] EFI_BOOT_SERVICES->CloseProtocol
[0x00003b35] EFI_BOOT_SERVICES->CloseProtocol
[0x0000511b] EFI_BOOT_SERVICES->CloseProtocol
[0x00005213] EFI_BOOT_SERVICES->CloseProtocol
[0x00005252] EFI_BOOT_SERVICES->CloseProtocol
Names:
[0x000067a0] gEfiUdp4ServiceBindingProtocolGuid_0x67a0
[0x00006790] gEfiDhcp4ServiceBindingProtocolGuid_0x6790
[0x000067c0] gEfiUdp4ProtocolGuid_0x67c0
[0x000067b0] gEfiDhcp4ProtocolGuid_0x67b0
[0x00006800] gEfiDriverBindingProtocolGuid_0x6800
[0x00006810] gEfiComponentNameProtocolGuid_0x6810
[0x00006820] gEfiComponentName2ProtocolGuid_0x6820
[0x00006790] gEfiDhcp4ServiceBindingProtocolGuid_0x6790
[0x000067b0] gEfiDhcp4ProtocolGuid_0x67b0
[0x000067b0] gEfiDhcp4ProtocolGuid_0x67b0
[0x000067b0] gEfiDhcp4ProtocolGuid_0x67b0
[0x00006800] gEfiDriverBindingProtocolGuid_0x6800
[0x00006810] gEfiComponentNameProtocolGuid_0x6810
[0x00006820] gEfiComponentName2ProtocolGuid_0x6820
[0x00006830] gEfiLoadedImageProtocolGuid_0x6830
[0x000067c0] gEfiUdp4ProtocolGuid_0x67c0
[0x000067c0] gEfiUdp4ProtocolGuid_0x67c0
[0x000067e0] gEfiUdp6ProtocolGuid_0x67e0
[0x000067a0] gEfiUdp4ServiceBindingProtocolGuid_0x67a0
[0x00006790] gEfiDhcp4ServiceBindingProtocolGuid_0x6790
[0x000067c0] gEfiUdp4ProtocolGuid_0x67c0
[0x000067b0] gEfiDhcp4ProtocolGuid_0x67b0
[0x00006800] gEfiDriverBindingProtocolGuid_0x6800
[0x00006810] gEfiComponentNameProtocolGuid_0x6810
[0x00006820] gEfiComponentName2ProtocolGuid_0x6820
[0x00006790] gEfiDhcp4ServiceBindingProtocolGuid_0x6790
[0x000067b0] gEfiDhcp4ProtocolGuid_0x67b0
[0x000067b0] gEfiDhcp4ProtocolGuid_0x67b0
[0x000067b0] gEfiDhcp4ProtocolGuid_0x67b0
[0x00006800] gEfiDriverBindingProtocolGuid_0x6800
[0x00006810] gEfiComponentNameProtocolGuid_0x6810
[0x00006820] gEfiComponentName2ProtocolGuid_0x6820
[0x00006830] gEfiLoadedImageProtocolGuid_0x6830
[0x000067c0] gEfiUdp4ProtocolGuid_0x67c0
[0x000067c0] gEfiUdp4ProtocolGuid_0x67c0
[0x000067e0] gEfiUdp6ProtocolGuid_0x67e0
Types:
[0x000002c8] EFI_BOOT_SERVICES->LocateHandleBuffer
	 [address] 0x000078f8
	 [message] type already applied
[0x000005a0] EFI_BOOT_SERVICES->OpenProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x00000856] EFI_BOOT_SERVICES->OpenProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x00000a07] EFI_BOOT_SERVICES->OpenProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x00000c74] EFI_BOOT_SERVICES->OpenProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x00000d63] EFI_BOOT_SERVICES->OpenProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x00003520] EFI_BOOT_SERVICES->OpenProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x00003eba] EFI_BOOT_SERVICES->OpenProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x0000506e] EFI_BOOT_SERVICES->OpenProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x000050bd] EFI_BOOT_SERVICES->OpenProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x00005dbb] EFI_BOOT_SERVICES->OpenProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x00000368] EFI_BOOT_SERVICES->UninstallProtocolInterface
	 [address] 0x000078f8
	 [message] type already applied
[0x000003b1] EFI_BOOT_SERVICES->UninstallProtocolInterface
	 [address] 0x000078f8
	 [message] type already applied
[0x000003fa] EFI_BOOT_SERVICES->UninstallProtocolInterface
	 [address] 0x000078f8
	 [message] type already applied
[0x00000a9a] EFI_BOOT_SERVICES->UninstallProtocolInterface
	 [address] 0x000078f8
	 [message] type already applied
[0x00000e04] EFI_BOOT_SERVICES->UninstallProtocolInterface
	 [address] 0x000078f8
	 [message] type already applied
[0x00000565] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
	 [address] 0x000078f8
	 [message] type already applied
[0x000008f0] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
	 [address] 0x000078f8
	 [message] type already applied
[0x00000c17] EFI_BOOT_SERVICES->InstallMultipleProtocolInterfaces
	 [address] 0x000078f8
	 [message] type already applied
[0x00000300] EFI_BOOT_SERVICES->HandleProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x0000038a] EFI_BOOT_SERVICES->HandleProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x000003d3] EFI_BOOT_SERVICES->HandleProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x0000048d] EFI_BOOT_SERVICES->HandleProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x0000098b] EFI_BOOT_SERVICES->OpenProtocolInformation
	 [address] 0x000078f8
	 [message] type already applied
[0x00003e37] EFI_BOOT_SERVICES->OpenProtocolInformation
	 [address] 0x000078f8
	 [message] type already applied
[0x00000e9f] EFI_BOOT_SERVICES->CloseProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x00003783] EFI_BOOT_SERVICES->CloseProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x00003b35] EFI_BOOT_SERVICES->CloseProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x0000511b] EFI_BOOT_SERVICES->CloseProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x00005213] EFI_BOOT_SERVICES->CloseProtocol
	 [address] 0x000078f8
	 [message] type already applied
[0x00005252] EFI_BOOT_SERVICES->CloseProtocol
	 [address] 0x000078f8
	 [message] type already applied
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

 * Copy `ida_uefi_re` directory to <IDA_DIRECTORY>
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