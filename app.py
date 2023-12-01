import os
import quickstart as main
from classes.Permutas import Permuta

LISTA_PERMUTAS = main.main()
del LISTA_PERMUTAS[0]
index = 2

def insere_permutas(lista):
    for permuta in lista:
        troca = Permuta(permuta[0],permuta[1],permuta[3],permuta[2],permuta[4],permuta[6], permuta[5])
        teste = troca.detalhar()
        troca.inserir()

def ler_permutas():
    lista = Permuta.lerArquivo()
    print(lista)

def excluir_permuta(selecionado):
    item_selecionado = int(selecionado)
    Permuta.excluir(item_selecionado)

excluir_permuta(0)

