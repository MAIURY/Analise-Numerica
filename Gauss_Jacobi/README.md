# Metodo de Gauss-Jacobi

## Objetivo
Implementar o metodo iterativo de Gauss-Jacobi para resolver aproximadamente um sistema linear, usando erro relativo como criterio de parada.

## Sistema do problema
```text
-4x1 + 2x2 - x3 = 1
-4x1 + 6x2 - x3 = 2
 x1 + 6x2 - 6x3 = 3
```

## Parametros
- Chute inicial: $x_0 = (2, 1, 1)$
- Tolerancia: $Er = 0,00001$
- Maximo de iteracoes: 100

## Formula do metodo
$$
x_i^{(k+1)} = \frac{b_i - \sum_{j \ne i} a_{ij} x_j^{(k)}}{a_{ii}}
$$

## Criterio de parada
O algoritmo encerra quando $\text{erro relativo} < 0,00001$.

## O que a implementacao registra
- Valores aproximados de $x_1$, $x_2$, $x_3$ por iteracao
- Erro absoluto e relativo por iteracao
- Numero total de iteracoes

## Observacao sobre convergencia
A convergencia costuma ser favorecida quando a matriz de coeficientes e diagonalmente dominante.
