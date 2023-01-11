from src.adapter.meu_computador import MeuComputador
from src.adapter.vizinho_roteador import VizinhoRoteador


class AdaptarorConectarVizinho(MeuComputador):
    def conecta(self, roteador: VizinhoRoteador) -> str:
        return super().conecta(roteador)
