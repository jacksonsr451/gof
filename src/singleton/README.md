# Padrão Singleton

Cria somente uma instancia de cada objeto

Padrão muito utilizado para criação de objetos aonde o sentido é ser criado somente um exemplo: 

Criando uma conexão com o banco de dados, está conexão para um melhor desempenho de nosso servidor é necessario que tenha somente uma instancia de conexão e que seja compartilhada entre cada cliente. 

O indicado é a criação de uma clase com o padrão Songleton

Em python ao se instanciar um modulo, altomaticamente já é um singleton pois não pode ter uma redundancia (importe circular), porem podemos utilizar uma metaclass tipando nossa classe que ira garantir a existencia de somente uma instancia de nossa classe rodando em todo o projeto.