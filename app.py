import streamlit as st # type: ignore
from functions.add_media import add_media
from functions.list_media import filter_media, order_media
from db.database import db_init

db_init()

st.set_page_config(layout="wide", page_title="Movies and Shows Manager", page_icon="🎬")

if "message" in st.session_state:
    msg, msg_type = st.session_state.pop("message")  # Po zobrazení smažeme
    if msg_type == "success":
        st.success(msg)
    elif msg_type == "warning":
        st.warning(msg)
    else:
        st.error(msg)

st.title("Movies and Shows Manager")

movies, shows = st.tabs(["Movies", "Shows"])

with movies:
    key = "movies"

    st.header("Movies")

    col1, col2 = st.columns([16, 1], vertical_alignment = "center")

    with col1:
        filter_media(key)

    with col2:
        add_media("Movie")

    st.divider()

    order_media(key)


with shows:
    key = "shows"

    st.header("Shows")

    col1, col2 = st.columns([16, 1], vertical_alignment = "center")
    
    with col1:
        filter_media(key)
    with col2:
        add_media("Show")

    st.divider()

    order_media(key)
