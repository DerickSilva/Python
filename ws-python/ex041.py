from datetime import date
atual = date.today().year
anoNascimento = int(input('Ano de nascimento: '))
idade = atual - anoNascimento 

if idade <= 9:
    print(f'Atleta com {idade} anos categoria MIRIM')
elif idade <=14:
    print(f'Atleta com {idade} anos categoria INFANTIL')
elif idade <= 19:
    print(f'Atleta com {idade} anos categoria JUNIOR')
elif idade <= 25:
    print(f'Atleta com {idade} anos categoria SENIOR')
else:
    print(f'Atleta com {idade} anos categoria MASTER')
