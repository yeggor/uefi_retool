# IDA plugin for UEFI analysis

This plugin performs automatic analysis of the input UEFI module.

Based on the [analysis.py](https://github.com/yeggor/UEFI_RETool/blob/master/ida_uefi_re/analyser.py) script (more info is [here](https://yeggor.github.io/UEFI_RETool/)).

### Usage:
  
 * Copy `uefi_analyser` and `uefi_analyser.py` to your `%IDA_DIR%/plugins` directory
 
 * Open the executable UEFI image in IDA and go to `Edit` -> `Plugins` -> `UEFI analyser`
 *(alternatively, you can use the key combination `Ctrl+Alt+U`)*

### Example

 * Before analysis:

    ![before_analysis](https://github.com/yeggor/UEFI_RETool/blob/master/img/before_analysis.png)

 * After analysis:

    ![after_analysis](https://github.com/yeggor/UEFI_RETool/blob/master/img/after_analysis.png)

    ![protocols](https://github.com/yeggor/UEFI_RETool/blob/master/img/protocols.png)
