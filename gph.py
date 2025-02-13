import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ler o arquivo Excel
df = pd.read_csv('dados_transposto.csv')

# Converter todas as colunas numéricas para float, exceto 'Perguntas'
numeric_columns = df.columns.drop('Perguntas')
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

#Transformar 'Perguntas' em coluna
df_melted = df.melt(id_vars='Perguntas', var_name='Modelos', value_name='Tempo')

# Criar a figura e os eixos
plt.figure(figsize=(20, 10))

# Plotar usando Seaborn
sns.barplot(x='Perguntas', y='Tempo', hue='Modelos', data=df_melted, palette='Set3')

# Configurações do gráfico
plt.xlabel("Perguntas", fontsize=12)
plt.ylabel("Tempo (s)", fontsize=12)
plt.title("Tempo de Resposta dos Modelos por Pergunta", fontsize=14, fontweight="bold")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=1)
plt.legend(title="Modelos", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()
plt.show()