from abc import ABC, abstractmethod

from src.factory_method.produto_x_salada import ProdutoXSalada


class Empresa(ABC):
    @abstractmethod
    def cadastrar_x_salada(
        self, produto: str, valor: float, descricao: str
    ) -> ProdutoXSalada:
        """Este metodo precisa ser implementado!"""
