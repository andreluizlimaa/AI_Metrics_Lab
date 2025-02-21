#%%
import os
import pandas as pd
from glob import glob

# Função para converter o arquivo .md para .csv
def converter_md_para_csv(caminho_arquivo_md, caminho_arquivo_csv):
    with open(caminho_arquivo_md, "r", encoding="utf-8") as f:
        conteudo = f.readlines()

    # Limpeza das linhas
    conteudo_limpo = [texto.replace(">", "").replace("#", "").strip() for texto in conteudo]
    
    # Excluindo a primeira linha da resposta (que é a pergunta)
    pergunta = "O que é " + conteudo_limpo[0].lower() + "?"  # A primeira linha (pergunta)
    resposta = "\n".join(conteudo_limpo[1:])  # As demais linhas são a resposta

    print(pergunta)
    
    # Criando o DataFrame
    df = pd.DataFrame({
        "Pergunta": [pergunta],  # A primeira linha (pergunta)
        "Resposta": [resposta]  # As linhas subsequentes (resposta)
    })

    # Salvando o DataFrame em um arquivo CSV
    df.to_csv(caminho_arquivo_csv, index=False, encoding="utf-8")
    print(f"Arquivo convertido: {caminho_arquivo_md} para {caminho_arquivo_csv}")

# Função principal que percorre a pasta e converte os arquivos .md
def processar_arquivos_md(diretorio_md, diretorio_csv):
    # Criar a pasta de destino se ela não existir
    if not os.path.exists(diretorio_csv):
        os.makedirs(diretorio_csv)

    # Encontrar todos os arquivos .md no diretório e subdiretórios
    arquivos_md = glob(os.path.join(diretorio_md, "*.md"))

    for arquivo_md in arquivos_md:
        # Nome do arquivo .csv que será gerado (o mesmo nome, mas com extensão .csv)
        nome_csv = os.path.splitext(os.path.basename(arquivo_md))[0] + ".csv"
        caminho_csv = os.path.join(diretorio_csv, nome_csv)

        # Converter o arquivo .md para .csv
        converter_md_para_csv(arquivo_md, caminho_csv)

# Exemplo de diretório onde os arquivos .md estão localizados
diretorio_md = "Data/Data_orivas_md"

# Exemplo de diretório onde os arquivos .csv serão salvos
diretorio_csv = "Data/Data_orivas_csv"

# Processando todos os arquivos .md dentro do diretório especificado
processar_arquivos_md(diretorio_md, diretorio_csv)

#%%
import os
import pandas as pd
from glob import glob

def juntar_csv(diretorio_juntar_csv):
    # Criar um DataFrame vazio para armazenar os dados concatenados
    df = pd.DataFrame()

    # Juntar todos os arquivos .csv em um único DataFrame
    for arquivo_csv in glob(os.path.join(diretorio_juntar_csv, "*.csv")):
        df_juntar = pd.read_csv(arquivo_csv)
        df = pd.concat([df, df_juntar], ignore_index=True)

    # Definir o caminho final do arquivo concatenado
    caminho_final_csv = os.path.join(diretorio_juntar_csv, "dados_concatenados.csv")

    # Salvando o DataFrame em um único arquivo CSV
    df.to_csv(caminho_final_csv, index=False, encoding="utf-8")
    print(f"Arquivos CSV foram concatenados e salvos em: {caminho_final_csv}")

# Função para juntar todos os arquivos .csv em um único arquivo
def processar_arquivos_csv(diretorio_csv, diretorio_juntar_csv):
    # Encontrar todos os arquivos .csv no diretório
    arquivos_csv = glob(os.path.join(diretorio_csv, "*.csv"))

    for arquivo_csv in arquivos_csv:
        # Nome do arquivo .csv que será gerado (o mesmo nome, mas com extensão .csv)
        nome_csv = os.path.basename(arquivo_csv)  # Mantém o mesmo nome
        caminho_csv = os.path.join(diretorio_juntar_csv, nome_csv)

        # Copiar o arquivo para o diretório de junção
        df = pd.read_csv(arquivo_csv)
        df.to_csv(caminho_csv, index=False, encoding="utf-8")

    # Agora que todos os arquivos foram copiados, chamamos a função para juntá-los
    juntar_csv(diretorio_juntar_csv)

# Exemplo de diretório onde os arquivos .csv estão localizados
diretorio_csv = "Data/Data_orivas_csv"

# Exemplo de diretório onde os arquivos .csv juntos serão salvos
diretorio_juntar_csv = "Data/Data_orivas_csv"

# Criar diretório de destino, se não existir
os.makedirs(diretorio_juntar_csv, exist_ok=True)

# Processando todos os arquivos .csv dentro do diretório especificado
processar_arquivos_csv(diretorio_csv, diretorio_juntar_csv)

#%%
import pandas as pd
# Carregar o arquivo CSV
df = pd.read_csv("Data/Data_orivas_csv/dados_concatenados.csv")
print(df)

#%%
import pandas as pd
df = pd.read_csv("Data\Data_augmentation\pares_qa4.csv")
duplicatas = df[df.duplicated(subset=["Pergunta"], keep="first")]
print(len(df["Pergunta"]))
print(len(duplicatas["Pergunta"]))
duplicatas_limpas = df.drop_duplicates(subset=["Pergunta"], keep="first")
print(len(duplicatas_limpas["Pergunta"]))

caminho_novo = "Data/Data_augmentation/pares_qa4_limpo.csv"

if len(duplicatas["Pergunta"]) > 0:
    df_limpo = duplicatas_limpas.to_csv({caminho_novo}, index=False)

#%%
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
df1 = process_csv_files("Data/Data_augmentation/pares_qa.csv")
df2 = process_csv_files("Data/Data_augmentation/pares_qa2_limpo.csv")
df3 = process_csv_files("Data/Data_augmentation/pares_qa3.csv")
df4 = process_csv_files("Data/Data_augmentation/pares_qa4.csv")

# Concatenando os DataFrames verticalmente
df_combined = pd.concat([df1, df2, df3, df4], ignore_index=True)
print("🗑️ Quantidade de linhas antes da limpeza:", len(df_combined), "\n")
# Contando duplicatas antes da limpeza
num_duplicatas = df_combined.duplicated(subset=["Pergunta"]).sum()
print("🧲 Quantidade de linhas duplicatas:", num_duplicatas)

# Removendo duplicatas
if num_duplicatas > 0:
    df_combined_limpo = df_combined.drop_duplicates(subset=["Pergunta"], keep="first")
    print("✅ Quantidade de linhas após remover duplicatas:", len(df_combined_limpo))
    # Salvando o resultado
    # df_combined_limpo.to_csv('avaliacoes_combinadas.csv', index=False)
else:
    print("Não há duplicatas.")
    df_combined_limpo = df_combined

# Imprimindo informações sobre o resultado
print("\nColunas presentes no arquivo:")
for col in df_combined_limpo.columns:
    print(f"- {col}")


