# Padrão Abstract Factory

Este padrão tem por intenção, fornecer uma interface para criação de familias de objetos relacionados ou dependentes sem especificar suas classes concretas.

Com isto podemos criar instâmcias de várias famílias, diferente do Factory Method que precisa de uma fábrica para cada objeto.

Para o exemplo é criado o Produto:

```python
from abc import ABC, abstractmethod


class Produto(ABC):
    __tipo: str
    __valor: float
    __descricao: str

    def __init__(self, tipo: str, valor: float, descricao: str) -> None:
        self.__tipo = tipo
        self.__valor = valor
        self.__descricao = descricao

    def get_tipo(self) -> str:
        return self.__tipo

    def get_valor(self) -> float:
        return self.__valor

    def get_descricao(self) -> str:
        return self.__descricao

    @abstractmethod
    def exibe_produto(self) -> str:
        """Este metodo precisa ser implementado!"""
```

E as fabricas referentes a este produto, ate ai nada de diferente do Factory Method

```python
from produto import Produto


class ProdutoXSalada(Produto):
    def __init__(self, produto: str, valor: float, descricao: str) -> None:
        super().__init__(produto, valor, descricao)

    def exibe_produto(self) -> str:
        produto = (
            '\n\nproduto: {}\n'.format(self.get_tipo())
            + 'valor: R${}\n'.format(self.get_valor())
            + 'descrição: {}\n'.format(self.get_descricao())
        )
        print(produto)


class ProdutoXSalada(Produto):
    def __init__(self, produto: str, valor: float, descricao: str) -> None:
        super().__init__(produto, valor, descricao)

    def exibe_produto(self) -> str:
        produto = (
            '\n\nproduto: {}\n'.format(self.get_tipo())
            + 'valor: R${}\n'.format(self.get_valor())
            + 'descrição: {}\n'.format(self.get_descricao())
        )
        print(produto)
```

As duas FÁBRICAS implementando os métodos de Produto.

A mudança ocorre ao criar uma única FÁBRICA para construção destes Produtos atráves de uma classe denominada Emrpesa.
Criamos este objeto com dois comportamentos, uma para criar ProdutoXSalada e o outro para criar ProdutoXSalada. Ficando da seguinte forma.

```python
from abc import ABC, abstractmethod

from produto_x_salada import ProdutoXSalada
from produto_humburquer import ProdutoHumburquer


class Empresa(ABC):

    @abstractmethod
    def cadastrar_x_salada(self, produto: str, valor: float, descricao: str) -> ProdutoXSalada:
        """Este metodo precisa ser implementado!"""

    @abstractmethod
    def cadastrar_humburquer(self, produto: str, valor: float, descricao: str) -> ProdutoHumburquer:
        """Este metodo precisa ser implementado!"""
```

Com isso, teremos somente uma FÁBRICA para os dois Produtos referente a classe Empressa.

```python
from empresa import Empresa
from produto_x_salada import ProdutoXSalada
from produto_humburquer import ProdutoHumburquer


class Lanchonete(Empresa):

    def cadastrar_x_salada(self, produto: str, valor: float, descricao: str) -> ProdutoXSalada:
        return ProdutoXSalada(produto=produto, valor=valor, descricao=descricao)

    def cadastrar_humburquer(self, produto: str, valor: float, descricao: str) -> ProdutoHumburquer:
        return ProdutoHumburquer(produto, valor, descricao)
```

Podemos observar que Abstract Factory é para se aplicar em um grupo de produtos bem definidos, se há alguma chance de se modificar é prefirivel o uso de Factory Method.

Mas a chamada deste padrão ficaria como.

```python 
from empresa import Empresa
from lanchonete import Lanchonete
from produto_humburquer import ProdutoHumburquer
from produto_x_salada import ProdutoXSalada


class App:
    empresa: Empresa
    x_salada: ProdutoXSalada
    humburquer: ProdutoHumburquer

    def __init__(self) -> None:
        self.empresa = Lanchonete()

        self.x_salada = self.empresa.cadastrar_x_salada('X-Salada', 12.50, 'O melhor da minha casa!')
        self.humburquer = self.empresa.cadastrar_humburquer('Humburquer', 10.50, 'Humburquer caseiro!')

        self.x_salada.exibe_produto()
        self.humburquer.exibe_produto()


if __name__ == '__main__':
    App()
```

O resultado que teriamos com está chamada é exatamente este:

```bash

produto: X-Salada
valor: R$12.5
descrição: O melhor da minha casa!



produto: Humburquer
valor: R$10.5
descrição: Humburquer caseiro!

```