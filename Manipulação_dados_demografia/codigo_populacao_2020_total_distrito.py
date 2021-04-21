# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:43:02 2021

@author: guilh
"""

import pandas as pd
import requests

#Importação dos dados via API Seade
distr = []
for i in range(80001,80097):
    link = requests.get(f'http://api-projpop.seade.gov.br/v1/dados/iq/dc/t/{i}/2020')
    dados = link.json()['dados']
    distr.append(dados)

#Transformação dos dados em formato DataFrame e concatenação em um único df
dfs = []
for j in range(len(distr)):
    dfs.append(pd.DataFrame(distr[j]))
df = pd.concat(dfs)

#Selecionando as colunas que nos interessam e ajustando as faixas etárias 
df_inter = df.iloc[:,-19:-3]
df_inter['Distrito Admin residência'] = df.nome
df_inter.set_index('Distrito Admin residência',inplace=True)
df_inter = df_inter.astype('int')
for y in range(len(df_inter.columns)):
    df_inter[f'populacao_2020_total_{df_inter.columns[y][6:8]}_{df_inter.columns[y+1][11:13]}_anos'] = df_inter.loc[:,df_inter.columns[y:y+2]].sum(axis=1)

#Selecionando as colunas que nos interessam e adicionando a coluna com os 
#valores totais da pop
df_inter = df_inter.iloc[:,-16:-1:2]
df_inter['populacao_2020_total'] = df_inter.sum(axis=1)

#Incluindo colunas com a informação sobre as % de cada faixa etária na pop
#de cada distrito
for z in range(len(df_inter.columns[:8])):
    df_inter[f'populacao_2020_percentagem_{df_inter.columns[z][21:23]}_{df_inter.columns[z][24:26]}_anos'] = df_inter.loc[:,df_inter.columns[z]]/df_inter['populacao_2020_total']

df_inter.to_csv(r'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\populacao_2020_distrito.csv')
