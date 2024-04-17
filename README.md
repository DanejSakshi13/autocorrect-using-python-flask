# Autocorrect using Python Flask

This project demonstrates a simple autocorrect feature implemented using Python and Flask. It suggests corrections for misspelled words based on the similarity of the input word to the words in a given vocabulary.

## Installation

1. Clone the repository:
git clone https://github.com/DanejSakshi13/autocorrect-using-python-flask.git


2. Navigate to the project directory:
cd autocorrect-using-python-flask

3. Install dependencies


## Usage

1. Run the Flask application:
python app.py


2. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Enter a word in the input field and click the "Autocorrect" button.

4. The autocorrected words, along with their probabilities and similarities, will be displayed in a table below.

## Code Structure

- `app.py`: Contains the Flask application that serves the autocorrect functionality.
- `index.html`: HTML template for the web interface.
- `book.txt`: Sample text file used to build the vocabulary for autocorrection.
- `README.md`: Documentation file (you're currently reading it).

## Dependencies

- Flask: A lightweight WSGI web application framework in Python.
- textdistance: A Python library for comparing and matching strings.
- Jinja2: A modern and designer-friendly templating engine for Python.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.


