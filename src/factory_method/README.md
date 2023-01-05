# Padrão Factory Method

Este padrão é utilizado para criar um objeto, mas deixa as subclasses decidirem que classe instanciar.
Logo seu objetivo é de criar várias classes derivadas.

Para implementar este padrão:

- Precisamos ter uma classe abstrata (produto)
- E uma classe concreta (FÁBRICA) para esta classe (produto)


Com este padrão deveremos ter uma FÁBRICA para cada produto.

Exemplo:

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
        """Este método precisa ser implementado!"""
```

Está é um para um produto, é para gerar uma instância dele teremos de usar uma FÁBRICA.

Que neste caso ficaria da seguinte forma

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
```

Agora temos nosso produto sendo criado por sua FÁBRICA, mas vamos ainda um pouco além.

Temos o produto para precisamos gerenciar, criar realmente este produto, então vamos criar uma nova classe Empresa.

```python
from abc import ABC, abstractmethod

from prodtuto_x_salada import ProdutoXSalada


class Empresa(ABC):

    @abstractmethod
    def cadastrar_x_salada(self, produto: str, valor: float, descricao: str) -> ProdutoXSalada:
        """Este método precisa ser implementado!"""
```

E da mesma forma que fizemos com o Produto, iremos criar uma FÁbrica para esta nossa Empressa.

```python
from empresa import Empresa
from prodtuto_x_salada import ProdutoXSalada


class Lanchonete(Empresa):

    def cadastrar_x_salada(self, produto: str, valor: float, descricao: str) -> ProdutoXSalada:
        return ProdutoXSalada(produto=produto, valor=valor, descricao=descricao)

```

Nesta fábrica de Empresa, Lanchonete, há um método para se gerar um novo Produto. Este especifico cadastrar_x_salada, que também foi incluído na FÁBRICA de produtos.

Logo ao instanciarmos a classe Lanchonete, teremos acesso ao methodo cadastrar_x_salada que retorna uma instância de Produto (ProdutoXSalada) e que pode chamar um método dentro da classe Produto que exibe o produto o qual criamos.

```python
from empresa import Empresa
from lanchonete import Lanchonete
from produto import Produto


class App:
    empresa: Empresa
    produto: Produto

    def __init__(self) -> None:
        self.empresa = Lanchonete()

        self.produto = self.empresa.cadastrar_x_salada('X-Salada', 12.25, 'O melhor X-Salada da minha casa!')
        
        self.produto.exibe_produto()


if __name__ == '__main__':
    App()
```

Resultado em tela.

```bash
produto: X-Salada
valor: R$12.25
descrição: O melhor X-Salada da minha casa!
```

Com isso o temos de vantagens a criação de produtos sem precisar saber como são criados nem mesmo nos preocuparmos com as dependências ao se criar cada instância de produtos. 
Passamos somente os parametros incluídos nos métodos de cada fábrica.
