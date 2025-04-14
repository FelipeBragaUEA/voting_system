# block.py
# Classe que representa um bloco individual na blockchain
import hashlib
import time
import json

class Block:
    def __init__(self, index, timestamp, previous_hash, data):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_str = json.dumps(self.data, sort_keys=True) if isinstance(self.data, dict) else str(self.data)
        content = f"{self.index}{self.timestamp}{self.previous_hash}{data_str}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()

    def proof_of_work(self, difficulty):
        prefix = '0' * difficulty
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __str__(self):
        return f"Block #{self.index} [Previous Hash: {self.previous_hash}, Timestamp: {time.ctime(self.timestamp)}, Data: {self.data}, Hash: {self.hash}]"
