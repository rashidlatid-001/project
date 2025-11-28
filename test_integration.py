import unittest, login

class TestIntegration(unittest.TestCase):

    def test_valid_login(self):
        self.assertTrue(login.login("admin", "1234"))

    def test_invalid_login(self):
        self.assertFalse(login.login("user", "0000"))
