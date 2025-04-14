# biometric_data.py
import json

class BiometricData:
    def __init__(self, elector_hash, vote):
        """
        Representa os dados anonimizados de um eleitor (hash + voto)
        """
        self.elector_hash = elector_hash
        self.vote = vote

    def to_dict(self):
        return {
            "elector_hash": self.elector_hash,
            "vote": self.vote
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return f"Hash do Eleitor: {self.elector_hash}, Voto: {self.vote}"
