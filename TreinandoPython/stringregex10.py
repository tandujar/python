import re

texto = input('Digite o nome completo e o ano de nascimento do paciente: ')

padrao = r'(\w+) (\w+) - (\d{4})'  

resultado = re.search(padrao, texto)

if resultado:
    primeiro_nome = resultado.group(1)
    sobrenome = resultado.group(2)
    ano_nascimento = resultado.group(3)

    print(f"Primeiro Nome: {primeiro_nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Ano de Nascimento: {ano_nascimento}")
else:
    print("Formato inválido!")

 