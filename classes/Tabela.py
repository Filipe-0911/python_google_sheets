import tkinter as tk

class TabelaTkinter:
    def __init__(self, root, linhas, colunas=7):
        self.linhas = linhas
        self.colunas = colunas
        self.root = root
        self.criar_tabela()

    def criar_tabela(self):
        self.caixas_entrada = []

        for j in range(self.colunas):
            label = tk.Label(self.root, text=f"Coluna {j + 1}", borderwidth=1, relief="solid", width=12)
            label.grid(row=2, column=j)

        for i in range(3, self.linhas + 3):
            linha_caixas_entrada = []
            for j in range(self.colunas):
                entry = tk.Entry(self.root, width=12)
                entry.grid(row=i, column=j)
                linha_caixas_entrada.append(entry)
            self.caixas_entrada.append(linha_caixas_entrada)