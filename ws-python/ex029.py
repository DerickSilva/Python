velocidade = int(input('Qual a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'MULTADO! Voce excedou o limite de 80K/h')    
    print(f'Voce deve pagar a multa de R${multa:.2f}')
else:
    print('Tenha um bom dia! Dirija com segurança')
    