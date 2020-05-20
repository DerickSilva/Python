import random
pc = random.randint(1, 5)
jogador = int(input('Digite um numero: '))

if pc == jogador:
    print(f'Parabens você ganhou, eu tambem pensei no numero {pc}')
else:
    print(f'Eu ganhei, pensei no numero {pc}')
