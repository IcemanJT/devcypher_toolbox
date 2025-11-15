import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conversions_service')))

from services.base64_encoder import Base64Encoder


class TestBase64Encoder:
    """Test suite for Base64Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup Base64Encoder instance for each test"""
        self.encoder = Base64Encoder()

    def test_base64_encode_simple_text(self):
        """Test encoding simple ASCII text to Base64"""
        input_text = "Hello World"
        expected_output = "SGVsbG8gV29ybGQ="

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_base64_encode_and_decode_roundtrip(self):
        """Test that encoding and then decoding returns the original text"""
        original_text = "DevCypher Toolbox"

        encoded = self.encoder.encode(original_text, key="")
        decoded = self.encoder.decode(encoded, key="")

        assert decoded == original_text

    def test_base64_encoder_properties(self):
        """Test Base64Encoder class properties"""
        assert self.encoder.name == "base64"
        assert self.encoder.is_symmetric == True

    def test_base64_encode_empty_string(self):
        """Test encoding an empty string"""
        input_text = ""
        expected_output = ""

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_base64_encode_special_characters(self):
        """Test encoding text with special characters"""
        input_text = "Hello! @#$%^&*()"

        encoded = self.encoder.encode(input_text, key="")
        decoded = self.encoder.decode(encoded, key="")

        assert decoded == input_text

    def test_base64_encode_unicode_characters(self):
        """Test encoding text with unicode characters"""
        input_text = "Hello 世界 🌍"

        encoded = self.encoder.encode(input_text, key="")
        decoded = self.encoder.decode(encoded, key="")

        assert decoded == input_text

    def test_base64_decode_valid_string(self):
        """Test decoding a valid Base64 string"""
        encoded_text = "SGVsbG8gV29ybGQ="
        expected_output = "Hello World"

        result = self.encoder.decode(encoded_text, key="")

        assert result == expected_output

    def test_base64_encode_returns_string(self):
        """Test that encode method returns a string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)

    def test_base64_decode_returns_string(self):
        """Test that decode method returns a string"""
        result = self.encoder.decode("dGVzdA==", key="")
        assert isinstance(result, str)

