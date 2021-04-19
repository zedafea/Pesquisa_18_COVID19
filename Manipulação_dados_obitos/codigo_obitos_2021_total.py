# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 21:04:49 2021

@author: guilh
"""

import pandas as pd

ls = [[0,9],[10,19],[20,29],[30,39],[40,49],[50,59],[60,69],[70,'inf']]
dfs = []

#2021

#0_9_anos
df_2021_0_9 = pd.read_csv(rf'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\obitos_total_distrito_2021\obitos_total_0_9_anos.csv',
                 sep = 'delimiter', encoding = 'Latin1',header = None)
df_2021_0_9 = df_2021_0_9.iloc[4:75,].reset_index(drop=True)
df_2021_0_9 = df_2021_0_9.rename(columns={0:'Name'})
df_2021_0_9 = df_2021_0_9.Name.str.split(';',expand = True).apply(lambda x:x.str.replace('"',""))
faixa_etaria = ls[0]
df_2021_0_9 = df_2021_0_9.rename(columns = df_2021_0_9.iloc[0]).drop(df_2021_0_9.index[0]) 
df_2021_0_9 = df_2021_0_9.iloc[:,:4]
df_2021_0_9.loc[5.5] = ['Barra Funda',0,0,0]
df_2021_0_9.loc[10.5] = ['Butantã',0,0,0]
df_2021_0_9.loc[11.5] = ['Cambuci',0,0,0]
df_2021_0_9.loc[17.5] = ['Casa Verde',0,0,0]
df_2021_0_9.loc[21.5] = ['Consolação',0,0,0]
df_2021_0_9.loc[22.5] = ['Ermelino Matarazzo',0,0,0]
df_2021_0_9.loc[26.5] = ['Ipiranga',0,0,0]
df_2021_0_9.loc[31.5] = ['Jaguara',0,0,0]
df_2021_0_9.loc[35.5] = ['Jardim Paulista',0,0,0]
df_2021_0_9.loc[38.2] = ['Lapa',0,0,0]
df_2021_0_9.loc[38.8] = ['Liberdade',0,0,0]
df_2021_0_9.loc[39.2] = ['Mandaqui',0,0,0]
df_2021_0_9.loc[39.5] = ['Marsilac',0,0,0]
df_2021_0_9.loc[39.8] = ['Moema',0,0,0]
df_2021_0_9.loc[40.5] = ['Morumbi',0,0,0]
df_2021_0_9.loc[45.5] = ['Perdizes',0,0,0]
df_2021_0_9.loc[46.5] = ['Pinheiros',0,0,0]
df_2021_0_9.loc[52.5] = ['Santa Cecília',0,0,0]
df_2021_0_9.loc[54.5] = ['São Domingos',0,0,0]
df_2021_0_9.loc[60.5] = ['Sé',0,0,0]
df_2021_0_9.loc[61.5] = ['Tatuapé',0,0,0]
df_2021_0_9.loc[65.5] = ['Vila Formosa',0,0,0]
df_2021_0_9.loc[68.1] = ['Vila Maria',0,0,0]
df_2021_0_9.loc[68.2] = ['Vila Mariana',0,0,0]
df_2021_0_9.loc[68.8] = ['Vila Matilde',0,0,0]
df_2021_0_9.loc[68.9] = ['Vila Medeiros',0,0,0]
df_2021_0_9 = df_2021_0_9.sort_index()
df_2021_0_9.set_index('Distrito Admin residência',inplace=True)

col_names = []
for j in df_2021_0_9.columns:
    col_names.append('obitos' + '_' + str(2021) + '_' + 'total' + '_' + j + '_' + str(faixa_etaria[0]) + '_' + str(faixa_etaria[1]) + '_' + 'anos')
df_2021_0_9.set_axis(col_names, axis=1, inplace=True)

dfs.append(df_2021_0_9)

#10_19_anos
df_2021_10_19 = pd.read_csv(rf'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\obitos_total_distrito_2021\obitos_total_10_19_anos.csv',
                 sep = 'delimiter', encoding = 'Latin1',header = None)
df_2021_10_19 = df_2021_10_19.iloc[4:43,].reset_index(drop=True)
df_2021_10_19 = df_2021_10_19.rename(columns={0:'Name'})
df_2021_10_19 = df_2021_10_19.Name.str.split(';',expand = True).apply(lambda x:x.str.replace('"',""))
faixa_etaria = ls[1]
df_2021_10_19 = df_2021_10_19.rename(columns = df_2021_10_19.iloc[0]).drop(df_2021_10_19.index[0]) 
df_2021_10_19 = df_2021_10_19.iloc[:,:4]
df_index = pd.DataFrame({'Distrito Admin residência':df_2021_0_9.index})
df_2021_10_19 = pd.merge(df_index,df_2021_10_19,how='outer',left_on = 'Distrito Admin residência',right_on='Distrito Admin residência')
df_2021_10_19 = df_2021_10_19.fillna(0)
df_2021_10_19.set_index('Distrito Admin residência',inplace=True)

col_names = []
for j in df_2021_10_19.columns:
    col_names.append('obitos' + '_' + str(2021) + '_' + 'total' + '_' + j + '_' + str(faixa_etaria[0]) + '_' + str(faixa_etaria[1]) + '_' + 'anos')
df_2021_10_19.set_axis(col_names, axis=1, inplace=True)

dfs.append(df_2021_10_19)

#20_29_anos
df_2021_20_29 = pd.read_csv(rf'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\obitos_total_distrito_2021\obitos_total_20_29_anos.csv',
                 sep = 'delimiter', encoding = 'Latin1',header = None)
df_2021_20_29 = df_2021_20_29.iloc[4:79,].reset_index(drop=True)
df_2021_20_29 = df_2021_20_29.rename(columns={0:'Name'})
df_2021_20_29 = df_2021_20_29.Name.str.split(';',expand = True).apply(lambda x:x.str.replace('"',""))
faixa_etaria = ls[2]
df_2021_20_29 = df_2021_20_29.rename(columns = df_2021_20_29.iloc[0]).drop(df_2021_20_29.index[0]) 
df_2021_20_29 = df_2021_20_29.iloc[:,:4]
df_2021_20_29 = pd.merge(df_index,df_2021_20_29,how='outer',left_on = 'Distrito Admin residência',right_on='Distrito Admin residência')
df_2021_20_29 = df_2021_20_29.fillna(0)
df_2021_20_29.set_index('Distrito Admin residência',inplace=True)

col_names = []
for j in df_2021_20_29.columns:
    col_names.append('obitos' + '_' + str(2021) + '_' + 'total' + '_' + j + '_' + str(faixa_etaria[0]) + '_' + str(faixa_etaria[1]) + '_' + 'anos')
df_2021_20_29.set_axis(col_names, axis=1, inplace=True)

dfs.append(df_2021_20_29)

#30_39_anos
df_2021_30_39 = pd.read_csv(rf'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\obitos_total_distrito_2021\obitos_total_30_39_anos.csv',
                 sep = 'delimiter', encoding = 'Latin1',header = None)
df_2021_30_39 = df_2021_30_39.iloc[4:91,].reset_index(drop=True)
df_2021_30_39 = df_2021_30_39.rename(columns={0:'Name'})
df_2021_30_39 = df_2021_30_39.Name.str.split(';',expand = True).apply(lambda x:x.str.replace('"',""))
faixa_etaria = ls[3]
df_2021_30_39 = df_2021_30_39.rename(columns = df_2021_30_39.iloc[0]).drop(df_2021_30_39.index[0]) 
df_2021_30_39 = df_2021_30_39.iloc[:,:4]
df_2021_30_39 = pd.merge(df_index,df_2021_30_39,how='outer',left_on = 'Distrito Admin residência',right_on='Distrito Admin residência')
df_2021_30_39 = df_2021_30_39.fillna(0)
df_2021_30_39.set_index('Distrito Admin residência',inplace=True)

col_names = []
for j in df_2021_30_39.columns:
    col_names.append('obitos' + '_' + str(2021) + '_' + 'total' + '_' + j + '_' + str(faixa_etaria[0]) + '_' + str(faixa_etaria[1]) + '_' + 'anos')
df_2021_30_39.set_axis(col_names, axis=1, inplace=True)

dfs.append(df_2021_30_39)

#40_49_anos / 50_59_anos / 60_69_anos / 70_inf_anos
for i in ls[4:]:
    df = pd.read_csv(rf'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\obitos_total_distrito_2021\obitos_total_{i[0]}_{i[1]}_anos.csv',
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
        col_names.append('obitos' + '_' + str(2019) + '_' + 'total' + '_' + j + '_' + str(faixa_etaria[0]) + '_' + str(faixa_etaria[1]) + '_' + 'anos')
    df.set_axis(col_names, axis=1, inplace=True)
    dfs.append(df)

df_2021 = pd.concat(dfs,axis=1)


