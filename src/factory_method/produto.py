from abc import ABC, abstractmethod


class Produto(ABC):
    __tipo: str
    __valor: float
    __descricao: str

    def __init__(self, tipo: str, valor: float, descricao: str) -> None:
        self.__tipo = tipo
        self.__valor = valor
        self.__descricao = descricao

    def get_tipo(self) -> str:
        return self.__tipo

    def get_valor(self) -> float:
        return self.__valor

    def get_descricao(self) -> str:
        return self.__descricao

    @abstractmethod
    def exibe_produto(self) -> str:
        """Este metodo precisa ser implementado!"""
