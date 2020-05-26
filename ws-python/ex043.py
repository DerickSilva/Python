peso = float(input('Qual é seu peso? '))
altura = float(input('Qual é sua altura? '))

imc = peso / (altura * altura) 

if imc < 18.5:
    print(f'IMC {imc:.1f} Abaixo do Peso')
elif imc < 25:
    print(f'IMC {imc:.1f} Peso Ideal')
elif imc < 30:
    print(f'IMC {imc:.1f} Sobrepeso')
elif imc < 40:
    print(f'IMC {imc:.1f} Obesidade')
else:
    print(f'IMC {imc:.1f} Obesidade Morbida')
