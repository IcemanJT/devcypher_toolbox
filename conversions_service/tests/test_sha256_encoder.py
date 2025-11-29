import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conversions_service')))

from services.sha256_encoder import Sha256Encoder


class TestSha256Encoder:
    """Test suite for Sha256Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup Sha256Encoder instance for each test"""
        self.encoder = Sha256Encoder()

    def test_sha256_encode_simple_text(self):
        """Test encoding simple ASCII text to SHA256 hash"""
        input_text = "Hello World"
        # SHA256 hash of "Hello World"
        expected_output = "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_sha256_encoder_properties(self):
        """Test Sha256Encoder class properties"""
        assert self.encoder.name == "sha256"
        assert self.encoder.is_symmetric == False

    def test_sha256_encode_returns_64_char_hex(self):
        """Test that SHA256 hash always returns 64 character hexadecimal string"""
        result = self.encoder.encode("test", key="")

        assert len(result) == 64
        assert all(c in '0123456789abcdef' for c in result)

    def test_sha256_encode_empty_string(self):
        """Test encoding an empty string"""
        input_text = ""
        # SHA256 hash of empty string
        expected_output = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_sha256_encode_special_characters(self):
        """Test encoding text with special characters"""
        input_text = "Hello! @#$%^&*()"

        result = self.encoder.encode(input_text, key="")

        assert isinstance(result, str)
        assert len(result) == 64

    def test_sha256_encode_numbers(self):
        """Test encoding text with numbers"""
        input_text = "Test123456"

        result = self.encoder.encode(input_text, key="")

        assert isinstance(result, str)
        assert len(result) == 64

    def test_sha256_encode_unicode_characters(self):
        """Test encoding text with unicode characters"""
        input_text = "Hello 世界 🌍"

        result = self.encoder.encode(input_text, key="")

        assert isinstance(result, str)
        assert len(result) == 64

