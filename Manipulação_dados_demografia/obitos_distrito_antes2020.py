# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:17:01 2021

@author: guilh
"""

import pandas as pd

#No Tabnet foram escolhidas as opções:
    #Linha: Distrito Admin residência
    #Coluna: Mês do Óbito
    #Conteúdo: Óbitos ocorridos MSP
dfs = []
for i in range(2017,2021):
    df = pd.read_csv(rf'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\obitos_distrito_{i}.csv',
                     sep = 'delimiter', encoding = 'Latin1',header = None)
    df = df.iloc[3:102,]
    df = df.rename(columns={0:'Name'})
    df = df.Name.str.split(';',expand = True).apply(lambda x:x.str.replace('"',""))
    df = df.rename(columns = df.iloc[0]).drop(df.index[0])    
    dfs.append(df)

df = pd.concat(dfs,axis=1)
df = df.reset_index().T.drop_duplicates().T
df = df.iloc[:,1:]
df.set_index('Distrito Admin residência',inplace=True)  

df = df.iloc[:,2:42]
df = df.drop(columns=['Total'])

#Óbitos de março(inclusive) a março(inclusive) 
df_17_18 = df.iloc[:,:13]
df_18_19 = df.iloc[:,12:25].replace('-',0)
df_19_20 = df.iloc[:,24:].replace('-',0)

df_17_18['Óbitos 03/17-03/18'] = df_17_18.astype(int).sum(axis=1)
df_18_19['Óbitos 03/18-03/19'] = df_18_19.astype(int).sum(axis=1)
df_19_20['Óbitos 03/19-03/20'] = df_19_20.astype(int).sum(axis=1)
df = pd.concat([df_17_18,df_18_19,df_19_20],axis=1)

df.to_csv('obitos_distrito_antes2020.csv')
