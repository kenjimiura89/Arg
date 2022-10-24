#1. Crie uma função que, ao receber um número inteiro, retorna se um número  é par ou ímpar (utilizando **kwargs).#

def decorator (function):
    def calcular (*args, **kwargs):
        print('indo para função de calculo')
        function (*args, **kwargs)
    return calcular
@decorator
def verificacao (numero):
    if numero % 2 ==0:
        print('é par!')
    else:
        print('é impar!')
verificacao(7)