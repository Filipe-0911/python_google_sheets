import os
import json
import os.path
from abc import ABC
from classes.PermutasCrud import PermutasCrud

class AbstractCrud(ABC, PermutasCrud):

    def detalhar(self):
        return self.__dict__
    
    def inserir(self):

        self.__gravar_arquivo()

        print('Registro Cadastrado com sucesso')

    def alterar(self):
        print(self)
        self.atualizar_registro()

        print('Registro Alterado com sucesso')

    def __gravar_arquivo(self):

        if self.arquivo == 'permutas.json':
            banco = PermutasCrud(self.banco)
            banco.conectar_banco()
            banco.criar_tabela()
            banco.inserir_registro(self.detalhar())
            banco.desconectar_banco()

        if self.arquivo == 'sdia.json':
            banco = PermutasCrud(self.banco)
            banco.conectar_banco()
            banco.criar_tabela()
            banco.inserir_sdia(self.detalhar())
            banco.desconectar_banco()