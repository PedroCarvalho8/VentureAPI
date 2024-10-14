import sqlite3

def initialize_db(tables: tuple[str]):
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
