# UEFI_RETool
### To analyse your UEFI firmware:
 * Copy "ida_uefi_re" directory to <IDA_DIRECTORY>
 * Define path to firmware file in `config.json` file
 * Define path to `ida.exe` and `ida64.exe` in `config.json` file
 * Run `python analyse_fw.py`
 * Check `log` directory
    - example: `log\result_log_all_tpx1c.log`
### Configuration file content (`config.json`):
 * "FW_PATH" is a path to your firmware file for analysis
 * "PE_DIR" is a folder that consist all PE-images from firmware file
 * "IDA_PATH" and "IDA64_PATH" are paths to IDA's executable files
### Additional tools
 * `tools\get_efi_images.py` is a script to get all PE-images from firmware file
    - usage: `python C:\Work\Github\UEFI_RETool\tools\get_efi_images.py <FIRMWARE_FILE_NAME>`
    - by default files are dumped into the "PE_DIR" directory
 * `tools\update_edk2_guids.py` is a script to update protocol GUIDs list from `conf` directory
    - usage: `python C:\Work\Github\UEFI_RETool\tools\update_edk2_guids.py <EDK2_PATH>`
    - current version of EDK2 your can get from https://github.com/tianocore/edk2