import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conversions_service')))

from services.md5_encoder import MD5Encoder
from services.sha1_encoder import Sha1Encoder
from services.sha224_encoder import Sha224Encoder
from services.sha256_encoder import Sha256Encoder
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


class TestHashDecoders:
    """Test suite to verify hash functions raise NotImplementedError on decode"""

    def test_md5_decode_raises_not_implemented(self):
        """Test that MD5 decode raises NotImplementedError"""
        encoder = MD5Encoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_sha1_decode_raises_not_implemented(self):
        """Test that SHA1 decode raises NotImplementedError"""
        encoder = Sha1Encoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_sha224_decode_raises_not_implemented(self):
        """Test that SHA224 decode raises NotImplementedError"""
        encoder = Sha224Encoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_sha256_decode_raises_not_implemented(self):
        """Test that SHA256 decode raises NotImplementedError"""
        encoder = Sha256Encoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_sha384_decode_raises_not_implemented(self):
        """Test that SHA384 decode raises NotImplementedError"""
        encoder = Sha384Encoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_sha512_decode_raises_not_implemented(self):
        """Test that SHA512 decode raises NotImplementedError"""
        encoder = Sha512Encoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_sha3_224_decode_raises_not_implemented(self):
        """Test that SHA3-224 decode raises NotImplementedError"""
        encoder = Sha3_224Encoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_sha3_256_decode_raises_not_implemented(self):
        """Test that SHA3-256 decode raises NotImplementedError"""
        encoder = Sha3_256Encoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_sha3_384_decode_raises_not_implemented(self):
        """Test that SHA3-384 decode raises NotImplementedError"""
        encoder = Sha3_384Encoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_sha3_512_decode_raises_not_implemented(self):
        """Test that SHA3-512 decode raises NotImplementedError"""
        encoder = Sha3_512Encoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_shake_128_decode_raises_not_implemented(self):
        """Test that SHAKE-128 decode raises NotImplementedError"""
        encoder = Shake_128Encoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_shake_256_decode_raises_not_implemented(self):
        """Test that SHAKE-256 decode raises NotImplementedError"""
        encoder = Shake_256Encoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_blake2b_decode_raises_not_implemented(self):
        """Test that BLAKE2b decode raises NotImplementedError"""
        encoder = Blake2bEncoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")

    def test_blake2s_decode_raises_not_implemented(self):
        """Test that BLAKE2s decode raises NotImplementedError"""
        encoder = Blake2sEncoder()
        with pytest.raises(NotImplementedError):
            encoder.decode("test", key="")


class TestHashEncodersIsNotSymmetric:
    """Test suite to verify hash functions have is_symmetric=False"""

    def test_md5_is_not_symmetric(self):
        """Test that MD5 is not symmetric"""
        encoder = MD5Encoder()
        assert encoder.is_symmetric == False

    def test_sha1_is_not_symmetric(self):
        """Test that SHA1 is not symmetric"""
        encoder = Sha1Encoder()
        assert encoder.is_symmetric == False

    def test_sha224_is_not_symmetric(self):
        """Test that SHA224 is not symmetric"""
        encoder = Sha224Encoder()
        assert encoder.is_symmetric == False

    def test_sha256_is_not_symmetric(self):
        """Test that SHA256 is not symmetric"""
        encoder = Sha256Encoder()
        assert encoder.is_symmetric == False

    def test_sha384_is_not_symmetric(self):
        """Test that SHA384 is not symmetric"""
        encoder = Sha384Encoder()
        assert encoder.is_symmetric == False

    def test_sha512_is_not_symmetric(self):
        """Test that SHA512 is not symmetric"""
        encoder = Sha512Encoder()
        assert encoder.is_symmetric == False

    def test_sha3_224_is_not_symmetric(self):
        """Test that SHA3-224 is not symmetric"""
        encoder = Sha3_224Encoder()
        assert encoder.is_symmetric == False

    def test_sha3_256_is_not_symmetric(self):
        """Test that SHA3-256 is not symmetric"""
        encoder = Sha3_256Encoder()
        assert encoder.is_symmetric == False

    def test_sha3_384_is_not_symmetric(self):
        """Test that SHA3-384 is not symmetric"""
        encoder = Sha3_384Encoder()
        assert encoder.is_symmetric == False

    def test_sha3_512_is_not_symmetric(self):
        """Test that SHA3-512 is not symmetric"""
        encoder = Sha3_512Encoder()
        assert encoder.is_symmetric == False

    def test_shake_128_is_not_symmetric(self):
        """Test that SHAKE-128 is not symmetric"""
        encoder = Shake_128Encoder()
        assert encoder.is_symmetric == False

    def test_shake_256_is_not_symmetric(self):
        """Test that SHAKE-256 is not symmetric"""
        encoder = Shake_256Encoder()
        assert encoder.is_symmetric == False

    def test_blake2b_is_not_symmetric(self):
        """Test that BLAKE2b is not symmetric"""
        encoder = Blake2bEncoder()
        assert encoder.is_symmetric == False

    def test_blake2s_is_not_symmetric(self):
        """Test that BLAKE2s is not symmetric"""
        encoder = Blake2sEncoder()
        assert encoder.is_symmetric == False
