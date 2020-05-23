n = int(input('Digite um numero inteiro '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para Binario
[ 2 ] converter para Octarl
[ 3 ] converter para Hexadecimal''')
opcao = int(input('Sua opcao '))

if opcao == 1:
    print(f'{n} para Binario {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} para Binario {oct(n)[2:]}') 
elif opcao == 3:
    print(f'{n} para Binario {hex(n)[2:]}')
else:
    print('Opcao invalida')
