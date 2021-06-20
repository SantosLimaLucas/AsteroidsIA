from agentes.abstrato import AgenteAbstrato
from agentes.heuristicaproj3.heuristicaAsteroids import ProblemaAsteroide
import pygame
from agentes.Desenhador import Desenhador_mundo
from .buscadores.busca import buscaAe


class AgenteAutomaticoA(AgenteAbstrato):
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    # nave
    naveImg = pygame.image.load('imagens/nave.png')

    #bullet
    bulletImg = pygame.image.load('imagens/laser.png')

    # tela de fundo
    fundoImg = pygame.image.load('imagens/fundo.jpg')

    # asteroides
    asteroideImg = pygame.image.load('imagens/asteroide.png')

    def __init__(self) -> None:
        super().__init__()

        self.prblema: ProblemaAsteroide = None
        self.solucao: list = None


    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao.
        """
        AgenteAutomaticoA.desenharMundo(self, percepcao_mundo)

        if not self.solucao:
            self.problema = ProblemaAsteroide()  # TODO: # percepcao_mundo)



    def escolherProximaAcao(self):
        if not self.solucao:
            solucao = buscaAe(self, self.problema)
            if not ProblemaAsteroide.teste_objetivo(solucao.estado):
                raise Exception("Agente BFS não encontrou solução.")


        #time.sleep(2)



    def desenharMundo(self, percepcao_mundo):
        Desenhador_mundo.DesenharMundo(self, percepcao_mundo)


    
