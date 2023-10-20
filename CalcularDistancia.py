import googlemaps
import networkx as nx
import pandas as pd

api_key = "--"
gmaps = googlemaps.Client(key=api_key)

def buscarDistância(aresta):
    origem = aresta[0]
    destino = aresta[1]
    matrix = gmaps.distance_matrix(origem, destino)["rows"][0]["elements"][0]

    # Verifique se a solicitação foi bem-sucedida
    if matrix["status"] == "OK":
        distancia = matrix["distance"]["text"]
        duracao = matrix["duration"]["text"]
        print(f"A distância entre {origem} e {destino} é de {distancia}.")
        print(f"A duração estimada da viagem é de {duracao}.\n")
        return distancia,duracao
        
    else:
        print("Não foi possível calcular a distância.")
        return None,None

df = pd.read_csv("./RedesMatriz/MatrizRDCE1501.csv", sep=',', encoding='Latin1',index_col='CNES')
rede = nx.DiGraph()
for municipio in df.columns:
    for hospital in df.index:
            rede.add_edge(municipio, hospital, weight=df[municipio][hospital])
            
#Plotar Arestas e suas propriedades
dfarestas = pd.DataFrame(columns=['Source', 'Target', 'Weight','Distancia','Duracao'])
for aresta in rede.edges():
    if aresta['weight'] > 0:
        distancia,duracao = buscarDistância([municipio, hospital])
        dfarestas = pd.concat([dfarestas, pd.DataFrame({'Source': aresta[0], 'Target': aresta[1], 'Weight': rede[aresta[0]][aresta[1]]['weight'],'Distancia':rede[aresta[0]][aresta[1]]['distancia'],'Duracao':rede[aresta[0]][aresta[1]]['duracao']}, index=[0])], ignore_index=True)
print(dfarestas)
