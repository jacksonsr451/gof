from abc import ABC, abstractmethod


class Roteador(ABC):
    @abstractmethod
    def obtem_conexao(self) -> str:
        """"""
