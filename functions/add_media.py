import streamlit as st # type: ignore
from datetime import datetime
from db.database import insert_media


def add_media(parent_key):
    """
    Creates a dialog for adding a movie or show.

    Parameters:
    parent_key (str): The type of media being added ("Movie" or "Show").

    """

    @st.dialog(f"Add {parent_key}")
    def add(parent_key):

        date = None
        rating = None

        media_title = st.text_input(f"{parent_key} Title")

        start_year = 1888
        curr_year = datetime.now().year
        years = list(range(curr_year, start_year - 1, -1))
        media_year = st.selectbox("Year", years, index = 0)

        if parent_key == "Movie":
            status_map = {
                "To Watch",
                "Watched",
            }
        if parent_key == "Show":
            status_map = {
                "To Watch",
                "Watched",
                "Watching",
            }
        media_status = st.pills("Status", options = status_map, selection_mode = "single")

        if media_status == "Watched":
            date = st.date_input("Date Watched", format = "DD/MM/YYYY")

            st.write("Rating")
            rating = st.feedback("stars")

        if st.button("Submit"):

            insert_media(media_title, media_year, media_status, date, rating, parent_key)

            st.rerun()
    
    if st.button(f"Add {parent_key}"):
        add(parent_key)
