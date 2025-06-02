atividadeA = int(input('Informe os dias para a atividade A: '))
atividadeB = int(input('Informe os dias para a atividade B: '))
atividadeC = int(input('Informe os dias para a atividade C: '))

if atividadeA > 0 and atividadeB > 0 and atividadeC > 0:
    total = atividadeA + atividadeB + atividadeC
    print(f'O tempo total do projeto foi: {total} dias')
else:
    print('Erro: Os dias não podem ser negativos')