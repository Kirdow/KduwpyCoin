from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base62

def sign_with_rsa256(private_key, bdata):
    digest = SHA256.new()
    digest.update(bdata)

    signer = PKCS1_v1_5.new(private_key)
    sig = signer.sign(digest)

    return sig

def verify_sign_with_rsa256(public_key, sig, bdata):
    digest = SHA256.new()
    digest.update(bdata)

    return verify_rsa_sign(public_key, sig, digest)

def verify_rsa_sign(public_key, sig, digest):
    verifier = PKCS1_v1_5.new(public_key)
    return verifier.verify(digest, sig)

def get_rsa_str(key):
    if type(key) == str:
        return key
    return base62.encodebytes(key.export_key('DER'))