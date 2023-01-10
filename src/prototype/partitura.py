from types import NoneType
from src.prototype.do import Do
from src.prototype.fa import Fa
from src.prototype.la import La
from src.prototype.mi import Mi
from src.prototype.nota_musical import NotaMusical
from src.prototype.re import Re
from src.prototype.si import Si
from src.prototype.sol import Sol


class Partitura:
    def __init__(self) -> None:
        self.notas: dict[str, NotaMusical] = dict()

    def caregar_notas(self) -> NoneType:
        self.notas = {
            'Dó': Do(),
            'Ré': Re(),
            'Mi': Mi(),
            'Fá': Fa(),
            'Sol': Sol(),
            'Lá': La(),
            'Si': Si()
        }

    def get_nota(self, nota: str) -> NotaMusical:
        return self.notas.get(nota).clone()
    