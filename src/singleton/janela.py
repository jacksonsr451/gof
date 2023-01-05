class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Janela(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.dimension = (640, 720)
        self.name = 'Window'
