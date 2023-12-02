import tkinter as tk
import os.path
from app import *
from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedStyle

def on_button_click():
    get_gs_data()

    permutas = ler_permutas()

    label2['textvariable'] = f"{permutas}"


root = Tk()
root.title("Exemplo com ThemedStyle")

style = ThemedStyle(root)
style.set_theme("plastik")

label_text = tk.StringVar()
label_text.set("Permutas")

label = Label(root, textvariable=label_text, wraplength=300, justify="center", font=("Helvetica", 12))
label.pack(pady=10)

button = Button(root, text="Obter permutas", command=on_button_click)
button.pack(pady=10)

label2 = Label(root, text='', wraplength=300, justify="center", font=("Helvetica", 12))
label2.pack(pady=10)

root.mainloop()
