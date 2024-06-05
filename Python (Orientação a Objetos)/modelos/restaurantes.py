class Restaurante:
    restaurantes = []
    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} {self.categoria}'
    def listar_restaurante():
        for restaurante in Restaurante.restaurantes:
          estado = 'ativo' if restaurante['ativo'] else 'inativo'
          print(f"{restaurante['nome']} restaurante {restaurante['categoria']}  {estado}")  
restaurante_praca = Restaurante('Praça','Gourmet')
print(vars(restaurante_praca))
restaurante_pizza = Restaurante ('Pizza Express','Italiano')
print(restaurante_pizza)