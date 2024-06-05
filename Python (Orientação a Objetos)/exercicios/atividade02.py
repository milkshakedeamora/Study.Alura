'''
Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
'''

class Carro:
    modelo = ''
    cor = ''
    ano = int 
uno = Carro()
uno.modelo = 'uno'
uno.cor = 'verde limão'
uno.ano = 2010

class Restaurante:
    def __init__(self, nome, categoria) :        
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.opcaoRestricoesAlimentares = False
        self.acessbilidade = False
    def __str__(self) -> str:
        return f'{self.nome} {self.categoria}'
hamburgueria = Restaurante("Papa's Burguer", 'Fast Food')
print(hamburgueria)

class Cliente:
    def __init__(self, nome, idade, profissao,estado):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.estado = estado

cliente1 = Cliente('Eduardo',45, 'Professor', 'São Paulo')
cliente1 = Cliente('Maria',65, 'Auxiliar', 'Minas Gerais')
cliente1 = Cliente('Paulo',25, 'Ator', 'Rio de Janeiro')