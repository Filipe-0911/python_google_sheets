from classes.AbstractCrud import AbstractCrud

class Permuta(AbstractCrud):

    arquivo = 'permutas.json'
    
    def __init__(self, data_da_troca, proponente, proponente_entra_no_turno, proponente_sai_do_turno, proposto, proposto_entra_no_turno, proposto_sai_do_turno):
        self.data_da_troca = data_da_troca
        self.proponente = proponente
        self.proponente_entra_no_turno = proponente_entra_no_turno
        self.proponente_sai_do_turno = proponente_sai_do_turno
        self.proposto = proposto
        self.proposto_entra_no_turno = proposto_entra_no_turno
        self.proposto_sai_do_turno = proposto_sai_do_turno

    def inserir(self):
        lista = self.lerArquivo()
        print(lista)
        produtoDuplicado = filter(lambda p: p[0] == self.data_da_troca, lista)
        # produtoDuplicado = filter(lambda p: p['data_da_troca'] == self.data_da_troca, lista)

        if len(list(produtoDuplicado)):
            print()
            print('Já existe um produto com esse código!')
        else: 
            super().inserir()