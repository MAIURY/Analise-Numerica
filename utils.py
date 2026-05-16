import math


def teorema_bolzano(funcao, a, b):
    # Retorna True se houver mudanca de sinal no intervalo [a, b]
    return funcao(a) * funcao(b) < 0


def derivada_aproximada(funcao, x, h=1e-6):
    # Diferenca central para aproximar a derivada
    return (funcao(x + h) - funcao(x - h)) / (2 * h)
