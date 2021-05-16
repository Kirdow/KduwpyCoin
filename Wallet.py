import Crypto, Utils
from Crypto.PublicKey import RSA
from Transaction import Transaction
from Chain import Chain,CHAIN_INST

class Wallet:
    def __init__(self):
        key = RSA.generate(2048)
        self.privateKey = key
        self.publicKey = key.publickey()

    def sendMoney(self, amount, receiver):
        transact = Transaction(amount, self.publicKey, receiver)

        signature = Utils.sign_with_rsa256(self.privateKey, transact.__str__().encode("utf-8"))
        CHAIN_INST.addBlock(transact, self.publicKey, signature)

