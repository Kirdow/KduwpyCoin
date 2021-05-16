from Block import Block
from Transaction import Transaction
from Crypto.Hash import SHA256
import Utils

import time

class Chain:
    def __init__(self):
        self.chain = [Block('', Transaction(100, 'genesis', 'kirdow'))]

    def lastBlock(self):
        return self.chain[-1]

    def mine(self, nonce):
        solution = -1
        print("Mining...")

        timer = 0.0
        timert = 0.0
        timerl = -1.0
        while True:
            hash = SHA256.new(str(nonce + solution).encode("utf-8"))
            attempt = hash.hexdigest()

            if attempt[0:4] == "0000":
                print("Solved in %.5f | Solution: %d" % (timer, solution))
                return solution

            timen = time.time()
            if timerl < 0.0:
                timerl = timen
            timed = timen - timerl
            timerl = timen

            timert += timed
            timer += timed

            if timert >= 0.2:
                timert -= 0.2
                print("Time Passed: %.3f" % timer)

            solution += 1

    def addBlock(self, transaction, senderPublicKey, signature):
        if Utils.verify_sign_with_rsa256(senderPublicKey, signature, transaction.__str__().encode("utf-8")):
            newBlock = Block(self.lastBlock().hash(), transaction)
            self.mine(newBlock.nonce)
            newBlock.log()
            self.chain.append(newBlock)
        

CHAIN_INST = Chain()