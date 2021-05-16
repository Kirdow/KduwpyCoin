import json
import Utils

class Transaction:
    def __init__(self, amount, spender, receiver):
        self.amount = amount
        self.spender = spender
        self.receiver = receiver

    def __jdata__(self):
        return {"amount": self.amount, "spender": Utils.get_rsa_str(self.spender), "receiver": Utils.get_rsa_str(self.receiver)}

    def __str__(self):
        return json.dumps(self.__jdata__(), separators=(',', ':'))

