# Padrão Adapter

O padrão adapter tem por intenção converter a interface de uma classe em outra interface, esperada pelos clientes. O Adapter permite que classes com interfaces incompatíveis trabalhem em conjunto o que, de outra forma, seria impossível.

Este padrão em python em bora que pareça não fazer sentido, pois conseguimos instânciar como parametros dentro de funções outros objetos, é uma boa prática a utilização para uma melhor compreenção do código ali contido!

Para este exemplo, criei uma classe abastrata chamada Roteador.

```python
from abc import ABC, abstractmethod


class Roteador(ABC):
    @abstractmethod
    def obtem_conexao(self) -> str:
        """"""
```

Logo mais duas classes que herdão de Roteador, MeuRoteador e VizinhoRoteador.
Cada uma retornando uma string indicando qual é a conexão!

```python
from src.adapter.roteador import Roteador


class MeuRoteador(Roteador):
    def obtem_conexao(self) -> str:
        return 'Conectado a minha rede em '


class VizinhoRoteador(Roteador):
    def obtem_conexao(self) -> str:
        return 'Conectado a rede do vizinho em '
```

Agora a classe abstrada Computador.
Em um metodo conecta, ela recebe o Roteador. E em um methodo get_nome que retornara nas classes que herdarão este Computador, ira retornar o nome.


```python
from abc import ABC, abstractmethod

from roteador import Roteador


class Computador(ABC):
    @abstractmethod
    def conecta(self, roteador: Roteador) -> str:
        """"""

    @abstractmethod
    def get_nome(self) -> str:
        """"""
```

Crio a classe MeuComputador herdando de Computador.

```python
from comptador import Computador
from meu_roteador import MeuRoteador


class MeuComputador(Computador):
    def conecta(self, roteador: MeuRoteador) -> str:
        return roteador.obtem_conexao() + self.get_nome()

    def get_nome(self) -> str:
        return 'meu computador'
```

E um adaptador para conseguir me conectar com o VizinhoRoteador, que ira herdar de MeuComputador. Porém no metodo conecta, recebera o VizinhoRoteador.

```python
from meu_computador import MeuComputador
from vizinho_roteador import VizinhoRoteador


class AdaptarorConectarVizinho(MeuComputador):
    def conecta(self, roteador: VizinhoRoteador) -> str:
        return super().conecta(roteador)
```

Exemplo de implementação:

```python
from adapter_conectar_vizinho import AdaptarorConectarVizinho
from comptador import Computador
from meu_computador import MeuComputador
from meu_roteador import MeuRoteador
from roteador import Roteador
from vizinho_roteador import VizinhoRoteador


class App:
    def __init__(self) -> None:

        meu_roteador: Roteador = MeuRoteador()

        vizinho_roteador: Roteador = VizinhoRoteador()

        computador = MeuComputador()

        print(computador.conecta(meu_roteador))

        adapter: Computador = AdaptarorConectarVizinho()

        print(adapter.conecta(vizinho_roteador))


if __name__ == '__main__':
    App()
```

Resultado apresentado ao final da execução:

```bash
Conectado a minha rede em meu computador
Conectado a rede do vizinho em meu computador
```
