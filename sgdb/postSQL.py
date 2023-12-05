import os
import sqlite3

pasta_db = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db')
caminho_banco = os.path.join(pasta_db, 'permutas.db')

print(caminho_banco)

connect = sqlite3.connect(caminho_banco)

cursor = connect.cursor()

cursor.execute("""
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
""")

cursor.execute("""
    INSERT INTO permutas (id, data_da_troca, proponente, proponente_sai_do_turno, proponente_entra_no_turno, proposto, proposto_sai_do_turno, proposto_entra_no_turno)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", (1, "30/10/2023 12:02:13", "SO GODOY", "06/11/2023", "07/11/2023", "SO WAGNER", "07/11/2023", "06/11/2023"))


cursor.execute("SELECT * FROM permutas")
for row in cursor.fetchall():
    print(row)

connect.commit()

connect.close()