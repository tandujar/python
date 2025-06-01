'''
Desafio 4: Adivinha o Número
Objetivo: Gere um número aleatório entre 1 e 10 e peça para o usuário tentar adivinhar. Dê dicas se o número é maior ou menor que o chute.
'''

import random

def adivinha_numero():

    numero_gerado = random.randint(1,10)
    numero = int(input('Informe um número: '))  

    if numero == numero_gerado:
        print(f'Você acertou, o número era: {numero_gerado}')
    elif numero < numero_gerado:
        print(f'O número informado: {numero} é menor que o número gerado: {numero_gerado}')
    elif numero > numero_gerado:
        print(f'O número informado: {numero} é maior que o número gerado: {numero_gerado} ')

adivinha_numero()


