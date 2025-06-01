peso = float(input('Informe o seu peso (kg): '))
altura = float(input('Informe a sua altura (m): '))

imc = round(peso / (altura ** 2),2)

print(f'Seu IMC é: {imc}')

if imc < 18.5:    
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:    
    print('Você está com o peso ideal.')
else:    
    print('Você está acima do peso.')
    