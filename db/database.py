import sqlite3

def get_conn():
    conn = sqlite3.connect("database.db")
    return conn


def db_init():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        create table if not exist media (
            id integer primary key autoincrement,
            title text not null,
            year integer not null,
            genre text,
            status integer not null,
            rating integer
        )              
    """)

    conn.commit()
    conn.close()


def add_media():
    pass


def remove_media():
    pass


def get_all_media():
    pass


