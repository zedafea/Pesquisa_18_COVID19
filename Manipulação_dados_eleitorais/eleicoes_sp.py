import pandas as pd

dados_18 = pd.read_csv(r'C:\Users\guilh\Documents\votacao_partido_munzona_2018_BRASIL.csv',
                       sep = ';', encoding = 'Latin1')

#O df possui os dados das eleições para presidência?
dados_18['DS_ELEICAO'].value_counts()

#Selecionando só os dados das Eleições Presidenciais
dados_18 = dados_18[dados_18['DS_ELEICAO'] == 'Eleição Geral Federal 2018']

#Verificando se possui todos os estados
dados_18['SG_UF'].value_counts()

#Selecionado só para o estado de SP
dados_18_sp = dados_18[dados_18['SG_UF'] == 'SP']

#Verificando os municípios disponíveis
dados_18_sp['NM_MUNICIPIO'].value_counts()

#Selecionando o município de SP
dados_18_sp = dados_18_sp[dados_18_sp['NM_MUNICIPIO'] == 'SÃO PAULO']

#Verificando o turno
dados_18_sp['NR_TURNO'].value_counts()

#Selecionando só o segundo turno
dados_18_sp = dados_18_sp[dados_18_sp['NR_TURNO'] == 2]

#Verificação
dados_18_sp['NR_PARTIDO'].value_counts()

#Selecionando as colunas de nosso interesse
dados_18_sp = dados_18_sp[['NR_ZONA','NR_PARTIDO','QT_VOTOS_NOMINAIS']]

#Pegando o número total de pessoas que votaram ou no PT ou no PSL por ZE
ZE_PSL_PT = dados_18_sp.groupby('NR_ZONA').sum().reset_index()[['NR_ZONA','QT_VOTOS_NOMINAIS']]

#df com ambas as informações
dados_ZE_sp = pd.merge(dados_18_sp,ZE_PSL_PT, on = 'NR_ZONA')

#Criando uma coluna com a % de voto em cada partido por ZE
dados_ZE_sp['% de votos no partido'] = dados_ZE_sp['QT_VOTOS_NOMINAIS_x']/dados_ZE_sp['QT_VOTOS_NOMINAIS_y']

#Selecionando as colunas de nosso interesse
dados_ZE_sp = dados_ZE_sp[['NR_ZONA','NR_PARTIDO','% de votos no partido']]
