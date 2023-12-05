import quickstart as main
from classes.Permutas import Permuta
from classes.Sdia import Sdia

def get_gs_data2():
    LISTA_PERMUTAS = main.main()
    del LISTA_PERMUTAS[0]

    for sdia in LISTA_PERMUTAS:
        dados_sdia = Sdia(sdia[0],sdia[1],sdia[2],sdia[6],
                     sdia[7],sdia[8],sdia[9], sdia[10],
                     sdia[12], sdia[15], sdia[18], sdia[21],
                     sdia[23], sdia[24], sdia[25], sdia[26],
                     sdia[27], sdia[28], sdia[29], sdia[30], 
                     sdia[31], sdia[32])
        
        dados_sdia.inserir()

def get_gs_data():
    LISTA_PERMUTAS = main.main()
    del LISTA_PERMUTAS[0]

    for permuta in LISTA_PERMUTAS:
        troca = Permuta(permuta[0],permuta[1],permuta[3],permuta[2],permuta[4],permuta[6], permuta[5])
        troca.inserir()

def ler_permutas():
    lista = Permuta.ler_arquivo()
    return lista

def excluir_permuta(selecionado):
    item_selecionado = int(selecionado)
    Permuta.excluir(item_selecionado)

def alterar_permuta(selecionado, item_alterar, novo_valor):
    item_selecionado = int(selecionado)
    item = Permuta.ler_arquivo(item_selecionado)
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


# get_gs_data()
# ler_permutas()
# excluir_permuta(0)
# alterar_permuta(0, 'proponente', 'SO GODOY')
get_gs_data2()