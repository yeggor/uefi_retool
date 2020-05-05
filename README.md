## [UEFI_RETool](https://github.com/yeggor/UEFI_RETool)

A tool for UEFI firmware reverse engineering.

## Table of Contents

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

 * Copy `ida_plugin\uefi_analyser` directory to IDA plugins directory
 * Edit `config-[win|nix].json` file
    - `PE_DIR` is a folder that contains all executable images from the UEFI firmware
    - `DUMP_DIR` is a folder that contains all components from the firmware filesystem
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

## get-info

```bash
python uefi_retool.py get-info --help
```

```
Usage: uefi_retool.py get-info [OPTIONS] FIRMWARE_PATH

  Analyze the entire UEFI firmware. The analysis result is saved to .md and
  .json files.

Options:
  --help  Show this message and exit.
```

## get-pp

```bash
python uefi_retool.py get-pp --help
```

```
Usage: uefi_retool.py get-pp [OPTIONS] FIRMWARE_PATH

  Get a list of proprietary protocols in the UEFI firmware. The result is
  saved to .md file.

Options:
  --help  Show this message and exit.
```

*Examples of logs can be viewed at the following links: [log_all](https://github.com/yeggor/UEFI_RETool/blob/master/log/examples/ida_log_all_tpt480s.md), [log_pp_guids](https://github.com/yeggor/UEFI_RETool/blob/master/log/examples/ida_log_pp_guids_tpt480s.md)*

# Additional tools

* `tools\update_edk2_guids.py` is a script that updates protocol GUIDs list from the conf directory

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
      uefi_retool.py get-info FIRMWARE_PATH
      ```

   * Next to the `ida_log_all.md` file should be the `ida_log_all.json` file

   * Load `ida_log_all.json` file to IDA (`File` -> `UEFI_RETool...`)

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
