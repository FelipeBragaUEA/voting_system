# blockchain.py
from .block import Block
import time

class Blockchain:
    def __init__(self, difficulty=2):
        self.difficulty = difficulty
        self.blocks = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), None, {"candidato": "genesis"})
        genesis_block.proof_of_work(self.difficulty)
        self.blocks.append(genesis_block)

    def latest_block(self):
        return self.blocks[-1]

    def add_block(self, data):
        prev_block = self.latest_block()
        new_block = Block(prev_block.index + 1, time.time(), prev_block.hash, data)
        new_block.proof_of_work(self.difficulty)
        self.blocks.append(new_block)

    def get_votes(self):
        votos = {}
        for block in self.blocks[1:]:
            candidato = block.data.get("candidato")
            if candidato:
                votos[candidato] = votos.get(candidato, 0) + 1
        return votos

    def __str__(self):
        return '\n'.join(str(block) for block in self.blocks)
