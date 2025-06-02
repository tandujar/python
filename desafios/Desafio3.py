'''
Desafio 3: Contador de Vogais
Objetivo: Solicitar uma palavra e contar quantas vogais ela possui.
'''

vogais = ['a','e','i','o','u']

def verifica_vogais():
    palavra = input('Informe uma palavra: ').lower()

    contador = 0

    for letra in palavra:
        if letra in vogais:
            contador += 1

    print(f"A palavra contém {contador} vogais.")

verifica_vogais()

