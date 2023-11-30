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

        seu_identificador = novo_item[0]

        item_existente = next((item for item in lista if item[0] == seu_identificador), None)

        if item_existente:

            lista = [novo_item if item[0] == seu_identificador else item for item in lista]
        else:

            lista.append(novo_item)

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
        banco = os.path.join(os.path.dirname(__file__), db)
        
        try:
            with open(banco) as file:
                lista =  json.load(file)
                print(lista)

                return lista[item] if isinstance(item, int) else lista

        except Exception:
                # print("erro")
                return []