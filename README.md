# Análise da Curva Tensão vs. Corrente (V x I)

Este repositório contém scripts em Python para a análise e visualização da curva característica Tensão vs. Corrente (V x I) de dois componentes elétricos distintos: uma carga de bancada (resistor ôhmico) e uma lâmpada incandescente (resistor não ôhmico).

O objetivo é demonstrar experimentalmente a validade da Lei de Ohm e as diferenças de comportamento entre esses dois tipos de cargas.

## Fundamentos Teóricos

A relação entre Tensão (V), Corrente (I) e Resistência (R) em um componente elétrico é um dos conceitos fundamentais da eletricidade.

### 1. Resistores Ôhmicos e a Lei de Ohm

Um **resistor ôhmico** é um componente que obedece à Lei de Ohm. A lei afirma que, para um condutor mantido a uma temperatura constante, a corrente elétrica é diretamente proporcional à tensão aplicada.

A fórmula matemática é:
$$V = R \cdot I$$
Onde:
- **V**: Tensão (em Volts)
- **I**: Corrente (em Amperes)
- **R**: Resistência (em Ohms), que é a **constante de proporcionalidade**.

A principal característica de um resistor ôhmico é que sua **resistência (R) é constante**. Graficamente, a curva I vs. V de um resistor ôhmico é uma **linha reta** que passa pela origem. A inclinação (`m`) dessa reta está relacionada à resistência (R = 1/m). A "Carga de Bancada" analisada neste projeto se comporta como um resistor ôhmico.

### 2. Resistores Não Ôhmicos

Um **resistor não ôhmico** é um componente cuja resistência **varia** com a mudança de condições, como temperatura ou tensão. Portanto, ele não obedece à Lei de Ohm de forma linear.

O exemplo clássico é a **lâmpada incandescente**. Seu filamento de tungstênio, quando frio, possui uma resistência baixa. Ao ser percorrido por uma corrente, ele se aquece a milhares de graus Celsius, e sua resistência aumenta drasticamente.

Graficamente, a curva I vs. V de um resistor não ôhmico **não é uma linha reta**, mas sim uma curva, indicando que a relação V/I (a resistência) não é constante.

## Códigos Utilizados

Os scripts abaixo utilizam as bibliotecas `matplotlib` para visualização e `numpy` para realizar o ajuste de curva (regressão linear ou polinomial), gerando gráficos que representam o comportamento dos componentes.

### 1. Código para a Carga de Bancada (Resistor Ôhmico)

Este script plota os dados experimentais e realiza uma **regressão linear** (ajuste de uma linha reta) para demonstrar o comportamento ôhmico e calcular o valor da resistência.

```python
import matplotlib.pyplot as plt
import numpy as np

# Dados da tabela "Carga de Bancada"
tensao_v = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220])
corrente_a = np.array([0, 0.13, 0.27, 0.43, 0.58, 0.73, 0.9, 1, 1.15, 1.3, 1.45, 1.6])

# Calcular a regressão linear (linha de tendência de grau 1)
m, c = np.polyfit(tensao_v, corrente_a, 1)

# O valor da resistência pode ser calculado como R = 1/m
resistencia = 1 / m
print(f"O valor da resistência calculado pela regressão é: {resistencia:.2f} Ohms")

# Gerar os pontos da linha de tendência
corrente_tendencia = m * tensao_v + c

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.scatter(tensao_v, corrente_a, color='green', label='Dados Experimentais', zorder=5)
plt.plot(tensao_v, corrente_tendencia, color='red', linestyle='--', label='Linha de Tendência (Regressão Linear)')

# Adicionar títulos e rótulos
plt.title('Gráfico I x V - Carga de Bancada (Resistor Ôhmico)')
plt.xlabel('Tensão (V) em Volts')
plt.ylabel('Corrente (I) em Amperes')
plt.grid(True)
plt.legend()

# Salvar e mostrar o gráfico
plt.savefig('grafico_IxV_resistencia_bancada_ajustado.png')
plt.show()
```

### 2. Código para a Lâmpada Incandescente (Resistor Não Ôhmico)

Este script plota os dados da lâmpada e realiza um **ajuste de curva polinomial** (grau 2) para modelar o comportamento não linear, evidenciando a variação da resistência com a temperatura.

```python
import matplotlib.pyplot as plt
import numpy as np

# Dados da tabela da Lâmpada Incandescente
tensao_v = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220])
corrente_a = np.array([0, 0.18, 0.26, 0.33, 0.39, 0.45, 0.51, 0.55, 0.59, 0.63, 0.67, 0.71])

# Calcular a curva de tendência (polinômio de grau 2 para um ajuste não linear)
coeficientes = np.polyfit(tensao_v, corrente_a, 2)
polinomio = np.poly1d(coeficientes)

# Gerar pontos para uma linha suave e contínua
tensao_suave = np.linspace(tensao_v.min(), tensao_v.max(), 300)
corrente_suave = polinomio(tensao_suave)

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.scatter(tensao_v, corrente_a, color='blue', label='Dados Experimentais', zorder=5)
plt.plot(tensao_suave, corrente_suave, color='red', linestyle='--', label='Curva de Tendência (Não Linear)')

# Adicionar títulos e rótulos
plt.title('Gráfico I x V - Lâmpada Incandescente (Não Ôhmico)')
plt.xlabel('Tensão (V) em Volts')
plt.ylabel('Corrente (I) em Amperes')
plt.grid(True)
plt.legend()

# Salvar e mostrar o gráfico
plt.savefig('grafico_IxV_Lampada_Ajustado.png')
plt.show()
```

## Como Executar os Scripts

### Pré-requisitos
Antes de executar, você precisa ter o Python e as bibliotecas `matplotlib` e `numpy` instaladas. Se não as tiver, instale-as usando o pip:

```bash
pip install matplotlib numpy
```

### Execução
Salve cada um dos códigos acima em arquivos separados (ex: `analise_bancada.py` e `analise_lampada.py`) e execute-os através do terminal:

```bash
python analise_bancada.py
python analise_lampada.py
```
Ao executar cada script, o gráfico correspondente será exibido na tela e também salvo como um arquivo de imagem (`.png`) no mesmo diretório.
