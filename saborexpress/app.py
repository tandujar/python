import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_programa():
    ''' Essa função é responsável por mostrar o título do app'''
    print('Sabor Express\n')

def exibir_opcoes():
    ''' Essa função é responsável por exibir as opções do app'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    ''' Essa função é responsável por voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def exibir_subtitulo(texto):
    ''' Essa função é responsável por exibir o subtitulo de cada opção selecionada'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcao():
    ''' Essa função é responsável por executar uma função para cada opção informada'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:        
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:        
            listar_restaurante()
        elif opcao_escolhida == 3:        
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:        
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria
    
    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de Novos Restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurante():
    ''' Essa função é responsável por listar os restaurantes'''
    exibir_subtitulo('Listando os Restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status ')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Essa função é responsável por alterar o estado do restaurante cadastrado'''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()
        
def finalizar_app():
    ''' Essa função é responsável por finalizar o app'''
    exibir_subtitulo('Finalizando o app')
    
def opcao_invalida():
    ''' Essa função retorna uma mensagem caso a opção informada seja inválida'''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()
        
def main():
    ''' Essa é a função principal'''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()