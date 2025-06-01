total_despesas = float(input('Digite o total de despesas do mês (R$): '))

if total_despesas > 3000:    
    print('Atenção! Você ultrapassou o limite do orçamento.')
else:
    print('Os seus gastos estão dentro do limite do orçamento.')