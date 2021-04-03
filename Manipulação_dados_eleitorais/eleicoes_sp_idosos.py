import pandas as pd 

dados_18 = pd.read_csv(r'C:\Users\guilh\Documents\perfil_eleitorado_2018.csv',
                       sep = ';', encoding = 'Latin1')

df = dados_18[dados_18['NM_MUNICIPIO'] == 'SÃO PAULO']

df = df[['NR_ZONA','CD_FAIXA_ETARIA','QT_ELEITORES_PERFIL']]

df['CD_FAIXA_ETARIA'].value_counts()

# Retirando as observações que não especificaram a faixa etária
# N retirado = 91
df = df[df.CD_FAIXA_ETARIA != -3]

#Obtendo o total de eleitores por ZE e faixa etária
df = df.groupby(['NR_ZONA','CD_FAIXA_ETARIA']).sum().reset_index()

#Obtendo o número de idosos (>=60 anos) por ZE
d = {}
for i in df['NR_ZONA'].unique():
    n_idoso = df[(df['NR_ZONA'] == i) & (df['CD_FAIXA_ETARIA'] >= 6064)].sum()['QT_ELEITORES_PERFIL']
    d[i] = n_idoso

df_aux = pd.DataFrame(data=d,index=['N_IDOSOS']).T
df_aux['N_ELEITORES'] = df.groupby('NR_ZONA').sum()['QT_ELEITORES_PERFIL']
df_aux['% de idosos'] = df_aux['N_IDOSOS']/df_aux['N_ELEITORES']
df_aux = df_aux.reset_index().rename(columns={'index':'NR_ZONA'})

