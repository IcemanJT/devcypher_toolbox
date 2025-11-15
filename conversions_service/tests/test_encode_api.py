import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conversions_service')))

from services.encode_api import EncodeApi


class TestEncodeApi:
    """Test suite for EncodeApi service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup EncodeApi instance for each test"""
        self.api = EncodeApi.get_instance()

    def test_encode_api_singleton(self):
        """Test that EncodeApi follows singleton pattern"""
        api1 = EncodeApi.get_instance()
        api2 = EncodeApi.get_instance()

        assert api1 is api2

    def test_encode_api_initialization(self):
        """Test that EncodeApi initializes with services"""
        assert self.api.services is not None
        assert isinstance(self.api.services, dict)
        assert len(self.api.services) > 0

    def test_available_encode_ciphers(self):
        """Test that available encode ciphers are returned"""
        ciphers = self.api.available_encode_ciphers

        assert isinstance(ciphers, list)
        assert "base64" in ciphers

    def test_available_decode_ciphers(self):
        """Test that available decode ciphers are returned (only symmetric)"""
        ciphers = self.api.available_decode_ciphers

        assert isinstance(ciphers, list)
        # Base64 is symmetric, so it should be in decode ciphers
        assert "base64" in ciphers

    def test_encode_with_base64(self):
        """Test encoding text with Base64 method"""
        data = {
            "method": "base64",
            "data": "Hello World",
            "key": ""
        }

        result = self.api.encode(data)

        assert result == "SGVsbG8gV29ybGQ="

    def test_decode_with_base64(self):
        """Test decoding text with Base64 method"""
        data = {
            "method": "base64",
            "data": "SGVsbG8gV29ybGQ=",
            "key": ""
        }

        result = self.api.decode(data)

        assert result == "Hello World"

    def test_encode_decode_roundtrip(self):
        """Test that encode and decode work together"""
        original_text = "DevCypher Toolbox Test"

        encode_data = {
            "method": "base64",
            "data": original_text,
            "key": ""
        }

        encoded = self.api.encode(encode_data)

        decode_data = {
            "method": "base64",
            "data": encoded,
            "key": ""
        }

        decoded = self.api.decode(decode_data)

        assert decoded == original_text

    def test_encode_without_method_raises_error(self):
        """Test that encoding without method raises ValueError"""
        data = {
            "data": "Test data"
        }

        with pytest.raises(ValueError, match="Cipher and data must be provided for encoding"):
            self.api.encode(data)

    def test_encode_without_data_raises_error(self):
        """Test that encoding without data raises ValueError"""
        data = {
            "method": "base64"
        }

        with pytest.raises(ValueError, match="Cipher and data must be provided for encoding"):
            self.api.encode(data)

    def test_decode_without_method_raises_error(self):
        """Test that decoding without method raises ValueError"""
        data = {
            "data": "SGVsbG8gV29ybGQ="
        }

        with pytest.raises(ValueError, match="Cipher and data must be provided for decoding"):
            self.api.decode(data)

    def test_decode_without_data_raises_error(self):
        """Test that decoding without data raises ValueError"""
        data = {
            "method": "base64"
        }

        with pytest.raises(ValueError, match="Cipher and data must be provided for decoding"):
            self.api.decode(data)

    def test_encode_with_whitespace_data(self):
        """Test encoding whitespace string"""
        data = {
            "method": "base64",
            "data": "   ",
            "key": ""
        }

        result = self.api.encode(data)

        # Whitespace should be encoded
        assert isinstance(result, str)
        assert len(result) > 0

    def test_encode_with_optional_key(self):
        """Test encoding without providing key (should use default empty string)"""
        data = {
            "method": "base64",
            "data": "Test"
        }

        result = self.api.encode(data)

        assert isinstance(result, str)
        assert len(result) > 0

    def test_encode_with_options(self):
        """Test encoding with additional options parameter"""
        data = {
            "method": "base64",
            "data": "Test with options",
            "key": "",
            "options": {}
        }

        result = self.api.encode(data)

        assert isinstance(result, str)

    def test_encode_special_characters(self):
        """Test encoding text with special characters"""
        data = {
            "method": "base64",
            "data": "Hello! @#$%^&*()",
            "key": ""
        }

        encoded = self.api.encode(data)

        decode_data = {
            "method": "base64",
            "data": encoded,
            "key": ""
        }

        decoded = self.api.decode(decode_data)

        assert decoded == "Hello! @#$%^&*()"

    def test_encode_unicode_characters(self):
        """Test encoding text with unicode characters"""
        data = {
            "method": "base64",
            "data": "Hello 世界 🌍",
            "key": ""
        }

        encoded = self.api.encode(data)

        decode_data = {
            "method": "base64",
            "data": encoded,
            "key": ""
        }

        decoded = self.api.decode(decode_data)

        assert decoded == "Hello 世界 🌍"

    def test_services_loaded_correctly(self):
        """Test that services dictionary contains Base64Encoder"""
        assert "base64" in self.api.services
        assert hasattr(self.api.services["base64"], "encode")
        assert hasattr(self.api.services["base64"], "decode")

    def test_encode_invalid_method_raises_error(self):
        """Test that using invalid method raises KeyError"""
        data = {
            "method": "invalid_cipher",
            "data": "Test",
            "key": ""
        }

        with pytest.raises(KeyError):
            self.api.encode(data)

