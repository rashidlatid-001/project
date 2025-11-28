from cryptography.fernet import Fernet
import os 

def encrypt(data: bytes, key: bytes) -> bytes:
    """Encrypts byte data using a Fernet key."""
    
    if not data: 
        raise ValueError("Data cannot be empty.")
    
    if not isinstance(key, bytes) or len(key) not in (32, 44): 
        raise ValueError("Invalid key format or length.")
        
    try:
        f = Fernet(key)
        return f.encrypt(data)
    except Exception as e:
        raise ValueError(f"Encryption failed: {e}")

def encrypt_file(filepath: str, key: bytes):
    """Encrypts the contents of a file in place."""
    
    
    with open(filepath, 'rb') as file:
        file_data = file.read()
    
    encrypted_data = encrypt(file_data, key)
    
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)