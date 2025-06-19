"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
"""
nome = input('Digite o nome da pessoa: ')
primeiro = nome.split()[0]
ultimo = nome.split()[-1]
print(f'o primeiro nome é {primeiro}')
print(f'o último nome é {ultimo}')
