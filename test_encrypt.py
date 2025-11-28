import unittest
from encrypt_decrypt_function import encryptText, decryptText, validateKey

class TestEncryptionTool(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encryptText("ABC", 3), "DEF")
        self.assertEqual(encryptText("xyz", 2), "zab")
        self.assertEqual(encryptText("", 5), "")
        self.assertEqual(encryptText("Hello123", 3), "Khoor123")

    def test_decrypt(self):
        self.assertEqual(decryptText("DEF", 3), "ABC")
        self.assertEqual(decryptText("zab", 2), "xyz")
        self.assertEqual(decryptText("", 5), "")
        self.assertEqual(decryptText("Khoor123", 3), "Hello123")

    def test_validate_key(self):
        self.assertTrue(validateKey(3))
        self.assertFalse(validateKey("a"))
        self.assertFalse(validateKey(-2))
        self.assertFalse(validateKey(0))
 
if __name__ == '__main__':
    unittest.main()