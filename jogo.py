#!/usr/bin/env python3

import time
from regras_jogo.asteroids_regras_joo import construir_jogo
from regras_jogo.personagens import Personagens
from agentes.abstrato import construir_agente
from agentes.tipos import TiposAgentes


def ler_tempo(em_turnos=False):
    """ Se o jogo for em turnos, retorna a passada de 1 rodada.
    
    Se não for em turno, é continuo ou estratégico, retorna tempo
    preciso (ns) do relógio.
    """
    return 1 if em_turnos else time.time()


def iniciar_jogo():
    
    # Inicializar e configurar jogo
    jogo = construir_jogo()
    personagem_jogador = jogo.registrarAgentePersonagem(Personagens.JOGADOR_ASTEROIDS)
    agente_jogador = construir_agente(TiposAgentes.AUTO_GULOSO, Personagens.JOGADOR_ASTEROIDS)
    tempo_de_jogo = 0
    finalizou = False
    while not finalizou:
        while not jogo.isFim():
            # Mostrar mundo ao jogador
            ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
            agente_jogador.adquirirPercepcao(ambiente_perceptivel)

            # Decidir jogada e apresentar ao jogo
            acao = agente_jogador.escolherProximaAcao()
            jogo.registrarProximaAcao(personagem_jogador, acao)

            # Atualizar jogo
            tempo_corrente = ler_tempo()
            jogo.atualizarEstado(tempo_corrente - tempo_de_jogo)
            tempo_de_jogo += tempo_corrente
        ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
        agente_jogador.adquirirPercepcao(ambiente_perceptivel)
        tempo_corrente = ler_tempo()
        jogo.atualizarEstado(tempo_corrente - tempo_de_jogo)
        tempo_de_jogo += tempo_corrente
        finalizou = True


if __name__ == '__main__':
    iniciar_jogo()