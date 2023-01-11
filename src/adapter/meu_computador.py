from src.adapter.comptador import Computador
from src.adapter.meu_roteador import MeuRoteador


class MeuComputador(Computador):
    def conecta(self, roteador: MeuRoteador) -> str:
        return roteador.obtem_conexao() + self.get_nome()

    def get_nome(self) -> str:
        return 'meu computador'
