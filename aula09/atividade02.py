# Crie um algoritmo que receba um valor que calcule o dobro, triplo e quadrado

def dobro(x):
    r = x * 2
    return r
def triplo(x):
    r = x * 3
    return r
def quadrado(x):
    r = x * x
    return r


num = float(input('informe o numero que deseja: '))

resultado_dobro = dobro(num)
resultado_triplo = triplo(num)
resultado_quadrado = quadrado(num)
print(f' o dobro é {resultado_dobro}')
print(f' o triplo é {resultado_triplo}')
print(f' o quadrado é {resultado_quadrado}')
