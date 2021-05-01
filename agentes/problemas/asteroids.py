from typing import Tuple, Set, Sequence
from dataclasses import dataclass
from regras_jogo.personagens import Personagens
from percepcoes import PercepcoesJogador
from enum import Enum
from acoes import DirecaoMoverNave


class Asteroide:
    x: int
    y: int

    def asteroide(self) -> Tuple[int, int]:
        return Tuple[self.x, self.y]


@dataclass
class EstadoAsteroids:
    estado_bala: "pronto"
    pos_asteroids: Set[Asteroide]
    dimensoes: Tuple[int, int] = (800, 600)
    posicao_nave: Tuple[int, int] = (400, 500)


class MoverNave(Enum):
    MOVER_NAVE = 'Mover_nave'

class DirecaoMoverNave(Enum):
    MOVER_PARA_DIREITA = 'Mover_para_direita'
    MOVER_PARA_ESQUERDA = 'Mover_para_esquerda'
    ATIRAR = 'Atirar'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple()

    @classmethod
    def dirigirNave(cls, direcao: DirecaoMoverNave) -> MoverNave:
        return cls(MoverNave.MOVER_NAVE, direcao)


class ProblemaAsteroide:

    @staticmethod
    def estado_inicial(self,*args, **kwargs) -> EstadoAsteroids:
        posicao_asteroides = {
            (200, 150), (300, 150), (400, 150), (500, 150)
        }

        self.asteroides = posicao_asteroides
        self.id_personagens = {Personagens.JOGADOR_ASTEROIDS: 0}
        self.posicaoNave = (400, 500)
        self.dimensoes = (800, 600)
        self.estadoBala = "pronto"

        percepcoes_jogador = PercepcoesJogador(
            pos_asteroids=set(self.asteroides),
            dimensoes=self.dimensoes,
            posicao_nave=self.posicaoNave,
            estado_bala=self.estadoBala
        )
        return percepcoes_jogador

    @staticmethod
    def acoes(estado: EstadoAsteroids) -> Sequence[DirecaoMoverNave]:
        acoes_possiveis = list()
        asteroide_mais_proximo = ProblemaAsteroide.encontrarAsteroideProximo(estado.posicao_nave[0], estado.pos_asteroids)
        if(asteroide_mais_proximo > estado.posicao_nave[0]):
            acoes_possiveis.append(DirecaoMoverNave.MOVER_PARA_DIREITA)
        if (asteroide_mais_proximo < estado.posicao_nave[0]):
            acoes_possiveis.append(DirecaoMoverNave.MOVER_PARA_ESQUERDA)
        if (asteroide_mais_proximo == estado.posicao_nave[0]):
            acoes_possiveis.append(DirecaoMoverNave.ATIRAR)

        return acoes_possiveis
    def encontrarAsteroideProximo(xNave, posicaoAsteroides: list):
        proximo = 1000
        listAsteroides = []
        for asteroide in posicaoAsteroides:

            listAsteroides.append(asteroide[0])
        for x in range(0, len(listAsteroides)):
            asteroide = listAsteroides[x]
            xAsteroide = asteroide

            if (ProblemaAsteroide.moduloNumero(xAsteroide, xNave) < ProblemaAsteroide.moduloNumero(proximo, xNave)):
                proximo = asteroide
        return proximo


    def moduloNumero(a, b):
        if((a-b) < 0):
            return (a-b)* (-1)
        else:
            return a-b

    @staticmethod
    def resultado(estado: EstadoAsteroids, acao: DirecaoMoverNave) -> EstadoAsteroids:

        estado_resultante = estado


        if acao == DirecaoMoverNave.MOVER_PARA_DIREITA:
            x = estado_resultante.posicao_nave[0] + 10
            y = estado_resultante.posicao_nave[1]

            estado_resultante.posicao_nave = (x, y)

        elif acao == DirecaoMoverNave.MOVER_PARA_ESQUERDA:
            x = estado_resultante.posicao_nave[0] - 10
            y = estado_resultante.posicao_nave[1]

            estado_resultante.posicao_nave = (x, y)

        elif acao == DirecaoMoverNave.ATIRAR:
            alvo = (estado_resultante.posicao_nave[0], 150)
            if alvo in estado_resultante.pos_asteroids:
                estado_resultante.pos_asteroids.discard(alvo)

        else:
            print(acao)
            raise ValueError("Movimento especificado inválido, cheater!")

        return estado_resultante

    @staticmethod
    def teste_objetivo(estado: EstadoAsteroids) -> bool:
        return len(estado.pos_asteroids) == 0

class ProblemAsteroideDFS:

    @staticmethod
    def estado_inicial(self,*args, **kwargs) -> EstadoAsteroids:
        posicao_asteroides = {
            (200, 150), (300, 150), (400, 150), (500, 150)
        }

        self.asteroides = posicao_asteroides
        self.id_personagens = {Personagens.JOGADOR_ASTEROIDS: 0}
        self.posicaoNave = (400, 500)
        self.dimensoes = (800, 600)
        self.estadoBala = "pronto"

        percepcoes_jogador = PercepcoesJogador(
            pos_asteroids=set(self.asteroides),
            dimensoes=self.dimensoes,
            posicao_nave=self.posicaoNave,
            estado_bala=self.estadoBala
        )
        return percepcoes_jogador

    @staticmethod
    def acoes(estado: EstadoAsteroids) -> Sequence[DirecaoMoverNave]:
        acoes_possiveis = list()
        asteroide_mais_proximo = ProblemAsteroideDFS.encontrarAsteroideProximo(estado.posicao_nave[0], estado.pos_asteroids)
        if(asteroide_mais_proximo > estado.posicao_nave[0]):
            acoes_possiveis.append(DirecaoMoverNave.MOVER_PARA_DIREITA)
        if (asteroide_mais_proximo < estado.posicao_nave[0]):
            acoes_possiveis.append(DirecaoMoverNave.MOVER_PARA_ESQUERDA)
        if (asteroide_mais_proximo == estado.posicao_nave[0]):
            acoes_possiveis.append(DirecaoMoverNave.ATIRAR)

        return acoes_possiveis
    def encontrarAsteroideProximo(xNave, posicaoAsteroides: list):
        proximo = 1000
        for asteroide in posicaoAsteroides:
            if ((asteroide[0] - xNave) < (proximo - xNave)):
                proximo = asteroide[0]


        return proximo

    @staticmethod
    def resultado(estado: EstadoAsteroids, acao: DirecaoMoverNave) -> EstadoAsteroids:

        estado_resultante = estado


        if acao == DirecaoMoverNave.MOVER_PARA_DIREITA:
            x = estado_resultante.posicao_nave[0] + 10
            y = estado_resultante.posicao_nave[1]

            estado_resultante.posicao_nave = (x, y)

        elif acao == DirecaoMoverNave.MOVER_PARA_ESQUERDA:
            x = estado_resultante.posicao_nave[0] - 10
            y = estado_resultante.posicao_nave[1]

            estado_resultante.posicao_nave = (x, y)

        elif acao == DirecaoMoverNave.ATIRAR:
            alvo = (estado_resultante.posicao_nave[0], 150)
            if alvo in estado_resultante.pos_asteroids:
                estado_resultante.pos_asteroids.discard(alvo)

        else:
            print(acao)
            raise ValueError("Movimento especificado inválido, cheater!")

        return estado_resultante

    @staticmethod
    def teste_objetivo(estado: EstadoAsteroids) -> bool:
        return len(estado.pos_asteroids) == 0

