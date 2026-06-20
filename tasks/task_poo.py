from typing import List, Text, Literal, Optional
from utils import digitar
from cores import colorired, coloriryellow
from abc import ABC, abstractmethod
from db.crud import update_score

class BaseLoreTask(ABC):
    def __init__(
            self,
            texto_apresentacao: Text,
            texto_alternativas: List[Text],
            resposta_texto_alternativas: List[str] | None = None,
    ):
        self.texto_apresentacao = texto_apresentacao
        self.texto_alternativas = texto_alternativas
        self.resposta_texto_alternativas = resposta_texto_alternativas
    

    @abstractmethod
    def apresentar(self):
        digitar(self.texto_apresentacao)

    @abstractmethod
    def mostrar_alternativas(self):
        coloriryellow('Escolha uma alternativa:\n')
        letras = ['A', 'B', 'C', 'D']
        for i in range(4):
            digitar(f'({letras[i]}) ->  {self.texto_alternativas[i]} ')
        print('\n')

    @abstractmethod
    def validar_resposta(self, resposta: str, user_id: int):
        pass



class Lore(BaseLoreTask):
    def __init__(
            self,
            texto_apresentacao,
            texto_alternativas,
            resposta_texto_alternativas, 
            pontuacao_por_alternativa: List[int],
    ):
        super().__init__(texto_apresentacao, texto_alternativas, resposta_texto_alternativas)
        self.pontuacao_por_alternativa = pontuacao_por_alternativa
        

    def apresentar(self):
        return super().apresentar()
    

    def mostrar_alternativas(self):
        return super().mostrar_alternativas()


    def validar_resposta(self, resposta, user_id) -> bool:
        if resposta == 'A':
            update_score(
                user_id=user_id,
                score=self.pontuacao_por_alternativa[0]
            )
            if self.resposta_texto_alternativas is not None:
                digitar(self.resposta_texto_alternativas[0])
            return True
            
        elif resposta == 'B':
            update_score(
                user_id=user_id,
                score=self.pontuacao_por_alternativa[1]
            )
            if self.resposta_texto_alternativas is not None:
                digitar(self.resposta_texto_alternativas[1])
            return True
            
        elif resposta == 'C':
            update_score(
                user_id=user_id,
                score=self.pontuacao_por_alternativa[2]
            )
            if self.resposta_texto_alternativas is not None:
                digitar(self.resposta_texto_alternativas[2])
            return True

        else:
            update_score(
                user_id=user_id,
                score=self.pontuacao_por_alternativa[3]
            )
            if self.resposta_texto_alternativas is not None:
                digitar(self.resposta_texto_alternativas[3])
            return True
            
        


class Task(BaseLoreTask):
    def __init__(
            self,
            texto_apresentacao,
            texto_alternativas,
            resposta_texto_alternativas, 
            alternativa_correta: Text | None = None,
    ):
        super().__init__(texto_apresentacao, texto_alternativas, resposta_texto_alternativas)
        self.alternativa_correta = alternativa_correta


    def apresentar(self):
        return super().apresentar()
    

    def mostrar_alternativas(self):
        return super().mostrar_alternativas()

    
    def validar_resposta(self, resposta, user_id):
        return 


            


    

if __name__ == '__main__':
    from rich import inspect

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

    # inspect(l, methods=True)

    l.apresentar()
    l.mostrar_alternativas()
    l.validar_resposta('B', 1)