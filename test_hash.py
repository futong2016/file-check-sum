import hashlib
import os
import unittest
from main import FileChecksumTool
import tkinter as tk

class TestHashCalculation(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = FileChecksumTool(self.root)
        self.test_file = "test_sample.txt"
        with open(self.test_file, "w") as f:
            f.write("hello world")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.root.destroy()

    def test_md5(self):
        expected = hashlib.md5(b"hello world").hexdigest()
        result = self.app.calculate_file_hash(self.test_file, "MD5")
        self.assertEqual(result, expected)

    def test_sha1(self):
        expected = hashlib.sha1(b"hello world").hexdigest()
        result = self.app.calculate_file_hash(self.test_file, "SHA-1")
        self.assertEqual(result, expected)

    def test_sha256(self):
        expected = hashlib.sha256(b"hello world").hexdigest()
        result = self.app.calculate_file_hash(self.test_file, "SHA-256")
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
