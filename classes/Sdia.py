from classes.AbstractCrud import AbstractCrud

class Sdia(AbstractCrud):

    arquivo = 'sdia.json'
    banco = 'data.db'
    
    def __init__(self, data_insercao, protocolo, data_recebimento, operador, localidade,
                  quem_originou, assunto, data_efetivacao, esclarecimento=0, telefone=0, 
                  email=0, retornou_ica=0, observacoes='', 
                  a1='',a2='',a3='',a4='',a5='',a6='',a7='',a8='',a9=''):
        self.data_insercao = data_insercao
        self.protocolo = protocolo
        self.data_recebimento = data_recebimento
        self.operador = operador
        self.localidade = localidade
        self.quem_originou = quem_originou
        self.assunto = assunto
        self.data_efetivacao = data_efetivacao
        self.esclarecimento = esclarecimento
        self.telefone = telefone
        self.email = email
        self.retornou_ica = retornou_ica
        self.observacoes = observacoes
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.a8 = a8
        self.a9 = a9


    def inserir(self):
        lista = self.ler_arquivo()
        produtoDuplicado = filter(lambda p: p["protocolo"] == self.protocolo, lista)

        if len(list(produtoDuplicado)):
            print()
            print('Já existe um produto com esse código!')
        else: 
            super().inserir()

        