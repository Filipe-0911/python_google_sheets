import tkinter as tk
from app import *
from classes.Crud import Crud
from tkinter import *
from ttkthemes import ThemedStyle

def on_button_click():
    get_permutas()

    conecta_permuta = Crud()
    conecta_permuta.conectar_banco()
    permutas = conecta_permuta.consultar_permutas()

    texto_completo = 'Permutas cadastradas no banco!'
    label2['text'] = texto_completo

    return permutas

def on_button_sdia_click():
    qtidadde_sdias = get_sdias()

    label2['text'] = f"{qtidadde_sdias} SDIA's registrados no banco"

root = tk.Tk()

style = ThemedStyle(root)
style.set_theme("equilux")

root.title("Permutas preenchidas")
largura_tela = 350
altura_tela = 1000

root.geometry(f"{largura_tela}x{altura_tela}")

root.configure(bg="#f0f0f0") 

largura_tela_real = root.winfo_screenwidth()
altura_tela_real = root.winfo_screenheight()
pos_x = (largura_tela_real - largura_tela) // 2
pos_y = (altura_tela_real - altura_tela) // 2
root.geometry(f"{largura_tela}x{altura_tela}+{pos_x}+{pos_y}")

label_text = tk.StringVar()
label_text.set("Permutas")

label = Label(root, textvariable=label_text, font=("Helvetica", 16), bg="#f0f0f0")
label.pack()

button_obter_permutas = Button(root, text="Obter permutas", command=on_button_click, font=("Helvetica", 12))
button_obter_permutas.pack(pady=10)

button_obter_sdia = Button(root, text="Obter SDIA", command=on_button_sdia_click, font=("Helvetica", 12))
button_obter_sdia.pack(pady=10)

label2 = Label(root, text='', font=("Helvetica", 8), wraplength=345, justify="center", bg="#f0f0f0")
label2.pack(pady=3)

root.mainloop()
