import time
from pathlib import Path
import json

file = Path('session.json')


def digitar(texto, velocidade=0.01):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(velocidade)
    print()
    


def get_data_session():
    with open(file, 'r') as f:
        data = json.load(f)
    
    return data


if __name__ == "__main__":
    print(get_data_session())