import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conversions_service')))

from services.rot13_encoder import Rot13Encoder


class TestRot13Encoder:
    """Test suite for Rot13Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup Rot13Encoder instance for each test"""
        self.encoder = Rot13Encoder()

    def test_rot13_encoder_properties(self):
        """Test Rot13Encoder class properties"""
        assert self.encoder.name == "rot13"
        assert self.encoder.is_symmetric == True

    def test_rot13_encode_simple_text(self):
        """Test encoding simple ASCII text with ROT13"""
        input_text = "ABC"
        expected_output = "NOP"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_rot13_decode_simple_text(self):
        """Test decoding simple ASCII text with ROT13"""
        input_text = "NOP"
        expected_output = "ABC"

        result = self.encoder.decode(input_text, key="")

        assert result == expected_output

    def test_rot13_encode_lowercase(self):
        """Test encoding lowercase text"""
        input_text = "abc"
        expected_output = "nop"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_rot13_decode_lowercase(self):
        """Test decoding lowercase text"""
        input_text = "nop"
        expected_output = "abc"

        result = self.encoder.decode(input_text, key="")

        assert result == expected_output

    def test_rot13_encode_mixed_case(self):
        """Test encoding mixed case text"""
        input_text = "Hello"
        expected_output = "Uryyb"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_rot13_decode_mixed_case(self):
        """Test decoding mixed case text"""
        input_text = "Uryyb"
        expected_output = "Hello"

        result = self.encoder.decode(input_text, key="")

        assert result == expected_output

    def test_rot13_encode_and_decode_roundtrip(self):
        """Test that encoding and then decoding returns the original text"""
        original_text = "DevCypher Toolbox"

        encoded = self.encoder.encode(original_text, key="")
        decoded = self.encoder.decode(encoded, key="")

        assert decoded == original_text

    def test_rot13_symmetric_property(self):
        """Test that ROT13 is symmetric (encode equals decode operation)"""
        text = "Hello World"

        # Applying ROT13 twice should return the original
        encoded = self.encoder.encode(text, key="")
        double_encoded = self.encoder.encode(encoded, key="")

        assert double_encoded == text

    def test_rot13_encode_decode_equivalence(self):
        """Test that encode and decode produce the same result"""
        text = "Test String"

        encoded = self.encoder.encode(text, key="")
        decoded = self.encoder.decode(text, key="")

        assert encoded == decoded

    def test_rot13_encode_empty_string(self):
        """Test encoding an empty string"""
        input_text = ""
        expected_output = ""

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_rot13_decode_empty_string(self):
        """Test decoding an empty string"""
        input_text = ""
        expected_output = ""

        result = self.encoder.decode(input_text, key="")

        assert result == expected_output

    def test_rot13_encode_preserves_non_alpha(self):
        """Test that non-alphabetic characters are preserved"""
        input_text = "Hello, World! 123"

        result = self.encoder.encode(input_text, key="")

        assert "," in result
        assert "!" in result
        assert " " in result
        assert "123" in result

    def test_rot13_decode_preserves_non_alpha(self):
        """Test that non-alphabetic characters are preserved during decode"""
        input_text = "Uryyb, Jbeyq! 123"

        result = self.encoder.decode(input_text, key="")

        assert "," in result
        assert "!" in result
        assert " " in result
        assert "123" in result

    def test_rot13_encode_special_characters(self):
        """Test encoding text with special characters"""
        input_text = "Test@#$%"

        encoded = self.encoder.encode(input_text, key="")
        decoded = self.encoder.decode(encoded, key="")

        assert decoded == input_text

    def test_rot13_encode_returns_string(self):
        """Test that encode method returns a string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)

    def test_rot13_decode_returns_string(self):
        """Test that decode method returns a string"""
        result = self.encoder.decode("grfg", key="")
        assert isinstance(result, str)

    def test_rot13_full_alphabet_encoding(self):
        """Test encoding the full alphabet"""
        input_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        expected_output = "NOPQRSTUVWXYZABCDEFGHIJKLM"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_rot13_full_alphabet_decoding(self):
        """Test decoding the full alphabet"""
        input_text = "NOPQRSTUVWXYZABCDEFGHIJKLM"
        expected_output = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        result = self.encoder.decode(input_text, key="")

        assert result == expected_output

    def test_rot13_known_phrase(self):
        """Test encoding a known phrase"""
        input_text = "The Quick Brown Fox"
        expected_output = "Gur Dhvpx Oebja Sbk"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_rot13_key_is_ignored(self):
        """Test that the key parameter is ignored in ROT13"""
        text = "Hello"

        result_no_key = self.encoder.encode(text, key="")
        result_with_key = self.encoder.encode(text, key="any_key")

        assert result_no_key == result_with_key
