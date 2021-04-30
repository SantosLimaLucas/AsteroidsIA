from agentes.abstrato import AgenteAbstrato
from agentes.problemas.asteroids import ProblemaAsteroide
import pygame
import time
from acoes import AcaoJogador, DirecaoMoverNave
from .buscadores.busca import busca_arvore_bfs

class AgenteAutomaticoBFS(AgenteAbstrato):


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
        AgenteAutomaticoBFS.desenharMundo(self, percepcao_mundo)

        if not self.solucao:
            self.problema = ProblemaAsteroide()  # TODO: # percepcao_mundo)



    def escolherProximaAcao(self):
        if not self.solucao:
            no_solucao = busca_arvore_bfs(self, self.problema)
            self.solucao = no_solucao.caminho_acoes()
            print(f"isso aqui {len(self.solucao)}  {self.solucao}")
            if not self.solucao:
                raise Exception("Agente BFS não encontrou solução.")

        acao = self.solucao.pop()
        print(f"Próxima ação é {acao}.")
        time.sleep(2)

        print(f"A acao retornada é: {acao} ")
        '''return AcaoJogador.dirigirNave'''

    def desenharMundo(self, percepcao_mundo):
        self.screen.fill((0, 0, 0,))
        self.screen.blit(self.fundoImg, (0, 0))
        linhas, colunas = percepcao_mundo.dimensoes

        start_linha = -300
        start_coluna = 0
        end_linha = 730

        xNave = percepcao_mundo.posicao_nave[0]
        yNave = percepcao_mundo.posicao_nave[1]
        if (xNave <= start_linha):
            xNave = start_linha
        if (xNave >= end_linha):
            xNave = end_linha
        if (percepcao_mundo.estado_bala == "atirando"):
            self.screen.blit(self.bulletImg, (xNave + 4, 90))
            print(yNave)
            print(percepcao_mundo.posicao_nave)
        for linha in range(start_linha, end_linha):
            for coluna in range(start_coluna, colunas):

                if (linha, coluna) in percepcao_mundo.pos_asteroids:
                    self.screen.blit(self.asteroideImg, (linha, coluna))
                    pygame.display.update()
                    '''print(f"asteroides: {percepcao_mundo.pos_asteroids} e nave : {percepcao_mundo.posicao_nave}")'''

                if (linha, coluna) == (xNave, yNave):
                    self.screen.blit(self.naveImg, (xNave, coluna))
                    pygame.display.update()