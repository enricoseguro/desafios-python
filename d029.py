"""
Escreva um programa que leia a velocidade de um carro. SE ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado, a multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade = float(input('Digite a velocidade do carro em Km/h: '))
if velocidade > 80:
    print('Você ultrapassou os limites de velocidade, será multado!')
    multa = (velocidade - 80) * 7
    print(f'A multa foi de R${multa:.2f}, tenha mais cuidado da próxima vez!')
