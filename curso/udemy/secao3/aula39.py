"""
Iterando strings com while
"""

#       012345678910
# nome = "Luiz Otávio"  # Iteráveis
#      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# nova_string = ""
# nova_string += "*L*u*i*z* *O*t*á*v*i*o"

nome = input("Digite o seu nome: ")
nome_alterado = ""
contador = 0

while contador < len(nome):
    nome_alterado += "*" + nome[contador]
    contador += 1

print(nome_alterado)
