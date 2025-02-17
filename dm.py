import subprocess

# Lista de modelos para baixar
modelos = ["gemma2:2b", "gemma2:9b"]

# Loop para baixar cada modelo
for modelo in modelos:
    print(f"Baixando {modelo}...")
    subprocess.run(["ollama", "pull", modelo])

# Lista de modelos para baixar
modelos = ["mistral:7b", "mistral:7b-instruct"]

print("Todos os modelos foram baixados!")

