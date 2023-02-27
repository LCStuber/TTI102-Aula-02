def raiz(x):
    import math
    z = 0
    while x < 0:
        x = int(input("Input invalido, escreva um numero positivo: "))
    z = math.sqrt(x)
    return z