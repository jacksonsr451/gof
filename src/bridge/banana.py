from src.bridge.frutas import Frutas
from src.bridge.implementacao import Implementacao


class Banana(Frutas):
    def __init__(self, executa_implementacao: Implementacao) -> None:
        super().__init__(executa_implementacao)

    def execute(self) -> None:
        self.executa_implementacao.implementa()
