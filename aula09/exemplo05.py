def soma(x, y):
    r = x + y
    # print(resultado)
    return r #retorna o resultado para quem chamou


# num1 = 5
# num2 = 9
# soma(num1, num2)
# soma(5, 9)
for i in range(3):
    num1 = float(input('informe um numero: '))
    num2 = float(input('informe outro numero: '))
    resultado = soma(num1, num2) # chamada da função
    print(resultado)