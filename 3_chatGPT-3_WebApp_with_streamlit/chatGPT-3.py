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





