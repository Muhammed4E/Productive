# Productive - Simple Note Taking App

![Project Mockup](https://github.com/Muhammed4E/Productive/blob/main/images/mockup.png?raw=true)

This is a simple note-taking web application built with Flask, SQLite3, HTML, CSS, JavaScript, and Jinja. The application allows users to add, edit, delete, and view their notes conveniently.

## Installation

Before running the application, ensure you have Python installed on your system. You can install Flask and other dependencies by running:

```bash
pip install -r requirements.txt
```

## Usage

To start the application, run the following command:

```bash
python app.py
```

Once the application is running, you can access it by navigating to `http://localhost:5000` in your web browser.

## Project Structure

```
├── __pycache__
├── flask_session
├── static
│   └── (CSS and JavaScript files)
├── templates
│   └── (HTML templates)
├── README.md
├── app.py
├── productive.db
└── requirements.txt
```

- `__pycache__`: Directory containing Python bytecode files.
- `flask_session`: Directory containing Flask session files.
- `static`: Directory containing static files such as CSS and JavaScript.
- `templates`: Directory containing HTML templates used by Jinja.
- `README.md`: This file, containing project documentation.
- `app.py`: The main Python script for the Flask application.
- `productive.db`: SQLite3 database file storing notes data.
- `requirements.txt`: File listing all Python dependencies required by the application.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
