"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
Digite um número: 1834
unidade: 4
dezena: 3
centeza: 8
milhar: 1
"""
num = str(input('Digite um número de 0 a 9999: '))
un = num[3]
de = num[2]
c = num[1]
m = num[0]
print(f'Unidade: {un}')
print(f'Dezena: {de}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
