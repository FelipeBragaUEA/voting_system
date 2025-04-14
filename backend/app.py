import sys
import os
import json
import hashlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from blockchain.voting_blockchain import VotingBlockchain
from blockchain.biometric_data import BiometricData

frontend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'frontend')
app = Flask(__name__, static_folder=frontend_path, static_url_path="/")
CORS(app)

# Inicializa a blockchain com dificuldade 3
blockchain = VotingBlockchain(difficulty=3)

# Caminho para o arquivo de eleitores
ELEITORES_PATH = os.path.join(os.path.dirname(__file__), "eleitor_data.json")

# Função para carregar os eleitores
def carregar_eleitores():
    with open(ELEITORES_PATH, "r") as f:
        return json.load(f)

# Função para salvar os eleitores
def salvar_eleitores(eleitores):
    with open(ELEITORES_PATH, "w") as f:
        json.dump(eleitores, f, indent=4)

# Função para anonimizar o ID
def anonimizar_id(id_eleitor):
    return hashlib.sha256(id_eleitor.encode()).hexdigest()

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/resultados')
def serve_resultados():
    return send_from_directory(app.static_folder, 'resultados.html')

@app.route('/votar', methods=['POST'])
def votar():
    data = request.json
    eleitor_id = data.get("eleitor_id")
    voto = data.get("voto")

    if not eleitor_id or not voto:
        return jsonify({"erro": "Dados incompletos"}), 400

    eleitores = carregar_eleitores()

    # Verifica se o ID existe e se já votou
    eleitor = next((e for e in eleitores if e["id"] == eleitor_id), None)
    if not eleitor:
        return jsonify({"erro": "ID de eleitor inválido"}), 403
    if eleitor["votou"]:
        return jsonify({"erro": "Este eleitor já votou"}), 403

    # Cria os dados anonimizados para a blockchain
    elector_hash = anonimizar_id(eleitor_id)
    biometric_data = BiometricData(elector_hash=elector_hash, vote=voto)

    novo_bloco = blockchain.new_block(biometric_data)
    blockchain.add_block(novo_bloco)

    # Marca como votou e salva
    eleitor["votou"] = True
    salvar_eleitores(eleitores)

    return jsonify({"mensagem": "Voto registrado com sucesso"}), 200

@app.route('/resultados_api', methods=['GET'])
def resultados():
    return jsonify(blockchain.contar_votos()), 200

@app.route('/blocos_api', methods=['GET'])
def blocos_api():
    blocos = blockchain.blocks
    return jsonify([{
        "index": bloco.index,
        "timestamp": bloco.timestamp,
        "nonce": bloco.nonce,
        "hash": bloco.hash,
        "hash_anterior": bloco.previous_hash,
        "dados": bloco.data.to_dict() if hasattr(bloco.data, 'to_dict') else bloco.data
    } for bloco in blocos])

@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
