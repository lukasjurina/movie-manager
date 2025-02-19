import streamlit as st # type: ignore

def filter_media(parent_key):
    status_map = {"Watching", "Watched"}

    status_choice = st.pills("empty", options = status_map, selection_mode = "single", label_visibility = "collapsed", key = f"{parent_key}_status")
