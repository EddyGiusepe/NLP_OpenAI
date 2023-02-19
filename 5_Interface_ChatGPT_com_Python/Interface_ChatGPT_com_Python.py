'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Link asombroso de estudo --> https://levelup.gitconnected.com/interfacing-chatgpt-with-python-824be63dfa2f



'''
Interface ChatGPT com Python

Até agora você deve ter ouvido falar do ChatGPT (Chat Generative Pre-trained Transformer) - um chatbot desenvolvido pela OpenAI.
Lançado em novembro de 2022, o ChatGPT foi desenvolvido com base na família GPT-3 de modelos de linguagem grande (Large Language Models - LLMs)
da OpenAI e ajustado usando técnicas de aprendizado supervisionado e por reforço. Desde então, o ChatGPT provocou uma mania de IA,
atingindo 100 milhões de usuários apenas dois meses após seu lançamento.

Em vez de experimentar o ChatGPT em https://chat.openai.com/chat, como desenvolvedor, acho mais emocionante poder integrá-lo aos seus aplicativos.
E assim, neste script, mostrarei como você pode interagir com o ChatGPT usando Python.
'''


'''
Como solicitar uma chave de API

A OpenAI fornece APIs para que os desenvolvedores acessem os serviços da OpenAI. Para usá-los, você precisa primeiro solicitar uma chave de API.
Vá para https://platform.openai.com/account/api-keys e clique no botão Criar nova chave secreta.
'''

'''
Instalando a biblioteca OpenAI Python

Em seguida, para usar o Python para chamar o ChatGPT, instale a biblioteca OpenAI Python
(https://github.com/openai/openai-python) usando o comando pip:

pip install openai
'''



'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
import os 
import openai 
from dotenv import load_dotenv 

print('Carregando a minha chave Key: ', load_dotenv())

Eddy_API_KEY = os.environ['API_KEY']  
openai.api_key = Eddy_API_KEY 


'''
Exibindo modelos suportados

Como mencionado, o ChatGPT é baseado no GPT-3. Existem quatro modelos principais que o modelo GPT-3 oferece:

* Davinci — Modelo GPT-3 mais capaz. Pode fazer qualquer tarefa que os outros modelos podem fazer, muitas vezes com maior qualidade,
            saída mais longa e melhor seguimento de instruções. Também suporta a inserção de conclusões no texto.

* Curie — Muito capaz, mas mais rápido e com menor custo do que Davinci.

* Babbage — Capaz de realizar tarefas simples, muito rápidas e de baixo custo.

* Ada — Capaz de tarefas muito simples, geralmente o modelo mais rápido da série GPT-3 e de menor custo.

Fonte: https://platform.openai.com/docs/models/gpt-3

A seguir, vamos listar os vários modelos suportados.
'''

models = openai.Model.list()
print("A saída é um JSON mostrando os vários modelos suportados: ", models)

print("Usando list comprehension para mostrar a lista de modelos: ")
print("")
lista_models = [model['id'] for model in models['data']]
print(lista_models)

'''
“text-davinci-003” é a versão mais recente e este é o modelo que usarei neste exemplo.
'''


'''
Criando uma conclusão (Creating a completion)

Para ter uma conversa de bate-papo com o ChatGPT, você executa uma completion (conclusão).
A ideia por trás da conclusão é que você forneça algum texto como um prompt e o modelo tentará completar sua frase.
Vamos usar a função "Completion.create()" para pedir ao ChatGPT que nos conte uma piada.
'''
model_engine = "text-davinci-003"
completion = openai.Completion.create(engine = model_engine, 
                                      prompt = 'Fala para mim uma piada, por favor!', 
                                      max_tokens = 1024,
                                      temperature = 0.8)

'''
A função "Completion.create()" recebe os seguintes argumentos:

* engine — o modelo a usar

* prompt — a mensagem a ser enviada ao bot de bate-papo (ao chat bot)

* max_tokens — o número máximo de tokens a serem gerados na conclusão. Se você definir isso como um número pequeno, a resposta retornada
               pode não ser completa.

* temperature — um valor entre 0 e 1. Um valor mais baixo torna a saída mais determinística. 
                Se você definir um valor mais alto, como 0.8, é mais provável que a saída seja diferente quando você chamar a função várias vezes.

Ver informações sobre TOKENS: https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
'''

print(completion)

'''
O resultado (print de completion) em JSON que contém inúmeras informações. Em particular, o valor da chave "choices" é um array,
cujo primeiro elemento contém o resultado que queremos, armazenado na chave "text".
'''
message = completion.choices[0].text
print(message)

'''
Fazendo com que o usuário pergunte ao ChatGPT

Agora que você pode interagir com o ChatGPT usando Python, vamos modificar um pouco nosso código para que
nossos usuários possam interagir diretamente com o ChatGPT.
'''
# Usando o ChatGPT para gerar texto
model_engine = "text-davinci-003"

while True:
    prompt = input('\nSou o ChatGPT, em que posso ajudá-lo: ')
    completion = openai.Completion.create(engine = model_engine, 
                                          prompt = prompt, 
                                          max_tokens = 1024, 
                                          temperature = 0.8)
    message = completion.choices[0].text
    print(message)
