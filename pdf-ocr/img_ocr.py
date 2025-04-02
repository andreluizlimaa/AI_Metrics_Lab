from PIL import Image
import pytesseract
import numpy as np
import os
from tqdm import tqdm

import google.generativeai as genai
import google.api_core.exceptions
from dotenv import load_dotenv
import os

#carregar variaveis de ambiente
load_dotenv()

# Configurar a API
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Escolher o modelo adequado
model = genai.GenerativeModel("gemini-2.0-flash")

import time
import random

def corrigir_texto(texto, max_retries=10):
    prompt = f"Corrija os erros gramaticais e ortográficos do seguinte texto, mantendo o sentido original (retorne somente o texto):\n\n{texto}"

    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text if response and hasattr(response, 'text') else "Erro ao gerar resposta"
        except google.api_core.exceptions.ResourceExhausted as e:
            wait_time = (2 ** attempt) + random.uniform(0, 2)  # Exponential backoff
            print(f"Limite excedido. Tentando novamente em {wait_time:.2f} segundos...")
            time.sleep(wait_time)
    
    return "Erro: Limite de requisições excedido mesmo após múltiplas tentativas."

if not os.path.exists('./txts'):
    os.makedirs('./txts')

for folder in sorted(os.listdir('./images')):
    text = ''
    
    for i in tqdm(range(len(os.listdir(f'./images/{folder}')))):
        img = np.array(Image.open(f'./images/{folder}/out{i}.jpg'))
        text += corrigir_texto(pytesseract.image_to_string(img))

    with open(f'./txts/{folder}.txt', 'w') as f:
        f.write(text)

