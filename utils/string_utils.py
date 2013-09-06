__author__ = 'noah'

import hashlib

def md5(str):
    m = hashlib.md5(str)
    m.digest()
    return m.hexdigest()