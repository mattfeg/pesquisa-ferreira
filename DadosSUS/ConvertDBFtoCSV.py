from dbfread import DBF
import pandas as pd

# Lista de anos e meses
anos = [str(ano)[2:] for ano in range(2015, 2018)]  # de "18" a "22"
meses = [f"{i:02d}" for i in range(1, 13)]  # de "01" a "12"

# Lista para armazenar DataFrames temporários
dfs = []
print("Iniciando a leitura dos arquivos...")
# Loop para ler os arquivos
for ano in anos:
    for mes in meses:
        try:
            print(f'Lendo arquivo {ano}{mes}...')
            dbf = DBF(f"./DadosSUS/DBF/RDCE{ano}{mes}.dbf")
            df_temp = pd.DataFrame(iter(dbf))
            dfs.append(df_temp)
            df_temp.to_csv(f"./DadosSUS/CSV/RDCE{ano}{mes}.csv", index=False)
        except:
            print(f"Arquivo {ano}{mes} não encontrado.")
        else:
            print(f"Arquivo {ano}{mes} concluido.")

# Concatenando todos os DataFrames em um único DataFrame
print("Concatenando os DataFrames...")
df_final = pd.concat(dfs, ignore_index=True)

# Mostrando o DataFrame final
print(df_final)