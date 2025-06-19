"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas.
O nome com todas minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.
"""
n1 = input('Digite o nome da pessoa: ')
n1 = n1.upper()
print(n1)
n1 = n1.lower()
print(n1)
n1 = n1.split()
