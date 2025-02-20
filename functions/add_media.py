import streamlit as st # type: ignore
from datetime import datetime
from db.database import insert_media

def add_media(media_type):

    @st.dialog(f"Add {media_type}")
    def add(media_type):

        date = None
        rating = None

        media_title = st.text_input(f"{media_type} Title")

        start_year = 1888
        curr_year = datetime.now().year

        years = list(range(curr_year, start_year - 1, -1))
        media_year = st.selectbox("Year", years, index = 0)

        if media_type == "Movie":
            status_map = {
                "To Watch",
                "Watched",
            }
        if media_type == "Show":
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

            insert_media(media_title, media_year, media_status, date, rating)

            st.rerun()


    if st.button(f"Add {media_type}"):
        add(media_type)
        
