import math
import utils


# Metodo da Bissecao (com historico de iteracoes)

def funcao_por_expressao(expressao):
    # Cria funcao f(x) a partir de uma expressao com x e funcoes de math
    permitidos = {
        'x': 0.0,
        'e': math.e,
        'pi': math.pi,
        'sqrt': math.sqrt,
        'exp': math.exp,
        'log': math.log,
        'log10': math.log10,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'abs': abs,
    }

    def f(x):
        escopo = dict(permitidos)
        escopo['x'] = x
        return eval(expressao, {'__builtins__': {}}, escopo)

    return f

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
        return None, 0, historico
    
    for iteracao in range(max_iteracoes):
        # Ponto medio e avaliacao da funcao
        meio = (limite_inferior + limite_superior) / 2
        f_meio = funcao(meio)
        meio_anterior = historico[-1]['c'] if historico else None

        # Erro absoluto (intervalo ou diferenca entre pontos medios)
        if meio_anterior is None:
            erro = abs(limite_superior - limite_inferior)
        else:
            erro = abs(meio - meio_anterior)
        
        # Guarda estado da iteracao
        historico.append({
            'iter': iteracao + 1, 
            'a': limite_inferior, 
            'b': limite_superior, 
            'c': meio, 
            'f(c)': f_meio,
            'erro': erro
        })
        
        # Criterio de parada
        if f_meio == 0 or erro < tolerancia:
            return meio, iteracao + 1, historico
            
        # Mantem o subintervalo com mudanca de sinal
        if utils.teorema_bolzano(funcao, limite_inferior, meio):
            limite_superior = meio
        else:
            limite_inferior = meio
            
    return meio, max_iteracoes, historico


if __name__ == "__main__":
    # Entrada interativa para testar manualmente
    expressao = input("Funcao em x (ex: exp(x) - x**2 - 3*x): ").strip()
    a = float(input("Limite inferior a: ").strip())
    b = float(input("Limite superior b: ").strip())
    tol = float(input("Tolerancia (ex: 1e-6): ").strip())
    max_iter = int(input("Maximo de iteracoes: ").strip())

    funcao = funcao_por_expressao(expressao)
    raiz, iteracoes, historico = bisseccao(funcao, a, b, tol=tol, max_iter=max_iter)

    print("raiz:", raiz)
    print("f(raiz):", funcao(raiz) if raiz is not None else None)
    print("erro final:", historico[-1]["erro"] if historico else None)
    print("iteracoes:", iteracoes)
