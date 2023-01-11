from src.adapter.roteador import Roteador


class VizinhoRoteador(Roteador):
    def obtem_conexao(self) -> str:
        return 'Conectado a rede do vizinho em '