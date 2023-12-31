import quickstart as main
from classes.Permutas import Permuta
from classes.Aim1 import AIM1
from classes.Crud import Crud

def get_sdias():
    lista_sdias = main.main('bancoAIM!A:BZ')  
    del lista_sdias[0]
    del lista_sdias[0]    

    for sdia in lista_sdias:
        dados_sdia = AIM1(sdia[0],sdia[1],sdia[2],sdia[3],
                     sdia[4], sdia[5],  sdia[6],  sdia[7],
                     sdia[8], sdia[9], sdia[10], sdia[11],
                     sdia[12], sdia[13], sdia[15], sdia[16],
                     sdia[16], sdia[18], sdia[19], sdia[21], 
                     sdia[24], sdia[25], sdia[26], sdia[27], 
                     sdia[28], sdia[29], sdia[30], sdia[31], 
                     sdia[32], sdia[33], sdia[34], sdia[35])

        try: 
            dados_sdia.inserir()
            
        except Exception as err: print(err)
        
    return len(lista_sdias)

def get_permutas():
    LISTA_PERMUTAS = main.main('permutas!A:G')
    del LISTA_PERMUTAS[0]

    for permuta in LISTA_PERMUTAS:
        troca = Permuta(permuta[0],permuta[1],permuta[3],permuta[2],permuta[4],permuta[6], permuta[5])
        
        try: troca.inserir()
        except Exception as err: print(err)

def ler_permutas(id=None):
    permutas = Crud().consultar_permutas(id)
    print(permutas)

    return permutas

def ler_sdias(id=None):
    sdia = Crud().consultar_sdias(id)
    print(sdia)

    return sdia

def excluir_permuta(selecionado):
    item_selecionado = int(selecionado)
    permuta = Crud()
    permuta.excluir_registro(item_selecionado)

def excluir_sdia(selecionado):
    sdia = Crud()
    sdia.excluir_sdia(selecionado)

def alterar_permuta(selecionado, item_alterar, novo_valor):
    item_selecionado = int(selecionado)
    dicionario = {item_alterar: novo_valor}
    
    item_para_alterar = Crud()
    item_para_alterar.atualizar_registro(item_selecionado, dicionario, 'permutas', 'id')

def alterar_sdia(selecionado, item_alterar, novo_valor):
    item_selecionado = str(selecionado)
    dicionario = {item_alterar: novo_valor}
    
    item_para_alterar = Crud()
    item_para_alterar.atualizar_registro(item_selecionado, dicionario, 'aim1', 'protocolo')


# ler_sdias('46a0b83f')
# excluir_sdia('46a0b83f')
# alterar_sdia('46a0b83f', 'localidades', 'SDRK')