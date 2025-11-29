import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conversions_service')))

from services.sha1_encoder import Sha1Encoder
from services.sha224_encoder import Sha224Encoder
from services.sha384_encoder import Sha384Encoder
from services.sha512_encoder import Sha512Encoder
from services.sha3_224_encoder import Sha3_224Encoder
from services.sha3_256_encoder import Sha3_256Encoder
from services.sha3_384_encoder import Sha3_384Encoder
from services.sha3_512_encoder import Sha3_512Encoder
from services.shake_128_encoder import Shake_128Encoder
from services.shake_256_encoder import Shake_256Encoder
from services.blake2b_encoder import Blake2bEncoder
from services.blake2s_encoder import Blake2sEncoder


class TestSha1Encoder:
    """Test suite for Sha1Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = Sha1Encoder()

    def test_sha1_encoder_properties(self):
        """Test Sha1Encoder class properties"""
        assert self.encoder.name == "sha1"
        assert self.encoder.is_symmetric == False

    def test_sha1_encode_simple_text(self):
        """Test encoding simple ASCII text"""
        result = self.encoder.encode("Hello World", key="")
        assert len(result) == 40
        assert all(c in '0123456789abcdef' for c in result)

    def test_sha1_encode_empty_string(self):
        """Test encoding empty string"""
        result = self.encoder.encode("", key="")
        assert result == "da39a3ee5e6b4b0d3255bfef95601890afd80709"

    def test_sha1_encode_returns_string(self):
        """Test that encode returns string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)


class TestSha224Encoder:
    """Test suite for Sha224Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = Sha224Encoder()

    def test_sha224_encoder_properties(self):
        """Test Sha224Encoder class properties"""
        assert self.encoder.name == "sha224"
        assert self.encoder.is_symmetric == False

    def test_sha224_encode_simple_text(self):
        """Test encoding simple ASCII text"""
        result = self.encoder.encode("Hello World", key="")
        assert len(result) == 56
        assert all(c in '0123456789abcdef' for c in result)

    def test_sha224_encode_empty_string(self):
        """Test encoding empty string"""
        result = self.encoder.encode("", key="")
        assert len(result) == 56

    def test_sha224_encode_returns_string(self):
        """Test that encode returns string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)


class TestSha384Encoder:
    """Test suite for Sha384Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = Sha384Encoder()

    def test_sha384_encoder_properties(self):
        """Test Sha384Encoder class properties"""
        assert self.encoder.name == "sha384"
        assert self.encoder.is_symmetric == False

    def test_sha384_encode_simple_text(self):
        """Test encoding simple ASCII text"""
        result = self.encoder.encode("Hello World", key="")
        assert len(result) == 96
        assert all(c in '0123456789abcdef' for c in result)

    def test_sha384_encode_empty_string(self):
        """Test encoding empty string"""
        result = self.encoder.encode("", key="")
        assert len(result) == 96

    def test_sha384_encode_returns_string(self):
        """Test that encode returns string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)


class TestSha512Encoder:
    """Test suite for Sha512Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = Sha512Encoder()

    def test_sha512_encoder_properties(self):
        """Test Sha512Encoder class properties"""
        assert self.encoder.name == "sha512"
        assert self.encoder.is_symmetric == False

    def test_sha512_encode_simple_text(self):
        """Test encoding simple ASCII text"""
        result = self.encoder.encode("Hello World", key="")
        assert len(result) == 128
        assert all(c in '0123456789abcdef' for c in result)

    def test_sha512_encode_empty_string(self):
        """Test encoding empty string"""
        result = self.encoder.encode("", key="")
        assert len(result) == 128

    def test_sha512_encode_returns_string(self):
        """Test that encode returns string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)


class TestSha3_224Encoder:
    """Test suite for Sha3_224Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = Sha3_224Encoder()

    def test_sha3_224_encoder_properties(self):
        """Test Sha3_224Encoder class properties"""
        assert self.encoder.name == "sha3_224"
        assert self.encoder.is_symmetric == False

    def test_sha3_224_encode_simple_text(self):
        """Test encoding simple ASCII text"""
        result = self.encoder.encode("Hello World", key="")
        assert len(result) == 56
        assert all(c in '0123456789abcdef' for c in result)

    def test_sha3_224_encode_empty_string(self):
        """Test encoding empty string"""
        result = self.encoder.encode("", key="")
        assert len(result) == 56

    def test_sha3_224_encode_returns_string(self):
        """Test that encode returns string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)


class TestSha3_256Encoder:
    """Test suite for Sha3_256Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = Sha3_256Encoder()

    def test_sha3_256_encoder_properties(self):
        """Test Sha3_256Encoder class properties"""
        assert self.encoder.name == "sha3_256"
        assert self.encoder.is_symmetric == False

    def test_sha3_256_encode_simple_text(self):
        """Test encoding simple ASCII text"""
        result = self.encoder.encode("Hello World", key="")
        assert len(result) == 64
        assert all(c in '0123456789abcdef' for c in result)

    def test_sha3_256_encode_empty_string(self):
        """Test encoding empty string"""
        result = self.encoder.encode("", key="")
        assert len(result) == 64

    def test_sha3_256_encode_returns_string(self):
        """Test that encode returns string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)


