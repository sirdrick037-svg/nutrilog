# NutriLog

NutriLog is a Django-based calorie tracking web application that allows users to record their meals, manage meal entries, and track their daily calorie intake.

## Features

- Add meal and calorie entries
- View meals recorded for the current day
- Calculate total calories for the day
- Edit existing meal entries
- Delete meal entries
- Reset today's meals and calorie total
- Form validation
- CSRF protection for POST requests
- Responsive user interface
- Tailwind CSS styling
- SQLite database for local development

## Technologies Used

- Python
- Django
- SQLite
- HTML5
- Tailwind CSS
- Git/GitHub

## Project Structure

```text
nutrilog/
├── meal_log/
│   ├── migrations/
│   ├── templates/
│   │   └── meal_log/
│   │       ├── base.html
│   │       ├── home.html
│   │       └── edit_meal.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── nutrilog/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md