from abc import ABC, abstractmethod
from regras_jogo.regras_abstratas import AbstractRegrasJogo
from .personagens import Personagens
from percepcoes import PercepcoesJogador
from acoes import MoverNave, DirecaoMoverNave


class RegrasAsteroids(AbstractRegrasJogo):
    """ Interface mínima para implementar um jogo interativo e modular. Não
    tente instanciar objetos dessa classe, ela deve ser herdada e seus métodos
    abstratos sobrecarregados.
    """
    def __init__(self) -> None:
        super().__init__()
        posicao_asteroides = {
                (200,150), (300,150), (400,150), (500,150)
            }

        self.asteroides = posicao_asteroides
        self.id_personagens = {Personagens.JOGADOR_ASTEROIDS: 0}
        self.acoes_personagens = {0: None}
        self.posicaoNave = (400,500)
        self.dimensoes = (800,600)
        '''self.posicaoBala = self.posicaoNave[0]+20'''
        self.estadoBala = "pronto"
        self.msg_jogador = None



    def registrarAgentePersonagem(self, personagem):
        """ Cria ou recupera id de um personagem agente.
        """
        return self.id_personagens[personagem]


    def isFim(self):
        """ Boolean indicando fim de jogo em True.
        """
        return len(self.asteroides) == 0


    def gerarCampoVisao(self, id_agente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        percepcoes_jogador = PercepcoesJogador(
            pos_asteroids=set(self.asteroides),
            dimensoes=self.dimensoes,
            posicao_nave=self.posicaoNave,
            estado_bala=self.estadoBala
            )

        self.msg_jogador = None
        return percepcoes_jogador


    def registrarProximaAcao(self, id_agente, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        self.acoes_personagens[id_agente] = acao


    def atualizarEstado(self, diferencial_tempo):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        acao_jogador = self.acoes_personagens[
            self.id_personagens[Personagens.JOGADOR_ASTEROIDS]]
        if acao_jogador.tipo == MoverNave.MOVER_NAVE:
            direcao =acao_jogador.parametros
            if direcao == DirecaoMoverNave.MOVER_PARA_ESQUERDA:
                soma = self.posicaoNave[0]-10
                '''o valor 500 é padrão pois a nave somente deve movimentar no eixo x'''
                self.posicaoNave = (soma, 500)
            if direcao == DirecaoMoverNave.MOVER_PARA_DIREITA:
                soma = self.posicaoNave[0]+10
                '''o valor 500 é padrão pois a nave somente deve movimentar no eixo x'''
                self.posicaoNave = (soma, 500)
            if direcao == DirecaoMoverNave.ATIRAR:
                self.estadoBala = "atirando"
                start_linha = -300
                start_coluna = 0
                end_linha = 730
                for linha in range(start_linha, end_linha):
                    for coluna in range(start_coluna, self.dimensoes[1]):

                        if (linha, coluna) in self.asteroides:
                            if (self.estadoBala == "atirando"):
                                if self.posicaoNave[0] in range(linha -30, linha +11):
                                    self.asteroides.discard((linha, coluna))
                                    self.posicaoBala = self.posicaoNave[0]

            else:
                self.estadoBala = "pronto"





    def terminarJogo(self):
        """ Faz procedimentos de fim de jogo, como mostrar placar final,
        gravar resultados, etc...
        """
        return


def construir_jogo(*args, **kwargs):
    """ Método factory para uma instância RegrasJogo arbitrária, de acordo com os
    parâmetros. Pode-se mudar à vontade a assinatura do método.
    """


    return RegrasAsteroids()