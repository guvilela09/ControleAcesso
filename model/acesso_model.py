import pandas as pd
import os

ARQUIVO_DADOS = "data/acessos.xlsx"

class AcessoModel:
    def __init__(self):
        self.df = pd.DataFrame(columns=["Nome", "CPF", "RG", "Empresa", "Responsável", "Data/Hora"])
        if os.path.exists(ARQUIVO_DADOS):
            self.df = pd.read_excel(ARQUIVO_DADOS)

    def adicionar(self, dados):
        self.df.loc[len(self.df)] = dados
        self.salvar_dados()

    def remover(self, cpf):
        if cpf in self.df['CPF'].values:
            self.df = self.df[self.df["CPF"] != cpf].reset_index(drop=True)
            self.salvar_dados()
        else:
            print(f"CPF {cpf} não encontrado para remoção.")


    def salvar_dados(self):
        os.makedirs("data", exist_ok=True)
        self.df.to_excel(ARQUIVO_DADOS, index=False)  # Garante que os dados sejam salvos

    def carregar_dados(self):
        return self.df.copy()

    def importar(self, arquivo):
        df = pd.read_excel(arquivo)
        self.df = df
        self.salvar_dados()
        return df

    def exportar(self, arquivo, df):
        df.to_excel(arquivo, index=False)

    def atualizar(self, cpf_antigo, novos_dados):
        idx = self.df[self.df["CPF"] == cpf_antigo].index
        if not idx.empty:
            for col, valor in zip(self.df.columns, novos_dados):
                self.df.at[idx[0], col] = valor
            self.salvar_dados()
        else:
            print(f"CPF {cpf_antigo} não encontrado para atualizar.")




        