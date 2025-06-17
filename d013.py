salario_inicial = float(input('Digite seu salário atual: '))
aumento = float(input('Digite a porcentagem de aumento: '))
aumento_porcentagem = aumento / 100
salario_aumento = salario_inicial * aumento_porcentagem
novo_salario = salario_inicial + salario_aumento
print(f'O seu salário atual com 15% de aumento será R${novo_salario:.2f}')