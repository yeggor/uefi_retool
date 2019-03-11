# UEFI_RETool
### To analyse UEFI firmware with IDA pro:
 * Copy "ida_uefi_re" directory to <IDA_DIRECTORY>
 * Edit `config.json` file
 * Run `pip install -r requirements.txt`
 * Run `python analyse_fw_ida.py -h` and read `help` message
    ```
        UEFI_RETool
        A tool for UEFI firmware analysis with IDA Pro
        usage: python analyse_fw_ida.py [-h] [--all] [--pp_guids] [--get_efi_images]
                                        [--update_edk2_guids EDK2_PATH]
                                        firmware_path

        positional arguments:
        firmware_path         the path to UEFI firmware for analysis

        optional arguments:
        -h, --help            show this help message and exit
        --all                 analyse of all UEFI firmware modules and out
                              information to .\log\ida_log_all.md file (example:
                              python analyse_fw_ida.py --all <firmware_path>)
        --pp_guids            analyse all UEFI firmware modules and write a table
                              with proprietry protocols to .\log\ida_pp_guids.md
                              file (example: python analyse_fw_ida.py --pp_guids
                              <firmware_path>)
        --get_efi_images      get all executable images from UEFI firmware (images
                              are stores in .\modules directory, example: python
                              analyse_fw_ida.py --get_efi_images <firmware_path>)
        --update_edk2_guids EDK2_PATH
                              update list of GUIDs from EDK2 (example: git clone
                              https://github.com/tianocore/edk2, python
                              analyse_fw_ida.py --update_edk2_guids edk2)
    ```
### Configuration file content (`config.json`):
 * "PE_DIR" is a folder that consist all executable images from UEFI firmware file
 * "DUMP_DIR" is a folder that consist all components from firmware filesystem
 * "IDA_PATH" and "IDA64_PATH" are paths to IDA Pro executable files
### Additional tools:
 * `tools\get_efi_images.py` is a script to get all PE-images from firmware file
 * `tools\update_edk2_guids.py` is a script to update protocol GUIDs list from `conf` directory
### To analyse UEFI firmware with radare2:
 * Run `pip install -r requirements.txt`
 * Run `python analyse_fw_r2.py -h` and read `help` message
    ```
        UEFI_RETool
        A tool for full UEFI firmware analysis with radare2
        usage: python analyse_fw_r2.py [-h] [--all] [--pp_guids] firmware_path

        positional arguments:
        firmware_path  the path to UEFI firmware for analysis

        optional arguments:
        -h, --help     show this help message and exit
        --all          analyse of all UEFI firmware modules and out information to
                       .\log\r2_log_all.md file (example: python analyse_fw_r2.py
                       --all <firmware_path>)
        --pp_guids     analyse all UEFI firmware modules and write a table with
                       proprietry protocols to .\log\r2_pp_guids.md file (example:
                       python analyse_fw_r2.py --pp_guids <firmware_path>)
    ```
### Contributors:
 * yeggor (vasilenko.yegor@gmail.com) 
 * p41l (philka9498@gmail.com)

*Examples of logs can be viewed at the following links: [log_all](https://github.com/yeggor/UEFI_RETool/blob/master/log/examples/ida_log_all_tpx1c.md), [log_pp_guids](https://github.com/yeggor/UEFI_RETool/blob/master/log/examples/ida_log_pp_guids_tpx1c.md)*