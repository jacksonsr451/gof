from src.adapter.adapter_conectar_vizinho import AdaptarorConectarVizinho
from src.adapter.comptador import Computador
from src.adapter.meu_computador import MeuComputador
from src.adapter.meu_roteador import MeuRoteador
from src.adapter.roteador import Roteador
from src.adapter.vizinho_roteador import VizinhoRoteador


class App:
    def __init__(self) -> None:

        meu_roteador: Roteador = MeuRoteador()

        vizinho_roteador: Roteador = VizinhoRoteador()

        computador = MeuComputador()

        print(computador.conecta(meu_roteador))

        adapter: Computador = AdaptarorConectarVizinho()

        print(adapter.conecta(vizinho_roteador))


if __name__ == '__main__':
    App()
