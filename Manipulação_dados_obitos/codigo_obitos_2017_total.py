# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:39:31 2021

@author: guilh
"""

import pandas as pd

ls = [[0,9],[10,19],[20,29],[30,39],[40,49],[50,59],[60,69],[70,'inf']]
dfs = []

#2017

#0_9_anos
df_2017_0_9 = pd.read_csv(r'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\obitos_total_distrito_2017\obitos_total_0_9_anos.csv',
                     sep = 'delimiter', encoding = 'Latin1',header = None)
df_2017_0_9 = df_2017_0_9.iloc[4:100,].reset_index(drop=True)
df_2017_0_9 = df_2017_0_9.rename(columns={0:'Name'})
df_2017_0_9 = df_2017_0_9.Name.str.split(';',expand = True).apply(lambda x:x.str.replace('"',""))
faixa_etaria = ls[0]
df_2017_0_9 = df_2017_0_9.rename(columns = df_2017_0_9.iloc[0]).drop(df_2017_0_9.index[0]) 
df_2017_0_9 = df_2017_0_9.iloc[:,:13]
df_2017_0_9.loc[11.5] = ['Butantã',0,0,0,0,0,0,0,0,0,0,0,0]
df_2017_0_9 = df_2017_0_9.sort_index()
df_2017_0_9.set_index('Distrito Admin residência',inplace=True)

col_names = []
for j in df_2017_0_9.columns:
    col_names.append('obitos' + '_' + str(2017) + '_' + 'total' + '_' + j + '_' + str(faixa_etaria[0]) + '_' + str(faixa_etaria[1]) + '_' + 'anos')
df_2017_0_9.set_axis(col_names, axis=1, inplace=True)

dfs.append(df_2017_0_9)

#10_19_anos
df_2017_10_19 = pd.read_csv(r'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\obitos_total_distrito_2017\obitos_total_10_19_anos.csv',
                     sep = 'delimiter', encoding = 'Latin1',header = None)
df_2017_10_19 = df_2017_10_19.iloc[4:93,].reset_index(drop=True)
df_2017_10_19 = df_2017_10_19.rename(columns={0:'Name'})
df_2017_10_19 = df_2017_10_19.Name.str.split(';',expand = True).apply(lambda x:x.str.replace('"',""))
faixa_etaria = ls[1]
df_2017_10_19 = df_2017_10_19.rename(columns =df_2017_10_19.iloc[0]).drop(df_2017_10_19.index[0]) 
df_2017_10_19 = df_2017_10_19.iloc[:,:13]
df_2017_10_19.loc[1.5] = ['Alto de Pinheiros',0,0,0,0,0,0,0,0,0,0,0,0]
df_2017_10_19.loc[10.5] = ['Butantã',0,0,0,0,0,0,0,0,0,0,0,0]
df_2017_10_19.loc[11.5] = ['Cambuci',0,0,0,0,0,0,0,0,0,0,0,0]
df_2017_10_19.loc[44.5] = ['Lapa',0,0,0,0,0,0,0,0,0,0,0,0]
df_2017_10_19.loc[45.5] = ['Limão',0,0,0,0,0,0,0,0,0,0,0,0]
df_2017_10_19.loc[47.5] = ['Moema',0,0,0,0,0,0,0,0,0,0,0,0]
df_2017_10_19.loc[50.5] = ['Pari',0,0,0,0,0,0,0,0,0,0,0,0]
df_2017_10_19.loc[73.5] = ['Socorro',0,0,0,0,0,0,0,0,0,0,0,0]
df_2017_10_19 = df_2017_10_19.sort_index()
df_2017_10_19.set_index('Distrito Admin residência',inplace=True)

col_names = []
for j in df_2017_10_19.columns:
    col_names.append('obitos' + '_' + str(2017) + '_' + 'total' + '_' + j + '_' + str(faixa_etaria[0]) + '_' + str(faixa_etaria[1]) + '_' + 'anos')
df_2017_10_19.set_axis(col_names, axis=1, inplace=True)

dfs.append(df_2017_10_19)

#20_29_anos
df_2017_20_29 = pd.read_csv(r'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\obitos_total_distrito_2017\obitos_total_20_29_anos.csv',
                     sep = 'delimiter', encoding = 'Latin1',header = None)
df_2017_20_29 = df_2017_20_29.iloc[4:100,].reset_index(drop=True)
df_2017_20_29 = df_2017_20_29.rename(columns={0:'Name'})
df_2017_20_29 = df_2017_20_29.Name.str.split(';',expand = True).apply(lambda x:x.str.replace('"',""))
faixa_etaria = ls[2]
df_2017_20_29 = df_2017_20_29.rename(columns =df_2017_20_29.iloc[0]).drop(df_2017_20_29.index[0]) 
df_2017_20_29 = df_2017_20_29.iloc[:,:13]
df_2017_20_29.loc[38.5] = ['Jaguara',0,0,0,0,0,0,0,0,0,0,0,0]
df_2017_20_29 = df_2017_20_29.sort_index()
df_2017_20_29.set_index('Distrito Admin residência',inplace=True)

col_names = []
for j in df_2017_20_29.columns:
    col_names.append('obitos' + '_' + str(2017) + '_' + 'total' + '_' + j + '_' + str(faixa_etaria[0]) + '_' + str(faixa_etaria[1]) + '_' + 'anos')
df_2017_20_29.set_axis(col_names, axis=1, inplace=True)

dfs.append(df_2017_20_29)

#30_39_anos
df_2017_30_39 = pd.read_csv(r'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\obitos_total_distrito_2017\obitos_total_30_39_anos.csv',
                     sep = 'delimiter', encoding = 'Latin1',header = None)
df_2017_30_39 = df_2017_30_39.iloc[4:100,].reset_index(drop=True)
df_2017_30_39 = df_2017_30_39.rename(columns={0:'Name'})
df_2017_30_39 = df_2017_30_39.Name.str.split(';',expand = True).apply(lambda x:x.str.replace('"',""))
faixa_etaria = ls[3]
df_2017_30_39 = df_2017_30_39.rename(columns =df_2017_30_39.iloc[0]).drop(df_2017_30_39.index[0]) 
df_2017_30_39 = df_2017_30_39.iloc[:,:13]
df_2017_30_39.loc[1.5] = ['Alto de Pinheiros',0,0,0,0,0,0,0,0,0,0,0,0]
df_2017_30_39 = df_2017_30_39.sort_index()
df_2017_30_39.set_index('Distrito Admin residência',inplace=True)

col_names = []
for j in df_2017_30_39.columns:
    col_names.append('obitos' + '_' + str(2017) + '_' + 'total' + '_' + j + '_' + str(faixa_etaria[0]) + '_' + str(faixa_etaria[1]) + '_' + 'anos')
df_2017_30_39.set_axis(col_names, axis=1, inplace=True)

dfs.append(df_2017_30_39)

#40_inf_anos
for i in ls[4:]:
    df = pd.read_csv(rf'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\obitos_total_distrito_2017\obitos_total_{i[0]}_{i[1]}_anos.csv',
                     sep = 'delimiter', encoding = 'Latin1',header = None)
    df = df.iloc[4:101,].reset_index(drop=True)
    df = df.rename(columns={0:'Name'})
    df = df.Name.str.split(';',expand = True).apply(lambda x:x.str.replace('"',""))
    faixa_etaria = i
    df = df.rename(columns = df.iloc[0]).drop(df.index[0]) 
    df = df.iloc[:,:13]
    df.set_index('Distrito Admin residência',inplace=True)
    col_names = []
    for j in df.columns:
        col_names.append('obitos' + '_' + str(2017) + '_' + 'total' + '_' + j + '_' + str(faixa_etaria[0]) + '_' + str(faixa_etaria[1]) + '_' + 'anos')
    df.set_axis(col_names, axis=1, inplace=True)
    dfs.append(df)
         
df_2017 = pd.concat(dfs,axis=1)
