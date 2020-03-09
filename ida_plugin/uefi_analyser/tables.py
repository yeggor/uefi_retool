# MIT License
#
# Copyright (c) 2018-2019 yeggor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

BOOT_SERVICES_OFFSET_x64 = {
    'InstallProtocolInterface': 0x80,
    'ReinstallProtocolInterface': 0x88,
    'UninstallProtocolInterface': 0x90,
    'HandleProtocol': 0x98,
    'RegisterProtocolNotify': 0xA8,
    'OpenProtocol': 0x118,
    'CloseProtocol': 0x120,
    'OpenProtocolInformation': 0x128,
    'ProtocolsPerHandle': 0x130,
    'LocateHandleBuffer': 0x138,
    'LocateProtocol': 0x140,
    'InstallMultipleProtocolInterfaces': 0x148,
    'UninstallMultipleProtocolInterfaces': 0x150
}

BOOT_SERVICES_OFFSET_x86 = {
    'InstallProtocolInterface': 0x4C,
    'ReinstallProtocolInterface': 0x50,
    'UninstallProtocolInterface': 0x54,
    'HandleProtocol': 0x58,
    'RegisterProtocolNotify': 0x60,
    'OpenProtocol': 0x98,
    'CloseProtocol': 0x9C,
    'OpenProtocolInformation': 0xA0,
    'ProtocolsPerHandle': 0xA4,
    'LocateHandleBuffer': 0xA8,
    'LocateProtocol': 0xAC,
    'InstallMultipleProtocolInterfaces': 0xB0,
    'UninstallMultipleProtocolInterfaces': 0xB4
}

SMM_SERVICES_OFFSET_x64 = {
    'SmmInstallProtocolInterface': 0xA8,
    'SmmUninstallProtocolInterface': 0xB0,
    'SmmHandleProtocol': 0xB8,
    'SmmRegisterProtocolNotify': 0xC0,
    'SmmLocateProtocol': 0xD0
}

SMM_SERVICES_OFFSET_x86 = {
    'SmmInstallProtocolInterface': 0x60,
    'SmmUninstallProtocolInterface': 0x64,
    'SmmHandleProtocol': 0x68,
    'SmmRegisterProtocolNotify': 0x6C,
    'SmmLocateProtocol': 0x74
}
