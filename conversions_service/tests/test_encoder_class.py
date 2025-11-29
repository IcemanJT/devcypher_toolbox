import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conversions_service')))

from encoder import Encoder


class TestEncoder:
    """Test suite for Encoder class"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup Encoder instance for each test"""
        # Reset singleton for testing
        Encoder._instance = None
        self.encoder = Encoder.get_instance()

    def test_encoder_singleton_pattern(self):
        """Test that Encoder follows singleton pattern"""
        encoder1 = Encoder.get_instance()
        encoder2 = Encoder.get_instance()
        assert encoder1 is encoder2

    def test_encoder_direct_instantiation_raises_error(self):
        """Test that direct instantiation raises RuntimeError"""
        Encoder._instance = None
        with pytest.raises(RuntimeError):
            Encoder()

    def test_encoder_available_ciphers(self):
        """Test available_ciphers property"""
        ciphers = self.encoder.available_ciphers
        assert isinstance(ciphers, list)
        assert "cesar" in ciphers
        assert "atbash" in ciphers
        assert "rot13" in ciphers
        assert "base64" in ciphers

    def test_encoder_cesar_shift_3(self):
        """Test Cesar cipher encoding with shift 3"""
        result = self.encoder.cesar("ABC", "3")
        assert result == "DEF"

    def test_encoder_cesar_lowercase(self):
        """Test Cesar cipher with lowercase"""
        result = self.encoder.cesar("abc", "3")
        assert result == "def"

    def test_encoder_cesar_mixed_case(self):
        """Test Cesar cipher with mixed case"""
        result = self.encoder.cesar("Hello", "3")
        assert result == "Khoor"

    def test_encoder_cesar_wrap_around(self):
        """Test Cesar cipher wrap around"""
        result = self.encoder.cesar("XYZ", "3")
        assert result == "ABC"

    def test_encoder_cesar_preserves_non_alpha(self):
        """Test Cesar cipher preserves non-alphabetic characters"""
        result = self.encoder.cesar("Hello, World!", "3")
        assert "," in result
        assert " " in result
        assert "!" in result

    def test_encoder_atbash_uppercase(self):
        """Test Atbash cipher with uppercase"""
        result = self.encoder.atbash("ABC")
        assert result == "ZYX"

    def test_encoder_atbash_lowercase(self):
        """Test Atbash cipher with lowercase"""
        result = self.encoder.atbash("abc")
        assert result == "zyx"

    def test_encoder_atbash_mixed_case(self):
        """Test Atbash cipher with mixed case"""
        result = self.encoder.atbash("Hello")
        assert result == "Svool"

    def test_encoder_atbash_symmetric(self):
        """Test Atbash cipher is symmetric"""
        text = "Hello World"
        encoded = self.encoder.atbash(text)
        decoded = self.encoder.atbash(encoded)
        assert decoded == text

    def test_encoder_atbash_preserves_non_alpha(self):
        """Test Atbash cipher preserves non-alphabetic characters"""
        result = self.encoder.atbash("Hello, World!")
        assert "," in result
        assert " " in result
        assert "!" in result

    def test_encoder_rot13(self):
        """Test ROT13 encoding"""
        result = self.encoder.rot13("Hello")
        assert result == "Uryyb"

    def test_encoder_rot13_symmetric(self):
        """Test ROT13 is symmetric"""
        text = "Hello World"
        encoded = self.encoder.rot13(text)
        decoded = self.encoder.rot13(encoded)
        assert decoded == text

    def test_encoder_rot13_full_alphabet(self):
        """Test ROT13 with full alphabet"""
        result = self.encoder.rot13("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        assert result == "NOPQRSTUVWXYZABCDEFGHIJKLM"
