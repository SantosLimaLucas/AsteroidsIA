from typing import Any, Optional
from dataclasses import dataclass
from percepcoes import PercepcoesJogador
from agentes.Desenhador import Desenhador_mundo

class ProblemaSemSolucaoException(Exception):
    pass


@dataclass
class No():
    estado: Any
    acao: Optional[Any] = None
    pai: Optional['No'] = None

    def calcular_profundidade(self):
        raiz = not self.pai
        return 0 if raiz else self.pai.calcular_profundidade() + 1
    
    def caminho_acoes(self) -> list:
        """Retorna uma lista com as ações em ordem para atingir o estado
        que este nó armazena.
        """
        raiz = not self.pai
        return [] if raiz else self.pai.caminho_acoes() + [self.acao]

    @classmethod
    def criar_no_filho(cls, problema, pai, acao):
        novo_estado = problema.resultado(pai.estado, acao)
        '''custo_solucao = pai.custo_solucao + problema.custo(pai.estado, acao, novo_estado)'''
        return cls(novo_estado, acao, pai)
    
    def __repr__(self) -> str:
        return f'No({self.estado!r},{self.acao!r})'

solucao = []
def busca_em_arvoreBFS(self, problema) -> No:
    """ Retorna uma solucao ou falha"""
    borda = [No(problema.estado_inicial(self))]
    while borda:
        folha = borda.pop(0)
        if problema.teste_objetivo(folha.estado):
            return folha
        for acao in problema.acoes(folha.estado):
            expandido = No.criar_no_filho(problema, folha, acao)
            borda.append(expandido)
            Desenhador_mundo.DesenharMundo(self, expandido.estado)
    raise ProblemaSemSolucaoException()

def busca_em_arvoreDFS(self, problema) -> No:
    """ Retorna uma solucao ou falha"""
    borda = [No(problema.estado_inicial(self))]
    while borda:
        folha = borda.pop()
        if problema.teste_objetivo(folha.estado):
            return folha
        for acao in problema.acoes(folha.estado):
            expandido = No.criar_no_filho(problema, folha, acao)
            borda.append(expandido)
            Desenhador_mundo.DesenharMundo(self, expandido.estado)
    raise ProblemaSemSolucaoException()


def busca_gulosa(self, problema) -> No:
    fronteira = [No(problema.estado_inicial(self))]
    while fronteira:
        adjacentes = fronteira.pop()
        if problema.teste_objetivo(adjacentes.estado):
            return adjacentes
        for acao in problema.acoes(adjacentes.estado):
            expandido = No.criar_no_filho(problema, adjacentes, acao)
            fronteira.append(expandido)
            Desenhador_mundo.DesenharMundo(self, expandido.estado)
    raise ProblemaSemSolucaoException()

def busca_Ae(self, problema) -> No:
    pass


class Busca_AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False

    def buscar(self, atual):
        atual.visitado = True

        if atual == self.objetivo:
            print("Objetivo {} foi alcançado. ".format(self.objetivo.nome))
            self.achou = True
        else:
            self.fronteira = No.criar_no_filho(len(atual.adjacentes))
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.inserir(a)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                Busca_AEstrela.buscar(self, self.fronteira.getPrimeiro())


class Busca_gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False

    def buscar(self, atual):
        atual.visitado = True

        if atual == self.objetivo:
            self.achou = True
        else:
            self.fronteira = No.criar_no_filho(len(atual.adjacentes))
            for i in atual.adjacentes:
                if i.cidade.visitado == False:
                    i.cidade.visitado = True
                    self.fronteira.inserir(i.cidade)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                Busca_gulosa.buscar(self, self.fronteira.getPrimeiro())


busca_arvore_bfs = busca_em_arvoreBFS
busca_arvore_dfs = busca_em_arvoreDFS
buscagulosa = busca_gulosa
buscaAe = busca_Ae
