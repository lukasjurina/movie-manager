import sqlite3
import streamlit as st

def get_conn():
    conn = sqlite3.connect("db/database.db")
    return conn


def db_init():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        create table if not exists media (
            id integer primary key autoincrement,
            title text not null,
            year integer not null,
            status text not null,
            date_watched text,
            rating integer,
            unique(title, year)
        )              
    """)

    conn.commit()
    conn.close()


def insert_media(title, year, status, date_watched, rating):
    conn = get_conn()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            insert into media (title, year, status, date_watched, rating)
            values (?, ?, ?, ?, ?)""", (title, year, status, date_watched, rating))
        
        conn.commit()

        st.session_state["message"] = ("✅ Film Added!", "success")
    except sqlite3.IntegrityError:
        st.session_state["message"] = (f"Movie already exists or missing information!", "warning")
    except Exception as e:
        st.session_state["message"] = (f"Error: {e}", "error")
    finally:
        conn.close()


def remove_media():
    pass


def get_all_media():
    pass


