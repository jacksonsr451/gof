# Padrão Singleton

Cria somente uma instancia de cada objeto

Padrão muito utilizado para criação de objetos aonde o sentido é ser criado somente um exemplo: 

Criando uma conexão com o banco de dados, está conexão para um melhor desempenho de nosso servidor é necessario que tenha somente uma instancia de conexão e que seja compartilhada entre cada cliente. 

O indicado é a criação de uma clase com o padrão Songleton

Em python ao se instanciar um modulo, altomaticamente já é um singleton pois não pode ter uma redundancia (importe circular), porem podemos utilizar uma metaclass tipando nossa classe que ira garantir a existencia de somente uma instancia de nossa classe rodando em todo o projeto.

```python
class SingletonMeta(type):
    class SingletonMeta(type):
    """
    A classe Singleton pode ser implementada de diferentes maneiras em Python. Alguns
    os métodos possíveis incluem: classe base, decorador, metaclasse. Nós usaremos o
    metaclasse porque é a mais adequada para este fim.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possíveis mudanças no valor do argumento `__init__` não afetam
        a instância retornada.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
```

Diferente de outras linguagens, para fazermos esta referencia não utilizamos o construtor privado. Mas a classe singleton fica implementada da seguinte forma!

```python
class Connection(metaclass=SingletonMeta):
    """
    Por fim, qualquer singleton deve definir alguma lógica de negócios, que pode ser
    executado em sua instância
    """

    connection = None

    def __init__(self) -> None:
        """
        Minhas Configurações para se iniciar uma conexão
        """
    
    def get_connection(self):
        return connection
```

Ao implementar este modelo, teremos uma unica conexão com o banco de dados para o nosso projeto!
