import os
import hmac
import hashlib
import binascii

def hmac_hash(key, data):
    byte_key = binascii.unhexlify(key)
    data = data.encode('utf-8')
    return hmac.new(byte_key, data, hashlib.sha256).hexdigest()