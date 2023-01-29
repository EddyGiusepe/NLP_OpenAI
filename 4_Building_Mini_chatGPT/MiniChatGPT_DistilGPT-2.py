'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''


'''
Step 1: Data Collection and Preprocessing

A primeira etapa no desenvolvimento de uma versão em pequena escala do ChatGPT é coletar e pré-processar
os dados. O modelo será treinado em um conjunto de dados de texto, como artigos, livros ou postagens de mídia
social. Quanto mais dados estiverem disponíveis, melhor o modelo entenderá e gerará linguagem natural.
'''

import pandas as pd

# Load data into a pandas dataframe
data = pd.read_csv("train.csv")
print(data.shape)
print(data.columns)
print('')
print(data.head(7))


# Eliminando as colunas que não precissamos 
data.drop(['question_id', 'question', 'document_title', 'label'], axis=1, inplace=True)
# Renomeando o neme da coluna 'answer' para 'text'
data.rename(columns={'answer': 'text'}, inplace=True)
print(data.head(7))

# Pré-processamento dos Dados 
data = data.dropna()  # Remove valores missing
data = data.drop_duplicates()  # Remove valores duplicados 
data = data.sample(frac=1)  # Shuffle (embaralhar) os dados 
print(data.shape)
print(data.head(8))

'''
Step 2: Tokenization

Depois que os dados forem coletados e pré-processados, a próxima etapa é tokenizar o texto.
A tokenização é o processo de dividir o texto em palavras ou subpalavras individuais.
Isso pode ser feito usando uma biblioteca como tokenizers NLTK ou Hugging Face.
'''

