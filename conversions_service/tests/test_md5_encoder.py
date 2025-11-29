import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conversions_service')))

from services.md5_encoder import MD5Encoder


class TestMd5Encoder:
    """Test suite for Md5Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup Md5Encoder instance for each test"""
        self.encoder = MD5Encoder()

    def test_md5_encode_simple_text(self):
        """Test encoding simple ASCII text to MD5 hash"""
        input_text = "Hello World"
        # MD5 hash of "Hello World"
        expected_output = "b10a8db164e0754105b7a99be72e3fe5"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_md5_encoder_properties(self):
        """Test Md5Encoder class properties"""
        assert self.encoder.name == "md5"
        assert self.encoder.is_symmetric == False

    def test_md5_encode_returns_32_char_hex(self):
        """Test that MD5 hash always returns 32 character hexadecimal string"""
        result = self.encoder.encode("test", key="")

        assert len(result) == 32
        assert all(c in '0123456789abcdef' for c in result)

    def test_md5_encode_empty_string(self):
        """Test encoding an empty string"""
        input_text = ""
        # MD5 hash of empty string
        expected_output = "d41d8cd98f00b204e9800998ecf8427e"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_output

    def test_md5_encode_special_characters(self):
        """Test encoding text with special characters"""
        input_text = "Hello! @#$%^&*()"

        result = self.encoder.encode(input_text, key="")

        assert isinstance(result, str)
        assert len(result) == 32

    def test_md5_encode_numbers(self):
        """Test encoding text with numbers"""
        input_text = "Test123456"

        result = self.encoder.encode(input_text, key="")

        assert isinstance(result, str)
        assert len(result) == 32

    def test_md5_encode_unicode_characters(self):
        """Test encoding text with unicode characters"""
        input_text = "Hello 世界 🌍"

        result = self.encoder.encode(input_text, key="")

        assert isinstance(result, str)
        assert len(result) == 32

    def test_md5_encode_is_deterministic(self):
        """Test that encoding the same text multiple times produces the same hash"""
        input_text = "Deterministic Test"

        result1 = self.encoder.encode(input_text, key="")
        result2 = self.encoder.encode(input_text, key="")
        result3 = self.encoder.encode(input_text, key="")

        assert result1 == result2 == result3

    def test_md5_encode_different_inputs_different_hashes(self):
        """Test that different inputs produce different hashes"""
        result1 = self.encoder.encode("test1", key="")
        result2 = self.encoder.encode("test2", key="")

        assert result1 != result2

    def test_md5_encode_case_sensitive(self):
        """Test that MD5 hashing is case-sensitive"""
        result_lower = self.encoder.encode("hello", key="")
        result_upper = self.encoder.encode("HELLO", key="")

        assert result_lower != result_upper

    def test_md5_encode_key_parameter_ignored(self):
        """Test that key parameter is ignored for MD5 (doesn't affect output)"""
        input_text = "Test"

        result_with_key = self.encoder.encode(input_text, key="some_key")
        result_without_key = self.encoder.encode(input_text, key="")

        assert result_with_key == result_without_key

    def test_md5_decode_raises_not_implemented(self):
        """Test that decode method raises NotImplementedError"""
        with pytest.raises(NotImplementedError, match="MD5 is a one-way hash function"):
            self.encoder.decode("b10a8db164e0754105b7a99be72e3fe5", key="")

    def test_md5_encode_returns_string(self):
        """Test that encode method returns a string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)

    def test_md5_encode_long_text(self):
        """Test encoding longer text"""
        input_text = "This is a longer text to test the MD5 hashing functionality with more content. " * 10

        result = self.encoder.encode(input_text, key="")

        # MD5 always produces 32 character hash regardless of input length
        assert len(result) == 32

    def test_md5_encode_known_hash(self):
        """Test encoding with known MD5 hash value"""
        input_text = "password"
        # Well-known MD5 hash of "password"
        expected_hash = "5f4dcc3b5aa765d61d8327deb882cf99"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_hash

