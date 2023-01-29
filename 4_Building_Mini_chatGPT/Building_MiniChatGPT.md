Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro

# Construindo seu próprio Mini ChatGPT

Desenvolver uma versão em pequena escala do `ChatGPT` é uma tarefa desafiadora que requer uma compreensão profunda dos conceitos de `Processamento de Linguagem Natural` (NLP) e aprendizado de máquina (ML). No entanto, com as ferramentas e recursos certos, é possível desenvolver uma versão em pequena escala do `ChatGPT` que pode gerar texto semelhante ao humano.

A arquitetura do modelo é baseada na arquitetura do `Transformers`, que usa `auto-atenção multicabeça` (multi-head self-attention) e redes neurais de alimentação (`feed-forward neural networks `) para gerar texto semelhante ao humano. Eu escrevi um pseudocódigo que pode ser usado.

# DistilGPT-2

É uma versão menor do `GPT-2`, que é um `modelo de linguagem` de última geração desenvolvido pela [OpenAI](https://openai.com/). O [DistilGPT-2](https://huggingface.co/distilgpt2) tem menos parâmetros do que o `GPT-2`, o que o torna mais rápido para treinar e executar, mantendo um alto nível de desempenho. Isso o torna mais acessível para uso em ambientes com recursos limitados, como em `dispositivos móveis` ou em `sistemas embarcados`. Além disso, o `DistilGPT-2` também é menor em tamanho e pode ser mais fácil de implantar em dispositivos de ponta. O modelo é treinado para gerar texto semelhante ao humano e pode ser ajustado para várias tarefas de linguagem, como `resposta a perguntas`, `tradução de idiomas` e `resumo de texto`.

<font color='orange'>DistilGPT2 was trained using [OpenWebTextCorpus](https://skylion007.github.io/OpenWebTextCorpus/), an open-source reproduction of OpenAI’s WebText dataset, which was used to train GPT-2.</font>

As etapas/passos que serão realizadas são:

* passo 1: Coleta e pré-processamento de dados

* passo 2: Tokenização

* passo 3: Arquitetura do modelo

* passo 4: Treinamento

* passo 5: Avaliação

* passo 6: Implantação (Deployment)




Thanks God!