import time
import ollama
import csv
from datetime import datetime
from tqdm.auto import tqdm  # usa automaticamente a versão adequada (console ou notebook)

#Lista de variações do modelo a serem testadas
# modelos = ["deepseek-r1:1.5b", "deepseek-r1:7b", "deepseek-r1:8b", 
#            "deepseek-r1:14b", "phi3:3.8b", "phi3:14b", "mistral:7b", "mistral-nemo:12b",
#            "phi4:14b", "gemma2:2b", "gemma2:9b"]

modelos = ["mistral-nemo:12b"]

# Lista de prompts
prompts = [
    #Nível Fácil
    "O que é um algoritmo?",
    "O que é uma variável em programação?",
    """ Qual será a saída do seguinte código?
        let x = 5;
        let y = 2;
        console.log(x + y);
    """,
    "O que faz a estrutura de controle if em programação?",
    """Qual o resultado da seguinte expressão lógica?
        console.log((true && false) || true);
    """,
    #Nível Médio
    """Qual será a saída do seguinte código?

        for (let i = 0; i < 3; i++) {
            console.log(i * 2);
        }
    """,
    "Explique a diferença entre um loop for e um loop while.",
    "O que acontece quando um programa entra em um loop infinito?",
    "O que significa depuração(debugging) em programação?",
    """Qual será a saída do seguinte código?
        let contador = 0;
        while (contador < 3) {
            if (contador % 2 === 0) {
                console.log("Par");
            } else {
                console.log("Ímpar");
            }
            contador++;
        }
    """,
    #Nível Difícil
    """Dado o código abaixo, qual será a saída?

        function func(x) { 
        return x * x; 
        } 
        console.log(func(3) + func(2));
    """,
    """Qual será a saída do seguinte código?
        let a = [1, 2, 3];
        let b = a;
        b.push(4);
        console.log(a);
    """,
    """Qual será a saída do seguinte código?

        let numeros = [10, 20, 30];
        numeros[1] = 50;
        console.log(numeros);
    """,
    """Qual será a saída do seguinte código?

        function dobro(x) {
            return x * 2;
        }
        console.log(dobro(5));
    """,
    """O que acontece se chamarmos uma função antes de sua declaração em JavaScript?

        console.log(somar(3, 4));

        function somar(a, b) {
            return a + b;
        }
    """
]

# Criar o arquivo CSV com cabeçalho
filename = f"Avaliacao-modelos-3-{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
file = open(filename, 'w', newline='', encoding='utf-8')
writer = csv.DictWriter(file, fieldnames=["Modelo", "Pergunta", "Resposta", "Tempo (s)"])
writer.writeheader()
file.close()

# Calculando total de iterações para a barra de progresso principal
total_iterations = len(modelos) * len(prompts)

# Loop principal com barra de progresso
with tqdm(total=total_iterations, desc="Progresso Total") as pbar:
    for model in modelos:
        # Barra de progresso para cada modelo
        print(f"\nProcessando modelo: {model}")
        for prompt in tqdm(prompts, desc=f"Prompts para {model}", leave=False):
            start_time = time.time()

            try:
                # Chama o modelo no Ollama
                response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
                
                elapsed_time = time.time() - start_time
                response_text = response["message"]["content"]

                # Criar dicionário com os resultados
                result = {
                    "Modelo": model,
                    "Pergunta": prompt,
                    "Resposta": response_text,
                    "Tempo (s)": round(elapsed_time, 2)
                }

                with open(filename, 'a', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=["Modelo", "Pergunta", "Resposta", "Tempo (s)"])
                    writer.writerows([result])

            except Exception as e:
                print(f"\nErro ao processar {model} com prompt {prompt[:50]}: {str(e)}")
                with open(filename, 'a', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=["Modelo", "Pergunta", "Resposta", "Tempo (s)"])
                    writer.writerow({
                        "Modelo": model,
                        "Pergunta": prompt,
                        "Resposta": f"ERRO: {str(e)}",
                        "Tempo (s)": round(time.time() - start_time, 2)
                    })
            
            # Atualizar a barra de progresso principal
            pbar.update(1)

file.close()

print(f"\nProcesso completo! Resultados salvos em {filename}")