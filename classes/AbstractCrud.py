import json
from abc import ABC
import os.path

class AbstractCrud(ABC):

    def detalhar(self):
        return self.__dict__
    
    def inserir(self):
        lista = self.lerArquivo()
        lista.append(self.detalhar())
        self.__gravarArquivo(lista)

        print('Registro Cadastrado com sucesso')

    def alterar(self, item):
        lista = self.lerArquivo()
        lista[item] = self.detalhar()
        self.__gravarArquivo(lista)

        print('Registro Alterado com sucesso')

    def __gravarArquivo(self, novo_item):
        db_folder = "db"
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", db_folder))
        os.makedirs(db_path, exist_ok=True)
        arquivo_path = os.path.join(db_path, self.arquivo)

        try:
            with open(arquivo_path, 'r') as file:
                lista = json.load(file)
    
        except FileNotFoundError:
            lista = []

        if isinstance(lista, list):
            lista.clear()

        print(novo_item)
        lista = novo_item

        with open(arquivo_path, 'w') as file:
            json.dump(lista, file, indent=4)


    @classmethod
    def excluir(cls, item):
        lista = cls.lerArquivo()
        del lista[item]
        
        with open(cls.arquivo, 'w') as file:
             json.dump(lista, file, indent=4)

    @classmethod
    def listarTodos(cls):
        lista = cls.lerArquivo()
        for i, p in enumerate(lista):
            print(f"{i} - {p}")

    @classmethod
    def lerArquivo(cls, item = None):
        db = cls.arquivo
        banco = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", db))
        
        try:
            with open(banco) as file:
                lista =  json.load(file)
                
                return lista[item] if isinstance(item, str) else lista

        except Exception:
                
                return []