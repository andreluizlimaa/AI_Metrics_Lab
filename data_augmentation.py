import pandas as pd
import random
import ollama  # Importando a biblioteca Ollama diretamente
from tqdm import tqdm

# Função para gerar novos pares de pergunta e resposta usando Ollama (Mistral-Nemo 12B)
def augment_data(question, answer, num_samples=5000):
    augmented_pairs = []

    while len(augmented_pairs) < num_samples:
        # Crie uma solicitação para o modelo Ollama (Mistral-Nemo 12B)
        prompt = f"Baseado na pergunta: '{question}' e resposta: '{answer}', crie uma variação."

        try:
            # Usando a função de chat da biblioteca Ollama para obter a resposta
            response = ollama.chat(model="mistral-nemo:12b", messages=[{"role": "user", "content": prompt}])

            # A resposta gerada
            augmented_answer = response["message"]["content"]

            if augmented_answer:
                augmented_pairs.append((question, augmented_answer))

        except Exception as e:
            print(f"Erro ao gerar resposta para a pergunta: '{question}'. Erro: {e}")
            # Opcional: Você pode decidir continuar mesmo em caso de erro e adicionar a resposta como vazia
            augmented_pairs.append((question, "Erro ao gerar resposta"))

    return augmented_pairs

# Carregar o CSV
try:
    df = pd.read_csv('Data/Data_orivas_csv/dados_concatenados.csv')
except FileNotFoundError as e:
    print(f"Erro: O arquivo CSV não foi encontrado. Verifique o caminho. Erro: {e}")
    exit()  # Encerra a execução caso o arquivo não seja encontrado
except pd.errors.EmptyDataError as e:
    print(f"Erro: O arquivo CSV está vazio. Erro: {e}")
    exit()  # Encerra a execução caso o arquivo esteja vazio
except Exception as e:
    print(f"Erro ao carregar o arquivo CSV. Erro: {e}")
    exit()  # Encerra a execução em caso de outros erros ao carregar o CSV

# Verificar se as colunas 'pergunta' e 'resposta' existem no CSV
if 'Pergunta' not in df.columns or 'Resposta' not in df.columns:
    print("Erro: O arquivo CSV não contém as colunas 'Pergunta' e 'Resposta'.")
    exit()  # Encerra a execução caso as colunas não existam

# Extração das colunas 'pergunta' e 'resposta'
perguntas = df['Pergunta'].tolist()
respostas = df['Resposta'].tolist()

# Gerar pares de pergunta e resposta
augmented_data = []
for i in tqdm(range(len(perguntas))):
    question = perguntas[i]
    answer = respostas[i]
    try:
        augmented_pairs = augment_data(question, answer, num_samples=100)  # Ajuste o número conforme necessário
        augmented_data.extend(augmented_pairs)
    except Exception as e:
        print(f"Erro ao processar a pergunta {i+1}: {question}. Erro: {e}")
        continue  # Continua para o próximo item mesmo após um erro

# Converter para DataFrame e salvar em CSV
try:
    augmented_df = pd.DataFrame(augmented_data, columns=['Pergunta', 'Resposta'])
    augmented_df.to_csv('Data/Data_augmentation/dados_augmentados3.csv', index=False)
    print("Data augmentation completo! Salvo em 'dados_augmentados.csv'")
except Exception as e:
    print(f"Erro ao salvar o arquivo CSV. Erro: {e}")

#%%
import ollama
response = ollama.chat(model="gemma2:2b", messages=[{"role": "user", "content": "O que é um algoritmo?"}])
print(response["message"]["content"])

#%%
import pandas as pd
df = pd.read_csv('Data/Data_orivas_csv/dados_concatenados.csv')
print(df["Pergunta"])