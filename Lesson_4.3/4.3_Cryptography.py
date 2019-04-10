# Caesar Cipher:


def caesar(text, key):
    text = list(text)
    for i in range(len(text)):
        print(text[i] + " is turned into " + chr(int(ord(text[i])) + key))
        text[i] = chr(int(ord(text[i])) + key)
    return text


print(caesar("Hello", 3))


def decryption(text, key):
    text = list(text)
    for i in range(len(text)):
        print(text[i] + " is the coded letter. It is decoded into " + chr(int(ord(text[i])) - key))
        text[i] = chr(int(ord(text[i])) - key)
    print(text)


decryption(text=caesar("Hello", 3), key=3)

