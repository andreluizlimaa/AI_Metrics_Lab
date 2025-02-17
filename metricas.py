#%%
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_model_metrics(csv_path):
    # Read and process the data
    df = pd.read_csv(csv_path)
    
    # Filter model columns
    model_columns = [col for col in df.columns if 'Idioma' not in col and 'Perguntas' not in col]
    
    # Calculate accuracy for each model
    accuracy = df[model_columns].mean() * 100
    
    # Dictionary with model parameters (em bilhões)
    model_params = {
        'deepseek-r1:1.5b': 1.5,
        'deepseek-r1:7b': 7.0,
        'deepseek-r1:8b': 8.0,
        'deepseek-r1:14b': 14.0,
        'mistral-nemo:12b': 1.5,
        'mistral:7b': 7.0,
        'phi3:3.8b': 3.8,
        'phi3:3.14b': 14.0,
        'gemma2:2b':2.0,
        'gemma2:9b':9.0,
    }
    
    # Criar DataFrame com acurácia e parâmetros
    metrics_df = pd.DataFrame({
        'Modelo': accuracy.index,
        'Acurácia': accuracy.values,
        'Parâmetros': [model_params.get(model, np.nan) for model in accuracy.index]
    })
    
    # Remover linhas com valores NaN
    valid_metrics = metrics_df.dropna(subset=['Parâmetros'])
    
    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 7))
    
    # Gráfico 1: Barras de Acurácia
    barplot = sns.barplot(data=metrics_df, x='Modelo', y='Acurácia', ax=ax1, palette='Set3')
    ax1.set_title("Acurácia por Modelo", pad=20, fontsize=14)
    ax1.set_ylabel("Acurácia (%)", fontsize=12)
    ax1.set_xlabel("Modelo", fontsize=12)
    plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')
    
    # Adicionar valores nas barras
    for i, v in enumerate(metrics_df['Acurácia']):
        ax1.text(i, v + 1, f'{v:.1f}%', ha='center', va='bottom')
    
    # Gráfico 2: Dispersão Acurácia vs Parâmetros com cores diferentes
    colors = plt.cm.Set3(np.linspace(0, 1, len(valid_metrics)))
    
    # Plotar apenas pontos válidos
    for i, (idx, row) in enumerate(valid_metrics.iterrows()):
        ax2.scatter(row['Parâmetros'], row['Acurácia'], 
                   color=colors[i], s=100, label=row['Modelo'])
        
        # # Adicionar labels com offset alternado
        # offset_y = 2 if i % 2 == 0 else -2
        # ax2.annotate(row['Modelo'],
        #             (row['Parâmetros'], row['Acurácia']),
        #             xytext=(5, offset_y),
        #             textcoords='offset points',
        #             fontsize=10)
    
    # Adicionar linha de tendência
    if len(valid_metrics) > 1:
        z = np.polyfit(valid_metrics['Parâmetros'], valid_metrics['Acurácia'], 1)
        p = np.poly1d(z)
        x_range = np.linspace(valid_metrics['Parâmetros'].min(), 
                            valid_metrics['Parâmetros'].max(), 100)
        ax2.plot(x_range, p(x_range), "r--", alpha=0.8, label='Linha de Tendência')
    
    ax2.set_title("Acurácia vs Número de Parâmetros", pad=20, fontsize=14)
    ax2.set_xlabel("Número de Parâmetros (bilhões)", fontsize=12)
    ax2.set_ylabel("Acurácia (%)", fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Ajustar layout
    plt.tight_layout()
    
    # Calcular estatísticas
    stats_summary = {
        'acuracia_media': accuracy.mean(),
        'desvio_padrao': accuracy.std(),
        'melhor_modelo': accuracy.idxmax(),
        'melhor_acuracia': accuracy.max(),
        'pior_modelo': accuracy.idxmin(),
        'pior_acuracia': accuracy.min()
    }
    
    # Adicionar correlação apenas se houver dados suficientes
    if len(valid_metrics) > 1:
        stats_summary['correlacao_params_acuracia'] = valid_metrics['Acurácia'].corr(valid_metrics['Parâmetros'])
    
    return metrics_df, stats_summary

# Exemplo de uso
if __name__ == "__main__":
    metrics, stats = analyze_model_metrics('Verificação_da_acertividade_dos_modelos.csv')
    plt.show()
    
    print("\nEstatísticas Resumidas:")
    print(f"Acurácia Média: {stats['acuracia_media']:.2f}%")
    print(f"Desvio Padrão: {stats['desvio_padrao']:.2f}%")
    print(f"Melhor Modelo: {stats['melhor_modelo']} ({stats['melhor_acuracia']:.2f}%)")
    print(f"Pior Modelo: {stats['pior_modelo']} ({stats['pior_acuracia']:.2f}%)")
    if 'correlacao_params_acuracia' in stats:
        print(f"Correlação entre Parâmetros e Acurácia: {stats['correlacao_params_acuracia']:.3f}")


