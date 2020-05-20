preco = float(input('Digite o preco do produto R$ '))
desc = preco - (preco * 5 / 100)
print(f'O produto que custava R${preco:.2f} com 5% de desconto custa R${desc:.2f}')
