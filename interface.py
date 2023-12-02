import tkinter as tk
import os.path
from app import *
from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedStyle
from ttkthemes import ThemedTk

def on_button_click():
    get_gs_data()

    permutas = ler_permutas()
    texto_permutas = []

    for permuta in permutas:
        texto_permuta = (
            f"Data da troca: {permuta['data_da_troca']} - "
            f"Proponente: {permuta['proponente']} - "
            f"Sai do turno: {permuta['proponente_sai_do_turno']} - "
            f"Entra no turno: {permuta['proponente_entra_no_turno']} - "
            f"Proposto: {permuta['proposto']} - "
            f"Sai do turno: {permuta['proposto_sai_do_turno']} - "
            f"Entra no turno: {permuta['proposto_entra_no_turno']} - "
        )

        texto_permutas.append(texto_permuta)

    texto_completo = '\n\n'.join(texto_permutas)
    label2['text'] = texto_completo


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

label2 = Label(root, text='', wraplength=700, justify="center", font=("Helvetica", 10))
label2.pack(pady=10)

root.mainloop()
