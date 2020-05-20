distancia = int(input('Qual a distancia da viagem: '))

if distancia <= 200:
    passagem = distancia * .50
else:
    passagem = distancia * .45
print(f'Viagem de {distancia}km')
print(f'Valor da passagem R${passagem:.2f}')