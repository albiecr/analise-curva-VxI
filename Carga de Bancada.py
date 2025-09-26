import matplotlib.pyplot as plt
import numpy as np

# Dados extraídos da tabela para a carga de bancada
tensao_v = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220])
corrente_a = np.array([0, 0.13, 0.27, 0.43, 0.58, 0.73, 0.9, 1, 1.15, 1.3, 1.45, 1.6])

# --- AJUSTES ---

# 1. Calcular a regressão linear (linha de tendência de grau 1)
# O '1' indica que queremos uma linha reta (y = mx + c), ideal para um resistor ôhmico.
m, c = np.polyfit(tensao_v, corrente_a, 1)

# A inclinação 'm' da reta I x V é o inverso da resistência (1/R)
# O valor da resistência pode ser calculado como R = 1/m
resistencia = 1 / m
print(f"A equação da reta de tendência é: I = {m:.4f} * V + {c:.4f}")
print(f"O valor da resistência calculado pela regressão é: {resistencia:.2f} Ohms")

# 2. Gerar os pontos da linha de tendência
corrente_tendencia = m * tensao_v + c

# --- GRÁFICO ---

# Criar o gráfico
plt.figure(figsize=(10, 6))

# 3. Plotar os dados originais como pontos de dispersão
plt.scatter(tensao_v, corrente_a, color='green', label='Dados Experimentais', zorder=5)

# 4. Plotar a linha de tendência reta
plt.plot(tensao_v, corrente_tendencia, color='red', linestyle='--', label='Linha de Tendência (Regressão Linear)')

# Adicionar títulos e rótulos (eixos corrigidos)
plt.title('Gráfico I x V - Carga de Bancada (Resistor Ôhmico)')
plt.xlabel('Tensão (V) em Volts')
plt.ylabel('Corrente (I) em Amperes')

# Adicionar grade, legenda e mostrar o gráfico
plt.grid(True)
plt.legend()

# Salvar o gráfico
plt.savefig('grafico_IxV_resistencia_bancada_ajustado.png')
plt.show()