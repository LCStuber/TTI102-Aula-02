def potencia(x,y):
    z = 0
    z = x ** y
    return z

def raiz(x):
    import math
    z = 0
    while x < 0:
        x = int(input("Input invalido, escreva um numero positivo: "))
    z = math.sqrt(x)
    return z