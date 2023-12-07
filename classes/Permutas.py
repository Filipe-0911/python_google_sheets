from classes.AbstractCrud import AbstractCrud
from classes.Crud import Crud

class Permuta(AbstractCrud, Crud):

    arquivo = 'permutas.json'
    banco = 'data.db'
    
    def __init__(self, data_da_troca, proponente, proponente_entra_no_turno, proponente_sai_do_turno, proposto, proposto_entra_no_turno, proposto_sai_do_turno):
        self.data_da_troca = data_da_troca
        self.proponente = proponente
        self.proponente_sai_do_turno = proponente_sai_do_turno
        self.proponente_entra_no_turno = proponente_entra_no_turno
        self.proposto = proposto
        self.proposto_sai_do_turno = proposto_sai_do_turno
        self.proposto_entra_no_turno = proposto_entra_no_turno

    def inserir(self):
        filtrar_por = self.data_da_troca

        banco_permutas = Crud(self.banco)
        banco_permutas.conectar_banco()
        banco_permutas.criar_tabela()

        produtoDuplicado = banco_permutas.consultar_permutas(filtrar_por)

        if produtoDuplicado:
            print()
            print('Já existe um produto com esse código!')
        else: 
            super().inserir()
