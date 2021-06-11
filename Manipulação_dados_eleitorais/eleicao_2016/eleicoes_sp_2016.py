# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 09:43:25 2021

@author: guilh
"""

import pandas as pd

df = pd.read_csv(r'\votacao_secao_2016_SP.txt',
                 sep = ';', encoding = 'Latin1')
df.iloc[0] = df.columns
df.set_axis(['DATA_GERACAO','HORA_GERACAO','ANO_ELEICAO','NUM_TURNO','DESCRICAO_ELEICAO','SIGLA_UF',
              'SIGLA_UE','CODIGO_MUNICIPIO','NOME_MUNICIPIO','NUM_ZONA','NUM_SECAO','CODIGO_CARGO',
              'DESCRICAO_CARGO','NUM_VOTAVEL','QTDE_VOTOS'],axis=1,inplace=True)
df_SP = df[df['NOME_MUNICIPIO'] == 'SÃO PAULO']
df_SP = df_SP[df_SP['DESCRICAO_CARGO'] == 'PREFEITO']

df_total = df_SP.groupby(['NUM_ZONA','NUM_SECAO']).sum().reset_index()[['NUM_ZONA','NUM_SECAO','QTDE_VOTOS']]

df_45 = df_SP[df_SP['NUM_VOTAVEL'] == 45].groupby(['NUM_ZONA','NUM_SECAO']).sum().reset_index()[['NUM_ZONA','NUM_SECAO','QTDE_VOTOS']]

df = pd.merge(df_total,df_45,how='left',on=['NUM_ZONA','NUM_SECAO']).fillna(0)

df['QTDE_VOTOS_x'] = df['QTDE_VOTOS_x'].astype('float64') 
df['votos_2016_Doria_1_percentual'] = df['QTDE_VOTOS_y']/df['QTDE_VOTOS_x']

df.to_excel(r'\eleicao_16_sp_ZE_SE.xlsx',index=False)
