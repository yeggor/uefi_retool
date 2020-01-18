# UEFI_RETool

## Table of Contents

- [IDA plugin](#ida-plugin)
- [IDAPython analyser script](#idapython-analyser-script)
- [r2pipe analyser script](#r2pipe-analyser-script)
- [Finding proprietary protocols in UEFI firmware with IDA Pro](#finding-proprietary-protocols-in-uefi-firmware-with-ida-pro)
- [Finding proprietary protocols in UEFI firmware with radare2](#finding-proprietary-protocols-in-uefi-firmware-with-radare2)
- [Additional tools](#additional-tools)
- [Similar works](#similar-works)
- [Contributors](#contributors)

# IDA plugin

[IDA plugin for UEFI analysis](https://github.com/yeggor/UEFI_RETool/tree/master/ida_plugin)

# IDAPython analyser script

[ida_plugin/uefi_analyser/analyser.py](https://github.com/yeggor/UEFI_RETool/blob/master/ida_plugin/uefi_analyser/analyser.py) is a script for simplifying reverse engineering of UEFI firmware modules with IDA Pro

Usage:

 * Open the UEFI module in IDA Pro
 * Run `pip install -r requirements.txt`
 * Run `analyser.py` script from IDA
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

 * Examples is [here](https://github.com/yeggor/UEFI_RETool/blob/master/log/examples/analyser_output.md)

In result:

 * Before analysis:

    ![before_analysis](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/before_analysis.png)

 * After analysis:

    ![after_analysis](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/after_analysis.png)

# r2pipe analyser script

[r2_uefi_re/analyser.py](https://github.com/yeggor/UEFI_RETool/blob/master/r2_uefi_re/analyser.py) is a script with similar functionality based on r2pipe

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

# Finding proprietary protocols in UEFI firmware with IDA Pro

[analyse_fw_ida.py](https://github.com/yeggor/UEFI_RETool/blob/master/analyse_fw_ida.py) is a script for finding proprietary protocols in UEFI firmware with IDA Pro

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
```

*Examples of logs can be viewed at the following links: [log_all](https://github.com/yeggor/UEFI_RETool/blob/master/log/examples/ida_log_all_tpt480s.md), [log_pp_guids](https://github.com/yeggor/UEFI_RETool/blob/master/log/examples/ida_log_pp_guids_tpt480s.md)*

# Finding proprietary protocols in UEFI firmware with radare2

[analyse_fw_r2.py](https://github.com/yeggor/UEFI_RETool/blob/master/analyse_fw_r2.py) is a similar script for UEFI firmware analysis with radare2

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
```

# Additional tools

 * `tools\get_efi_images.py` is a script that gets all PE-images from the firmware file
 * `tools\update_edk2_guids.py` is a script that updates protocol GUIDs list from the `conf` directory

# Similar works

 * [ida-efiutils](https://github.com/snare/ida-efiutils)
 * [EFISwissKnife](https://github.com/gdbinit/EFISwissKnife)

# Contributors

 * yeggor (vasilenko.yegor@gmail.com)
 * p41l (philka9498@gmail.com)
