
import pandas as pd

def carregar_excel(caminho):
    return pd.read_excel(caminho)

def salvar_excel(df, caminho):
    df.to_excel(caminho, index=False)
