import matplotlib.pyplot as plt
import numpy as np

# Dados extraídos da tabela
tensao_v = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220])
corrente_a = np.array([0, 0.18, 0.26, 0.33, 0.39, 0.45, 0.51, 0.55, 0.59, 0.63, 0.67, 0.71])

# --- AJUSTES ---

# 1. Calcular a curva de tendência (polinômio de grau 2 para um ajuste não linear)
# O '2' significa que queremos uma curva do tipo y = ax^2 + bx + c
coeficientes = np.polyfit(tensao_v, corrente_a, 2)
polinomio = np.poly1d(coeficientes)

# 2. Gerar pontos para uma linha suave e contínua
# Criamos mais pontos de tensão para que a curva desenhada seja bem suave
tensao_suave = np.linspace(tensao_v.min(), tensao_v.max(), 300)
corrente_suave = polinomio(tensao_suave)

# --- GRÁFICO ---

# Criar o gráfico
plt.figure(figsize=(10, 6))

# 3. Plotar os dados originais como pontos de dispersão (scatter plot)
plt.scatter(tensao_v, corrente_a, color='blue', label='Dados Experimentais', zorder=5)

# 4. Plotar a curva de tendência suave
plt.plot(tensao_suave, corrente_suave, color='red', linestyle='--', label='Curva de Tendência (Não Linear)')

# Adicionar títulos e rótulos 
plt.title('Gráfico I x V - Lâmpada Incandescente (Não Ôhmico)')
plt.xlabel('Tensão (V) em Volts') 
plt.ylabel('Corrente (I) em Amperes') 

# Adicionar grade para melhor visualização
plt.grid(True)
plt.legend() # Adiciona a legenda para identificar os pontos e a curva

# Salvar e mostrar o gráfico
plt.savefig('grafico_IxV_Lampada_Ajustado.png')
plt.show()