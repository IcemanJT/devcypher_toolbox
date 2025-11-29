import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conversions_service')))

from decoder import Decoder
from encoder import Encoder


class TestDecoder:
    """Test suite for Decoder class"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup Decoder instance for each test"""
        # Reset singletons for testing
        Decoder._instance = None
        Encoder._instance = None
        self.decoder = Decoder.get_instance()

    def test_decoder_singleton_pattern(self):
        """Test that Decoder follows singleton pattern"""
        decoder1 = Decoder.get_instance()
        decoder2 = Decoder.get_instance()
        assert decoder1 is decoder2

    def test_decoder_direct_instantiation_raises_error(self):
        """Test that direct instantiation raises RuntimeError"""
        Decoder._instance = None
        with pytest.raises(RuntimeError):
            Decoder()

    def test_decoder_available_ciphers(self):
        """Test available_ciphers property"""
        ciphers = self.decoder.available_ciphers
        assert isinstance(ciphers, list)
        assert "cesar" in ciphers
        assert "atbash" in ciphers
        assert "rot13" in ciphers
        assert "base64" in ciphers

    def test_decoder_cesar_shift_3(self):
        """Test Cesar cipher decoding with shift 3"""
        result = self.decoder.cesar("DEF", "3")
        assert result == "ABC"

    def test_decoder_cesar_lowercase(self):
        """Test Cesar cipher decode with lowercase"""
        result = self.decoder.cesar("def", "3")
        assert result == "abc"

    def test_decoder_cesar_mixed_case(self):
        """Test Cesar cipher decode with mixed case"""
        result = self.decoder.cesar("Khoor", "3")
        assert result == "Hello"

    def test_decoder_cesar_wrap_around(self):
        """Test Cesar cipher decode wrap around"""
        result = self.decoder.cesar("ABC", "3")
        assert result == "XYZ"

    def test_decoder_cesar_preserves_non_alpha(self):
        """Test Cesar cipher decode preserves non-alphabetic characters"""
        result = self.decoder.cesar("Khoor, Zruog!", "3")
        assert "," in result
        assert " " in result
        assert "!" in result

    def test_decoder_atbash_uppercase(self):
        """Test Atbash cipher decode with uppercase"""
        result = self.decoder.atbash("ZYX")
        assert result == "ABC"

    def test_decoder_atbash_lowercase(self):
        """Test Atbash cipher decode with lowercase"""
        result = self.decoder.atbash("zyx")
        assert result == "abc"

    def test_decoder_atbash_mixed_case(self):
        """Test Atbash cipher decode with mixed case"""
        result = self.decoder.atbash("Svool")
        assert result == "Hello"

    def test_decoder_atbash_symmetric(self):
        """Test Atbash cipher decode is symmetric with encode"""
        text = "Hello World"
        # Atbash is symmetric, so encoding and decoding produce the same result
        encoded = self.decoder.atbash(text)
        decoded = self.decoder.atbash(encoded)
        assert decoded == text

    def test_decoder_rot13(self):
        """Test ROT13 decoding"""
        result = self.decoder.rot13("Uryyb")
        assert result == "Hello"

    def test_decoder_rot13_symmetric(self):
        """Test ROT13 is symmetric"""
        text = "Hello World"
        encoded = self.decoder.rot13(text)
        decoded = self.decoder.rot13(encoded)
        assert decoded == text

    def test_encoder_decoder_cesar_roundtrip(self):
        """Test Cesar encode/decode roundtrip"""
        encoder = Encoder.get_instance()
        original = "Test Message"
        encoded = encoder.cesar(original, "5")
        decoded = self.decoder.cesar(encoded, "5")
        assert decoded == original

    def test_encoder_decoder_atbash_roundtrip(self):
        """Test Atbash encode/decode roundtrip"""
        encoder = Encoder.get_instance()
        original = "Test Message"
        encoded = encoder.atbash(original)
        decoded = self.decoder.atbash(encoded)
        assert decoded == original

    def test_encoder_decoder_rot13_roundtrip(self):
        """Test ROT13 encode/decode roundtrip"""
        encoder = Encoder.get_instance()
        original = "Test Message"
        encoded = encoder.rot13(original)
        decoded = self.decoder.rot13(encoded)
        assert decoded == original
