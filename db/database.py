import sqlite3
import streamlit as st # type: ignore

def get_conn():
    conn = sqlite3.connect("db/database.db")
    return conn


def db_init():
    conn = get_conn()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            create table if not exists media (
                id integer primary key autoincrement,
                title text not null,
                year integer not null,
                status text not null,
                date_watched text,
                rating integer,
                type text,
                unique(title, year)
            )              
        """)

        conn.commit()
    except Exception as e:
        st.session_state["message"] = (f"Database error: {e}", "error")
    finally:
        conn.close()


def insert_media(title, year, status, date_watched, rating, type):
    conn = get_conn()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            insert into media (title, year, status, date_watched, rating, type)
            values (?, ?, ?, ?, ?, ?)""", (title, year, status, date_watched, rating, type))
        
        conn.commit()
        st.session_state["message"] = ("Media Added!", "success")
    except sqlite3.IntegrityError:
        st.session_state["message"] = (f"Media already exists or missing information!", "warning")
    except Exception as e:
        st.session_state["message"] = (f"Database error: {e}", "error")
    finally:
        conn.close()


def get_media(media_type=None, status=None, order=None):
    """Fetch media from the database based on filters."""
    conn = get_conn()
    cursor = conn.cursor()

    try:
        query = "SELECT * FROM media"
        conditions = []
        params = []

        if media_type:
            conditions.append(f"type = ?")
            params.append(media_type)
        if status:
            conditions.append(f"status = ?")
            params.append(status)
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        if order:
            query += f" ORDER BY {order}"

        cursor.execute(query, params)
        return cursor.fetchall()
    except Exception as e:
        st.session_state["message"] = (f"Database error: {e}", "error")
        return []
    finally:
        conn.close()


def remove_media():
    pass