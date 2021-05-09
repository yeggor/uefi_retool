## IDA plugin for UEFI analysis

This plugin allows you to automatically analyse the input UEFI images, as well as search for dependencies between UEFI images in firmware.

## Analyser & Protocol explorer

### Installation

Copy `uefi_analyser` and `uefi_analyser.py` to your `%IDA_DIR%/plugins` directory.

### Usage
 
Open the executable UEFI image in IDA and go to `Edit` -> `Plugins` -> `UEFI analyser` *(alternatively, you can use the key combination `Ctrl+Alt+U`)*

### Example

#### Pseudocode after plugin work

![after_analysis](https://raw.githubusercontent.com/yeggor/uefi_retool/master/img/after_analysis.png)

#### Protocol explorer window

![protocols](https://raw.githubusercontent.com/yeggor/uefi_retool/master/img/protocols.png)

## Dependency browser & Dependency graph

### Usage

  * Analyse the firmware with `uefi_retool.py`

    ```bash
    python uefi_retool.py get-info FIRMWARE_PATH
    ```

   * Load `{LOGS_DIR}/{FIRMWARE_NAME}-all-info.json` file to IDA (`File` -> `uefi_retool...`)

      ![db-usage](https://raw.githubusercontent.com/yeggor/uefi_retool/master/img/db-usage.png)

      *alternatively, you can use the key combination `Ctrl+Alt+J`*)

### Example

#### Dependency browser window

![db-usage](https://raw.githubusercontent.com/yeggor/uefi_retool/master/img/depend-browser.png)

#### Dependency graph

![db-graph](https://raw.githubusercontent.com/yeggor/uefi_retool/master/img/depend-graph.png)
