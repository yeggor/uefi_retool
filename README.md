![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg)
![Python Versions](https://img.shields.io/pypi/pyversions/yt2mp3.svg)
![Version](https://img.shields.io/badge/version-1.2.0-blue)

# [UEFI_RETool](https://github.com/yeggor/UEFI_RETool)

A tool for UEFI firmware reverse engineering.

# Table of Contents

<details>
 <summary>Click to open TOC</summary>
<!-- MarkdownTOC autolink="true" bracket="round" style="unordered" indent="  " autoanchor="false" markdown_preview="github" -->

- [UEFI firmware analysis with uefi_retool.py script](#uefi-firmware-analysis-with-uefi_retoolpy-script)
  - [Commands](#commands)
  - [get-images](#get-images)
  - [get-info](#get-info)
  - [get-pp](#get-pp)
- [Additional tools](#additional-tools)
- [IDA plugin](#ida-plugin)
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
- [Similar works](#similar-works)
- [Contributors](#contributors)

<!-- /MarkdownTOC -->
</details>

# UEFI firmware analysis with [uefi_retool.py](https://github.com/yeggor/UEFI_RETool/blob/master/uefi_retool.py) script

Usage:

 * Copy `ida_plugin/uefi_analyser.py` script and `ida_plugin/uefi_analyser` directory to IDA plugins directory
 * Edit `config.json` file
    - `PE_DIR` is a directory that contains all executable images from the UEFI firmware
    - `DUMP_DIR` is a directory that contains all components from the firmware filesystem
    - `LOGS_DIR` is a directory for logs
    - `IDA_PATH` and `IDA64_PATH` are paths to IDA Pro executable files
 * Run `pip install -r requirements.txt`
 * Run `python uefi_retool.py` command to display the help message

## Commands

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

## get-images

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

## get-info

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

## get-pp

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

# Additional tools

* `tools/update_edk2_guids.py` is a script that updates protocol GUIDs list from the conf directory

# IDA plugin

[IDA plugin for UEFI analysis](https://github.com/yeggor/UEFI_RETool/tree/master/ida_plugin)

## Analyser & Protocol explorer

### Usage
  
  * Copy `uefi_analyser` and `uefi_analyser.py` to your `%IDA_DIR%/plugins` directory
 
  * Open the executable UEFI image in IDA and go to `Edit` -> `Plugins` -> `UEFI analyser` *(alternatively, you can use the key combination `Ctrl+Alt+U`)*

### Example

#### Before analysis

![before_analysis](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/before_analysis.png)

#### After analysis

![after_analysis](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/after_analysis.png)

#### Protocol explorer window

![protocols](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/protocols.png)

## Dependency browser & Dependency graph

### Usage

  * Analyse the firmware using [uefi_retool.py](https://github.com/yeggor/UEFI_RETool/blob/master/uefi_retool.py)

      ```bash
      python uefi_retool.py get-info FIRMWARE_PATH
      ```

   * Load `<LOGS_DIR>/<FIRMWARE_NAME>-all-info.json` file to IDA (`File` -> `UEFI_RETool...`)

      ![db-usage](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/db-usage.png)

      *alternatively, you can use the key combination `Ctrl+Alt+J`*)

### Example

#### Dependency browser window

![db-usage](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/depend-browser.png)

#### Dependency graph

![db-graph](https://raw.githubusercontent.com/yeggor/UEFI_RETool/master/img/depend-graph.png)


# Similar works

 * [ida-efiutils](https://github.com/snare/ida-efiutils)
 * [EFISwissKnife](https://github.com/gdbinit/EFISwissKnife)

# Contributors

 * yeggor (vasilenko.yegor@gmail.com)
 * p41l (philka9498@gmail.com)
