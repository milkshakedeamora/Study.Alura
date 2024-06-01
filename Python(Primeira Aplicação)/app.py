import os

restaurantes = []

def exibirNome():
    '''
    Exibe o título do app
    '''
    print("""
     ██████████████████████████████
     █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀█
     █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄█
     ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀
███████████████████████████████████████████
█▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
██─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    """)

def exibirOpcoes():
    '''
    Exibe as opções que o úsuario pode escolher
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/desativar restaurante')
    print('4. Sair')

def voltarMenu():
    '''
    Solicita ao úsuario digitar um tecla e executar a função main()
    '''
    input('Digite uma tecla para voltar ao menu principal...')
    os.system('cls')
    main()

def cadastrarRestaurante():
    '''
    Cadastra um restaurante: insere um dicionario no array restaurantes com o nome e categoria informados pelo úsuario.
    '''
    os.system('cls')
    nome = input('Nome do novo restaurante: ')
    categoria = input(f'Categoria do {nome}: ')
    restaurantes.append({'nome': nome, 'categoria': categoria, 'ativo': False})
    print(f'{nome} cadastrado.')
    voltarMenu()

def listarRestaurantes():
    '''
    lista os restaurantes: exibe todos os itens do array restaurantes.
    '''
    os.system('cls')
    for restaurante in restaurantes:
        estado = 'ativo' if restaurante['ativo'] else 'inativo'
        print(f"{restaurante['nome']} restaurante {restaurante['categoria']}  {estado}")
    voltarMenu()

def alterarEstado():
    '''
    Modifica o valor de ativo em um dicionario se encontrado pelo campo nome.
    '''
    os.system('cls')
    nome_restaurante = input("Qual restaurante deseja ativar/desativar? ")
    for restaurante in restaurantes:
        if nome_restaurante.lower() == restaurante['nome'].lower():
            restaurante['ativo'] = not restaurante['ativo']
            estado = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'{restaurante["nome"]} foi {estado}.')
            voltarMenu()
            return
    print(f'{nome_restaurante} não encontrado.')
    voltarMenu()

def finalizarPrograma():
    '''
    Exibe uma mensagem de programa finalizado.
    '''
    os.system('cls')
    print("Programa finalizado.")
    

def escolherOpcao():
    '''
    Recebe a opção escolhida pelo úsuario.
    '''
    try:
        opcao = int(input('Escolha sua opção: '))
        print(f'Opção {opcao} escolhida.')
        return opcao
    except :
        print('Opção inválida...')
        voltarMenu()

def realizarOpcao():
    '''
    Realiza a opção escolhida pelo usuario apartir da função escolherOpcao()
    '''
    match (escolherOpcao()):
        case 1:
            cadastrarRestaurante()
        case 2:
            listarRestaurantes()
        case 3:
            alterarEstado()
        case 4:
            finalizarPrograma()
        case _:
            print('Opção inválida...')
            voltarMenu()

def main():
    '''
    Chama as funções exibirNome, exibirOpoes e realizarOpcao
    '''
    exibirNome()
    exibirOpcoes()
    realizarOpcao()

if __name__ == '__main__':
    main()
