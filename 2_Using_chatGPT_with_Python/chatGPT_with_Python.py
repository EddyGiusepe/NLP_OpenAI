'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''

'''
ChatGPT é uma variante do modelo de linguagem GPT-3, projetado especificamente
para geração de linguagem de conversação. Para usar o ChatGPT em Python, você precisará
instalar o cliente OpenAI API e obter uma chave de API.
'''
import os 
import openai 
import gradio as gr
from dotenv import load_dotenv 

print('Minha chave Key: ', load_dotenv())
Eddy_API_KEY = os.environ['API_KEY'] 

# Configurar o cliente OpenAI API
openai.api_key = Eddy_API_KEY

# Configure o modelo e o prompt
model_engine = "text-davinci-003"
prompt = "Olá, como vai você, hoje?"

# Gerar uma resposta
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None, # Especifica string ou sequência de strings que, se encontradas no texto gerado, farão com que o modelo pare de gerar mais texto.
    # Isso pode ser útil para controlar o comprimento do texto gerado ou para garantir que o modelo não gere conteúdo inapropriado.
    temperature=0.5, # Mais alta resultará em respostas mais variadas e potencialmente menos coerentes, mais baixa resultará em respostas mais
    # previsíveis e potencialmente mais coerentes.
)

response = completion.choices[0].text # A resposta retorna como uma string nesta variável response.
print(response)
