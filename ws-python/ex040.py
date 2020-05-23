n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7.0:
    print(f'Sua media foi {media} e você esta aprovado')
elif media >= 5.0:
    print(f'Sua media foi {media} e você esta de recuperação')
else:
    print(f'Sua media foi {media} e você esta reprovado')
