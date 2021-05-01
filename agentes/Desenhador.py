import pygame


class Desenhador_mundo:
    def DesenharMundo(self, percepcao_mundo):
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