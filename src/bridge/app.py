from src.bridge.banana import Banana
from src.bridge.banana_implementacao import BananaImplementacao
from src.bridge.frutas import Frutas
from src.bridge.maca import Maca
from src.bridge.maca_implementacao import MacaImplementacao


class App:
    def __init__(self) -> None:
        banana: Frutas = Banana(BananaImplementacao())

        maca: Frutas = Maca(MacaImplementacao())

        banana.execute()

        maca.execute()


if __name__ == '__main__':
    App()
