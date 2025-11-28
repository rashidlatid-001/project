import os
import base64 
import json 

def generate_key(length: int = 32) -> bytes:
    """Generates a Base64 encoded Fernet key, with length validation."""
    if length <= 0:
        raise ValueError("Key length must be positive.")
        
    raw_key = os.urandom(32) 
    
    encoded_key = base64.urlsafe_b64encode(raw_key)
    
    return encoded_key

def save_key(key: bytes, filename: str):
    """Saves the key to a file."""
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename: str) -> bytes:
    """Loads a key from a file."""
    with open(filename, 'rb') as f:
        return f.read()