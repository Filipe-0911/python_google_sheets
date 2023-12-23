from classes.AbstractCrud import AbstractCrud
from classes.Crud import Crud

class Sdia(AbstractCrud, Crud):

    arquivo = 'sdia.json'
    banco = 'data.db'
    
    def __init__(self, data_insercao, protocolo, data_recebimento, operador, localidade,
                  quem_originou, assunto, data_efetivacao, esclarecimento=0, telefone=0, 
                  email=0, retornou_ica=0, observacoes=None, 
                  a1=None,a2=None,a3=None,a4=None,a5=None,a6=None,a7=None,a8=None,a9=None, opr2=None, status_do_processo=None, ultima_att=None):
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
        self.opr2 = opr2
        self.status_do_processo = status_do_processo
        self.ultima_att = ultima_att


    def inserir(self):
        protocolo = self.protocolo

        banco_permutas = Crud(self.banco)
        banco_permutas.conectar_banco()
        banco_permutas.criar_tabela()

        produtoDuplicado = banco_permutas.consultar_sdias(protocolo)

        if produtoDuplicado:
            mensagem = f"Já existe um SDIA com o código {protocolo}!"
            print(mensagem)
            return mensagem
        else: 
            super().inserir()

        