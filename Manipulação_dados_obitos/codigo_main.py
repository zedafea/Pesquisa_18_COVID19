# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 12:30:58 2021

@author: guilh
"""

import pandas as pd

#Unindo os dataframes de cada ano em um único df_main
dfs = [df_2017,df_2018,df_2019,df_2020,df_2021]
df_main = pd.concat(dfs,axis=1)

#Substituindo a expressão '-' por zeros e transformando todos os valores em numéricos
df_main = df_main.replace({'-':0})
df_main = df_main.astype('int')

#Por meio desse loop nós passamos pelos anos e pelas faixas etárias obtendo a informação
#do número de óbitos de Abril a Março do ano seguinte
ls = [[0,9],[10,19],[20,29],[30,39],[40,49],[50,59],[60,69],[70,'inf']]
la = [2017,2018,2019,2020,2021]
df_total = {}
for i in la:
    if i != 2021:
        for j in ls:
            df_aux0 = df_main.loc[:,f'obitos_{i}_total_Abril_{j[0]}_{j[1]}_anos':f'obitos_{i}_total_Dezembro_{j[0]}_{j[1]}_anos']
            df_aux1 = df_main.loc[:,f'obitos_{i+1}_total_Janeiro_{j[0]}_{j[1]}_anos':f'obitos_{i+1}_total_Março_{j[0]}_{j[1]}_anos']
            df_aux = pd.concat([df_aux0,df_aux1],axis=1)
            df_total[f'obitos_{i}/{i+1}_total_{j[0]}_{j[1]}_anos'] = df_aux.sum(axis=1)

df_total = pd.DataFrame(df_total)           
df_total.to_csv(r'\total_obitos_distrito.csv')