class TestSha3_384Encoder:
    """Test suite for Sha3_384Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = Sha3_384Encoder()

    def test_sha3_384_encoder_properties(self):
        """Test Sha3_384Encoder class properties"""
        assert self.encoder.name == "sha3_384"
        assert self.encoder.is_symmetric == False

    def test_sha3_384_encode_simple_text(self):
        """Test encoding simple ASCII text"""
        result = self.encoder.encode("Hello World", key="")
        assert len(result) == 96
        assert all(c in '0123456789abcdef' for c in result)

    def test_sha3_384_encode_empty_string(self):
        """Test encoding empty string"""
        result = self.encoder.encode("", key="")
        assert len(result) == 96

    def test_sha3_384_encode_returns_string(self):
        """Test that encode returns string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)


class TestSha3_512Encoder:
    """Test suite for Sha3_512Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = Sha3_512Encoder()

    def test_sha3_512_encoder_properties(self):
        """Test Sha3_512Encoder class properties"""
        assert self.encoder.name == "sha3_512"
        assert self.encoder.is_symmetric == False

    def test_sha3_512_encode_simple_text(self):
        """Test encoding simple ASCII text"""
        result = self.encoder.encode("Hello World", key="")
        assert len(result) == 128
        assert all(c in '0123456789abcdef' for c in result)

    def test_sha3_512_encode_empty_string(self):
        """Test encoding empty string"""
        result = self.encoder.encode("", key="")
        assert len(result) == 128

    def test_sha3_512_encode_returns_string(self):
        """Test that encode returns string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)


class TestShake128Encoder:
    """Test suite for Shake_128Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = Shake_128Encoder()

    def test_shake_128_encoder_properties(self):
        """Test Shake_128Encoder class properties"""
        assert self.encoder.name == "shake_128"
        assert self.encoder.is_symmetric == False

    def test_shake_128_encode_simple_text(self):
        """Test encoding simple ASCII text"""
        result = self.encoder.encode("Hello World", key="")
        # Default output length is 32 bytes = 64 hex chars
        assert len(result) == 64
        assert all(c in '0123456789abcdef' for c in result)

    def test_shake_128_encode_empty_string(self):
        """Test encoding empty string"""
        result = self.encoder.encode("", key="")
        assert len(result) == 64

    def test_shake_128_encode_returns_string(self):
        """Test that encode returns string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)

    def test_shake_128_custom_output_length(self):
        """Test encoding with custom output length"""
        result = self.encoder.encode("test", key="", output_length=16)
        assert len(result) == 32  # 16 bytes = 32 hex chars


class TestShake256Encoder:
    """Test suite for Shake_256Encoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = Shake_256Encoder()

    def test_shake_256_encoder_properties(self):
        """Test Shake_256Encoder class properties"""
        assert self.encoder.name == "shake_256"
        assert self.encoder.is_symmetric == False

    def test_shake_256_encode_simple_text(self):
        """Test encoding simple ASCII text"""
        result = self.encoder.encode("Hello World", key="")
        # Default output length is 64 bytes = 128 hex chars
        assert len(result) == 128
        assert all(c in '0123456789abcdef' for c in result)

    def test_shake_256_encode_empty_string(self):
        """Test encoding empty string"""
        result = self.encoder.encode("", key="")
        assert len(result) == 128

    def test_shake_256_encode_returns_string(self):
        """Test that encode returns string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)

    def test_shake_256_custom_output_length(self):
        """Test encoding with custom output length"""
        result = self.encoder.encode("test", key="", output_length=32)
        assert len(result) == 64  # 32 bytes = 64 hex chars


class TestBlake2bEncoder:
    """Test suite for Blake2bEncoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = Blake2bEncoder()

    def test_blake2b_encoder_properties(self):
        """Test Blake2bEncoder class properties"""
        assert self.encoder.name == "blake2b"
        assert self.encoder.is_symmetric == False

    def test_blake2b_encode_simple_text(self):
        """Test encoding simple ASCII text"""
        result = self.encoder.encode("Hello World", key="")
        # BLAKE2b default is 64 bytes = 128 hex chars
        assert len(result) == 128
        assert all(c in '0123456789abcdef' for c in result)

    def test_blake2b_encode_empty_string(self):
        """Test encoding empty string"""
        result = self.encoder.encode("", key="")
        assert len(result) == 128

    def test_blake2b_encode_returns_string(self):
        """Test that encode returns string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)


class TestBlake2sEncoder:
    """Test suite for Blake2sEncoder service"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = Blake2sEncoder()

    def test_blake2s_encoder_properties(self):
        """Test Blake2sEncoder class properties"""
        assert self.encoder.name == "blake2s"
        assert self.encoder.is_symmetric == False

    def test_blake2s_encode_simple_text(self):
        """Test encoding simple ASCII text"""
        result = self.encoder.encode("Hello World", key="")
        # BLAKE2s default is 32 bytes = 64 hex chars
        assert len(result) == 64
        assert all(c in '0123456789abcdef' for c in result)

    def test_blake2s_encode_empty_string(self):
        """Test encoding empty string"""
        result = self.encoder.encode("", key="")
        assert len(result) == 64

    def test_blake2s_encode_returns_string(self):
        """Test that encode returns string"""
        result = self.encoder.encode("test", key="")
        assert isinstance(result, str)
