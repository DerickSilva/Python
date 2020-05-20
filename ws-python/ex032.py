ano = int(input('Que ano deseja analisar? '))
if ano % 4 == 0:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano {ano} não é bissexto')
