from CriarRede import CriarRedeNx, CriarRedeMatriz, grau_medio_por_mes, densidade_por_mes, quantidade_de_nos_por_mes, quantiodade_de_arestas_por_mes 
import matplotlib.pyplot as plt

Plots = 0
for ano in range(18, 19):
    for mes in range(1, 4):
        CriarRedeMatriz(f'./DadosSUS/CSV/RDCE{ano}{mes:02d}.csv')
        CriarRedeNx(f'./RedesMatriz/MatrizRDCE{ano}{mes:02d}.csv')
        Plots += 1
        
#plt.show()
print("Graus por mês: ", grau_medio_por_mes)
print("Densidade por mês: ", densidade_por_mes)
print("Quantidade de nós por mês: ", quantidade_de_nos_por_mes)
print("Quantidade de arestas por mês: ", quantiodade_de_arestas_por_mes)

#plotar histograma de graus por mês
plt.title("Grau médio por mês")
plt.plot(range(1, Plots),grau_medio_por_mes)
plt.show()

#plotar histograma de densidade por mês
plt.title("Densidade por mês")
plt.plot(range(1, Plots),densidade_por_mes)
plt.show()

#plotar histograma de quantidade de nós por mês
plt.title("Nós por mês")
plt.plot(range(1, Plots),quantidade_de_nos_por_mes)
plt.show()

#plotar histograma de quantidade de arestas por mês
plt.title("Arestas por mês")
plt.plot(range(1, Plots),quantiodade_de_arestas_por_mes)
plt.show()