from abc import ABC, abstractmethod


class NotaMusical(ABC):
    def clone(self):
        return self

    @abstractmethod
    def desenhar(self) -> None:
        """"""
