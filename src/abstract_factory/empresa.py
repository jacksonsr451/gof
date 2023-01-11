from abc import ABC, abstractmethod

from src.abstract_factory.produto_humburquer import ProdutoHumburquer
from src.abstract_factory.produto_x_salada import ProdutoXSalada


class Empresa(ABC):
    @abstractmethod
    def cadastrar_x_salada(
        self, produto: str, valor: float, descricao: str
    ) -> ProdutoXSalada:
        """Este metodo precisa ser implementado!"""

    @abstractmethod
    def cadastrar_humburquer(
        self, produto: str, valor: float, descricao: str
    ) -> ProdutoHumburquer:
        """Este metodo precisa ser implementado!"""
