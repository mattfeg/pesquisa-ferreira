from CriarRede import CriarRedeNx, CriarRedeMatriz
import matplotlib.pyplot as plt

for ano in range(18, 19):
    for mes in range(1, 5):
        CriarRedeMatriz(f'./DadosSUS/CSV/RDCE{ano}{mes:02d}.csv')
        CriarRedeNx(f'./RedesMatriz/MatrizRDCE{ano}{mes:02d}.csv')
        
plt.show()