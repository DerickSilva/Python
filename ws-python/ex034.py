salario = float(input('Digite o salario R$ '))

if salario > 1250:
    novoSalario = salario + (salario * 10 / 100)
else:
    novoSalario = salario + (salario * 15 / 100)

print(f'O funcionario que ganhava R${salario:.2f} passa a ganhar R${novoSalario:.2f}')
