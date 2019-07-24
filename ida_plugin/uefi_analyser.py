import idc
import idaapi
import idautils
import uefi_analyser.analyser as analyser
from uefi_analyser.analyser import Analyser

AUTHOR = "yeggor"
VERSION = "v1.0.0"

IMAGE_FILE_MACHINE_IA64 = 0x8664
IMAGE_FILE_MACHINE_I386 = 0x014c
PE_OFFSET = 0x3c

class UefiAnalyserPlugin(idaapi.plugin_t):
    flags = (idaapi.PLUGIN_MOD | idaapi.PLUGIN_PROC | idaapi.PLUGIN_FIX)
    comment = "This plugin performs automatic analysis of the input UEFI module"
    help  = "This plugin performs automatic analysis of the input UEFI module.\n"
    help += "Based on the https://github.com/yeggor/UEFI_RETool/blob/master/ida_uefi_re/analyser.py script."
    wanted_name = "UEFI analyser"
    wanted_hotkey = "Ctrl+Alt+U"

    def init(self):
        self.input_file_path = idaapi.get_input_file_path()
        self.machine_type = self._get_machine_type()
        self._welcome()
        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        if (self._check_input_file() == True):
            self._analyse_all()
    
    def term(self):
        pass
    
    def _check_input_file(self):
        if (self.machine_type == IMAGE_FILE_MACHINE_IA64):
            return True
        else:
            idc.Message("File format is not supported")
            return False

    def _get_machine_type(self):
        with open(self.input_file_path, "rb") as f:
            header = f.read(1024)
        PE_POINTER = self._get_num_le(header[PE_OFFSET:PE_OFFSET+1:])
        FH_POINTER = PE_POINTER + 4
        machine_type = header[FH_POINTER:FH_POINTER+2:]
        type_value = self._get_num_le(machine_type)
        return type_value

    @staticmethod
    def _welcome():
        main_line = " UEFI analyser plugin {version} by {author} ".format(
            version=VERSION, 
            author=AUTHOR
        )
        message =  "[{line}]\n".format(line="="*len(main_line))
        message += "|{line}|\n".format(line=" "*len(main_line))
        message += "|{main_line}|\n".format(main_line=main_line)
        message += "|{line}|\n".format(line=" "*len(main_line))
        message += "[{line}]\n".format(line="="*len(main_line))
        print(message)

    @staticmethod
    def _analyse_all():
        analyser.main()
    
    @staticmethod
    def _get_num_le(bytearr):
        num_le = 0
        for i in range(len(bytearr)):
            num_le += ord(bytearr[i]) * pow(256, i)
        return num_le

def PLUGIN_ENTRY():
    try:
        return UefiAnalyserPlugin()
    except Exception, err:
        import traceback
        print("Error: %s\n%s" % str((err), traceback.format_exc()))
        raise
