def utf8_to_utf16(utf8_hex_str):
    '''
    输入：utf8 编码的十六进制字符串, 如 0xE4B8AD
    输出：utf16 编码的十六进制字符串, 如 0x4E2D
    '''
    utf8_bytes = bytes.fromhex(utf8_hex_str[2:])
    utf8_char = utf8_bytes.decode('utf-8')
    utf16_bytes = utf8_char.encode('utf-16-be').hex().upper()
    return f'0x{utf16_bytes}'
