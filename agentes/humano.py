from agentes.abstrato import AgenteAbstrato
import pygame
from acoes import AcaoJogador, DirecaoMoverNave

class AgentePrepostoESHumano(AgenteAbstrato):


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


    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
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
            self.screen.blit(self.bulletImg, (xNave+4,90))
        for linha in range(start_linha, end_linha):
            for coluna in range(start_coluna, colunas):

                if (linha, coluna) in percepcao_mundo.pos_asteroids:
                    self.screen.blit(self.asteroideImg, (linha, coluna))
                    pygame.display.update()
                    '''print(f"asteroides: {percepcao_mundo.pos_asteroids} e nave : {percepcao_mundo.posicao_nave}")'''

                if (linha, coluna) == (xNave, yNave):
                    self.screen.blit(self.naveImg, (xNave, coluna))
                    pygame.display.update()


    def escolherProximaAcao(self):
        jogada = None
        while not jogada:
            for event in pygame.event.get():
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        return AcaoJogador.dirigirNave(DirecaoMoverNave.MOVER_PARA_ESQUERDA)
                        jogada ="jogou"
                    if event.key == pygame.K_RIGHT:
                        return AcaoJogador.dirigirNave(DirecaoMoverNave.MOVER_PARA_DIREITA)
                        jogada = "jogou"
                    if event.key == pygame.K_SPACE:
                        return AcaoJogador.dirigirNave(DirecaoMoverNave.ATIRAR)
                        jogada = "jogou"