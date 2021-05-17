import time
import json
import hashlib
import math
from random import random as frand

class Block:
    def __init__(self, prevHash, transaction, timeStamp=None):
        self._prevHash = prevHash
        self._transactions = []
        self._time = timeStamp or math.floor(time.time() * 1000.0)

        self.nonce = frand() * 999999999

    def hash(self):
        bstr = self.__str__()
        return hashlib.sha256(self.__str__().encode("utf-8")).hexdigest()

    def __jdata__(self):
        return {"prev_hash": self._prevHash, "_transaction": self._transaction.__jdata__(), "time": self._time}

    def __str__(self):
        _str = json.dumps(self.__jdata__(), separators=(',',':'))
        return _str

    def log(self):
        _data = json.loads(self.__str__())
        print("BLOCK:\n%s" % (json.dumps(_data, indent=4, sort_keys=True)))
