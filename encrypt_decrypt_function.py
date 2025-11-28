# ============================
#   Encryption Function
# ============================
def encryptText(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result


# ============================
#   Decryption Function
# ============================
def decryptText(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += char
    return result


# ============================
#   Key Validation Function
# ============================
def validateKey(key):
    return isinstance(key, int) and key > 0
