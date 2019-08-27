BOOT_SERVICES_OFFSET_x64 = {
    "InstallProtocolInterface": 0x80,
    "ReinstallProtocolInterface": 0x88,
    "UninstallProtocolInterface": 0x90,
    "HandleProtocol": 0x98,
    "RegisterProtocolNotify": 0xA8,
    "OpenProtocol": 0x118,
    "CloseProtocol": 0x120,
    "OpenProtocolInformation": 0x128,
    "ProtocolsPerHandle": 0x130,
    "LocateHandleBuffer": 0x138,
    "LocateProtocol": 0x140,
    "InstallMultipleProtocolInterfaces": 0x148,
    "UninstallMultipleProtocolInterfaces": 0x150
}

BOOT_SERVICES_OFFSET_x86 = {
    "InstallProtocolInterface": 0x4C,
    "ReinstallProtocolInterface": 0x50,
    "UninstallProtocolInterface": 0x54,
    "HandleProtocol": 0x58,
    "RegisterProtocolNotify": 0x60,
    "OpenProtocol": 0x98,
    "CloseProtocol": 0x9C,
    "OpenProtocolInformation": 0xA0,
    "ProtocolsPerHandle": 0xA4,
    "LocateHandleBuffer": 0xA8,
    "LocateProtocol": 0xAC,
    "InstallMultipleProtocolInterfaces": 0xB0,
    "UninstallMultipleProtocolInterfaces": 0xB4
}

SMM_SERVICES_OFFSET_x64 = {
    "SmmInstallProtocolInterface": 0xA8,
    "SmmUninstallProtocolInterface": 0xB0,
    "SmmHandleProtocol": 0xB8,
    "SmmRegisterProtocolNotify": 0xC0,
    "SmmLocateProtocol": 0xD0
}

SMM_SERVICES_OFFSET_x86 = {
    "SmmInstallProtocolInterface": 0x60,
    "SmmUninstallProtocolInterface": 0x64,
    "SmmHandleProtocol": 0x68,
    "SmmRegisterProtocolNotify": 0x6C,
    "SmmLocateProtocol": 0x74
}