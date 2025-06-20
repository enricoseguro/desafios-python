salario = float(input('Digite o seu salário: '))
cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m', }
if salario > 1250.00:
    salario = salario + (salario * 0.10)
    print(
        f'Seu salário irá aumentar {cores['vermelho']}10%{cores['limpa']}, ficando {cores['vermelho']}R${salario:.2f}{cores['limpa']}.')
else:
    salario = salario + (salario * 0.15)
    print(
        f'Seu salário irá aumentar {cores['verde']}15%{cores['limpa']}, ficando {cores['verde']}R${salario:.2f}{cores['limpa']}.')
