from Crypto.Cipher import DES
import sys
import os


def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text


if __name__ == '__main__':
    key_len = len(sys.argv[2])
    if key_len != 8:
        raise Exception(f'Key must be 8-byte len, not {key_len}-byte')

    iv_vector = os.urandom(8)

    des = DES.new(sys.argv[2], DES.MODE_CBC, iv_vector)

    print(f'CBC sign: {iv_vector}')
    text = open(sys.argv[1], 'rb').read()
    padded_text = pad(text)
    print(f'Text:\n{text}')

    encrypted_text = des.encrypt(padded_text)
    print(f'Encrypted text:\n'
          f'{encrypted_text}')

    des1 = DES.new(sys.argv[2], DES.MODE_CBC, iv_vector)
    data = des1.decrypt(encrypted_text).decode("utf-8")
    print(f'Text:\n{data.lstrip(" ")}')

    print('################################################################################')

    des = DES.new(sys.argv[2], DES.MODE_ECB)
    text = open(sys.argv[1], 'rb').read()
    padded_text = pad(text)
    print(f'Text:\n{text}')

    encrypted_text = des.encrypt(padded_text)
    print(f'Encrypted text:\n'
          f'{encrypted_text}')

    data = des.decrypt(encrypted_text)
    print(data)
