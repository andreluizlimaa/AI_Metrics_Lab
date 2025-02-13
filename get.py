import pandas as pd

def extrair_dados_transposto(caminho_arquivo_entrada, caminho_arquivo_saida):
    """
    Lê um arquivo de entrada, extrai as colunas 'Modelo' e 'Tempo (s)',
    transpõe os dados para que os modelos sejam colunas,
    e salva em um novo arquivo CSV.
    
    Parâmetros:
    caminho_arquivo_entrada (str): Caminho do arquivo de entrada
    caminho_arquivo_saida (str): Caminho onde o arquivo CSV será salvo
    """
    try:
        # Lê o arquivo de entrada
        df = pd.read_csv(caminho_arquivo_entrada)
        
        # Seleciona apenas as colunas desejadas
        df_selecionado = df[['Modelo', 'Tempo (s)']]
        
        # Cria um novo DataFrame com os modelos como colunas
        df_transposto = pd.DataFrame()
        df_transposto['Perguntas'] = pd.Series(range(1, 16))
        
        # Agrupa os tempos por modelo
        for modelo in df_selecionado['Modelo'].unique():
            tempos = df_selecionado[df_selecionado['Modelo'] == modelo]['Tempo (s)'].values
            df_transposto[modelo] = pd.Series(tempos)
    
        # Salva o DataFrame transposto em um novo arquivo CSV
        df_transposto.to_csv(caminho_arquivo_saida, index=False)
        
        print(f"Arquivo CSV gerado com sucesso em: {caminho_arquivo_saida}")
        
        # Mostra uma prévia dos dados
        print("\nPrévia dos dados:")
        print(df_transposto.head())
        
    except FileNotFoundError:
        print("Erro: Arquivo de entrada não encontrado.")
    except KeyError:
        print("Erro: Uma ou ambas as colunas 'Modelo' ou 'Tempo (s)' não foram encontradas.")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")

# Exemplo de uso
if __name__ == "__main__":
    arquivo_entrada = "avaliacoes_combinadas.csv"  # Substitua pelo nome do seu arquivo
    arquivo_saida = "dados_transposto.csv"
    
    extrair_dados_transposto(arquivo_entrada, arquivo_saida)


def temp_medio_modelo():
    # Ler o arquivo CSV
    df = pd.read_csv('avaliacoes_combinadas.csv')
    # Calcular o tempo médio por cada modelo
    tempo_medio_por_modelo = df.mean(numeric_only=True)




