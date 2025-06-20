salario = float(input('Digite o seu salário: '))
if salario > 1250.00:
    salario = salario + (salario * 0.10)
    print(f'Seu salário irá aumentar 10%, ficando R${salario:.2f}')
else:
    salario = salario + (salario * 0.15)
    print(f'Seu salário irá aumentar 15%, ficando R${salario:.2f}')
