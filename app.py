import streamlit as st # type: ignore
from functions.add_media import add_media
from functions.list_media import filter_media

st.set_page_config(layout="wide", page_title="Movies and Shows Manager", page_icon="🎬")

st.title("Movies and Shows Manager")

movies, shows = st.tabs(["Movies", "Shows"])

with movies:
    st.header("Movies")

    col1, col2 = st.columns([16, 1], vertical_alignment = "center")

    with col1:
        filter_media("movies")

    with col2:
        add_media("Movie")

    st.divider()


with shows:
    st.header("Shows")

    col1, col2 = st.columns([16, 1], vertical_alignment = "center")
    
    with col1:
        filter_media("shows")
    with col2:
        add_media("Show")

    st.divider()
