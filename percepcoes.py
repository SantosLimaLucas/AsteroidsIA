from dataclasses import dataclass
from typing import Tuple, Set, Optional


@dataclass
class PercepcoesJogador():
    '''Coloque aqui atributos que descrevam as percepções possíveis de
    mundo por parte do agente jogador
    
    Vide documentação sobre dataclasses em python.
    '''
    estado_bala: "pronto"
    pos_asteroids: Set[Tuple[int, int]]
    dimensoes: Tuple[int, int] = (800, 600)
    posicao_nave : Tuple[int, int] = (400, 500)
    posicao_bala : Tuple[int, int] = (0, 500)

    '''mensagem_jogo: Optional[str] = None'''