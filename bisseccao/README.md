# Método da Bisseção

## Descrição do trabalho

Este trabalho tem como objetivo desenvolver a implementação do cálculo numérico utilizando o **Método da Bisseção**.

O método será aplicado para encontrar uma raiz aproximada da função:

\[
f(x) = e^x - x^2 - 3x
\]

no intervalo:

\[
[-4, -3]
\]

A implementação deve utilizar o **erro absoluto** como critério de parada e também deve guardar a **quantidade de iterações** realizadas até encontrar a solução aproximada.

---

## Função utilizada

A função escolhida para o problema é:

```text
f(x) = e^x - x^2 - 3x
```

Onde:

- `e^x` representa o número de Euler elevado a `x`.
- `x^2` representa `x` ao quadrado.
- `-3x` representa o termo linear da função.

---

## Intervalo inicial

O intervalo informado para aplicação do método é:

```text
a = -4
b = -3
```

Antes de aplicar o método da bisseção, é necessário verificar se existe mudança de sinal no intervalo, ou seja:

```text
f(a) * f(b) < 0
```

Caso essa condição seja verdadeira, existe pelo menos uma raiz no intervalo informado.

---

## Método da Bisseção

O Método da Bisseção consiste em dividir o intervalo ao meio repetidamente, aproximando-se da raiz da função.

A cada iteração, calcula-se o ponto médio:

```text
m = (a + b) / 2
```

Depois, verifica-se em qual metade do intervalo está a raiz, analisando o sinal da função.

---

## Critério de parada

O critério de parada utilizado será o **erro absoluto**.

No método da bisseção, uma definição comum para o erro absoluto é:

```text
erro = |b - a| / 2
```

O processo continua até que o erro seja menor que a tolerância definida.

Exemplo:

```text
erro < tolerancia
```

---

## Dados do problema

```text
Função: f(x) = e^x - x^2 - 3x
Intervalo: [-4, -3]
Método: Bisseção
Critério de parada: Erro absoluto
Informação armazenada: Quantidade de iterações
```

---

## Como executar

No terminal, execute:

```bash
python bisseccao.py
```

Depois informe os dados:

```text
Limite inferior a: -4
Limite superior b: -3
Tolerância (ex: 1e-6): 1e-6
Máximo de iterações: 100
```

---

## Resultado esperado

Ao final da execução, o programa deve apresentar:

- A raiz aproximada da função.
- O valor de `f(x)` na raiz aproximada.
- O erro absoluto final.
- A quantidade de iterações realizadas.

Exemplo de saída esperada:

```text
Raiz aproximada: -3.016240119934082
f(raiz): 0.000000949
Erro absoluto: 0.000000953
Quantidade de iterações: 20
```

---

## Objetivo da implementação

O objetivo principal é compreender e aplicar o Método da Bisseção para resolver equações não lineares, utilizando uma função matemática específica e controlando o processo por meio do erro absoluto.

Ademais, a implementação deve permitir acompanhar a quantidade de iterações necessárias para que o método encontre uma aproximação aceitável da raiz.

---

## Conclusão

O Método da Bisseção é um método numérico simples e eficiente para encontrar raízes de funções contínuas em intervalos onde há mudança de sinal.

Neste trabalho, ele será utilizado para resolver a equação:

\[
e^x - x^2 - 3x = 0
\]

no intervalo `[-4, -3]`, utilizando erro absoluto como critério de parada e registrando o número de iterações realizadas.