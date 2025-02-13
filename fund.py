import pandas as pd

def process_csv_files(file_path):
    """
    Lê o arquivo CSV e realiza o processamento necessário.
    
    Args:
        file_path (str): Caminho para o arquivo CSV
    
    Returns:
        pandas.DataFrame: DataFrame processado
    """
    # Lê o arquivo CSV
    df = pd.read_csv(file_path)
    
    # Remove duplicatas se houver
    df = df.drop_duplicates()
    
    # Retorna o DataFrame processado
    return df

# Lendo os arquivos
df1 = process_csv_files('Avaliacao-modelos-4.csv')
df2 = process_csv_files('Avaliacao-modelos-5.csv')

# Concatenando os DataFrames verticalmente (um embaixo do outro)
df_combined = pd.concat([df1, df2], ignore_index=True)

# Salvando o resultado
df_combined.to_csv('avaliacoes_combinadas.csv', index=False)

# Imprimindo informações sobre o resultado
print(f"Número de linhas no arquivo combinado: {len(df_combined)}")
print("\nColunas presentes no arquivo:")
for col in df_combined.columns:
    print(f"- {col}")

