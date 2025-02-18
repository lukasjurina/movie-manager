import streamlit as st
from functions.add_media import add_media

st.set_page_config(layout="wide", page_title="Movies and Shows Manager", page_icon="🎬")

st.title("Movies and Shows Manager")

movies, shows = st.tabs(["Movies", "Shows"])

with movies:
    st.header("Movies")

    add_media("Movie")

with shows:
    st.header("Shows")

    add_media("Show")
