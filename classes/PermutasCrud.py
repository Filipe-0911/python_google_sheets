import sqlite3
import os.path

class PermutasCrud:
    def __init__(self, nome_banco='permutas.db'):
        pasta_raiz = os.path.dirname(os.path.dirname(__file__))
        pasta_db = os.path.join(pasta_raiz, 'database')
        caminho_banco = os.path.join(pasta_db, nome_banco)

        self.nome_banco = caminho_banco
        self.conectar_banco()

    def conectar_banco(self):
        self.conn = sqlite3.connect(self.nome_banco)
        self.cursor = self.conn.cursor()

    def desconectar_banco(self):
        self.conn.close()

    def criar_tabela(self):
        if not os.path.exists(os.path.dirname(self.nome_banco)):
            os.makedirs(os.path.dirname(self.nome_banco))

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
        self.conn.commit()

    def inserir_registro(self, permuta):
        self.cursor.execute('''
            INSERT INTO permutas (data_da_troca, proponente, proponente_sai_do_turno, proponente_entra_no_turno, proposto, proposto_sai_do_turno, proposto_entra_no_turno)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (permuta['data_da_troca'], permuta['proponente'], permuta['proponente_sai_do_turno'], permuta['proponente_entra_no_turno'], permuta['proposto'], permuta['proposto_sai_do_turno'], permuta['proposto_entra_no_turno']))
        self.conn.commit()

    def consultar_permutas(self):
        self.cursor.execute('SELECT * FROM permutas')
        return self.cursor.fetchall()

    def atualizar_registro(self, registro_id, modificacoes):
        if not modificacoes:
            print("Nada a ser atualizado.")
            return

        campos_atualizar = ', '.join(f"{campo} = ?" for campo in modificacoes.keys())
        valores_atualizar = tuple(modificacoes.values())

        self.cursor.execute(f'''
            UPDATE permutas
            SET {campos_atualizar}
            WHERE id=?
        ''', valores_atualizar + (registro_id,))
        self.conn.commit()

    def excluir_registro(self, registro_id):
        self.cursor.execute('DELETE FROM permutas WHERE id=?', (registro_id,))
        self.conn.commit()