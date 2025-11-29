import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conversions_service')))

from cipher_bundle import caesar_cipher, atbash_cipher, rot13_cipher, base64_encode, base64_decode


class TestCaesarCipher:
    """Test suite for caesar_cipher function"""

    def test_caesar_encode_shift_3(self):
        """Test Caesar cipher encoding with shift of 3"""
        result = caesar_cipher("ABC", 3)
        assert result == "DEF"

    def test_caesar_decode_shift_3(self):
        """Test Caesar cipher decoding with shift of 3"""
        result = caesar_cipher("DEF", 3, decode=True)
        assert result == "ABC"

    def test_caesar_encode_lowercase(self):
        """Test Caesar cipher with lowercase"""
        result = caesar_cipher("abc", 3)
        assert result == "def"

    def test_caesar_decode_lowercase(self):
        """Test Caesar cipher decode with lowercase"""
        result = caesar_cipher("def", 3, decode=True)
        assert result == "abc"

    def test_caesar_mixed_case(self):
        """Test Caesar cipher with mixed case"""
        result = caesar_cipher("Hello", 3)
        assert result == "Khoor"

    def test_caesar_wrap_around(self):
        """Test Caesar cipher wrap around"""
        result = caesar_cipher("XYZ", 3)
        assert result == "ABC"

    def test_caesar_preserves_non_alpha(self):
        """Test Caesar cipher preserves non-alphabetic characters"""
        result = caesar_cipher("Hello, World!", 3)
        assert result == "Khoor, Zruog!"

    def test_caesar_empty_string(self):
        """Test Caesar cipher with empty string"""
        result = caesar_cipher("", 3)
        assert result == ""

    def test_caesar_roundtrip(self):
        """Test Caesar cipher encode/decode roundtrip"""
        original = "Test Message"
        encoded = caesar_cipher(original, 5)
        decoded = caesar_cipher(encoded, 5, decode=True)
        assert decoded == original


class TestAtbashCipher:
    """Test suite for atbash_cipher function"""

    def test_atbash_uppercase(self):
        """Test Atbash cipher with uppercase"""
        result = atbash_cipher("ABC")
        assert result == "ZYX"

    def test_atbash_lowercase(self):
        """Test Atbash cipher with lowercase"""
        result = atbash_cipher("abc")
        assert result == "zyx"

    def test_atbash_mixed_case(self):
        """Test Atbash cipher with mixed case"""
        result = atbash_cipher("Hello")
        assert result == "Svool"

    def test_atbash_preserves_non_alpha(self):
        """Test Atbash cipher preserves non-alphabetic characters"""
        result = atbash_cipher("Hello, World!")
        assert "," in result
        assert " " in result
        assert "!" in result

    def test_atbash_symmetric(self):
        """Test Atbash cipher is symmetric"""
        text = "Hello World"
        encoded = atbash_cipher(text)
        decoded = atbash_cipher(encoded)
        assert decoded == text

    def test_atbash_empty_string(self):
        """Test Atbash cipher with empty string"""
        result = atbash_cipher("")
        assert result == ""

    def test_atbash_full_alphabet(self):
        """Test Atbash cipher with full alphabet"""
        result = atbash_cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        assert result == "ZYXWVUTSRQPONMLKJIHGFEDCBA"


class TestRot13Cipher:
    """Test suite for rot13_cipher function"""

    def test_rot13_encode(self):
        """Test ROT13 encoding"""
        result = rot13_cipher("Hello")
        assert result == "Uryyb"

    def test_rot13_symmetric(self):
        """Test ROT13 is symmetric"""
        text = "Hello World"
        encoded = rot13_cipher(text)
        decoded = rot13_cipher(encoded)
        assert decoded == text

    def test_rot13_full_alphabet(self):
        """Test ROT13 with full alphabet"""
        result = rot13_cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        assert result == "NOPQRSTUVWXYZABCDEFGHIJKLM"

    def test_rot13_preserves_non_alpha(self):
        """Test ROT13 preserves non-alphabetic characters"""
        result = rot13_cipher("Hello, World! 123")
        assert "," in result
        assert " " in result
        assert "!" in result
        assert "123" in result


class TestBase64Functions:
    """Test suite for base64_encode and base64_decode functions"""

    def test_base64_encode_simple(self):
        """Test Base64 encoding"""
        result = base64_encode("Hello World")
        assert result == "SGVsbG8gV29ybGQ="

    def test_base64_decode_simple(self):
        """Test Base64 decoding"""
        result = base64_decode("SGVsbG8gV29ybGQ=")
        assert result == "Hello World"

    def test_base64_roundtrip(self):
        """Test Base64 encode/decode roundtrip"""
        original = "Test Message 123!"
        encoded = base64_encode(original)
        decoded = base64_decode(encoded)
        assert decoded == original

    def test_base64_empty_string(self):
        """Test Base64 with empty string"""
        result = base64_encode("")
        assert result == ""

    def test_base64_decode_invalid(self):
        """Test Base64 decode with invalid input"""
        result = base64_decode("not-valid-base64!!!")
        assert result == "Błąd dekodowania Base64"

    def test_base64_unicode(self):
        """Test Base64 with unicode characters"""
        original = "Hello 世界"
        encoded = base64_encode(original)
        decoded = base64_decode(encoded)
        assert decoded == original
