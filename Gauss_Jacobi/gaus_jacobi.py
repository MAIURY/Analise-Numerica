def gauss_jacobi(A, b, tol=1e-5, max_iter=100, x0=None):
    """
    Resolve o sistema linear Ax = b pelo método iterativo de Gauss-Jacobi.

    Parâmetros:
    A        -> matriz de coeficientes do sistema
    b        -> vetor de termos independentes
    tol      -> tolerância do erro (critério de parada)
    max_iter -> número máximo de iterações
    x0       -> aproximação inicial das incógnitas

    Retorna:
    x_new     -> solução aproximada
    k + 1     -> número de iterações executadas
    iteracoes -> histórico das iterações
    """

    # Preparacao dos vetores e estrutura de historico.
    n = len(b)
    x = x0[:] if x0 else [0.0] * n
    x_new = [0.0] * n
    iteracoes = []

    for k in range(max_iter):
        # Calcula a nova aproximacao para cada equacao do sistema.
        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - soma) / A[i][i]

        # Calcula erros absoluto e relativo.
        erro_abs = max(abs(x_new[i] - x[i]) for i in range(n))
        max_x = max(abs(v) for v in x_new)
        erro_rel = erro_abs / max_x if max_x != 0 else erro_abs

        # Registra os dados da iteracao atual.
        iteracoes.append(
            {
                'iter': k + 1,
                'x': x_new[:],
                'erro_abs': erro_abs,
                'erro_rel': erro_rel,
            }
        )

        # Criterio de parada: erro relativo ou absoluto abaixo da tolerancia.
        if erro_rel < tol or erro_abs < tol:
            return x_new, k + 1, iteracoes

        # Atualiza x para a proxima iteracao.
        x = x_new[:]

    # Se nao convergir dentro do limite, retorna a ultima aproximacao.
    return x_new, max_iter, iteracoes


# ---------------------------------------------------------
# Definicao do sistema linear
# ---------------------------------------------------------
# Sistema de referencia:
#
# -4x1 + 2x2 - x3 = 1
# -4x1 + 6x2 - x3 = 2
#  x1 + 6x2 - 6x3 = 3
#
# A matriz A contem os coeficientes das incognitas x1, x2 e x3.
A = [
    [-4, 2, -1],
    [-4, 6, -1],
    [1, 6, -6],
]

# Vetor b contem os termos independentes do sistema.
b = [1, 2, 3]

# Aproximacao inicial informada na questao: x0 = (2, 1, 1)
x0 = [2, 1, 1]

# Tolerancia do erro relativo: Er = 0,00001
tol = 0.00001

# Numero maximo de iteracoes permitido.
max_iter = 100


# ---------------------------------------------------------
# Execucao do metodo de Gauss-Jacobi
# ---------------------------------------------------------

# Chama gauss_jacobi com A, b, tolerancia, max_iter e aproximacao inicial.
solucao, num_iter, iteracoes = gauss_jacobi(
    A,
    b,
    tol=tol,
    max_iter=max_iter,
    x0=x0
)


# ---------------------------------------------------------
# Impressao das iteracoes
# ---------------------------------------------------------

print("Iterações do método de Gauss-Jacobi:\n")

# Percorre o historico e imprime os valores de cada iteracao.
for item in iteracoes:
    x = item['x']

    print(
        f"Iteração {item['iter']}: "
        f"x1 = {x[0]:.6f}, "
        f"x2 = {x[1]:.6f}, "
        f"x3 = {x[2]:.6f}, "
        f"Erro Absoluto = {item['erro_abs']:.8f}, "
        f"Erro Relativo = {item['erro_rel']:.8f}"
    )


# ---------------------------------------------------------
# Impressao do resultado final
# ---------------------------------------------------------

print("\nResultado final:")
print(f"x1 = {solucao[0]:.6f}")
print(f"x2 = {solucao[1]:.6f}")
print(f"x3 = {solucao[2]:.6f}")
print(f"Número de iterações = {num_iter}")