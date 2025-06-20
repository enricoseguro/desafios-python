"""
Escreva um programa que faça o computador "pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random

num = random.randint(0, 5)
escolha = int(input('Adivinhe um número de 0 a 5: '))
if num == escolha:
    print('Parabéns, você venceu!')
else:
    print('Você perdeu!:(')
    print(f'O número escolhido foi {num}')
