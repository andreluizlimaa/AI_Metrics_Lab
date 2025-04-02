import os

# Diretório onde os arquivos .txt estão localizados
diretorio = "./txts"

# Criar diretório de saída se não existir
saida = "./txts_limpos"
os.makedirs(saida, exist_ok=True) # cria pasta caso n exista

# Lista todos os arquivos do diretório
arquivos = os.listdir(diretorio)

# Itera sobre cada arquivo
for arquivo in arquivos:
    if arquivo.endswith(".txt"):  # Verifica se é um arquivo .txt
        caminho_arquivo = os.path.join(diretorio, arquivo) #indica o caminho do arquivo
        
        # Abre o arquivo e lê o conteúdo
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            text = f.read()

        # Limpa o texto
        text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        text = " ".join(text.split())  # Remove espaços extras

        # Caminho do novo arquivo
        caminho_saida = os.path.join(saida, arquivo)

        # Salva o conteúdo limpo em um novo arquivo
        with open(caminho_saida, "w", encoding="utf-8") as f:
            f.write(text)

print("Processo concluído! Arquivos salvos em:", saida)
