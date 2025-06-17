l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
ar = a * l #Calcula a área da parede (nome da variável "ar"
rt = 2 #Rendimento de tinta é 2 metros quadrados p/L
lt = ar / rt
print(f'A área da parede é {ar:.2f}m²')
print(f'Serão necessários {lt:.2f}L de tinta para pintar toda a área')