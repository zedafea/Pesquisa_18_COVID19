import pandas as pd

df = pd.read_excel(r'C:\Users\guilh\Documents\7_populacao_residente_por_grupos_de_idade__2017_595.xls')
df = df.rename(columns=df.iloc[3])
df = df.iloc[3:,].reset_index(drop=True)



