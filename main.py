from inicializacao.inicio import boas_vindas_calourinho, menu
from pathlib import Path

file = Path('crud/user.json')


# aqui vai ficar tudo
def main():
    if not file.is_file():
        boas_vindas_calourinho()

    menu()


if __name__ == '__main__':
    main()