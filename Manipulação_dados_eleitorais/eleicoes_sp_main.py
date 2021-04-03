import pandas as pd

df_main = pd.merge(dados_ZE_sp,df_aux,on='NR_ZONA')
df_main = df_main[['NR_ZONA','NR_PARTIDO','% de votos no partido','% de idosos']]

df_main.to_csv(r'C:\Users\guilh\Documents\perfil_eleitorado_2018_main.csv')