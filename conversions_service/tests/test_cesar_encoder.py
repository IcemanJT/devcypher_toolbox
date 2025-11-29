import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conversions_service')))

from services.cesar_encoder import CesarEncoder


class TestCesarEncoder:
    """Test suite for CesarEncoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup CesarEncoder instance for each test"""
        self.encoder = CesarEncoder()

    def test_cesar_encoder_properties(self):
        """Test CesarEncoder class properties"""
        assert self.encoder.name == "cesar"
        assert self.encoder.is_symmetric == True

    def test_cesar_encode_shift_3(self):
        """Test encoding with shift of 3 (classic Caesar cipher)"""
        input_text = "ABC"
        expected_output = "DEF"

        result = self.encoder.encode(input_text, key="3")

        assert result == expected_output

    def test_cesar_decode_shift_3(self):
        """Test decoding with shift of 3 (classic Caesar cipher)"""
        input_text = "DEF"
        expected_output = "ABC"

        result = self.encoder.decode(input_text, key="3")

        assert result == expected_output

    def test_cesar_encode_lowercase(self):
        """Test encoding lowercase text"""
        input_text = "abc"
        expected_output = "def"

        result = self.encoder.encode(input_text, key="3")

        assert result == expected_output

    def test_cesar_decode_lowercase(self):
        """Test decoding lowercase text"""
        input_text = "def"
        expected_output = "abc"

        result = self.encoder.decode(input_text, key="3")

        assert result == expected_output

    def test_cesar_encode_mixed_case(self):
        """Test encoding mixed case text"""
        input_text = "Hello"
        expected_output = "Khoor"

        result = self.encoder.encode(input_text, key="3")

        assert result == expected_output

    def test_cesar_decode_mixed_case(self):
        """Test decoding mixed case text"""
        input_text = "Khoor"
        expected_output = "Hello"

        result = self.encoder.decode(input_text, key="3")

        assert result == expected_output

    def test_cesar_encode_and_decode_roundtrip(self):
        """Test that encoding and then decoding returns the original text"""
        original_text = "DevCypher Toolbox"

        encoded = self.encoder.encode(original_text, key="5")
        decoded = self.encoder.decode(encoded, key="5")

        assert decoded == original_text

    def test_cesar_encode_wrap_around(self):
        """Test encoding with wrap around at end of alphabet"""
        input_text = "XYZ"
        expected_output = "ABC"

        result = self.encoder.encode(input_text, key="3")

        assert result == expected_output

    def test_cesar_decode_wrap_around(self):
        """Test decoding with wrap around at beginning of alphabet"""
        input_text = "ABC"
        expected_output = "XYZ"

        result = self.encoder.decode(input_text, key="3")

        assert result == expected_output

    def test_cesar_encode_shift_0(self):
        """Test encoding with shift of 0 (no change)"""
        input_text = "Hello"
        expected_output = "Hello"

        result = self.encoder.encode(input_text, key="0")

        assert result == expected_output

    def test_cesar_decode_shift_0(self):
        """Test decoding with shift of 0 (no change)"""
        input_text = "Hello"
        expected_output = "Hello"

        result = self.encoder.decode(input_text, key="0")

        assert result == expected_output

    def test_cesar_encode_shift_26(self):
        """Test encoding with shift of 26 (full rotation, no change)"""
        input_text = "Hello"
        expected_output = "Hello"

        result = self.encoder.encode(input_text, key="26")

        assert result == expected_output

    def test_cesar_decode_shift_26(self):
        """Test decoding with shift of 26 (full rotation, no change)"""
        input_text = "Hello"
        expected_output = "Hello"

        result = self.encoder.decode(input_text, key="26")

        assert result == expected_output

    def test_cesar_encode_large_shift(self):
        """Test encoding with shift larger than 26"""
        input_text = "ABC"
        # Shift 29 is equivalent to shift 3
        expected_output = "DEF"

        result = self.encoder.encode(input_text, key="29")

        assert result == expected_output

    def test_cesar_encode_negative_shift(self):
        """Test encoding with negative shift"""
        input_text = "DEF"
        expected_output = "ABC"

        result = self.encoder.encode(input_text, key="-3")

        assert result == expected_output

    def test_cesar_decode_negative_shift(self):
        """Test decoding with negative shift"""
        input_text = "ABC"
        expected_output = "DEF"

        result = self.encoder.decode(input_text, key="-3")

        assert result == expected_output

    def test_cesar_encode_empty_string(self):
        """Test encoding an empty string"""
        input_text = ""
        expected_output = ""

        result = self.encoder.encode(input_text, key="3")

        assert result == expected_output

    def test_cesar_decode_empty_string(self):
        """Test decoding an empty string"""
        input_text = ""
        expected_output = ""

        result = self.encoder.decode(input_text, key="3")

        assert result == expected_output

    def test_cesar_encode_preserves_non_alpha(self):
        """Test that non-alphabetic characters are preserved"""
        input_text = "Hello, World! 123"

        result = self.encoder.encode(input_text, key="3")

        assert "," in result
        assert "!" in result
        assert " " in result
        assert "123" in result

    def test_cesar_decode_preserves_non_alpha(self):
        """Test that non-alphabetic characters are preserved during decode"""
        input_text = "Khoor, Zruog! 123"

        result = self.encoder.decode(input_text, key="3")

        assert "," in result
        assert "!" in result
        assert " " in result
        assert "123" in result

    def test_cesar_encode_special_characters(self):
        """Test encoding text with special characters"""
        input_text = "Test@#$%"

        encoded = self.encoder.encode(input_text, key="5")
        decoded = self.encoder.decode(encoded, key="5")

        assert decoded == input_text

    def test_cesar_encode_returns_string(self):
        """Test that encode method returns a string"""
        result = self.encoder.encode("test", key="3")
        assert isinstance(result, str)

    def test_cesar_decode_returns_string(self):
        """Test that decode method returns a string"""
        result = self.encoder.decode("whvw", key="3")
        assert isinstance(result, str)

    def test_cesar_full_alphabet_encoding(self):
        """Test encoding the full alphabet with shift 13"""
        input_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        expected_output = "NOPQRSTUVWXYZABCDEFGHIJKLM"

        result = self.encoder.encode(input_text, key="13")

        assert result == expected_output

    def test_cesar_full_alphabet_decoding(self):
        """Test decoding the full alphabet with shift 13"""
        input_text = "NOPQRSTUVWXYZABCDEFGHIJKLM"
        expected_output = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        result = self.encoder.decode(input_text, key="13")

        assert result == expected_output

    def test_cesar_different_shifts_roundtrip(self):
        """Test roundtrip with various shift values"""
        original_text = "Hello World"

        for shift in [1, 5, 10, 13, 20, 25]:
            encoded = self.encoder.encode(original_text, key=str(shift))
            decoded = self.encoder.decode(encoded, key=str(shift))
            assert decoded == original_text, f"Failed for shift {shift}"
