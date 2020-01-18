## [IDA plugin for UEFI analysis](https://github.com/yeggor/UEFI_RETool/tree/master/ida_plugin)

This plugin allows you to automatically analyse the input UEFI images, as well as search for dependencies between UEFI images in firmware.

## Table of Contents

- [Analyser & Protocol explorer](#analyser--protocol-explorer)
  - [Usage](#usage)
  - [Example](#example)
    - [Before analysis](#before-analysis)
    - [After analysis](#after-analysis)
    - [Protocol explorer window](#protocol-explorer-window)
- [Dependency browser & Dependency graph](#dependency-browser--dependency-graph)
  - [Usage](#usage-1)
  - [Example](#example-1)
    - [Dependency browser window](#dependency-browser-window)
    - [Dependency graph](#dependency-graph)

# Analyser & Protocol explorer

## Usage
  
  * Copy `uefi_analyser` and `uefi_analyser.py` to your `%IDA_DIR%/plugins` directory
 
  * Open the executable UEFI image in IDA and go to `Edit` -> `Plugins` -> `UEFI analyser` *(alternatively, you can use the key combination `Ctrl+Alt+U`)*

## Example

### Before analysis

![before_analysis](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/before_analysis.png)

### After analysis

![after_analysis](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/after_analysis.png)

### Protocol explorer window

![protocols](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/protocols.png)

# Dependency browser & Dependency graph

## Usage

  * Analyse the firmware using [analyse_fw_ida.py](https://github.com/yeggor/UEFI_RETool/blob/master/analyse_fw_ida.py) script with `--all` key

      ```bash
      UEFI_RETool
      A tool for UEFI firmware analysis with IDA Pro
      usage: python analyse_fw_ida.py [-h] [--all] [--pp_guids] [--get_efi_images]
                                    [--update_edk2_guids EDK2_PATH]
                                    firmware_path

      positional arguments:
      firmware_path           path to UEFI firmware for analysis

      optional arguments:
      -h, --help              show this help message and exit
      --all                   analyse of all UEFI firmware modules and output of
                              information to .\log\ida_log_all.md file (example:
                              python analyse_fw_ida.py --all <firmware_path>)
      --pp_guids              analyse all UEFI firmware modules and save a table
                              with proprietry protocols to .\log\ida_pp_guids.md
                              file (example: python analyse_fw_ida.py --pp_guids
                              <firmware_path>)
      --get_efi_images        get all executable images from UEFI firmware (images
                              are stored in .\modules directory, example: python
                              analyse_fw_ida.py --get_efi_images <firmware_path>)
      ```

   * Next to the `ida_log_all.md` file should be the `ida_log_all.json` file

   * Load `ida_log_all.json` file to IDA (`File` -> `UEFI_RETool...`)

      ![db-usage](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/db-usage.png)

      *alternatively, you can use the key combination `Ctrl+Alt+J`*)

## Example

### Dependency browser window

![db-usage](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/depend-browser.png)

### Dependency graph

![db-graph](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/depend-graph.png)
