preco = float(input('Digite o valor do produto: '))
formaPagamento = int(input('''
Formas de Pagemento
[1] à vista dinheiro/cheque
[2] à vista cartao
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual é a opção: '''))

if formaPagamento == 1:
    aVista = preco - (preco * 10 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${aVista:.2f}')
elif formaPagamento == 2:
    aVista = preco - (preco * 5 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${aVista:.2f}')
elif formaPagamento == 3:
    novoPreco = preco / 2
    print(f'A compra de R${preco:.2f} sera parcelada em 2x de {novoPreco:.2f}')
else:
    qtdParcelas = int(input('Quantas parcelas: '))
    if qtdParcelas >= 3:
        novoPreco = preco + (preco * 20 / 100)
        parcelada = (preco + (preco * 20 / 100)) / qtdParcelas
        print(f'Sua compra sera parcelada em {qtdParcelas}x de {parcelada:.2f} com juros')
        print(f'Sua compra de R${preco:.2f} vai custar R${novoPreco:.2f} no final')
    else:
        print('Atenção!! Quantidade de parcelas invalida')
    
