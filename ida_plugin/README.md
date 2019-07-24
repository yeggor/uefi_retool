# IDA plugin for UEFI analysis

This plugin performs automatic analysis of the input UEFI module.

Based on the [analysis.py](https://github.com/yeggor/UEFI_RETool/blob/master/ida_uefi_re/analyser.py) script.

### Usage:
 
 * Install dependencies:
    
    ```bash
    python -m pip install requirements.txt
    ```
 
 * Copy `uefi_analyser` and `uefi_analyser.py` to your `%IDA_DIR%/plugins` directory
 
 * Open the executable UEFI image in IDA and go to `Edit` -> `Plugins` -> `UEFI analyser`
 *(alternatively, you can use the key combination `Ctrl+Alt+U`)*

### Example:
    
![example](https://github.com/yeggor/UEFI_RETool/blob/master/ida_plugin/rsrc/usage.gif)