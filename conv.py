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
df = pd.read_csv("Data/Data_aumentation/perguntas_respostas_javascript.csv")
duplicatas = df[df.duplicated(subset=["Pergunta"], keep="first")]
print(len(df["Pergunta"]))
print(len(duplicatas["Pergunta"]))
duplicatas_limpas = df.drop_duplicates(subset=["Pergunta"], keep="first")
print(len(duplicatas_limpas["Pergunta"]))

df_limpo = duplicatas_limpas.to_csv("Data/Data_aumentation/data_aumentation_limpo.csv", index=False)

#%%
df = pd.read_csv("Data/Data_aumentation/data_aumentation_limpo.csv")
print(len(df["Pergunta"]))
print(len(df[df.duplicated(subset=["Pergunta"], keep="first")]))
