import streamlit as st # type: ignore
from db.database import get_media

def filter_media(parent_key):
    if parent_key == "Movie":
        status_map = {"To Watch", "Watched"}
    else:
        status_map = {"To Watch", "Watching", "Watched"}

    status_choice = st.pills("empty", options = status_map, selection_mode = "single", label_visibility = "collapsed", key = f"{parent_key}_status")

    return status_choice


def order_media(parent_key):

    filter_map = {"title": "Alphabet", "year": "Year", "date_watched": "Date Watched", "rating": "Rating"}
    filter_choice = st.segmented_control("Order By", filter_map, format_func = lambda option: filter_map[option], selection_mode = "single", key = f"{parent_key}_filter")

    return filter_choice


def list_media(parent_key, status, order):
    result = get_media(parent_key, status, order)
    st.write(result)
