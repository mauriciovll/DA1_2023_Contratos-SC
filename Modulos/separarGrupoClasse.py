import pandas as pd
import numpy as np
import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

df = pd.read_csv('datasets/ELIC_fornecedores_cadastro.csv')
df1 = df
df1[['Grupo','Classe','Descricao']] = df['produtos_habilitados'].str.split(' - ',2,expand=True)
df2 = df1
df2['Grupo1'] = df2['Grupo'].str[0:2]
df2['Grupo2'] = df2['Grupo'].str[2:]
df2.rename(columns={'Grupo':'Código GC'}, inplace=True)
df2['Grupo_desc'] = df2['Grupo1']+' - '+df2['Classe']
df2['Classe_desc'] = df2['Grupo2']+' - '+df2['Descricao']
df2.drop(columns=['Classe','Descricao','Grupo1','Grupo2'], inplace=True)
df2.rename(columns={'Grupo_desc':'Grupo','Classe_desc':'Classe'},inplace=True)
df2.to_csv('./Datasets/df2_fornecedores.csv', index=False)