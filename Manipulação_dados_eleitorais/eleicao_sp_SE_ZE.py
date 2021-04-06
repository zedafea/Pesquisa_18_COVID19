import pandas as pd

#Zona,seção e voto

#Importação
df = pd.read_csv('votacao_secao_2018_BR.csv',
                 sep = ';', encoding = 'Latin1')
#Filtrando para o município de SP capital e para eleições presidenciais
df_sp = df[df['NM_MUNICIPIO'] == 'SÃO PAULO']
#Checagens
[df_sp[x].value_counts() for x in df_sp.columns[:21]]
#Selecionando as colunas de nosso interesse
df_sp = df_sp[['NR_TURNO','NR_ZONA','NR_SECAO','NR_VOTAVEL',
               'QT_VOTOS']].reset_index(drop=True)

#Selecionando o 1º Turno
df_sp_1 = df_sp[df_sp['NR_TURNO'] == 1]
#Total de votos por ZE e SE
df_total = df_sp_1.groupby(['NR_ZONA','NR_SECAO']).sum().reset_index()[['NR_ZONA',
                                                                        'NR_SECAO',
                                                                        'QT_VOTOS']]
#Total de votos no Bolsonaro por ZE e SE
df_17 = df_sp_1[df_sp_1['NR_VOTAVEL'] == 17].groupby(['NR_ZONA','NR_SECAO']).sum().reset_index()[['NR_ZONA',
                                                             'NR_SECAO',
                                                             'QT_VOTOS']]
#Checagens
df_total[df_total['QT_VOTOS'] <= 0]
df_17[df_17['QT_VOTOS'] <= 0]
#Juntando os dfs
df_main = pd.merge(df_17,df_total,on=['NR_ZONA','NR_SECAO'])
df_main['% de votos no Bolsonaro'] = df_main['QT_VOTOS_x']/df_main['QT_VOTOS_y']
df_main = df_main[['NR_ZONA','NR_SECAO','% de votos no Bolsonaro']]
df_main['NR_TURNO'] = 1

#Selecionando o 2º Turno
df_sp_2 = df_sp[df_sp['NR_TURNO'] == 2]
#Total de votos por ZE e SE
df_total_2 = df_sp_2.groupby(['NR_ZONA','NR_SECAO']).sum().reset_index()[['NR_ZONA',
                                                                        'NR_SECAO',
                                                                        'QT_VOTOS']]
#Total de votos no Bolsonaro por ZE e SE
df_17_2 = df_sp_2[df_sp_2['NR_VOTAVEL'] == 17].groupby(['NR_ZONA','NR_SECAO']).sum().reset_index()[['NR_ZONA',
                                                             'NR_SECAO',
                                                             'QT_VOTOS']]
#Checagens
df_total_2[df_total_2['QT_VOTOS'] <= 0]
df_17_2[df_17_2['QT_VOTOS'] <= 0]
#Juntando os dfs
df_main_2 = pd.merge(df_17_2,df_total_2,on=['NR_ZONA','NR_SECAO'])
df_main_2['% de votos no Bolsonaro'] = df_main_2['QT_VOTOS_x']/df_main_2['QT_VOTOS_y']
df_main_2 = df_main_2[['NR_ZONA','NR_SECAO','% de votos no Bolsonaro']]
df_main_2['NR_TURNO'] = 2

#Unindo em um único main
dfMain = pd.merge(df_main,df_main_2,on=['NR_ZONA','NR_SECAO'],suffixes=('1º_Turno',
dfMain = dfMain[['NR_ZONA','NR_SECAO','% de votos no Bolsonaro1º_Turno', '% de votos no Bolsonaro2º_Turno']]

#Exportando para csv
dfMain.to_csv('eleicao_18_sp_ZE_SE.csv')
