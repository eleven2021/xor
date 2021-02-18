def crypto_text_to_hex(src_text, key):
    xor_code = key
    while len(src_text) > len(xor_code):
        xor_code += key
    return "".join([chr(ord(data) ^ ord(code))
                    for (data, code) in zip(src_text, xor_code)]).encode().hex()

def decrypto_hex_to_text(hex_text, key):
    crypt_data = bytes.fromhex(hex_text).decode()
    xor_code = key
    while len(crypt_data) > len(xor_code):
        xor_code += key
    return "".join([chr(ord(data) ^ ord(code))
                    for (data, code) in zip(crypt_data, xor_code)])
