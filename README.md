# Music Database Application
This is a Python application that stores data related to music in a SQLite3 database. It provides functionality to perform CRUD (Create, Read, Update, Delete) operations on the data. The application is built using the Flask web framework and the SQLite database is managed using the built-in sqlite3 module in Python.

## Installation
To install the application, follow these steps:

1- Clone the repository to your local machine.
2- Create a virtual environment and activate it:
    $ python -m venv env
    $ source env/bin/activate (for Linux/MacOS) or $ env\Scripts\activate (for Windows)
3- Install the dependencies using pip:
    $ pip install -r requirements.txt

## Database schema
The database schema consists of a single table, songs, with the following columns:

1- id (integer): the unique identifier for the song.
2- title (text): the title of the song.
3- artist (text): the artist who performed the song.
4- genre (text): the genre of the song.
5- year (integer): the year the song was released.

## Contacts
For any questions or feedback, please contact us at [ahmad-mujtaba.com](http://www.ahmad-mujtaba.com/)