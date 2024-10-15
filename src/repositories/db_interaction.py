import sqlite3


def initialize_db(tables: tuple):
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    for table in tables:

        main_table = table
        read_status_table = f'{main_table}_read_status'

        c.execute(f'''DROP TABLE IF EXISTS {main_table}''')
        c.execute(f'''DROP TABLE IF EXISTS {read_status_table}''')

        c.execute(f'''CREATE TABLE IF NOT EXISTS {main_table} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        message TEXT)''')

        c.execute(f'''CREATE TABLE IF NOT EXISTS {read_status_table} (
                        id INTEGER PRIMARY KEY, 
                        last_read_id INTEGER)''')

        c.execute(f"SELECT COUNT(*) FROM {read_status_table}")
        if c.fetchone()[0] == 0:
            c.execute(f"INSERT INTO {read_status_table} (id, last_read_id) VALUES (1, 0)")

    c.execute(f'''CREATE TABLE IF NOT EXISTS solicitacoes (
                            id INTEGER PRIMARY KEY, 
                            class_name TEXT,
                            status TEXT
                            )''')

    c.execute('''
        UPDATE solicitacoes SET status = ? WHERE status = ?
        ''', ('Cancelado', 'Requisitado'))

    conn.commit()
    conn.close()


def send_msg(msg, table):
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    c.execute(f"INSERT INTO {table} (message) VALUES (?)", (msg,))
    conn.commit()
    conn.close()


def get_msg(table):
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    main_table = table
    read_status_table = f'{main_table}_read_status'

    c.execute(f"SELECT last_read_id FROM {read_status_table} WHERE id = 1")
    last_read_id = c.fetchone()[0]

    c.execute(f"SELECT id, message FROM {main_table} WHERE id > ?", (last_read_id,))
    rows = c.fetchall()

    if rows:
        last_read_id = rows[-1][0]
        c.execute(f"UPDATE {read_status_table} SET last_read_id = ? WHERE id = 1", (last_read_id,))

    conn.commit()
    conn.close()

    return rows


def  insert_item_solicitacoes(dados):
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    c.execute('''
    INSERT INTO solicitacoes (class_name, status) VALUES (?, ?)
    ''', (dados.get('class_name'), dados.get('status')))

    conn.commit()
    conn.close()


def get_items_solicitacoes():
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    c.execute('''
    SELECT * FROM solicitacoes
    ''')

    rows = c.fetchall()

    conn.commit()
    conn.close()

    return rows


def item_encontrado(class_name: str):
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    c.execute('''
    SELECT * FROM solicitacoes 
    WHERE 
        class_name = ? and
        status = ?
    ''', (class_name, 'Requisitado'))

    rows = c.fetchall()

    idx_min = min([i[0] for i in rows])

    c.execute('''
    UPDATE solicitacoes SET status = ? WHERE id = ?
    ''', ('Encontrado', idx_min))

    conn.commit()
    conn.close()
