import sqlite3



def create_table_items():
    """Create initial table"""
    testing_tasks = [
                    (1, 'sgaga', 1),
                    (2, 'agagagaga', 1),
                    (3, 'agssgsgsss', 0)]

    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Tasks")
    cur.execute("CREATE TABLE Tasks ("
                "id INTEGER PRIMARY KEY,"
                "name TEXT,"
                "done INTEGER)")

    cur.executemany("INSERT INTO Tasks VALUES(?, ?, ?)", testing_tasks)
    conn.commit()
    conn.close()

def create_table_user():
    testing_users = [
        (1, 'Pawel', 'pass'),
        (2, 'Robert', 'pass'),
        (3, 'Mati', 'pass')]

    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS User")
    cur.execute("CREATE TABLE User ("
                "id INTEGER PRIMARY KEY,"
                "name TEXT,"
                "password TEXT)")

    cur.executemany("INSERT INTO User VALUES(?, ?, ?)", testing_users)
    conn.commit()
    conn.close()


def data_query(query, arguments):
    """Execute query and return needed data"""
    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()
    cur.execute(query, arguments)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    return data
