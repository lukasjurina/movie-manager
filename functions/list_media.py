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

    #st.write(result)

    #pass

    col1, col2, col3, col4 = st.columns(4)

    #0: id, 1: title, 2: year, 3: status, 4: date_watched, 5: rating

    for i, record in enumerate(result):
        with [col1, col2, col3, col4][i % 4]:
            with st.container(border = True, height = 320):
                st.markdown(f"<h3 style='white-space: nowrap; overflow: hidden; max-width: 100%; display: inline-block; animation: scroll-text 10s linear infinite;'>{record[1]}</h3>", unsafe_allow_html=True)

                st.write(f"{record[2]}")
                st.write(f"{record[3]}")
                if record[4]:
                    st.write(f"{record[4]}")
                else:
                    st.markdown("<div style='height: 41.6px;'></div>", unsafe_allow_html=True)
                if record[5]:
                    rating = "⭐" * (record[5] + 1)
                    st.write(f"{rating}")
                else:
                    st.markdown("<div style='height: 41.6px;'></div>", unsafe_allow_html=True)

                with st.expander(f"Options"):
                    col_edit, col_delete = st.columns([1, 1])

                    with col_edit:
                        if st.button("Edit", key=f"edit_{parent_key}{i}"):
                            #TODO add functionality of edit, probably modification of add
                            pass

                    with col_delete:
                        if st.button("Delete", key=f"delete_{parent_key}{i}"):
                            #TODO add functionality of delete, need to create in db\database.py
                            pass