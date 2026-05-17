import math


def teorema_bolzano(funcao, a, b):
    # Retorna True se houver mudanca de sinal no intervalo [a, b]
    return funcao(a) * funcao(b) < 0
