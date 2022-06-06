# -*- coding: utf-8 -*-
"""Arquivo Inicial - Minicurso Analise de Dados Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1spnWppv7u31EtL8NHsSrETto20huAPvf

# Desafio: 

Você trabalha em uma grande empresa de Cartão de Crédito e o diretor da empresa percebeu que o número de clientes que cancelam seus cartões tem aumentado significativamente, causando prejuízos enormes para a empresa

O que fazer para evitar isso? Como saber as pessoas que têm maior tendência a cancelar o cartão?

# O que temos:

Temos 1 base de dados com informações dos clientes, tanto clientes atuais quanto clientes que cancelaram o cartão

Download da Base de Dados: Botão na página

Referência: https://www.kaggle.com/sakshigoyal7/credit-card-customers

# **- Passo 1: Importar a base de dados**
"""

import pandas as pd

tabela = pd.read_csv('/content/drive/MyDrive/Minicurso Análise de dados com python/ClientesBanco.csv', encoding = 'latin1') # encoding define o idioma que vai ser lido
display(tabela)

"""# **- Passo 2: Visualizar e tratar essa base de dados**








"""

tabela = tabela.drop('CLIENTNUM', axis = 1) # drop('nome da coluna', axis = ) axis = 0 exclui linha, axis = 1 exclui coluna
display(tabela)

"""# **- Passo 3: Dar uma olhada na base de dados**
1.  ***Categoria:*** se é um cliente ou se cancelou o cartão
2.  ***Idade:*** idade do cliente
3.  ***Sexo:*** o sexo do cliente
4.  ***Dependentes:*** ex. informa quantas pessoas depende do cliente
5.  ***Educação:*** nivel de formação do cliente
6.  ***Estado civil:*** informa se o cliente é casado ou solteiro
7.  ***Faixa salarial anual:*** categorias de salario anual
8.  ***Categoria do cartão:*** blue, silver, gold
9.  ***Meses como Cliente:*** informa quanto tempo ele é cliente
10. ***Produtos contratados:*** quantos cartões ou serviço o cliente tem
11. ***Inatividade 12m:*** durante 1 ano quanto tempo ele ficou sem usar o cartão
12. ***Contatos 12m:*** durante 1 ano quantas vezes ele ligou pra central para resolver algum problema
13. ***Limite:*** limite maximo do cartão
14. ***Limite consumido:*** o que o cliente consumiu
15. ***Limite disponivel:*** o que o cliente pode ainda usar
16. ***Mudanças Transacoes_Q4_Q1:*** transações do 4º trimestre para o 1º trimestre
17. ***Valor Transacoes 12m:*** quanto ele gastou no cartão durante um ano
18. ***Qtde Transacoes 12m:*** quantas vezes ele passou o cartão
19. ***Mudança Qtde Transações_Q4_Q1:*** quantidade de transações do 4º trimestre para o 1º trimestre
20. ***Taxa de Utilização Cartão:*** indice que informa o quanto ele usa o cartão (0 à 1)
"""

tabela = tabela.dropna() # apaga as linha que tiver pelo menos 1 valor nulo(não tem nada)
display(tabela.info()) # informa informações da tabela

display(tabela.describe().round(1)) # descrição da tabela, round arredonda

"""# **- Passo 4: Construir uma análise para identificar o motivo de cancelamento**

*   Identificar qual o motivo ou os principais motivos dos clientes estarem cancelando o cartão de crédito

**Vamos avaliar Clientes x Cancelados**
"""

qtde_categoria = tabela['Categoria'].value_counts(normalize = False) # Conta quantidade de cada opção
print(qtde_categoria)

qtde_categoria_perc = tabela['Categoria'].value_counts(normalize = True) # Conta quantidade de cada opção, normalize para percentual 
print(qtde_categoria_perc)

"""**Temos várias formas de descobrir o motivo de cancelamento**

*   Podemos olhar a comparação entre clientes e cancelados em cada uma das colunas da nossa base de dados, para ver se essa informação traz algum insight novo para a gente



"""

import plotly.express as px # Biblioteca para graficos 

for coluna in tabela: # percorre as colunas
  grafico = px.histogram(tabela, x = coluna, color = 'Categoria') # Metodo para criar um grafico .histogram('Banco de dados, variavel no eixo x, separar por cor )
  grafico.show() # Metodo para mostrar o grafico

"""# **Informações obtidas de analise dos graficos:**



*   Apresenta menor taxa de cancelado quando o cliente tem mais produtos contratados 
*  E quanto mais transações e quanto maior o valor de transação menor os cancelamentos
*  Quanto maior a quantidade do cliente entra em contato com a empresa maior é a taxa de cancelamento


"""