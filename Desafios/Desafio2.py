'''
Desafio 2: Calculadora de Média
Objetivo: Pedir 3 notas e calcular a média. Exiba se o aluno está Aprovado (média ≥ 7), Recuperação (média entre 5 e 6.9) ou Reprovado (média < 5).
'''

def verifica_media():
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    nota3 = float(input('Informe a terceira nota: '))

    notas = [nota1,nota2,nota3]

    media = sum(notas) / 3

    if media < 5:
        print(f'Sua média foi: {round(media,2)} você está reprovado')
    elif 5 <= media < 7:
        print(f'Sua média foi: {round(media,2)} você está em recuperação')
    else:
        print(f'Sua média foi: {round(media,2)} você está aprovado')

verifica_media()


        
