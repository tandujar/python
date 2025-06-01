import re

nome = str(input('Digite o nome do cliente para validação: '))

if re.fullmatch(r'[A-Z][a-z]*', nome):
    print('Nome válido!')
else:
    print('Nome inválido!')