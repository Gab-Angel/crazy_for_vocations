from typing import List, Text
from utils import digitar
from cores import colorired, coloriryellow, colorirgreen
from abc import ABC, abstractmethod
from db.crud import update_score


# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Classe Pai 
class BaseLoreTask(ABC):
    def __init__(
            self,
            texto_apresentacao: Text,
            texto_alternativas: List[Text],
    ):
        self.texto_apresentacao = texto_apresentacao
        self.texto_alternativas = texto_alternativas
        self.resposta_user = None
    

    @abstractmethod
    def apresentar(self):
        digitar(self.texto_apresentacao)

    @abstractmethod
    def mostrar_alternativas(self):
        coloriryellow('Escolha:\n')
        letras = ['A', 'B', 'C', 'D']
        for i in range(4):
            digitar(f'({letras[i]}) ->  {self.texto_alternativas[i]} ')
        print('\n')


    @abstractmethod
    def pegar_resposta(self):
        while True:
            resposta = input(': ').upper().strip()
            if resposta not in ['A', 'B', 'C', 'D']:
                colorired('Resposta Inválida')
            else:
                break
        self.resposta_user = resposta


    @abstractmethod
    def validar_resposta(self, user_id: int):
        pass



# ---------------------------------------------------------------------------------------------------------------------------------------------------



# Classe Lore que é responsável por gerir lores
class Lore(BaseLoreTask):
    def __init__(
            self,
            texto_apresentacao,
            texto_alternativas,
            pontuacao_por_alternativa: List[int],
            resposta_texto_alternativas: List[str] | None = None, 
    ):
        super().__init__(texto_apresentacao, texto_alternativas)
        self.pontuacao_por_alternativa = pontuacao_por_alternativa
        self.resposta_texto_alternativas = resposta_texto_alternativas
        

    def apresentar(self):
        return super().apresentar()
    

    def mostrar_alternativas(self):
        return super().mostrar_alternativas()

    def pegar_resposta(self):
        return super().pegar_resposta()


    def validar_resposta(self, user_id) -> bool:
        if self.resposta_user == 'A':
            update_score(
                user_id=user_id,
                score=self.pontuacao_por_alternativa[0]
            )
            if self.resposta_texto_alternativas is not None:
                coloriryellow(self.resposta_texto_alternativas[0])
            return True
            
        elif self.resposta_user == 'B':
            update_score(
                user_id=user_id,
                score=self.pontuacao_por_alternativa[1]
            )
            if self.resposta_texto_alternativas is not None:
                coloriryellow(self.resposta_texto_alternativas[1])
            return True
            
        elif self.resposta_user == 'C':
            update_score(
                user_id=user_id,
                score=self.pontuacao_por_alternativa[2]
            )
            if self.resposta_texto_alternativas is not None:
                coloriryellow(self.resposta_texto_alternativas[2])
            return True

        else:
            update_score(
                user_id=user_id,
                score=self.pontuacao_por_alternativa[3]
            )
            if self.resposta_texto_alternativas is not None:
                coloriryellow(self.resposta_texto_alternativas[3])
            return True
            

# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Classe Task que é responsável por gerir tasks
class Task(BaseLoreTask):
    def __init__(
            self,
            texto_apresentacao,
            texto_alternativas,
            ponto_alternativa: int,
            alternativa_correta: Text,
            resposta_acerto_erro: List[str] | None = None, 
    ):
        super().__init__(texto_apresentacao, texto_alternativas)
        self.ponto_alternativa = ponto_alternativa
        self.alternativa_correta = alternativa_correta
        self.resposta_acerto_erro = resposta_acerto_erro


    def apresentar(self):
        return super().apresentar()
    

    def mostrar_alternativas(self):
        return super().mostrar_alternativas()

    def pegar_resposta(self):
        return super().pegar_resposta()
    
    def validar_resposta(self, user_id):
        if self.resposta_user == self.alternativa_correta:
            update_score(
                user_id=user_id,
                score=self.ponto_alternativa
            )

            if self.resposta_acerto_erro is not None:
                colorirgreen(self.resposta_acerto_erro[0])
            else:
                colorirgreen('Resposta Correta')

            return True
        
        elif self.resposta_acerto_erro is not None:
            colorired(self.resposta_acerto_erro[1])
        else:
            colorired('Reposta Errada')



# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Classe que é responsável por gerir uma lista de várias lores ou tasks
class Carrosel():
    def __init__(self, tasks: List[Task | Lore]):
        self.tasks = tasks

    
    def apresentar_tasks(self, user_id: int) -> bool:
        for task in self.tasks:
            task.apresentar()
            task.mostrar_alternativas()
            task.pegar_resposta()
            task.validar_resposta(user_id=user_id)
        
        return True
    

    

if __name__ == '__main__':
    # from rich import inspect

    texto = """
        - Voce chega na UFS... observa muitas pessoas de diferentes tipos, cores, personalidades, jeitos... 
        Seu corpo treme e voce tem seu primeiro desafio
        na faculdade: encontrar a sala de apresentação de seu curso:
        """

    texto_alternativas= [
        "olhar no grupo de whatsapp que voce entrou pra ter ctz de qual sala é",
        "ir pro seu departamento e buscar informações por lá",
        "mandar mensagem no grupo dos veteranos correndo o risco de ser ignorado",
        "abrir o mapa da UFS que voce baixou em baixa qualidade pois seu smartphone estava sem memoria e verificar o local"
    ]

    resposta = [
        'boaa',
        'aii naooo',
        'muito bem',
        'fodaaa'
    ]

    l = Lore(
        texto_apresentacao=texto,
        texto_alternativas=texto_alternativas,
        resposta_texto_alternativas=resposta,
        pontuacao_por_alternativa=[20, 50, 40, 60]
    )


    t = Task(
        texto_apresentacao=texto,
        texto_alternativas=texto_alternativas,
        resposta_acerto_erro=['boaaa', 'aiiii não'],
        ponto_alternativa=100,
        alternativa_correta='A'
    )

    t2 = Task(
        texto_apresentacao=texto,
        texto_alternativas=texto_alternativas,
        resposta_acerto_erro=['boaaa', 'aiiii não'],
        ponto_alternativa=100,
        alternativa_correta='A'
    )

    t3 = Task(
        texto_apresentacao=texto,
        texto_alternativas=texto_alternativas,
        resposta_acerto_erro=['boaaa', 'aiiii não'],
        ponto_alternativa=100,
        alternativa_correta='A'
    )

    t_ = Carrosel(
        tasks=[t, t2, l, t3]
    )

    t_.apresentar_tasks(1)