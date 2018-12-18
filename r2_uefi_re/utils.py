def get_word(bytes):
    word  = (bytes[1] << 8) & 0xff00
    word |= (bytes[0] << 0) & 0x00ff
    return word

def get_dword(bytes):
    dword  = (bytes[3] << 24) & 0xff000000
    dword |= (bytes[2] << 16) & 0x00ff0000
    dword |= (bytes[1] <<  8) & 0x0000ff00
    dword |= (bytes[0] <<  0) & 0x000000ff
    return dword
