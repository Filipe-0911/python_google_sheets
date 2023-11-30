import os
import quickstart as main
from classes.Permutas import Permuta

LISTA_PERMUTAS = main.main()
del LISTA_PERMUTAS[0]


def insere_permutas(lista):
    for permuta in lista:
        troca = Permuta(permuta[0],permuta[1],permuta[2],permuta[3],permuta[4],permuta[5], permuta[6])
        teste = troca.detalhar()
        troca.inserir()


def ler_permutas():
    lista = Permuta.listarTodos()
    print(lista)

insere_permutas(LISTA_PERMUTAS)