"""
Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.
"""
frase = input('Digite uma frase: ')
frase = frase.upper()
contar = frase.count('A')
achar1 = frase.find('A')
achar2 = frase.rfind('A')
print(f'A letra "A" aparece {contar} vezes.')
print(f'A letra "A" aparece pela primeira vez em {achar1}.')
print(f'A letra "A" aparece pela última vez em {achar2}.')
