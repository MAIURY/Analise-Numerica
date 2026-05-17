import math
import utils


# Metodo da Bissecao (com historico de iteracoes)

def funcao(x):
    return math.exp(x) - x**2 - 3 * x

def bisseccao(funcao, a, b, tol=1e-6, max_iter=100):
    # Lista com o resumo de cada iteracao
    historico = [] 
    
    limite_inferior = a
    limite_superior = b
    tolerancia = tol
    max_iteracoes = max_iter
    
    # Valida mudanca de sinal no intervalo
    f_limite_inferior = funcao(limite_inferior)
    f_limite_superior = funcao(limite_superior)
    if f_limite_inferior * f_limite_superior >= 0:
        raise ValueError("O intervalo informado nao possui mudanca de sinal.")
    
    for iteracao in range(1, max_iteracoes + 1):
        # Ponto medio e avaliacao da funcao
        meio = (limite_inferior + limite_superior) / 2
        f_meio = funcao(meio)
        # Erro absoluto (metade do intervalo)
        erro = abs(limite_superior - limite_inferior) / 2
        
        # Guarda estado da iteracao
        historico.append({
            'iter': iteracao, 
            'a': limite_inferior, 
            'b': limite_superior, 
            'c': meio, 
            'f(c)': f_meio,
            'erro': erro
        })
        
        # Criterio de parada
        if f_meio == 0 or erro < tolerancia:
            return meio, iteracao, historico
            
        # Mantem o subintervalo com mudanca de sinal
        if utils.teorema_bolzano(funcao, limite_inferior, meio):
            limite_superior = meio
        else:
            limite_inferior = meio
            
    return meio, max_iteracoes, historico


if __name__ == "__main__":
    # Entrada interativa para testar manualmente
    a = float(input("Limite inferior a: ").strip())
    b = float(input("Limite superior b: ").strip())
    tol = float(input("Tolerancia (ex: 1e-6): ").strip())
    max_iter = int(input("Maximo de iteracoes: ").strip())

    try:
        raiz, iteracoes, historico = bisseccao(funcao, a, b, tol=tol, max_iter=max_iter)
    except ValueError as exc:
        print(str(exc))
    else:
        print("Raiz aproximada:", raiz)
        print("f(raiz):", funcao(raiz))
        print("Erro absoluto:", historico[-1]["erro"])
        print("Quantidade de iteracoes:", iteracoes)
