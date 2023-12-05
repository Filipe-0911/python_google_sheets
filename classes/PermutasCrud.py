import sqlite3
import os.path

class PermutasCrud:
    def __init__(self, nome_banco='data.db'):
        pasta_raiz = os.path.dirname(os.path.dirname(__file__))
        pasta_db = os.path.join(pasta_raiz, 'database')
        caminho_banco = os.path.join(pasta_db, nome_banco)

        print(caminho_banco)

        self.nome_banco = caminho_banco
        self.conectar_banco()

    def conectar_banco(self):
        try:
            if not os.path.exists(os.path.dirname(self.nome_banco)):
                os.makedirs(os.path.dirname(self.nome_banco))

            self.conn = sqlite3.connect(self.nome_banco)
            self.cursor = self.conn.cursor()

        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")


    def desconectar_banco(self):
        self.conn.close()

    def criar_tabela(self):
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS permutas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_da_troca TEXT,
                proponente TEXT,
                proponente_sai_do_turno TEXT,
                proponente_entra_no_turno TEXT,
                proposto TEXT,
                proposto_sai_do_turno TEXT,
                proposto_entra_no_turno TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sdia (
                protocolo TEXT PRIMARY KEY,
                data_insercao TEXT,
                data_recebimento TEXT,
                operador TEXT,
                localidade TEXT,
                quem_originou TEXT,
                assunto TEXT,
                data_efetivacao TEXT,
                esclarecimento INTEGER,
                telefone INTEGER,
                email INTEGER,
                retornou_ica  INTEGER,
                observacoes TEXT,
                a1 TEXT,
                a2 TEXT,
                a3 TEXT,
                a4 TEXT,
                a5 TEXT,
                a6 TEXT,
                a7 TEXT,
                a8 TEXT,
                a9 TEXT

            )
        ''')
        self.conn.commit()

    def inserir_registro(self, permuta):
        self.cursor.execute('''
            INSERT INTO permutas (data_da_troca, proponente, proponente_sai_do_turno, proponente_entra_no_turno, proposto, proposto_sai_do_turno, proposto_entra_no_turno)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (permuta['data_da_troca'], permuta['proponente'], permuta['proponente_sai_do_turno'], permuta['proponente_entra_no_turno'], permuta['proposto'], permuta['proposto_sai_do_turno'], permuta['proposto_entra_no_turno']))
        self.conn.commit()

    def inserir_sdia(self, sdia):
        self.cursor.execute('''
            INSERT INTO sdia (protocolo, data_insercao, data_recebimento, operador, localidade, quem_originou, assunto, data_efetivacao, esclarecimento, telefone, email, retornou_ica, observacoes, a1, a2, a3, a4, a5, a6, a7, a8, a9)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (sdia['protocolo'], sdia['data_insercao'], sdia['data_recebimento'], sdia['operador'], sdia['localidade'], sdia['quem_originou'], sdia['assunto'], sdia['data_efetivacao'], sdia['esclarecimento'], sdia['telefone'], sdia['email'], sdia['retornou_ica'], sdia['observacoes'], sdia['a1'], sdia['a2'], sdia['a3'], sdia['a4'], sdia['a5'], sdia['a6'], sdia['a7'], sdia['a8'], sdia['a9']))
        self.conn.commit()

    def consultar_permutas(self, data_da_troca=None):
        if data_da_troca:
            self.cursor.execute('SELECT * FROM permutas WHERE data_da_troca=?', (data_da_troca,))
        else: self.cursor.execute('SELECT * FROM permutas')

        return self.cursor.fetchall()
    
    def consultar_sdias(self, protocolo=None):
        print(protocolo)
        if protocolo:
            self.cursor.execute('SELECT * FROM sdia WHERE protocolo=?', (protocolo,))
        else: 
            self.cursor.execute('SELECT * FROM sdia')

        return self.cursor.fetchall()

    def atualizar_registro(self, registro_id, modificacoes, banco, parametro_busca):
        
        if not modificacoes:
            print("Nada a ser atualizado.")
            return
        print(modificacoes)

        campos_atualizar = ', '.join(f"{campo} = ?" for campo in modificacoes.keys())
        print(registro_id)
        valores_atualizar = tuple(modificacoes.values())
        print(valores_atualizar)

        self.cursor.execute(f'''
            UPDATE {banco}
            SET {campos_atualizar}
            WHERE {parametro_busca}=?
        ''', valores_atualizar + (registro_id,))
        self.conn.commit()

    def excluir_registro(self, id):
        self.cursor.execute('DELETE FROM permutas WHERE id=?', (id,))
        print("Permuta excluído do banco.")
        self.conn.commit()

    def excluir_sdia(self, registro_id):
        self.cursor.execute('DELETE FROM sdia WHERE protocolo=?', (registro_id,))
        print("SDIA excluída do banco.")
        self.conn.commit()