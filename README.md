# 🗳️ Sistema de Votação com Blockchain para a UEA

Este projeto utiliza uma **blockchain** utilizada em sala para registrar e gerenciar votos de alunos da Universidade do Estado do Amazonas (UEA). 
O sistema permite que cada aluno vote uma única vez, garantindo segurança e anonimato. 
As matrículas dos alunos são convertidas em **hashes**, assegurando que as identidades dos votantes sejam preservadas.


## 🚀 Funcionalidades

- **Blockchain para Votação:** Implementação de uma blockchain personalizada para registrar e validar votos.
- **Validação de IDs:** Verifica se as matrículas são válidas e se o aluno já votou.
- **Anonimização de Matrículas:** A matrícula do aluno é transformada em uma hash, mantendo a identidade do eleitor oculta.
- **Visualização dos Votos:** A blockchain pode ser visualizada em tempo real, mostrando os detalhes dos blocos, incluindo o voto e o hash do eleitor.
- **Página de Resultados:** Exibe os resultados da votação de forma segura e transparente.

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python 3.13.3**
- 🔗 **Blockchain personalizada**
- 🌐 **Flask** (backend)
- 🔒 **SHA-256** (anonimização dos eleitores)
- 🎨 **HTML + CSS** (frontend)
- 🔁 **JSON** (armazenamento de dados de eleitores e votos)

## 🧪 Como Executar Localmente

1. Clone o repositório:

git clone https://github.com/FelipeBragaUEA/voting_system.git
cd voting_system
python backend/gerar_eleitores.py (para gerar o json de possíveis matrículas dos alunos)
pip install flask flask-cors
python backend/app.py

2. Instale as dependências:

pip install flask flask-cors


3. Rode o servidor:

python app.py

4. Acesse o sistema em seu navegador:

Página de votação: http://127.0.0.1:5000/

Resultados: http://127.0.0.1:5000/resultados

Blockchain: http://127.0.0.1:5000/blocos.html


🔒 Observação: Este sistema é um protótipo e não deve ser utilizado em eleições oficiais.
