import json

eleitores = []

# Anos de entrada: de 2016 a 2023
for ano in range(16, 24):  # de 16 até 23
    for numero in range(1, 41):  # de 0001 até 0040
        numero_formatado = f"{numero:04d}"  # força a ter 4 dígitos (ex: 0001)
        id_eleitor = f"{ano}1531{numero_formatado}"
        eleitores.append({
            "id": id_eleitor,
            "votou": False
        })

with open("backend/eleitor_data.json", "w") as f:
    json.dump(eleitores, f, indent=4)

print("Arquivo eleitor_data.json gerado com sucesso.")
