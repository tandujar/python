'''
Desafio 1: Verificador de Número Par ou Ímpar
Objetivo: Solicitar um número ao usuário e dizer se é par ou ímpar.
'''

def verifica_numero():    
    numero = int(input('Informe um número: '))    
    if numero % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é ímpar')

verifica_numero()