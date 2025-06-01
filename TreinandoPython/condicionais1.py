macas = int(input('Informe a quantidade de maças vendidas: '))
bananas = int(input('Informe a quantidade de bananas vendidas: '))

if macas > bananas:
    print('As maças tiveram mais vendas')
elif bananas > macas:
    print('As bananas tiveram mais vendas')
else:
    print('Houve empate nas vendas')
    
    