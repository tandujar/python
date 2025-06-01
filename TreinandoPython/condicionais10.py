valor_renda = float(input('Digite o valor da sua renda mensal: '))
valor_parcela = float(input('Digite o valor da parcela desejada: '))

if valor_renda > 2000 and (valor_parcela / valor_renda) >= 0.3:    
    print('Empréstimo negado: parcela acima de 30% da renda')
elif valor_renda <= 2000:
    print('Empréstimo negado: renda insuficiente')
else:
    print('Empréstimo aprovado')
    