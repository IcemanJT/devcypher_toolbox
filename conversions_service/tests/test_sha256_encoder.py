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

    def test_sha256_encode_is_deterministic(self):
        """Test that encoding the same text multiple times produces the same hash"""
        input_text = "Deterministic Test"

        result1 = self.encoder.encode(input_text, key="")
        result2 = self.encoder.encode(input_text, key="")
        result3 = self.encoder.encode(input_text, key="")

        assert result1 == result2 == result3

    def test_sha256_encode_different_inputs_different_hashes(self):
        """Test that different inputs produce different hashes"""
        result1 = self.encoder.encode("test1", key="")
        result2 = self.encoder.encode("test2", key="")

        assert result1 != result2

    def test_sha256_encode_case_sensitive(self):
        """Test that SHA256 hashing is case-sensitive"""
        result_lower = self.encoder.encode("hello", key="")
        result_upper = self.encoder.encode("HELLO", key="")

        assert result_lower != result_upper

    def test_sha256_encode_key_parameter_ignored(self):
        """Test that key parameter is ignored for SHA256 (doesn't affect output)"""
        input_text = "Test"

        result_with_key = self.encoder.encode(input_text, key="some_key")
        result_without_key = self.encoder.encode(input_text, key="")

        assert result_with_key == result_without_key

    def test_sha256_decode_raises_not_implemented(self):
        """Test that decode method raises NotImplementedError"""
        with pytest.raises(NotImplementedError, match="SHA256 is a one-way hash function"):
            self.encoder.decode("a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e", key="")

    def test_sha256_encode_returns_string(self):
        """Test that encode method returns a string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)

    def test_sha256_encode_long_text(self):
        """Test encoding longer text"""
        input_text = "This is a longer text to test the SHA256 hashing functionality with more content. " * 10

        result = self.encoder.encode(input_text, key="")

        # SHA256 always produces 64 character hash regardless of input length
        assert len(result) == 64

    def test_sha256_encode_known_hash(self):
        """Test encoding with known SHA256 hash value"""
        input_text = "password"
        # Well-known SHA256 hash of "password"
        expected_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

        result = self.encoder.encode(input_text, key="")

        assert result == expected_hash

    def test_sha256_vs_md5_different_outputs(self):
        """Test that SHA256 produces different output than MD5 for same input"""
        from services.md5_encoder import Md5Encoder

        md5_encoder = Md5Encoder()
        input_text = "test"

        sha256_result = self.encoder.encode(input_text, key="")
        md5_result = md5_encoder.encode(input_text, key="")

        # SHA256 is 64 chars, MD5 is 32 chars
        assert len(sha256_result) == 64
        assert len(md5_result) == 32
        assert sha256_result != md5_result

