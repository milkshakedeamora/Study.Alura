class Restaurante:
    restaurantes = []
    def __init__(self,nome,categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} {self._categoria}'
    
    @classmethod
    def listar_restaurante(cls):
        for restaurante in cls.restaurantes:
          print(f"{restaurante._nome} restaurante {restaurante._categoria} Ativo: {restaurante.ativo}")  
          
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alterar_ativo(self):
        self._ativo = not self._ativo
restaurante_praca = Restaurante('praça','Gourmet')
print(vars(restaurante_praca))
restaurante_pizza = Restaurante ('Pizza Express','Italiano')
restaurante_pizza.alterar_ativo()
print(restaurante_pizza)

Restaurante.listar_restaurante()