import streamlit as st

def add_media(media_type):

    @st.dialog(f"Add {media_type}")
    def add(media_type):

        movie_name = st.text_input(f"{media_type} Title")

        start_year = 2000
        years = list(range(start_year - 50, start_year + 101))
        year = st.selectbox("Year", years)

        date = st.date_input("Date Watched", format = "DD/MM/YYYY")

        st.write("Rating")
        rating = st.feedback("stars")

        if st.button("Submit"):

            st.rerun()

    if st.button(f"Add {media_type}"):

        #database magic

        add("Movie")
