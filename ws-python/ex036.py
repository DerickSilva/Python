valorCasa = float(input('Valor da casa R$ '))
salarioComprador = float(input('Salario Comprador R$ '))
anosFinanciamento = int(input('Quantos anos de financiamento? '))

meses = anosFinanciamento * 12
prestacao = valorCasa / meses

if prestacao <= salarioComprador * 30 / 100:
    print(f'Valor da prestação R${prestacao:.2f}, emprestimo aprovado')
else:
    print(f'Para a prestação R${prestacao:.2f} seu salario ultrapassa 30%, emprestimo negado')



