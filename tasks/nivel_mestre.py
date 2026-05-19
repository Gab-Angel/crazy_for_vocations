from crud.crud import atualizar_tasks, atualizar_score
from random import shuffle

from cores import colorirgreen, colorired
#começaremos por cáculo

import time
from utils import digitar


def task_01():
    print(">>"* 10)
    digitar("questão 1 !!!")
    print(">>"*10)
    print("")            
    digitar("a partir de agora quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Seja f(x) = x^ln(x) para x > 0. Qual é a primeira derivada f'(x)?")
    print("")

    resposta1 = input("sua resposta(para dividi use X\Y): ")

    if resposta1 == "2\ln(x)":
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_01", 40)
        atualizar_score("mestre", 40)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_01", -35)
        atualizar_score("mestre", -35)
        colorired("você perdeu 35 pontos!!")


def task_02():
    print(">>"* 10)
    digitar("questão 2 !!!")
    print(">>"*10)
    print("")            
    digitar("a partir de agora quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Considere a curva definida implicitamente pela equação x^3 + y^3 = 3xy. \nDetermine a inclinação da reta tangente à curva no ponto {3}/{2}, {3}/{2}).")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == 2:
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_02", 35)
        atualizar_score("mestre", 35)
        colorirgreen("parabéns + 35 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_02", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")
    

def task_03():
    print(">>"* 10)
    digitar("questão 3 !!!")
    print(">>"*10)
    print("")            
    digitar("a partir de agora quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Se uma função f(x) é descontínua num ponto x = c, \nqual das seguintes afirmações teóricas é necessariamente verdadeira?")
    print("")
    print("")
    print("A) O limite lim_{x -> c} f(x) nunca existe.\nB) A função não está definida em x = c.\nC) Os limites laterais em $c$ são obrigatoriamente infinitos.\nD) Pelo menos uma das três condições de continuidade falha: a existência de f(c),\n a existência de lim_{x -> c} f(x) ou a igualdade entre ambos.")

    resposta1 = (input("sua resposta: "))

    if resposta1 == "D":
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_03", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_03", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")



def task_04():
    print(">>"* 10)
    digitar("questão 4 !!!")
    print(">>"*10)
    print("")            
    digitar("a partir de agora quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Qual é a interpretação geométrica correta da afirmação de que lim_{x -> infty} f(x) = L?")
    print("")
    print("")
    print("A) A reta y = L é uma assíntota horizontal do gráfico de f(x) quando x cresce indefinidamente.\nB)A reta x = L é uma assíntota vertical do gráfico da função\nC)A função cessa o seu crescimento e estabiliza rigidamente a partir de um determinado valor de x\nD)A função é limitada superiormente por L para todo e qualquer valor do seu domínio.")

    resposta1 = (input("sua resposta: "))

    if resposta1 == "A":
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_04", 35)
        atualizar_score("mestre", 35)
        colorirgreen("parabéns + 35 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_04", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")


def task_05():
    print(">>"* 10)
    digitar("questão 5 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Seja a função f(x) = 5x^4 - 3x^2 + 7x - 12. Qual é a sua primeira derivada, f'(x)?")
    print("")
    print("")
    print("a) 20x^3 - 6x + 7\nb) 5x^3 - 3x + 7\nc) 20x^4 - 6x^2 + 7\nd) 20x^3 - 6x")

    resposta1 = (input("sua resposta: ")).upper()

    if resposta1 == "A":
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_05", 35)
        atualizar_score("mestre", 35)
        colorirgreen("parabéns + 35 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_05", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")



tasks_mestre = [task_01,task_02,task_03, task_04, task_05 ]




if __name__ =="__main__":
    time.sleep(0.1)
    digitar("      ____________________________________")
    digitar("   //\\                                    |")
    digitar("  //        CRAZY FOR VOCATIONS         |")
    digitar(" //____________________________________|")
    digitar("  |=====================================[ ]>>>")
    digitar(" -|------------------------------------|")
    digitar("  \\ |                                    |")
    digitar("   \\|____________________________________|")
    time.sleep(0.5)
    print("")
    print("")
    print("")
    digitar("####         ____________________________________")
    digitar(" ########//\\                                    |")
    digitar(" ###########//        CRAZY FOR VOCATIONS         |")
    digitar(" ############//____________________________________|")
    digitar(" ###########|=====================================[ ]>>>")
    digitar(" #########|------------------------------------|")
    digitar(" #######\\ |                                    |")
    digitar(" ###### \\|____________________________________|")
    print("")
    print("")
    print("")
    time.sleep(0.5)
    digitar("                                    ____________________________________")
    digitar("   _____                       /|                                    |")
    digitar(" ######### \\_______             / |        CRAZY FOR VOCATIONS         |")
    digitar(" ####___\\       \\___________/_|____________________________________|")
    digitar("########  [====|   UFS   |===============================================[ ]>>>")
    digitar("######## \---/-------/-----------^-|------------------------------------|")
    digitar("#########/-------'             \\ |                                    |")
    digitar("#######-'                      \\|____________________________________|")
    print("")
    print("")
    print("")
    time.sleep(0.5)
    digitar("                                    ____________________________________")
    digitar("   //\\_____                       /|                                    |")
    digitar("  //   \\    \\_______             / |        CRAZY FOR VOCATIONS         |")
    digitar(" //     \\___\\       \\___________/_|____________________________________|")
    digitar("##   ##  [====|   UFS   |===============================================[ ]>>>")
    digitar(" \\\\     /---/-------/-----------^-|------------------------------------|")
    digitar("  \\\\   /    /-------'             \\ |                                    |")
    digitar("   \\\\/`-----'                      \\|____________________________________|")
    print("")
    print("")
    print("")
    time.sleep(0.5)
    digitar("     ====>")
    digitar("   =======>")
    digitar("  ==========>")
    digitar(" ==============> [IGNIÇÃO COMPLETA]")
    digitar("  ==========>")
    digitar("   =======>")
    digitar("     ====>")
    print("")
    print("")
    print("")
    time.sleep(0.3)
    digitar(">>     <<        << <          *      <<<    *     <<<  * ")
    digitar(">>>>>    < <<    *      <<         >     < < <               ")
    digitar(">>>>>>> ___________________________  *   <<      *      < < <      *  ")
    digitar("<<>>>><<<                    \ |   ----_____ < < <<<       *  ")
    digitar("<<>>><<<<        for          | |          ----_______  ")
    digitar("<<<<<<<<<  crazy    vocations | |       ___----  ")
    digitar("<<>>><<<< ___________________/_|___-----          * <<  <*  << <     * ")
    digitar(">>>>>>.      *         < <        <  <<    <<     *   <<   <<  << <       *            ")
    digitar(">>>>            <<    *      << < <          *     < < *  * ")
    digitar(">>       *        <<            << <     *         *       ")
    digitar("   *                 *          < <      ")
    print("")
    print("")
    digitar("GAIA É QUE NEM ANEMIA, SÓ TEM QUEM NÃO COME DIREITO!!!!!!")
    print("")
    print("")
    aleatorio = [task_01,task_02,task_03, task_04, task_05 ]
    shuffle(aleatorio) 
    for comando in aleatorio:
        comando ()
