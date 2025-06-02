'''
Desafio 5: Tabuada Simples
Objetivo: Pedir um número e mostrar a tabuada de 1 a 10.
'''

def calcula_tabuada():       
    
    numero = int(input('Informe um número: '))  

    print(f'Tabuada do número: {numero}\n')

    for valor in range(1, 11):
        resultado = numero * valor        
        print(f'{numero} x {valor} = {resultado}')

calcula_tabuada()

