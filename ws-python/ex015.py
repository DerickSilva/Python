km = float(input('Quantos Km percorrido: '))
diaria = int(input('Quantos dias alugado: '))
total = (diaria * 60) + (km * .15)
print(f'Foram percorridos {km}km e {diaria} diarias, total de R${total:.2f}')
