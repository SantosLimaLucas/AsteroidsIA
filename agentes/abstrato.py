from agentes.tipos import TiposAgentes
from abc import ABC, abstractmethod
class AgenteAbstrato(ABC):
    '''
    Classe abstrata de agentes artificiais racionais.
    '''

    @abstractmethod
    def adquirirPercepcao(self, percepcao_mundo):
        ''' Forma uma percepcao interna por meio de seus sensores, a partir das
        informacoes de um objeto de visao de mundo.
        '''
        return
    
    @abstractmethod
    def escolherProximaAcao(self):
        ''' Escolhe proxima acao, com base em seu entendimento do mundo, a partir
        das percepções anteriores.
        '''
        return

def construir_agente(*args, **kwargs):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    from agentes.bfs import AgenteAutomaticoBFS
    from agentes.humano import AgentePrepostoESHumano
    from agentes.dfs import AgenteAutomaticoDFS
    if args[0] is TiposAgentes.AUTO_BFS:
        return AgenteAutomaticoBFS()
    if args[0] is TiposAgentes.PREPOSTO_HUMANO:
        return AgentePrepostoESHumano()
    if args[0] is TiposAgentes.AUTO_DFS:
        return AgenteAutomaticoDFS()
