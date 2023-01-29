'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
import openai

import streamlit as st
from streamlit_chat import message

import os 
from dotenv import load_dotenv
load_dotenv('api_key.env')

openai.api_key = os.environ.get('API_KEY')

def generate_response(prompt):
    completion=openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.6, # Pode ser definida entre 0 e 1. 0 produz saídas estáveis, enquanto 1 é altamente criativo.
    )
    message=completion.choices[0].text
    return message

# A seguir implementamos a interação com usuário com o streamlit

st.title("Web App similar ao chatGPT-3 da OpenAI")
# Armazenando o chat 
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
user_input=st.text_input("Você:",key='input')
if user_input:
    output=generate_response(user_input)
    # Armazenar a saída
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

