# CRIAR REDE DE MOVIMENTAÇÃO DAS AIH
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

figuras = []
grau_medio_por_mes = []
densidade_por_mes = []
quantidade_de_nos_por_mes = []
quantiodade_de_arestas_por_mes = []


def CriarRedeNx(caminho_csv): # Informar o caminho no seguinte formato './RedesCSV/xxxx.csv'
    df = pd.read_csv(caminho_csv, sep=',', encoding='Latin1',index_col='CNES')
    rede = nx.DiGraph()
    for municipio in df.columns:
        for hospital in df.index:
            rede.add_edge(municipio, hospital, weight=df[municipio][hospital])
    
    #Plotar Rede
    #figuras.append(plt.figure(figsize=(10,10)))
    #nx.draw(rede,with_labels=True)
    #plt.show()

    print("-------------------------")
    print("Rede: ", caminho_csv.split('/')[-1].split('.')[0])
    print("Quantidade de Nós: ", len(rede.nodes()))
    print("Quantidade de Arestas: ", len(rede.edges()))
    print("Densidade: ", nx.density(rede))
    print("Grau médio dos nós: ", np.mean([d for n, d in rede.degree()]))

    grau_medio_por_mes.append(np.mean([d for n, d in rede.degree()]))
    densidade_por_mes.append(nx.density(rede))
    quantidade_de_nos_por_mes.append(len(rede.nodes()))
    quantiodade_de_arestas_por_mes.append(len(rede.edges()))

    dfarestas = pd.DataFrame(columns=['Source', 'Target', 'Weight'])
    for aresta in rede.edges():
        dfarestas = pd.concat([dfarestas, pd.DataFrame({'Source': aresta[0], 'Target': aresta[1], 'Weight': rede[aresta[0]][aresta[1]]['weight']}, index=[0])], ignore_index=True)
    print(dfarestas)
    
    #Remover Arestas com peso 0
    #for aresta in rede.edges():
    #    if rede[aresta[0]][aresta[1]]['weight'] == 0:
    #        rede.remove_edge(aresta[0], aresta[1])

def CriarRedeMatriz(caminho_csv): # Informar o caminho no seguinte formato './DadosSUS/CSV/xxxx.csv'
    df = pd.read_csv(caminho_csv, sep=',', encoding='Latin1')

    df = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])]
    
    dfcnes = pd.read_csv('./DadosSUS/CNESBR.csv', sep=',', encoding='Latin1')
    dfmunics = pd.read_csv('./DadosSUS/MUNICSBR.csv', sep=',')
    
    df['CNES'] = df['CNES'].map(dfcnes.set_index('CNES')['NOMEFANT'])
    df['MUNIC_RES'] = df['MUNIC_RES'].map(dfmunics.set_index('COD')['MUNIC'])

    tabela_cruzada = pd.crosstab(df['CNES'] , df['MUNIC_RES'])
    tabela_cruzada.to_csv(f"./RedesMatriz/Matriz{caminho_csv.split('/')[-1].split('.')[0]}.csv", index=True, header=True)
