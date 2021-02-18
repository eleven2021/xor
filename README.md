# xor

#########
`python`
key = "password"
src_text = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
print("src:" + src_text)

hex_text = crypto_text_to_hex(src_text, key)
print("enc:" + hex_text)

decode_text = decrypto_hex_to_text(hex_text, key)
print("dec:" + decode_text)

if src_text == decode_text:
    print("decode OK.")

```
