import tkinter as tk
from app import *
from classes.PermutasCrud import PermutasCrud
from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedStyle
from ttkthemes import ThemedTk

def on_button_click():
    get_permutas()

    conecta_permuta = PermutasCrud()
    conecta_permuta.conectar_banco()
    permutas = conecta_permuta.consultar_permutas()

    print(permutas)

    texto_permutas = []

    for permuta in permutas:
        texto_permuta = (
            f"Data da troca: {permuta[1]} - "
            f"Proponente: {permuta[2]} - "
            f"Sai do turno: {permuta[3]} - "
            f"Entra no turno: {permuta[4]} - "
            f"Proposto: {permuta[5]} - "
            f"Sai do turno: {permuta[6]} - "
            f"Entra no turno: {permuta[7]} - "
        )

        texto_permutas.append(texto_permuta)

    texto_completo = '\n\n'.join(texto_permutas)
    label2['text'] = texto_completo


def on_button_sdia_click():
    get_sdias()

    label2['text'] = 'SDIAS cadastrados no banco!'
    
root = Tk()

style = ThemedStyle(root)
style.set_theme("blue")

root.title("Permutas preenchidas")
largura_tela = 800
altura_tela = 1000

root.geometry(f"{largura_tela}x{altura_tela}")

label_text = tk.StringVar()
label_text.set("Permutas")

label = Label(root, textvariable=label_text, wraplength=300, justify="center", font=("Helvetica", 12))
label.pack(pady=10)

button = Button(root, text="Obter permutas", command=on_button_click)
button.pack(pady=10)

button = Button(root, text="Obter SDIA", command=on_button_sdia_click)
button.pack(pady=10)

label2 = Label(root, text='', wraplength=700, justify="center", font=("Helvetica", 10))
label2.pack(pady=10)

root.mainloop()
