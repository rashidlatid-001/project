from cryptography.fernet import Fernet, InvalidToken
import os

def decrypt(cipher: bytes, key: bytes) -> bytes:
    """Decrypts byte data using a Fernet key."""
    
    # Key validation (for completeness)
    if not isinstance(key, bytes) or len(key) not in (32, 44): 
        raise ValueError("Invalid key format or length for decryption.")
        
    try:
        f = Fernet(key)
        return f.decrypt(cipher)
    except InvalidToken:
        raise ValueError("Decryption failed: Invalid key or corrupted ciphertext.")
    except Exception as e:
        # Koi aur generic error
        raise ValueError(f"Decryption failed due to an unknown error: {e}")


def decrypt_file(filepath: str, key: bytes):
    """Decrypts the contents of a file in place."""
    
    # Lines 17-19 (Missing: FileNotFoundError will be raised by 'with open' 
    # if the file doesn't exist, which the new test will catch.)

    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    
    decrypted_data = decrypt(encrypted_data, key)
    
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)