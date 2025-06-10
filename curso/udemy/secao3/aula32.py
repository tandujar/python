"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

print("Exercicio 1")

numero = None
resultado = None

try:
    numero = int(input("Digite um número inteiro: "))
    resultado = numero % 2
    if resultado == 0:
        print(f"O número: {numero} é par")
    else:
        print(f"O número: {numero} é ímpar")
except:
    print("O número digitado não é inteiro")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print("")
print("Exercicio 2")

hora = None

try:
    hora = int(input("Informe a hora em números inteiros: "))
    if hora >= 0 and hora <= 11:
        print("Bom dia")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde")
    elif hora >= 18 and hora <= 23:
        print("Boa noite")
    else:
        print("Hora inválida")
except:
    print("O número digitado não é inteiro")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print("")
print("Exercicio 3")

nome = input("Digite o seu primeiro nome: ")
tamanho = len(nome)

if tamanho <= 4:
    print("Seu nome é curto")
elif tamanho >= 5 and tamanho <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
