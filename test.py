import unittest
from crypt import crypt

class TestCrypt(unittest.TestCase):

    def test_1(self):
        """
            encrypted_message = "th3s 3s 1 m2ss1g2."
            decrypted_message = "this is a message."

            crypt(encrypted_message) must equal to decrypted_message
            also
            crypt(decrypted_message) must equal to encrypted_message
        """
        encrypt_message = "th3s 3s 1 m2ss1g2."
        decrypted_message = "this is a message."

        self.assertEqual(decrypted_message, crypt(encrypt_message))
        self.assertEqual(encrypt_message, crypt(decrypted_message))


    def test_2(self):
        """
            encrypted_message = "another message here!"
            decrypted_message = "1n4th2r m2ss1g2 h2r2!"

            crypt(encrypted_message) must equal to decrypted_message
            also
            crypt(decrypted_message) must equal to encrypted_message
        """
        encrypt_message = "another message here!"
        decrypted_message = "1n4th2r m2ss1g2 h2r2!"

        self.assertEqual(decrypted_message, crypt(encrypt_message))
        self.assertEqual(encrypt_message, crypt(decrypted_message))
