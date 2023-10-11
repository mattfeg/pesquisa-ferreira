# CRIAR REDE DE MOVIMENTAÇÃO DAS AIH

# ENTRADA: CSV com os Municípios de Residência e Hospitais de Internação

# SAÍDA: Um arquivo CSV com os nós da Rede;
# Um arquivo CSV com as arestas da Rede;
# e a Rede montada no Networkx.

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

figuras = []
def CriarRedeNx(caminho_csv): # Informar o caminho no seguinte formato './RedesCSV/xxxx.csv'
    df = pd.read_csv(caminho_csv, sep=',', encoding='Latin1',index_col='CNES')
    rede = nx.DiGraph()
    for municipio in df.columns:
        for hospital in df.index:
            rede.add_edge(municipio, hospital, weight=df[municipio][hospital])
    figuras.append(plt.figure(figsize=(10,10)))
    nx.draw(rede, with_labels=True)
    #plt.show()
    print("Quantidade de Nós: ", len(rede.nodes()))
    print("Quantidade de Arestas: ", len(rede.edges()))

def CriarRedeMatriz(caminho_csv): # Informar o caminho no seguinte formato './DadosSUS/CSV/xxxx.csv'
    df = pd.read_csv(caminho_csv, sep=',', encoding='Latin1')

    #Filtro para câncer de pulmão
    df = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])]
    
    # Lendo os arquivos CSV de CNES e MUNICS
    dfcnes = pd.read_csv('./DadosSUS/CNESBR.csv', sep=',', encoding='Latin1')
    dfmunics = pd.read_csv('./DadosSUS/MUNICSBR.csv', sep=',')
    
    # Procura o nome do hospital pelo código CNES e substitui o código pelo nome
    df['CNES'] = df['CNES'].map(dfcnes.set_index('CNES')['NOMEFANT'])
    df['MUNIC_RES'] = df['MUNIC_RES'].map(dfmunics.set_index('COD')['MUNIC'])

    tabela_cruzada = pd.crosstab(df['CNES'] , df['MUNIC_RES'])
    tabela_cruzada.to_csv(f'./RedesMatriz/Matriz{caminho_csv.split('/')[-1].split('.')[0]}.csv', index=True, header=True)
