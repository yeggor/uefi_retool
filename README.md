## Table of Contents

- [UEFI_RETool](#uefiretool)
- [IDA plugin](#ida-plugin)
- [UEFI firmware analysis with IDA Pro](#uefi-firmware-analysis-with-ida-pro)
- [UEFI firmware analysis with radare2](#uefi-firmware-analysis-with-radare2)
- [Additional tools](#additional-tools)
- [Similar works](#similar-works)
- [Contributors](#contributors)

# UEFI_RETool

A tool for UEFI firmware reverse engineering.

The tool consists of a plugin for IDA and a set of scripts for UEFI firmware analysing.

# IDA plugin

[IDA plugin for UEFI analysis](https://github.com/yeggor/UEFI_RETool/tree/master/ida_plugin)

# UEFI firmware analysis with IDA Pro

[analyse_fw_ida.py](https://github.com/yeggor/UEFI_RETool/blob/master/analyse_fw_ida.py) is a script for UEFI firmware analysis with IDA Pro

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

# UEFI firmware analysis with radare2

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
