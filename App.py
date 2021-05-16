from Wallet import *
from Chain import *
from Block import *
from Transaction import *

class App:
    def __init__(self):
        pass

    def run(self):
        kirdow = Wallet()
        bob = Wallet()
        alice = Wallet()
        kirdow.sendMoney(50, bob.publicKey)
        bob.sendMoney(23, alice.publicKey)
        alice.sendMoney(5, bob.publicKey)
