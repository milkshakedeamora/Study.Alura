'''1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.
3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.'''
informacoes = {'nome':'Pedro','idade':29,'cidade':'Rio de Janeiro'}
print(informacoes)
informacoes['idade'] = 35
print(informacoes)
informacoes['profissao'] = 'Professor'
print(informacoes)
informacoes.pop('cidade')
print(informacoes)
quadrados = [{'1':'1'},{'2':'4'},{'3':'9'},{'4':'16'},{'5':'25'}]
print(quadrados)
dicionario = [{'info1':'info-1'},{'info2':'info-2'},{'info4':'info-4'},{'info5':'info-5'}]
if 'info3' in dicionario: 
    print("A chave existe no dicionário.") 
else: 
    print("A chave  não existe no dicionário.") 
