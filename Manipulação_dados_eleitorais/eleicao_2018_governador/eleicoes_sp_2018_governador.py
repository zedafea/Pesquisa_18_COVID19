# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 10:14:52 2021

@author: guilh
"""

import pandas as pd

df = pd.read_csv(r'\votacao_secao_2018_SP.csv',
                 sep = ';', encoding = 'Latin1', chunksize= 10000)

dfs = []
for df in df:
    df = df[(df['NM_MUNICIPIO'] == 'SÃO PAULO')&(df['DS_CARGO'] == 'GOVERNADOR')]
    dfs.append(df)
    
df_SP = pd.concat(dfs)

df_SP_1 = df_SP[df_SP['NR_TURNO'] == 1]    

df_total_1 = df_SP_1.groupby(['NR_ZONA','NR_SECAO']).sum().reset_index()[['NR_ZONA','NR_SECAO','QT_VOTOS']]

df_45_1 = df_SP_1[df_SP_1['NR_VOTAVEL'] == 45].groupby(['NR_ZONA','NR_SECAO']).sum().reset_index()[['NR_ZONA','NR_SECAO','QT_VOTOS']]

df_1 = pd.merge(df_total_1,df_45_1,how='left',on=['NR_ZONA','NR_SECAO']).fillna(0)
df_1['votos_2018_Doria_1_percentual'] = df_1['QT_VOTOS_y']/df_1['QT_VOTOS_x']

df_1.to_excel(r'\eleicao_18_sp_ZE_SE_1_governador.xlsx',index=False)

df_SP_2 = df_SP[df_SP['NR_TURNO'] == 2]    

df_total_2 = df_SP_2.groupby(['NR_ZONA','NR_SECAO']).sum().reset_index()[['NR_ZONA','NR_SECAO','QT_VOTOS']]

df_45_2 = df_SP_2[df_SP_2['NR_VOTAVEL'] == 45].groupby(['NR_ZONA','NR_SECAO']).sum().reset_index()[['NR_ZONA','NR_SECAO','QT_VOTOS']]

df_2 = pd.merge(df_total_2,df_45_2,how='left',on=['NR_ZONA','NR_SECAO']).fillna(0)
df_2['votos_2018_Doria_2_percentual'] = df_2['QT_VOTOS_y']/df_2['QT_VOTOS_x']

df_2.to_excel(r'\eleicao_18_sp_ZE_SE_2_governador.xlsx',index=False)

