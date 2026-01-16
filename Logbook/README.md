# Flask Learning App

## Description
Flask Learning App is a beginner-friendly web application that demonstrates
core Flask and Python web development concepts.  
It includes authentication, session management, template inheritance,
form handling, and role-based access control.

The app allows users to log in, greet users with string operations,
and manage a list of favorite programming languages.
Admin users have additional permissions.

## File Overview

### `app.py`
- Main Flask application
- Handles routing, sessions, login logic, and protected pages
- Manages user roles (admin / user)
- Controls favorites functionality

### `static/style.css`
- Styles the application layout, fonts, navigation, and buttons

### `templates/base.html`
- Base layout template
- Contains navigation bar and shared page structure
- Extended by all other templates

### `templates/index.html`
- Home page
- Introduces the Flask Learning App

### `templates/login.html`
- Login form for users
- Displays error messages for invalid credentials

### `templates/greet.html`
- Allows users to enter a name
- Displays a greeting and string operation results

### `templates/favorites.html`
- Protected page (login required)
- Users can add and sort favorite programming languages
- Admin users can:
  - Delete selected languages
  - Clear all languages

## Features

- Flask routing and URL handling
- Template inheritance with Jinja2
- HTML forms using POST requests
- User authentication with sessions
- Role-based access control
- Protected routes
- Greeting page with dynamic output
- Favorites management
- Admin-only actions
- Logout functionality

## Default Users

### Admin Account
- **Username:** admin  
- **Password:** admin123  

### Student Account
- **Username:** student  
- **Password:** student123  

## Requirements

- Python 3.x
- Flask
Install Flask:
```bash
pip install flask

## How to run
1.Open a terminal in the project directory
2.Run the Flask application:
python app.py
Open a browser and visit:
http://127.0.0.1:5000/

## Notes
1.User data is hardcoded for learning purposes
2.Favorite languages are stored in memory
3.Data resets when the app restarts
4.Debug mode is enabled for development only

Author
Suvana Gajurel