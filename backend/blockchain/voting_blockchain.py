# voting_blockchain.py
from .block import Block
from .biometric_data import BiometricData
import time

class VotingBlockchain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), None, "Bloco gênesis")
        genesis_block.proof_of_work(self.difficulty)
        self.blocks.append(genesis_block)

    def latest_block(self):
        return self.blocks[-1]

    def new_block(self, data):
        if not isinstance(data, BiometricData):
            raise ValueError("Os dados devem ser do tipo BiometricData")
        latest_block = self.latest_block()
        return Block(latest_block.index + 1, time.time(), latest_block.hash, data)

    def add_block(self, block):
        if block and self.is_valid_new_block(block, self.latest_block()):
            block.proof_of_work(self.difficulty)
            self.blocks.append(block)

    def is_first_block_valid(self):
        first_block = self.blocks[0]
        return (first_block.index == 0 and
                first_block.previous_hash is None and
                first_block.hash == first_block.calculate_hash())

    def is_valid_new_block(self, new_block, previous_block):
        return (new_block and previous_block and
                previous_block.index + 1 == new_block.index and
                new_block.previous_hash == previous_block.hash and
                new_block.hash == new_block.calculate_hash())

    def is_blockchain_valid(self):
        if not self.is_first_block_valid():
            return False
        for i in range(1, len(self.blocks)):
            if not self.is_valid_new_block(self.blocks[i], self.blocks[i - 1]):
                return False
        return True

    def contar_votos(self):
        contagem = {}
        for block in self.blocks[1:]:  # Ignora o bloco gênesis
            if isinstance(block.data, BiometricData):
                voto = block.data.vote
                contagem[voto] = contagem.get(voto, 0) + 1
        return contagem
