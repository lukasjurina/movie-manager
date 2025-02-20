import streamlit as st # type: ignore


def filter_media(parent_key):
    if parent_key == "movies":
        status_map = {"To Watch", "Watched"}
    else:
        status_map = {"To Watch", "Watching", "Watched"}

    status_choice = st.pills("empty", options = status_map, selection_mode = "single", label_visibility = "collapsed", key = f"{parent_key}_status")

    return status_choice


def order_media(parent_key):

    filter_options = ["Alphabet", "Year", "Date Watched", "Rating"]
    filter_choice = st.segmented_control("Order By", filter_options, selection_mode = "single", key = f"{parent_key}_filter")

    return filter_choice

def list_media(parent_key):
    pass