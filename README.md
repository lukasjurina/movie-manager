
# Media Manager

This is a simple **Streamlit** web application for managing and tracking media such as movies and TV shows. The application allows users to add, view, and manage media entries with details like title, year, genre, (watched, to watch, etc.), and rating.

## Features
- **Add Media**: Users can add movies and TV shows with information like title, year, status, and rating.
- **View Media**: The app displays media entries in a grid, grouped by columns.
- **Media Update and Delete**: Each media entry can be edited or deleted using buttons provided next to the entry.
- **Persistent Storage**: The app uses an SQLite database to store media entries, ensuring data persistence across sessions.

## Technologies Used
- **Streamlit**: For the user interface and application logic.
- **SQLite**: For storing media data in a local database.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/media-manager.git
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the SQLite database is created:
   The app will create a SQLite database (`database.db`) automatically when it runs.

## Usage

1. To run the application, execute the following command:
   ```bash
   streamlit run app.py
   ```

2. Open the provided link (usually `http://localhost:8501`) in your web browser to start interacting with the app.

## Database Structure

The app uses an SQLite database to store media entries. The `media` table has the following structure:

| Column       | Type     | Description                        |
|--------------|----------|------------------------------------|
| id           | INTEGER  | Primary key, autoincrement         |
| title        | TEXT     | Title of the movie/show            |
| year         | INTEGER  | Release year of the movie/show     |
| genre        | TEXT     | Genre of the movie/show            |
| status       | TEXT     | Status (To Watch, Watched, Watching)|
| date_watched | TEXT     | Date when the media was watched    |
| rating       | INTEGER  | Rating of the media                |
| type         | TEXT     | Type of media (Movie or Show)      |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
