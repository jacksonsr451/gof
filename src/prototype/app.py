from src.prototype.partitura import Partitura


class App:
    def __init__(self) -> None:
        self.partitura = Partitura()

        self.partitura.caregar_notas()

        self.partitura.get_nota('Dó').desenhar()
        self.partitura.get_nota('Ré').desenhar()
        self.partitura.get_nota('Mi').desenhar()
        self.partitura.get_nota('Fá').desenhar()
        self.partitura.get_nota('Fá').desenhar()
        self.partitura.get_nota('Fá').desenhar()
        self.partitura.get_nota('Dó').desenhar()
        self.partitura.get_nota('Ré').desenhar()
        self.partitura.get_nota('Dó').desenhar()
        self.partitura.get_nota('Ré').desenhar()
        self.partitura.get_nota('Ré').desenhar()
        self.partitura.get_nota('Ré').desenhar()


if __name__ == '__main__':
    App()
