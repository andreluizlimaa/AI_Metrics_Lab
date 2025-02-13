import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV
df = pd.read_csv('dados_transposto.csv')

# Remover a coluna 'Perguntas'
df = df.drop('Perguntas', axis=1)

# Calcular a média de cada coluna
avg_df = df.mean()

# Criar um novo DataFrame com a média
def_trans_avg = pd.DataFrame(avg_df).T

# Adicionar a coluna 'Perguntas' com o valor '15'
def_trans_avg['Perguntas'] = "15"

# Definir a coluna 'Perguntas' como índice
def_trans_avg = def_trans_avg.set_index('Perguntas')

# Salvar o DataFrame ajustado em um novo CSV
def_trans_avg.to_csv('Avg_temp_mod.csv')

# Carregar o CSV gerado
df = pd.read_csv('Avg_temp_mod.csv')
df = df.drop('Perguntas', axis=1)

# Reorganizar o DataFrame para formato longo (melt)
df_melted = df.melt(var_name='Modelos', value_name='Tempo')

# Criar o gráfico
plt.figure(figsize=(8, 5))

# Plotar usando Seaborn
sns.barplot(y='Tempo', hue = "Modelos",data=df_melted, palette='Set1', ci=None, width=0.6)

# Configurações do gráfico
plt.xlabel("15", fontsize=12)  # Aqui você deve mudar "Perguntas" para "Modelos"
plt.ylabel("Tempo (s)", fontsize=12)
plt.title("Comparação do Tempo Médio de Resposta dos Modelos", fontsize=14, fontweight="bold")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Definir a legenda manualmente, associando o título "Modelos" e os dados
plt.legend(title="Modelos", labels=df_melted['Modelos'].unique(), bbox_to_anchor=(1.05, 1), loc="upper left")

# Ajustar o layout para evitar cortes
plt.tight_layout()

# Mostrar o gráfico
plt.show()
