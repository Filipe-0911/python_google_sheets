import sqlite3
import os.path

class Crud:
    def __init__(self, nome_banco='data.db'):
        pasta_raiz = os.path.dirname(os.path.dirname(__file__))
        pasta_db = os.path.join(pasta_raiz, 'database')
        caminho_banco = os.path.join(pasta_db, nome_banco)

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
            CREATE TABLE IF NOT EXISTS aim1 (
                protocolo TEXT PRIMARY KEY,
                data_insercao TEXT,
                data_recebimento TEXT,
                mes INTEGER,
                operador1 TEXT,
                operador2 TEXT,
                operador3 TEXT,
                operador4 TEXT,
                localidades TEXT,
                quem_originou TEXT,
                assunto TEXT,
                data_efetivacao TEXT,
                esclarecimento BOOLEAN,
                esclarecimento_quantidade INTEGER,
                telefone BOOLEAN,
                telefone_quantidade INTEGER,
                email BOOLEAN,
                email_quantidade INTEGER,
                retornou_ica  BOOLEAN,
                retornou_ica_quantidade  INTEGER,
                observacoes TEXT,
                a1 TEXT,
                a2 TEXT,
                a3 TEXT,
                a4 TEXT,
                a5 TEXT,
                a6 TEXT,
                a7 TEXT,
                a8 TEXT,
                a9 TEXT,
                status_do_processo TEXT,
                ultima_att TEXT

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
            INSERT INTO aim1 (protocolo, data_insercao, data_recebimento, mes, operador1, operador2, operador3, operador4, localidades, quem_originou, assunto, data_efetivacao, esclarecimento, esclarecimento_quantidade, telefone, telefone_quantidade, email, email_quantidade, retornou_ica, retornou_ica_quantidade, observacoes, a1, a2, a3, a4, a5, a6, a7, a8, a9, status_do_processo, ultima_att)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (sdia['protocolo'], sdia['data_insercao'], sdia['data_recebimento'], sdia['mes'], sdia['operador1'], sdia['operador2'], sdia['operador3'], sdia['operador4'], sdia['localidades'], sdia['quem_originou'], sdia['assunto'], sdia['data_efetivacao'], sdia['esclarecimento'], sdia['esclarecimento_quantidade'], sdia['telefone'], sdia['telefone_quantidade'], sdia['email'], sdia['email_quantidade'], sdia['retornou_ica'], sdia['retornou_ica_quantidade'], sdia['observacoes'], sdia['a1'], sdia['a2'], sdia['a3'], sdia['a4'], sdia['a5'], sdia['a6'], sdia['a7'], sdia['a8'], sdia['a9'], sdia['status_do_processo'], sdia['ultima_att']))
        self.conn.commit()

    def consultar_permutas(self, data_da_troca=None):
        if data_da_troca:
            self.cursor.execute('SELECT * FROM permutas WHERE data_da_troca=?', (data_da_troca,))
        else: self.cursor.execute('SELECT * FROM permutas')

        return self.cursor.fetchall()
    
    def consultar_sdias(self, protocolo=None):
        if protocolo:
            self.cursor.execute('SELECT * FROM aim1 WHERE protocolo=?', (protocolo,))
        else: 
            self.cursor.execute('SELECT * FROM aim1')

        return self.cursor.fetchall()

    # corrigir nome banco aim1
    def atualizar_registro(self, registro_id, modificacoes, banco, parametro_busca):
        # banco = self.banco
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
        banco_permutas = Crud()
        produto_encontrado = banco_permutas.consultar_sdias(registro_id)
        if produto_encontrado:
            self.cursor.execute('DELETE FROM aim1 WHERE protocolo=?', (registro_id,))
            self.conn.commit()
            
            mensagem = f"SDIA {registro_id} excluída do banco."
            print(mensagem)
            return mensagem
        
        else:
            mensagem = f"SDIA {registro_id} não está cadastrada!"
            print(mensagem)
            return mensagem