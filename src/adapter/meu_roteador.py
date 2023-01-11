from src.adapter.roteador import Roteador


class MeuRoteador(Roteador):
    def obtem_conexao(self) -> str:
        return 'Conectado a minha rede em '
