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

    # n corresponde ao número de equações (e de incógnitas)
    n = len(b)

    # Usa x0 se fornecido; caso contrário, inicia com zeros
    x = x0[:] if x0 else [0.0] * n

    # Vetor que recebe os valores calculados a cada iteração
    x_new = [0.0] * n

    # Lista para registrar o histórico das iterações
    iteracoes = []

    # Laço principal do método, limitado por max_iter
    for k in range(max_iter):

        # Calcula a nova aproximação para cada equação do sistema
        for i in range(n):

            # Soma dos termos A[i][j] * x[j], excluindo a diagonal A[i][i] * x[i]
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)

            # Fórmula do Gauss-Jacobi
            x_new[i] = (b[i] - soma) / A[i][i]

        # Erro absoluto: maior diferenca entre os vetores atual e anterior
        erro_abs = max(abs(x_new[i] - x[i]) for i in range(n))

        # Maior valor absoluto em x_new, usado no calculo do erro relativo
        max_x = max(abs(v) for v in x_new)

        # Erro relativo; usa erro absoluto quando max_x == 0
        erro_rel = erro_abs / max_x if max_x != 0 else erro_abs

        # Registra os dados da iteracao atual
        iteracoes.append({
            'iter': k + 1,           # número da iteração
            'x': x_new[:],           # cópia dos valores atuais de x
            'erro_abs': erro_abs,    # erro absoluto calculado
            'erro_rel': erro_rel     # erro relativo calculado
        })

        # Criterio de parada: erro relativo ou absoluto abaixo da tolerancia
        if erro_rel < tol or erro_abs < tol:
            return x_new, k + 1, iteracoes

        # Atualiza x para a proxima iteracao
        x = x_new[:]

    # Se nao convergir dentro do limite, retorna a ultima aproximacao
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
# A matriz A contem os coeficientes das incognitas x1, x2 e x3

A = [
    [-4, 2, -1],   # coeficientes da primeira equacao
    [-4, 6, -1],   # coeficientes da segunda equacao
    [1, 6, -6]     # coeficientes da terceira equacao
]

# Vetor b contem os termos independentes do sistema
b = [1, 2, 3]

# Aproximacao inicial informada na questao:
# x0 = (2, 1, 1)
x0 = [2, 1, 1]

# Tolerancia do erro relativo:
# Er = 0,00001
tol = 0.00001

# Numero maximo de iteracoes permitido
max_iter = 100


# ---------------------------------------------------------
# Execucao do metodo de Gauss-Jacobi
# ---------------------------------------------------------

# Chama gauss_jacobi com A, b, tolerancia, max_iter e aproximacao inicial
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

# Percorre o historico e imprime os valores de cada iteracao
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