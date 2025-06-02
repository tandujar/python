
while True:
    
    usuario = str(input('Digite seu nome de usuário: '))
    senha = str(input('Digite sua senha: '))
    
    if len(usuario) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres')
        continue
    elif len(senha) < 8:
        print('A senha deve ter pelo menos 8 caracteres')
        continue
    else:
        print('Cadastro realizado com sucesso!')
        break
    