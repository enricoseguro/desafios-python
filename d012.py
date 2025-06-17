p = float(input('Digite o preço inicial do produto: '))
d = float(input('Digite a porcentagem de desconto dele: '))
vd = p * (d / 100)
t = p - vd
print(f'O preço atual do produto com o desconto ficará R${t:.2f}')