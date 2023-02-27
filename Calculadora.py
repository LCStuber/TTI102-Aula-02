import Divisao, Multiplicacao, Potencia, Raiz, Soma, Subtracao

def coletorDeNúmero(msg="",errorMsg="Digite um valor válido"):
    ERRO = True
    while ERRO:
        try:
            a = float(input(msg))
            return a
        except:
            print(errorMsg)

def início():
    print('''
    ============ Bem-Vindo a nossa calculadora :D ============
    Para começar digite o número abaixo a operação que você deseja realizar:
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Potenciação
    6 - Radiciação
    0 - Sair do Programa''')
    a = coletorDeNúmero("","Digite um valor válido de 1 à 6")
    if a == 0:
        exit()
    elif a == 1:
        x = coletorDeNúmero("Digite o primeiro número da soma")
        y = coletorDeNúmero("Digite o segundo número da soma")
        print(f"O resultado da operação é: {Soma.soma(x,y)}")
    elif a == 2:
        x = coletorDeNúmero("Digite o primeiro número da subtração")
        y = coletorDeNúmero("Digite o segundo número da subtração")
        print(f"O resultado da operação é: {Subtracao.subtracao(x,y)}")
    elif a == 3:
        x = coletorDeNúmero("Digite o primeiro número da multiplicação")
        y = coletorDeNúmero("Digite o segundo número da multiplicação")
        print(f"O resultado da operação é: {Multiplicacao.multiplicacao(x,y)}")
    elif a == 4:
        x = coletorDeNúmero("Digite o número da divisor")
        ERRO = True
        while ERRO:
            y = coletorDeNúmero("Digite o número da dividendo")
            if y == 0:
                print("Digite um valor válido (diferente de 0)")
            else:
                ERRO = False
        print(f"O resultado da operação é: {Divisao.divisao(x,y)}")
    elif a == 5:
        x = coletorDeNúmero("Digite o número a ser elevado")
        y = coletorDeNúmero("Digite a potência")
        print(f"O resultado da operação é: {Potencia.potencia(x,y)}")
    elif a == 5:
        x = coletorDeNúmero("Digite o número a ser elevado")
        y = coletorDeNúmero("Digite a potência")
        print(f"O resultado da operação é: {Potencia.potencia(x,y)}")
    elif a == 6:
        ERRO = True
        while ERRO:
            x = coletorDeNúmero("Digite o número para extrair a raiz")
            if x < 0:
                print("Digite um valor válido (maior do que 0)")
            else:
                ERRO = False
        print(f"O resultado da operação é: {Raiz.raiz(x)}")
    else:
        print("Digite um valor de 0 a 6")

if __name__ == "__main__":
    while True:
        início()