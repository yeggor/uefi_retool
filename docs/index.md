# UEFI_RETool

A tool for finding proprietary protocols in UEFI firmware and UEFI modules analysing

## `ida_uefi_re\analyser.py`

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
┌─────────┬──────────────────────────┐
│ Address │ Service                  │
├─────────┼──────────────────────────┤
│ 0x250aL │ InstallProtocolInterface │
│ 0xbabL  │ HandleProtocol           │
│ 0xbcdL  │ HandleProtocol           │
│ 0xbfbL  │ HandleProtocol           │
│ 0xd84L  │ LocateProtocol           │
│ 0xde7L  │ LocateProtocol           │
│ 0xe05L  │ LocateProtocol           │
│ 0xe23L  │ LocateProtocol           │
│ 0xe4aL  │ LocateProtocol           │
│ 0xed5L  │ LocateProtocol           │
└─────────┴──────────────────────────┘
Protocols:
┌────────────────────────────────────────────────────────────────────┬─────────────────────────────┬─────────┬────────────────┬────────────────┐
│ GUID                                                               │ Protocol name               │ Address │ Service        │ Protocol place │
├────────────────────────────────────────────────────────────────────┼─────────────────────────────┼─────────┼────────────────┼────────────────┤
│ [0x6378fef3-0xc89f-0x492f-0xbd-0xb1-0xbf-0xb4-0x43-0x19-0xcf-0xda] │ ProprietaryProtocol         │ 0x678L  │ HandleProtocol │ unknown        │
│ [0x4c8a2451-0xc207-0x405b-0x96-0x94-0x99-0xea-0x13-0x25-0x13-0x41] │ gEfiDebugMaskProtocolGuid   │ 0x658L  │ HandleProtocol │ edk2_guids     │
│ [0x5b1b31a1-0x9562-0x11d2-0x8e-0x3f-0x0-0xa0-0xc9-0x69-0x72-0x3b]  │ gEfiLoadedImageProtocolGuid │ 0x628L  │ HandleProtocol │ edk2_guids     │
│ [0xcd2333d7-0x6a0a-0x4c76-0x83-0x50-0x24-0xa-0xda-0x36-0xa2-0xc7]  │ ProprietaryProtocol         │ 0x6f0L  │ LocateProtocol │ unknown        │
│ [0xae80d021-0x618e-0x11d4-0xbc-0xd7-0x0-0x80-0xc7-0x3c-0x88-0x81]  │ gEfiDataHubProtocolGuid     │ 0x6c0L  │ LocateProtocol │ edk2_guids     │
│ [0xe49d33ed-0x513d-0x4634-0xb6-0x98-0x6f-0x55-0xaa-0x75-0x1c-0x1b] │ gEfiSmbusHcProtocolGuid     │ 0x6b0L  │ LocateProtocol │ edk2_guids     │
│ [0xef9fc172-0xa1b2-0x4693-0xb3-0x27-0x6d-0x32-0xfc-0x41-0x60-0x42] │ gEfiHiiDatabaseProtocolGuid │ 0x648L  │ LocateProtocol │ edk2_guids     │
│ [0xfd96974-0x23aa-0x4cdc-0xb9-0xcb-0x98-0xd1-0x77-0x50-0x32-0x2a]  │ gEfiHiiStringProtocolGuid   │ 0x638L  │ LocateProtocol │ edk2_guids     │
└────────────────────────────────────────────────────────────────────┴─────────────────────────────┴─────────┴────────────────┴────────────────┘
```

*Example №2*

```
Python>analyser.analyse_all()
Comments:
[0x250aL] EFI_BOOT_SERVICES->InstallProtocolInterface
[0xbabL] EFI_BOOT_SERVICES->HandleProtocol
[0xbcdL] EFI_BOOT_SERVICES->HandleProtocol
[0xbfbL] EFI_BOOT_SERVICES->HandleProtocol
[0xd84L] EFI_BOOT_SERVICES->LocateProtocol
[0xde7L] EFI_BOOT_SERVICES->LocateProtocol
[0xe05L] EFI_BOOT_SERVICES->LocateProtocol
[0xe23L] EFI_BOOT_SERVICES->LocateProtocol
[0xe4aL] EFI_BOOT_SERVICES->LocateProtocol
[0xed5L] EFI_BOOT_SERVICES->LocateProtocol
Names:
[0x678L] ProprietaryProtocol_0x678L
[0x658L] gEfiDebugMaskProtocolGuid_0x658L
[0x628L] gEfiLoadedImageProtocolGuid_0x628L
[0x6f0L] ProprietaryProtocol_0x6f0L
[0x6c0L] gEfiDataHubProtocolGuid_0x6c0L
[0x6b0L] gEfiSmbusHcProtocolGuid_0x6b0L
[0x648L] gEfiHiiDatabaseProtocolGuid_0x648L
[0x638L] gEfiHiiStringProtocolGuid_0x638L
Types:
[0xde7] EFI_BOOT_SERVICES->LocateProtocol
	 [address] 0x3170
	 [message] type successfully applied
[0xe05] EFI_BOOT_SERVICES->LocateProtocol
	 [address] 0x3170
	 [message] type already applied
[0xe23] EFI_BOOT_SERVICES->LocateProtocol
	 [address] 0x3170
	 [message] type already applied
[0xe4a] EFI_BOOT_SERVICES->LocateProtocol
	 [address] 0x3170
	 [message] type already applied
[0xed5] EFI_BOOT_SERVICES->LocateProtocol
	 [address] 0x3170
	 [message] type already applied
```

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

## TODO
 * Add support for 32-bit executable images

## Contributors

 * yeggor (vasilenko.yegor@gmail.com)
 * p41l (philka9498@gmail.com)