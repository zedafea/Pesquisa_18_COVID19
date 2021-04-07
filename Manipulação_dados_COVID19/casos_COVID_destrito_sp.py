# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:28:33 2021

@author: guilh
"""

import pandas as pd

ls = [['marco',20],['abril',20],['maio',20],['junho',20],['julho',20],['agosto',20],
      ['setembro',20],['outubro',20],['novembro',20],['dezembro',20],['janeiro',21],
      ['fevereiro',21],['marco',21]]

dfs = []
for i in ls:
    df = pd.read_csv(rf'C:\Users\guilh\Documents\Apoio_p_18_COVID19_\casos_destrito_{i[0]}_{i[1]}.csv',
                encoding = 'Latin1', sep='delimiter', header=None )
    df = df.iloc[3:9,]
    df = df.rename(columns={0:'Name'})
    df = df.Name.str.split(';',expand = True)
    df = df.rename(columns = df.iloc[0]).drop(df.index[0])           
    dfs.append(df)
df = pd.concat(dfs)
df.set_index(df.iloc[:,0],inplace = True)  
df = df.iloc[:,1:]
df = df.replace('-',0)
df = df.fillna(0)
df = df.apply(pd.to_numeric)

Distrito = []
Caso_Confirmado_Covid_19 = []
Caso_Descartado = []
Síndrome_Gripal = []
Ignorado = []
Total = []
for j in df.columns:
    Distrito.append(j)
    Caso_Confirmado_Covid_19.append(df.loc['"Caso confirmado de Covid-19"',f'{j}'].sum())
    Caso_Descartado.append(df.loc['"Caso Descartado"',f'{j}'].sum())
    Síndrome_Gripal.append(df.loc['"Síndrome Gripal"',f'{j}'].sum())
    Ignorado.append(df.loc['"Ignorado"',f'{j}'].sum())
    Total.append(df.loc['"Total"',f'{j}'].sum())

df_total = pd.DataFrame([Distrito,Caso_Confirmado_Covid_19,Caso_Descartado,
                        Síndrome_Gripal,Ignorado,Total]).T
df_total = df_total.rename(columns={0: 'Distrito',
                                    1:'Casos confirmados de Covid-19',
                                    2:"Caso Descartado",
                                    3:"Síndrome Gripal",
                                    4:"Ignorado",
                                    5:"Total"})
df_total['Distrito'] = df_total.Distrito.str.replace('"'," ")
df_total.set_index(df_total.iloc[:,0],inplace=True)
df_total = df_total.iloc[:,1:]

