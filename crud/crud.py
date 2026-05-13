import json
from pathlib import Path

file = Path("crud/user.json")

def criar_user(nome: str):

    initial_data = {
        "nick_name": 'bot',
        "level": 'calourinho',
        "score": {
            "calourinho": 0,
            "veterano": 0,
            "senior": 0,
            "estombelo": 0
        },
        "tasks": {
            "calourinho": {
                "task_01": 0,
                "task_02": 0,
                "task_03": 0,
                "task_04": 0,
                "task_05": 0
            },
            "veterano": {
                "task_01": 0,
                "task_02": 0
            },
            "senior": {
                "task_01": 0,
                "task_02": 0,
                "task_03": 0
            },
            "estombelo": {
                "task_01": 0,
                "task_02": 0
            },
        }
    }

    if file.is_file():
        ...
    else:
        with open(file, "w") as f:
            json.dump(initial_data, f)
    

    with open(file, 'r') as f:
        dados = json.load(f)

    dados['nick_name'] = nome

    with open(file, 'w') as f:
        json.dump(dados, f, indent=4)


def atualizar_level(level: str):
    with open(file, 'r') as f:
        dados = json.load(f)
    
    dados['level'] = level 

    with open(file, 'w') as f:
        json.dump(dados, f, indent=4)
    

def atualizar_score(level: str, score: int):
    # Abriu o arquivo para edição
    with open(file, 'r') as f:
        dados = json.load(f)


    # verificação de level e atribuição de score
    if level == 'calourinho':
        dados['score']['calourinho'] += score 
    elif level == 'veterano':
        dados['score']['veterano'] += score 
    elif level == 'senior':
        dados['score']['senior'] += score
    elif level == 'estombelo':
        dados['score']['estombelo'] += score 
    else:
        raise ValueError('Esse nível não existe')

    # atualiza o arquivo
    with open(file, 'w') as f:
        json.dump(dados, f, indent=4)
    
def atualizar_tasks(level: str, task_name: str, score: int):
    with open(file, 'r') as f:
        dados = json.load(f)

    dados['tasks'][level][task_name] = score

    with open(file, 'w') as f:
        json.dump(dados, f, indent=4)


if __name__ == "__main__":
    # criar_user(input('digite um nome: '))
    # atualizar_level(input('level: '))
    # atualizar_score(input('level: '), int(input('score: ')))
    atualizar_tasks(input('level: '), input('task_name: '), int(input('score: ')))