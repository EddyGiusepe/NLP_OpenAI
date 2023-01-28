'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
import os 
import openai 
import gradio as gr
from dotenv import load_dotenv 

print('Carregando a minha chave Key: ', load_dotenv())

Eddy_API_KEY = os.environ['API_KEY']  
openai.api_key = Eddy_API_KEY 

start_sequence = "\AI:"
restart_sequence = "\Human:"

prompt = "Digita aqui para começar uma conversa com um assistente de AI: "

def openai_create(prompt):
    '''
    Esta função usa a API da OpenAI para gerar texto com base no prompt fornecido. O prompt é uma string que representa o ponto
    de partida para a geração de texto.
    A função usa o método Completion.create() da API OpenAI para gerar o texto.
    Este método possui vários parâmetros que controlam o comportamento da geração de texto:  
    '''
    response = openai.Completion.create(
           model = "text-davinci-003", # Modelo GPT-3 para a geração de texto. Neste caso, modelo "text-davinci-003".
           prompt = prompt, # Prompt, fornecido para a função como um argumento. Ponto de partida para a geração de texto.
           temperature = 0.9, # Controla a aleatoriedade do texto gerado
           # Uma temperatura mais alta resultará em respostas mais variadas e criativas, enquanto uma temperatura mais baixa resultará em respostas mais previsíveis.
           max_tokens=150, # Número máximo de tokens (palavras individuais ou sinais de pontuação) que devem ser gerados na resposta. 
           top_p=1, # Controla a probabilidade de gerar respostas mais comuns.
           # Um valor mais alto resultará em respostas mais comuns, enquanto um valor mais baixo permitirá respostas mais variadas.
           frequency_penalty=0, # Controla a probabilidade de gerar respostas menos comuns.
           # Um valor mais alto resultará em respostas menos comuns, enquanto um valor mais baixo permitirá respostas mais comuns.
           presence_penalty=0.6, # Controla a probabilidade de gerar respostas que contenham palavras ou frases específicas.
           # Um valor mais alto resultará em respostas com maior probabilidade de conter essas palavras ou frases, enquanto um valor mais baixo permitirá respostas mais variadas.
           stop=[" Human:", " AI:"] # Este parâmetro especifica uma lista de palavras ou frases que interromperão a geração de texto quando encontradas.
           # Nesse caso, a geração de texto será interrompida quando as palavras "Human:" ou "AI:" forem encontradas.
       ) 
    return response.choices[0].text # Você acessa o text atributo do choices[0] elemento do objeto response. 

def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history 

block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>Meu chatGPT</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])
    
block.launch(debug = True)
