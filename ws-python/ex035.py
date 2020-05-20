r1 = float(input('Primeiro Segmento '))
r2 = float(input('Segundo Segmento '))
r3 = float(input('Terceiro Segmento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos podem formar triangulo')
else:
    print(f'Os segmentos não podem formar triangulo')
