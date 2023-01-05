class Janela():
    __janela = {}

    def __init__(self) -> None:
        self.dimension = (640, 720)
        self.name = 'Window'

    @staticmethod
    def get_instance():
        if Janela not in Janela.__janela:
            Janela.__janela[Janela] = Janela()
        return Janela.__janela[Janela]
