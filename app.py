import streamlit as st # type: ignore
from functions.add_media import add_media
from functions.list_media import filter_media, order_media, list_media
from db.database import db_init

db_init()

st.set_page_config(layout="wide", page_title="Movies and Shows Manager", page_icon="🎬")

if "message" in st.session_state:
    msg, msg_type = st.session_state.pop("message")
    if msg_type == "success":
        st.success(msg)
    elif msg_type == "warning":
        st.warning(msg)
    else:
        st.error(msg)

st.title("Movies and Shows Manager")

movies, shows = st.tabs(["Movies", "Shows"])

with movies:
    key = "Movie"
    status = None
    order = None

    st.header(f"{key}s")

    col1, col2 = st.columns([15.8, 1], vertical_alignment = "center")

    with col1:
        status = filter_media(key)

    with col2:
        add_media(key)

    st.divider()

    order = order_media(key)

    list_media(key, status, order)


with shows:
    key = "Show"
    status = None
    order = None

    st.header(f"{key}s")

    col1, col2 = st.columns([15.8, 1], vertical_alignment = "center")
    
    with col1:
        status = filter_media(key)
    with col2:
        add_media(key)

    st.divider()

    order = order_media(key)


    list_media(key, status, order)
