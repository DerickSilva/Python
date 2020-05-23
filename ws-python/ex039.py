anoNascimento = int(input('Ano de nascimento: '))
idade = 2020 - anoNascimento
alistamento = anoNascimento + 18
if idade > 18:
    print(f'Voce tem {idade} anos e passou do tempo de se alistar')     
    print(f'Seu alistamento foi em {alistamento}')
elif idade == 18:
    print(f'Voce tem {idade} anos e esta na hora de se alistar')
else:
    print(f'Voce tem {idade} anos e vai se alistar em {alistamento}')
