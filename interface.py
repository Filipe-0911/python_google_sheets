import tkinter as tk
from app import *
from classes.PermutasCrud import PermutasCrud
from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedStyle
#from ttkthemes import ThemedTk

def on_button_click():
    get_permutas()

    conecta_permuta = PermutasCrud()
    conecta_permuta.conectar_banco()
    permutas = conecta_permuta.consultar_permutas()

    print(permutas)

    # texto_permutas = []

    # for permuta in permutas:
    #     texto_permuta = (
    #         f"Data da troca: {permuta[1]} - "
    #         f"Proponente: {permuta[2]} - "
    #         f"Sai do turno: {permuta[3]} - "
    #         f"Entra no turno: {permuta[4]} - "
    #         f"Proposto: {permuta[5]} - "
    #         f"Sai do turno: {permuta[6]} - "
    #         f"Entra no turno: {permuta[7]} - "
    #     )

    #     texto_permutas.append(texto_permuta)

    # texto_completo = '\n\n'.join(texto_permutas)
    texto_completo = 'Permutas cadastradas no banco!'
    label2['text'] = texto_completo


def on_button_sdia_click():
    get_sdias()

    label2['text'] = 'SDIAS cadastradas no banco!'

root = tk.Tk()

style = ThemedStyle(root)
style.set_theme("equilux")

root.title("Permutas preenchidas")
largura_tela = 350
altura_tela = 1000

root.geometry(f"{largura_tela}x{altura_tela}")

# Adiciona uma cor de fundo
root.configure(bg="#f0f0f0")  # Substitua pela cor desejada em formato hexadecimal

# Centraliza o conteúdo na tela
largura_tela_real = root.winfo_screenwidth()
altura_tela_real = root.winfo_screenheight()
pos_x = (largura_tela_real - largura_tela) // 2
pos_y = (altura_tela_real - altura_tela) // 2
root.geometry(f"{largura_tela}x{altura_tela}+{pos_x}+{pos_y}")

label_text = tk.StringVar()
label_text.set("Permutas")

label = Label(root, textvariable=label_text, font=("Helvetica", 16), bg="#f0f0f0")
label.grid(row=0, column=0)

button_obter_permutas = Button(root, text="Obter permutas", command=on_button_click, font=("Helvetica", 12))
button_obter_permutas.grid(row=1, column=0, pady=10)

button_obter_sdia = Button(root, text="Obter SDIA", command=on_button_sdia_click, font=("Helvetica", 12))
button_obter_sdia.grid(row=1, column=2, pady=10)

# Adiciona wrap na label2 e uma cor de fundo
label2 = Label(root, text='', font=("Helvetica", 8), wraplength=345, justify="center", bg="#f0f0f0")
label2.grid(row=2, column=0, columnspan=2, pady=3)

root.mainloop()
