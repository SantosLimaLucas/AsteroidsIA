from enum import Enum
from dataclasses import dataclass
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