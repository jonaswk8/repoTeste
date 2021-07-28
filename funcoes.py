#Arquivo de funcoes para projeto neoway
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#funcao para importacao de arquivos csv

#argumentos:

#dir --> diretorio onde esta o arquivo csv
#file_name --> nome do arquivo csv
#sep --> delimiter
def importa_csv(dir,file_name,sep):
    
    #cria caminho completo para o arquivo
    full_dir = os.path.join(dir,file_name)
    
    #realiza leitura com pandas
    out_df = pd.read_csv(full_dir,sep=sep)

    return out_df


#funcao para plot de correlacao

#argumentos:
#df --> dataframe contendos os dados que se deseja plotar as correlacoes
#vars --> lista contendo as variaveis que se desejas plotar as correlacoes
#annot --> booelana para indicar se plota os valores no plot ou nao

def corr_plot(df,vars,annot):
    
    #calcula correlacoes
    corr = df[vars].corr()
    
    #mascara
    mask = np.zeros_like(corr,dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    #configura area de plotagem
    f, ax = plt.subplots(figsize=(11,9))

    #definindo mapa de cores
    cmap = sns.diverging_palette(10,240, as_cmap=True)

    #desenhando o mapa de calor das correlacoes
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, center=0, vmin=-1, annot=annot, square=True,fmt='.1f', linewidths=.5, cbar_kws={"shrink": .5})


#funcao para binarizar variaveis categoricas

#df --> dataframe contendo os dados que se deseja binarizar
#vars --> lista contendo as colunas que se deseja binarizar
#prefixos --> lista de prefixos desejavel para as variaveis binarias a serem criadas

#retorna  df como novas colunas binarizadas

def binarizar(df,vars,prefixos):

    for i in range(0,len(vars)):
        #gera dummies
        dummies = pd.get_dummies(df[vars[i]], dummy_na=True, prefix = prefixos[i])
        
        #concatena dummies no dataframe original
        df = pd.concat([df,dummies],axis = 1, sort=False)

    return df


#funcao para substituicao de dados missing pela media ou moda

#df --> dataframe contendo os dados que se deseja tratar os dados missing
#variaveis --> lista contendo os dados que se deseja substituir os missing pela media
#tipo --> recebe media para tratar dados missing pela media e moda para tratar dados missing pela moda

def trata_missing(df,vars,tipo):

    #trata pela media
    if tipo=='media':
        print('substituindo pela media')
        for i in vars:
            print('tratando:',i)
            df['{}'.format(i)] = df['{}'.format(i)].fillna(df['{}'.format(i)].mean())

        
        
    else:
        #trata pela moda
        if tipo=='moda':
            print('substituindo pela moda')
            for i in vars:
                print('tratando',i)
                df['{}'.format(i)] = df['{}'.format(i)].fillna(df['{}'.format(i)].mode()[0])
            
        else:
            print('tratamento nao efetuado. Por favor colocar media ou moda no argumento tipo.')