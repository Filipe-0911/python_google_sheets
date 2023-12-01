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
    lista = Permuta.listarTodos()
    print(lista)

def excluir_permuta(selecionado):
    item_selecionado = int(selecionado)
    Permuta.excluir(item_selecionado)

def alterar_permuta(selecionado, item_alterar, novo_valor):

    item_selecionado = int(selecionado)
    item = Permuta.lerArquivo(item_selecionado)
    print(item)

    match item_alterar:
        case 'data_da_troca' : 
            permuta = Permuta(novo_valor, item['proponente'], item['proponente_sai_do_turno'], item['proponente_entra_no_turno'], item['proposto'], item['proposto_sai_do_turno'], item['proposto_entra_no_turno'])

        case 'proponente' : 
            permuta = Permuta(item['data_da_troca'], novo_valor, item['proponente_sai_do_turno'], item['proponente_entra_no_turno'], item['proposto'], item['proposto_sai_do_turno'], item['proposto_entra_no_turno'])

        case 'proponente_sai_do_turno' : 
            permuta = Permuta(item['data_da_troca'], item['proponente'], novo_valor, item['proponente_entra_no_turno'], item['proposto'], item['proposto_sai_do_turno'], item['proposto_entra_no_turno'])

        case 'proponente_entra_no_turno' : 
            permuta = Permuta(item['data_da_troca'], item['proponente'], item['proponente_sai_do_turno'], novo_valor, item['proposto'], item['proposto_sai_do_turno'], item['proposto_entra_no_turno'])

        case 'proposto' : 
            permuta = Permuta(item['data_da_troca'], item['proponente'], item['proponente_sai_do_turno'], item['proponente_entra_no_turno'], novo_valor, item['proposto_sai_do_turno'], item['proposto_entra_no_turno'])

        case 'proposto_sai_do_turno' : 
            permuta = Permuta(item['data_da_troca'], item['proponente'], item['proponente_sai_do_turno'], item['proponente_entra_no_turno'], item['proposto'], novo_valor, item['proposto_entra_no_turno'])

        case 'proposto_entra_no_turno' : 
            permuta = Permuta(item['data_da_troca'], item['proponente'], item['proponente_sai_do_turno'], item['proponente_entra_no_turno'], item['proposto'], item['proposto_sai_do_turno'], novo_valor)

    
    permuta.alterar(item_selecionado)


# insere_permutas(LISTA_PERMUTAS)
# ler_permutas()
# excluir_permuta(0)
# alterar_permuta(0, 'proponente', 'SO GODOY')