import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conversions_service')))

from services.atbash_encoder import AtbashEncoder


class TestAtbashEncoder:
    """Test suite for AtbashEncoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup AtbashEncoder instance for each test"""
        self.encoder = AtbashEncoder()

    def test_atbash_encoder_properties(self):
        """Test AtbashEncoder class properties"""
        assert self.encoder.name == "atbash"
        assert self.encoder.is_symmetric == True

    def test_atbash_encode_simple_text(self):
        """Test encoding simple ASCII text with Atbash cipher"""
        input_text = "ABC"
        expected_output = "ZYX"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_atbash_encode_lowercase(self):
        """Test encoding lowercase text with Atbash cipher"""
        input_text = "abc"
        expected_output = "zyx"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_atbash_encode_mixed_case(self):
        """Test encoding mixed case text with Atbash cipher"""
        input_text = "Hello"
        expected_output = "Svool"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_atbash_decode_simple_text(self):
        """Test decoding simple ASCII text with Atbash cipher"""
        input_text = "ZYX"
        expected_output = "ABC"

        result = self.encoder.decode(input_text, key="")

        assert result == expected_output

    def test_atbash_decode_lowercase(self):
        """Test decoding lowercase text with Atbash cipher"""
        input_text = "zyx"
        expected_output = "abc"

        result = self.encoder.decode(input_text, key="")

        assert result == expected_output

    def test_atbash_decode_mixed_case(self):
        """Test decoding mixed case text with Atbash cipher"""
        input_text = "Svool"
        expected_output = "Hello"

        result = self.encoder.decode(input_text, key="")

        assert result == expected_output

    def test_atbash_encode_and_decode_roundtrip(self):
        """Test that encoding and then decoding returns the original text"""
        original_text = "DevCypher Toolbox"

        encoded = self.encoder.encode(original_text, key="")
        decoded = self.encoder.decode(encoded, key="")

        assert decoded == original_text

    def test_atbash_symmetric_property(self):
        """Test that Atbash is symmetric (encode equals decode)"""
        text = "Hello World"

        encoded = self.encoder.encode(text, key="")
        decoded = self.encoder.decode(text, key="")

        assert encoded == decoded

    def test_atbash_encode_empty_string(self):
        """Test encoding an empty string"""
        input_text = ""
        expected_output = ""

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_atbash_decode_empty_string(self):
        """Test decoding an empty string"""
        input_text = ""
        expected_output = ""

        result = self.encoder.decode(input_text, key="")

        assert result == expected_output

    def test_atbash_encode_preserves_non_alpha(self):
        """Test that non-alphabetic characters are preserved"""
        input_text = "Hello, World! 123"

        result = self.encoder.encode(input_text, key="")

        assert "," in result
        assert "!" in result
        assert " " in result
        assert "123" in result

    def test_atbash_decode_preserves_non_alpha(self):
        """Test that non-alphabetic characters are preserved during decode"""
        input_text = "Svool, Dliow! 123"

        result = self.encoder.decode(input_text, key="")

        assert "," in result
        assert "!" in result
        assert " " in result
        assert "123" in result

    def test_atbash_encode_special_characters(self):
        """Test encoding text with special characters"""
        input_text = "Test@#$%"

        encoded = self.encoder.encode(input_text, key="")
        decoded = self.encoder.decode(encoded, key="")

        assert decoded == input_text

    def test_atbash_encode_returns_string(self):
        """Test that encode method returns a string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)

    def test_atbash_decode_returns_string(self):
        """Test that decode method returns a string"""
        result = self.encoder.decode("gvhg", key="")
        assert isinstance(result, str)

    def test_atbash_full_alphabet_encoding(self):
        """Test encoding the full alphabet"""
        input_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        expected_output = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_atbash_full_alphabet_decoding(self):
        """Test decoding the full alphabet"""
        input_text = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
        expected_output = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        result = self.encoder.decode(input_text, key="")

        assert result == expected_output
