import streamlit as st # type: ignore
from datetime import datetime

def add_media(media_type):

    @st.dialog(f"Add {media_type}")
    def add(media_type):

        media_title = st.text_input(f"{media_type} Title")

        start_year = 1888
        curr_year = datetime.now().year

        years = list(range(curr_year, start_year - 1, -1))
        year = st.selectbox("Year", years, index = 0)

        genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Fantasy", "Thriller", "Documentary", "Romance"]
        media_genre = st.multiselect("Genre", genres)

        if media_type == "Movie":
            status_map = {
                0: "To Watch",
                1: "Watched",
            }
        if media_type == "Show":
            status_map = {
                0: "To Watch",
                1: "Watched",
                2: "Watching",
            }

        status = st.pills("Status", options = status_map, format_func = lambda option: status_map[option], selection_mode = "single")

        if status == 1:
            date = st.date_input("Date Watched", format = "DD/MM/YYYY")

            st.write("Rating")
            rating = st.feedback("stars")

        if st.button("Submit"):

            st.rerun()

    if st.button(f"Add {media_type}"):

        #database magic

        add(media_type)
