from abc import ABC, abstractmethod

from src.adapter.roteador import Roteador


class Computador(ABC):
    @abstractmethod
    def conecta(self, roteador: Roteador) -> str:
        """"""

    @abstractmethod
    def get_nome(self) -> str:
        """"""
