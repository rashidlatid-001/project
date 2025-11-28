import pytest
import os
import tempfile
import unittest

from tool import key_manager, encryptor, decryptor

# Hum unittest use kar rahe hain, isliye TestCase se inherit karna hoga
class TestEndToEnd(unittest.TestCase):
    
    # 1. Full encrypt/decrypt flow
    def test_full_encrypt_decrypt_flow(self):
        """Full integration test: key_manager -> encryptor -> decryptor."""
        key = key_manager.generate_key()
        self.assertIsInstance(key, bytes)
        plaintext = b"This is integration test data!"
        cipher = encryptor.encrypt(plaintext, key)
        self.assertNotEqual(cipher, plaintext)
        recovered = decryptor.decrypt(cipher, key)
        self.assertEqual(recovered, plaintext)

    # 2. Key Persistence Test
    def test_key_persistence(self):
        """Checks if key can be saved to a file and loaded back correctly."""
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            temp_path = tmp.name
        
        try:
            original_key = key_manager.generate_key()
            key_manager.save_key(original_key, temp_path)
            loaded_key = key_manager.load_key(temp_path)
            self.assertEqual(original_key, loaded_key)
        finally:
            os.remove(temp_path)

    # 3. File Encryption/Decryption Test
    def test_full_file_flow(self):
        """Tests end-to-end file encryption and decryption."""
        key = key_manager.generate_key()
        original_data = b"This is file test data."
        
        # Temp file banana
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            temp_path = tmp.name
            tmp.write(original_data)
        
        try:
            # Encrypt karna
            encryptor.encrypt_file(temp_path, key)
            
            # File contents check karein (encrypted hona chahiye)
            with open(temp_path, 'rb') as f:
                encrypted_data = f.read()
            self.assertNotEqual(encrypted_data, original_data)
            
            # Decrypt karna
            decryptor.decrypt_file(temp_path, key)
            
            # File contents check karein (original data wapas aana chahiye)
            with open(temp_path, 'rb') as f:
                recovered_data = f.read()
            self.assertEqual(recovered_data, original_data)
        
        finally:
            os.remove(temp_path)

    # 4. Wrong Key Test 
    def test_wrong_key_integration(self):
       
        key1 = key_manager.generate_key()
        key2 = key_manager.generate_key()
        plaintext = b"Secret integration message"
        
        cipher = encryptor.encrypt(plaintext, key1)
        
        with self.assertRaises(ValueError):
            decryptor.decrypt(cipher, key2)

   
    def test_corrupted_cipher_integration(self):
        """Corrupted ciphertext par error raise hona chahiye."""
        key = key_manager.generate_key()
        cipher = encryptor.encrypt(b"Test corrupted data", key)
        
        corrupted = bytearray(cipher)
      
        if len(corrupted) > 0:
            corrupted[0] ^= 0xFF  
        
        with self.assertRaises(ValueError):
            decryptor.decrypt(bytes(corrupted), key)


    def test_invalid_key_format(self):
        """Tests that invalid keys raise ValueError."""
        
        # Encryptor ka check (tool/encryptor.py line 6)
        with self.assertRaises(ValueError):
            encryptor.encrypt(b"data", b"short")
            
        # Decryptor ka check (tool/decryptor.py lines 8-9)
        cipher = encryptor.encrypt(b"data", key_manager.generate_key())
        with self.assertRaises(ValueError):
            decryptor.decrypt(cipher, b"short")
            
    # NEW TEST 7: Key Generation Invalid Length (Covers tool/key_manager.py Line 6)
    def test_key_generation_invalid_length(self):
        """Covers key_manager.generate_key() when length is invalid."""
        with self.assertRaises(ValueError):
            key_manager.generate_key(length=0)
        with self.assertRaises(ValueError):
            key_manager.generate_key(length=-5)

    # NEW TEST 8: Encrypt Empty Data (Covers tool/encryptor.py Line 8)
    def test_encrypt_empty_data(self):
        """Covers encryptor.encrypt() when data is empty."""
        key = key_manager.generate_key()
        with self.assertRaises(ValueError):
            encryptor.encrypt(b"", key) # Empty bytes bhejna

    # NEW TEST 9: Encrypt File Not Found (Covers tool/encryptor.py Lines 17-19)
    def test_encrypt_file_not_found(self):
        """Covers encryptor.encrypt_file() when file is not found."""
        key = key_manager.generate_key()
        non_existent_path = "non_existent_file_for_test_encrypt.tmp"
        with self.assertRaises(FileNotFoundError): 
            encryptor.encrypt_file(non_existent_path, key)

    # NEW TEST 10: Decrypt File Not Found (Covers tool/decryptor.py Lines 17-19)
    def test_decrypt_file_not_found(self):
        """Covers decryptor.decrypt_file() when file is not found."""
        key = key_manager.generate_key()
        non_existent_path = "non_existent_file_for_test_decrypt.tmp"
        with self.assertRaises(FileNotFoundError): 
            decryptor.decrypt_file(non_existent_path, key)