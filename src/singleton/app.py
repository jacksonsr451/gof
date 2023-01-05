from src.singleton.janela import Janela


class App:
    def __init__(self) -> None:
        self.janela = Janela()

        print(self.janela.name)


if __name__ == '__main__':
    App()
