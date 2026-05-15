from pathlib import Path
import json

file = Path('anotacoes/notes.json')

def nova_nota(nome: str, conteudo: str):

    note = {}

    if  file.is_file():
        ...
    else:
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(note, f)

    with open(file, 'r') as f:
        dados = json.load(f)

    dados[nome] = conteudo

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4)
    
    print(f'Nota --> {nome} <-- criada!!!')

def listar_notas():
    if file.is_file():
        with open(file, 'r') as f:
            notas = json.load(f)
            for nota in notas: print(f"{'='*10}> {nota}")

    else:
        print(f"""
              {'='*24}
              Você não possui notas!!!
              {'='*24}
              """) 
        

def editar_nota(nome: str, conteudo: str):
    if file.is_file():
        with open(file, 'r') as f:
            notas = json.load(f)
            
            for nota in notas:
                if nota == nome:
                    notas[nota] = conteudo

                    with open(file, 'w', encoding='utf-8') as f:
                        json.dump(notas, f, indent=4)
                    
                    print('Nota atualizada')
                    break

            else:
                print('Você deve ter errado o nome')

    else:
        print(f"""
              {'='*24}
              Você não possui notas!!!
              {'='*24}
              """)

def ver_conteudo(nome):
    with open(file, 'r') as f:
        dados = json.load(f)
    
    conteudo = dados[nome]

    print(f'Conteúdo === {conteudo} ===')

if __name__ == '__main__':
    # nova_nota(input('nome da nota: '), input('Conteudo da nota: '))
    # listar_notas()
    # editar_nota(input('nome da nota: '), input('Conteudo da nota: '))
    # ver_conteudo(input('nome da nota para ver o conteudo: '))

    ...



