'''
Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

Crie uma instância da classe e imprima o valor da propriedade titular.

Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

Crie um método de classe para a conta ClienteBanco.


'''
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo 
        self.ativo = False
        
    def __str__(self):
        return f'Titular {self.titular} - Saldo: R${self.saldo}'
    def ativar_conta(self):
       self.ativo = True
        
    
cliente1 = ContaBancaria('Joaquim',15000)
cliente2 = ContaBancaria('Pedro',785)
print(cliente1)
print(cliente2)
cliente3 = ContaBancaria('Julia',150)
cliente3.ativar_conta()
print(cliente3.ativo)