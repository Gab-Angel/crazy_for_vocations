import json
from pathlib import Path

file = Path("crud/user.json")

def criar_user(nome: str):

    initial_data = {
        "name_user": ''
    }

    if file.is_file():
        ...
    else:
        with open(file, "w") as f:
            json.dump(initial_data, f)
    
    initial_data = {
        "nome": nome
    }

    with open(file, 'r') as f:
        dados = json.load(f)

    dados['name_user'] = nome

    with open(file, 'w') as f:
        json.dump(dados, f, indent=4)


if __name__ == "__main__":
    criar_user(input('digite um nome: '))
