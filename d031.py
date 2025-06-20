"""
Desenvolva um programa que pergunte a distânca de uma viagem em Km, calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""
distancia = float(input('Qual a distância da viagem em Km? '))
if distancia <= 200:
    preco = distancia * 0.50
    print(f'O valor da viagem vai dar R${preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'O valor da viagem vai dar R${preco:.2f}')
