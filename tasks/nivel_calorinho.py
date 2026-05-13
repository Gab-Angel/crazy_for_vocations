from crud.crud import atualizar_tasks, atualizar_score


#começaremos por cáculo

import time
import sys

def digitar(texto, velocidade=0.05):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(velocidade)
    print() 
#tesk 1

# --- Desenho de Foguete com >> ---

print("         / \\")
print("        /   \\")
print("       /     \\")
print("       |     |")
print("       | cfv |")
print("       |     |")
print("      /|     |\\")
print("     / |     | \\")
print("    >> |_____| <<")
print("   >>>>  |  |  <<<<")
print("  >>>>>>      <<<<<<")
print(" >>>>>>>>    >>>>>>>>")

digitar("\n   UMA CAMISINHA ESTOUROU PRA EU NASCER E EU NASCI PARA ESTOURAR!")
print("")
print("") 

digitar(">>"* 10)
digitar("nível calouro!!!")
digitar(">>"*10)

print("")
print("")
#primeira task
def task_01(resposta):
    digitar("vamos dar início a nossa aventura, sua missão começa pelo mundo dos cáculos")
    digitar("lembrando que antes de chegar no mundo dos limites precisamos testa nossa matématica elementar")
    print("")
    print("")
    digitar("\n resolva: ")
    print("\n (5)²³\n -----\n (5)²¹")

    time.sleep(1)
    while True:
        resposta = int(input("sua resposta: "))

        if resposta == 25:
            digitar(f"very good ")
            atualizar_tasks('calourinho', "task_01", 10)
            atualizar_score("calourinho", 10)
            break
        else:
            digitar("errou feio painho")
            digitar("tente novamente: ")
    
resposta = 1  
resultado = task_01(resposta)
