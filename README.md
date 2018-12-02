# UEFI_RETool
### To analyse your UEFI firmware:
 * Copy "ida_uefi_re" directory to <IDA_DIRECTORY>
 * Edit `config.json` file
 * Run `pip install -r requirements.txt`
 * Run `python analyse_fw.py` and read `help` message
### Configuration file content (`config.json`):
 * "PE_DIR" is a folder that consist all PE-images from firmware file
 * "DUMP_DIR" is a folder that consist all firmware items
 * "IDA_PATH" and "IDA64_PATH" are paths to IDA's executable files
### Additional tools
 * `tools\get_efi_images.py` is a script to get all PE-images from firmware file
 * `tools\update_edk2_guids.py` is a script to update protocol GUIDs list from `conf` directory