from abc import ABC, abstractmethod

from src.bridge.implementacao import Implementacao


class Frutas(ABC):
    executa_implementacao: Implementacao

    def __init__(self, executa_implementacao: Implementacao) -> None:
        self.executa_implementacao = executa_implementacao

    @abstractmethod
    def execute(self) -> None:
        """"""
