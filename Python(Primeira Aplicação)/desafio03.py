""" 
1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
"""
numeros = [1,2,3,4,5,6,7,8,9,10]
nomes =['Lucas','Pedro','Ana','Carla']
anos = ['2024','1999']

listaloop =['valor1','valor2','valor3']
for item in listaloop:
    print(item)
for i in range(10,0,-1):
    print(i)
numero = int(input('numero:'))
for i in range(0,11):
    print(f'{numero} x {i} = {numero*i}')
listasoma = [4,8,78,56,78]
try:
    soma = 0
    for numero in listasoma:
        soma+=numero
    print(soma)
except:
    print('Impossivel Calcular')

listaMedia = [80,78,54,2,48]
media = 0
for numero in listasoma:
    media+=numero
try:
    media/= len(listaMedia) 
    print(media)
except:
    print('Impossivel Media')