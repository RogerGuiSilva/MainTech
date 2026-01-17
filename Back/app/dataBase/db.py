import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "app.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            setor TEXT NOT NULL,
            tipo TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS maquinas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            setor TEXT NOT NULL,
            tipo TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS falhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            tipo TEXT NOT NULL,
            gravidade TEXT NOT NULL,
            data_ocorrencia TEXT NOT NULL,
            status TEXT NOT NULL,
            maquina_id INTEGER,
            equipamento_id INTEGER,
            FOREIGN KEY (maquina_id) REFERENCES maquinas(id),
            FOREIGN KEY (equipamento_id) REFERENCES equipamentos(id)
        )
    """)

    conn.commit()
    conn.close()
    print("Banco inicializado com sucesso")

if __name__ == "__main__":
    init_db()
