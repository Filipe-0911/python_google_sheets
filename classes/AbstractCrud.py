from classes.Crud import Crud

class AbstractCrud(Crud):

    def detalhar(self):
        return self.__dict__
    
    def inserir(self):

        self.__gravar_arquivo()


    def alterar(self):
        print(self)
        self.atualizar_registro()

        print('Registro Alterado com sucesso')

    def __gravar_arquivo(self):
        
        dados = self.arquivo.split('.')

        if dados[0] == 'permutas':
            banco = Crud(self.banco)
            banco.conectar_banco()
            banco.criar_tabela()
            banco.inserir_registro(self.detalhar())
            banco.desconectar_banco()
            
            print(f'Permuta do(a) {self.proponente} cadastrada com sucesso')

        if dados[0] == 'sdia':
            banco = Crud(self.banco)
            banco.conectar_banco()
            banco.criar_tabela()
            banco.inserir_sdia(self.detalhar())
            banco.desconectar_banco()
            
            print(f'SDIA {self.protocolo} Cadastrado com sucesso')