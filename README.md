# uefi_retool

A tool for UEFI firmware reverse engineering.

## UEFI firmware analysis with uefi_retool script

Usage:

- Copy `ida_plugin/uefi_analyser.py` script and `ida_plugin/uefi_analyser` directory to IDA plugins directory
- Edit `config.json` file
  - `PE_DIR` is a directory that contains all executable images from the UEFI firmware
  - `DUMP_DIR` is a directory that contains all components from the firmware filesystem
  - `LOGS_DIR` is a directory for logs
  - `IDA_PATH` and `IDA64_PATH` are paths to IDA Pro executable files
- Run `pip install -r requirements.txt`
- Run `python uefi_retool.py` command to display the help message

### Commands

```bash
python uefi_retool.py
```

```
Usage: uefi_retool.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  get-images  Get executable images from UEFI firmware.
  get-info    Analyze the entire UEFI firmware.
  get-pp      Get a list of proprietary protocols in the UEFI firmware.
```

### get-images

```bash
python uefi_retool.py get-images --help
```

```
Usage: uefi_retool.py get-images [OPTIONS] FIRMWARE_PATH

  Get executable images from UEFI firmware. Images are stored in "modules"
  directory.

Options:
  --help  Show this message and exit.
```

Example:

```bash
python uefi_retool.py get-images test_fw/fw-tp-x1-carbon-5th.bin
```

### get-info

```bash
python uefi_retool.py get-info --help
```

```
Usage: uefi_retool.py get-info [OPTIONS] FIRMWARE_PATH

  Analyze the entire UEFI firmware. The analysis result is saved to .json
  file.

Options:
  -w, --workers INTEGER  Number of workers (8 by default).
  --help                 Show this message and exit.
```

Example:

```bash
python uefi_retool.py get-info -w 6 test_fw/fw-tp-x1-carbon-5th.bin
```

### get-pp

```bash
python uefi_retool.py get-pp --help
```

```
Usage: uefi_retool.py get-pp [OPTIONS] FIRMWARE_PATH

  Get a list of proprietary protocols in the UEFI firmware. The result is
  saved to .json file.

Options:
  -w, --workers INTEGER  Number of workers (8 by default).
  --help                 Show this message and exit.
```

Example:

```bash
python uefi_retool.py get-pp -w 6 test_fw/fw-tp-x1-carbon-5th.bin
```

## Additional tools

- `tools/update_edk2_guids.py` is a script that updates protocol GUIDs list from `edk2` project

## IDA plugin

[IDA plugin for UEFI analysis](https://github.com/yeggor/uefi_retool/tree/master/ida_plugin)

## Similar works

- [ida-efiutils](https://github.com/snare/ida-efiutils)
- [EFISwissKnife](https://github.com/gdbinit/EFISwissKnife)
- [ghidra-firmware-utils](https://github.com/al3xtjames/ghidra-firmware-utils)
