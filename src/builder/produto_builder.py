from abc import ABC, abstractmethod

from src.builder.produto import Produto


class ProdutoBuilder(ABC):
    
    @abstractmethod
    def set_tipo(self, tipo: str) -> None:
        """"""

    @abstractmethod
    def set_valor(self, valor: float) -> None:
        """"""

    @abstractmethod
    def set_descricao(self, descricao: str) -> None:
        """"""

    @abstractmethod
    def get_produto(self) -> Produto:
        """"""
