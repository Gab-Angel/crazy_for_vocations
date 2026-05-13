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


def task_02(resposta):
    digitar(">>"* 10)
    digitar("questão 2 !!!")
    digitar(">>"*10)
    print("")            
    print("")        
    print("")
    digitar("resolva: ")
    print("\nx² -x - 12 ")
    print("")
    while True:
        resposta2 = float(input("sua resposta: "))

        if resposta2 == -3.4:
            digitar(f"muito bem zequinha,continue assim !!!")
            atualizar_tasks('calourinho', "task_02", 20)
            atualizar_score("calourinho", 20)
            break
        else:
            digitar("não foi dessa fez meu peixe")
            digitar("tente novamente: ")        
responsa2 = 1
resultado1 = task_02(responsa2)        

def task_03(resposta):
    digitar(">>"* 10)
    digitar("questão 3 !!!")
    digitar(">>"*10)
    print("")            
    print("")        
    print("")
    digitar("resolva: ")
    print("\n|x-4| < 3 ")
    print("")
    while True:
        resposta3 = input("obs: os dois agarismos devem se separados por vírgula\n sua resposta: ")

        if resposta3 == "1,7":
            digitar(f"muito bem zequinha,continue assim !!!")
            atualizar_tasks('calourinho', "task_03", 15)
            atualizar_score("calourinho", 15)
            break
        else:
            digitar("não foi dessa fez meu peixe")
            digitar("tente novamente: ")        
responsa3 = 1
resultado1 = task_03(responsa3)


def task_04(resposta):
    digitar(">>"* 10)
    digitar("questão 4 !!!")
    digitar(">>"*10)
    print("")            
    print("")        
    print("")
    digitar("resolva: ")
    print("\nlim x²-1/x-1\n(x->1)")
    print("")
    while True:
        resposta3 = float(input("sua resposta: "))

        if resposta3 == 2:
            digitar(f"muito bem zequinha,continue assim !!!")
            atualizar_tasks('calourinho', "task_04", 25)
            atualizar_score("calourinho", 25)
            break
        else:
            digitar("não foi dessa fez meu peixe")
            digitar("tente novamente: ")        
responsa4 = 1
resultado2 = task_04(responsa4)

#iniciaremos fem

digitar(">>"*10)
digitar("partiu FEM calourinho!!!")
digitar(">>"*10)
print('')
print("")

def task_05(resposta):
    print(">>"* 10)
    digitar("questão 1 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    digitar("resolva: ")
    digitar("p:faltar aula pra jogar sinuca\nq:serei aprovado ")
    print("\np => q")
    print("")
    while True:
        resposta4 = (input("responda se a sentença é verdadeira ou falsa:  "))

        if resposta4 == "falsa":
            digitar(f"infelizmente o cara não pode ter tudo na vida")
            atualizar_tasks('calourinho', "task_05", 25)
            atualizar_score("calourinho", 25)
            break
        else:
            digitar("queria que fosse verdade...")
            digitar("tente novamente: ")        
responsa5 = 1
resultado5 = task_05(responsa5)
