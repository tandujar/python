distancia = float(input('Digite a distância percorrida (em km): '))

if distancia <= 100:    
    print(f'Valor do pedágio: R$ 10,00')
elif 100 < distancia <= 200:
    print(f'Valor do pedágio: R$ 20,00')
else:
    print(f'Valor do pedágio: R$ 30,00')
    