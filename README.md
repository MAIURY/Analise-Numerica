# Metodo da Bissecao

## Descricao do trabalho

Este trabalho tem como objetivo desenvolver a implementacao do calculo numerico utilizando o **Metodo da Bissecao**.

O metodo sera aplicado para encontrar uma raiz aproximada da funcao:

\[
f(x) = e^x - x^2 - 3x
\]

no intervalo:

\[
[-4, -3]
\]

A implementacao deve utilizar o **erro absoluto** como criterio de parada e tambem deve guardar a **quantidade de iteracoes** realizadas ate encontrar a solucao aproximada.

---

## Funcao utilizada

A funcao escolhida para o problema e:

```text
f(x) = e^x - x^2 - 3x
```

Onde:

- `e^x` representa o numero de Euler elevado a `x`.
- `x^2` representa `x` ao quadrado.
- `-3x` representa o termo linear da funcao.

---

## Intervalo inicial

O intervalo informado para aplicacao do metodo e:

```text
a = -4
b = -3
```

Antes de aplicar o metodo da bissecao, e necessario verificar se existe mudanca de sinal no intervalo, ou seja:

```text
f(a) * f(b) < 0
```

Caso essa condicao seja verdadeira, existe pelo menos uma raiz no intervalo informado.

---

## Metodo da Bissecao

O Metodo da Bissecao consiste em dividir o intervalo ao meio repetidamente, aproximando-se da raiz da funcao.

A cada iteracao, calcula-se o ponto medio:

```text
m = (a + b) / 2
```

Depois, verifica-se em qual metade do intervalo esta a raiz, analisando o sinal da funcao.

---

## Criterio de parada

O criterio de parada utilizado sera o **erro absoluto**.

O erro absoluto pode ser calculado por:

```text
erro = |b - a|
```

ou pela diferenca entre dois pontos medios consecutivos:

```text
erro = |m_atual - m_anterior|
```

O processo continua ate que o erro seja menor que a tolerancia definida.

Exemplo:

```text
erro < tolerancia
```

---

## Dados do problema

```text
Funcao: f(x) = e^x - x^2 - 3x
Intervalo: [-4, -3]
Metodo: Bissecao
Criterio de parada: Erro absoluto
Informacao armazenada: Quantidade de iteracoes
```

---

## Resultado esperado

Ao final da execucao, o programa deve apresentar:

- A raiz aproximada da funcao.
- O valor de `f(x)` na raiz aproximada.
- O erro absoluto final.
- A quantidade de iteracoes realizadas.

Exemplo de saida esperada:

```text
Raiz aproximada: -3.05
f(raiz): valor proximo de zero
Erro absoluto: valor menor que a tolerancia
Quantidade de iteracoes: numero total de repeticoes
```

---

## Objetivo da implementacao

O objetivo principal e compreender e aplicar o Metodo da Bissecao para resolver equacoes nao lineares, utilizando uma funcao matematica especifica e controlando o processo por meio do erro absoluto.

Ademais, a implementacao deve permitir acompanhar a quantidade de iteracoes necessarias para que o metodo encontre uma aproximacao aceitavel da raiz.

---

## Conclusao

O Metodo da Bissecao e um metodo numerico simples e eficiente para encontrar raizes de funcoes continuas em intervalos onde ha mudanca de sinal.

Neste trabalho, ele sera utilizado para resolver a equacao:

\[
e^x - x^2 - 3x = 0
\]

no intervalo `[-4, -3]`, utilizando erro absoluto como criterio de parada e registrando o numero de iteracoes realizadas.