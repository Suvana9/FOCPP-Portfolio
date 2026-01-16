from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "dev-secret-key"   # REQUIRED for sessions

# Dummy users
USERS = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "student": {
        "password": "student123",
        "role": "user"
    }
}

# ---------------- HOME ----------------
@app.route('/')
def home():
    # Redirect / to login
    return redirect(url_for('login'))

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in USERS:
            if USERS[username]['password'] == password:
                session['username'] = username
                session['role'] = USERS[username]['role']
                return redirect(url_for('favorites'))
            else:
                message = "Incorrect password"
        else:
            message = "User not found"

    return render_template("login.html", message=message)

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ---------------- FAVORITES (PROTECTED) ----------------
@app.route('/favorites', methods=['GET', 'POST'])
def favorites():
    # Protect route
    if 'username' not in session:
        return redirect(url_for('login'))

    is_admin = session.get('role') == 'admin'

    # Dummy data
    global languages
    if 'languages' not in globals():
        languages = ["Python", "C++", "JavaScript"]

    message = None

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            lang = request.form.get('language')
            if lang:  # prevent empty input
                languages.append(lang)
                message = "Language added"
            else:
                message = "Please enter a language"

        elif action == 'delete_selected' and is_admin:
            selected = request.form.getlist('selected_languages')
            if selected:
                for lang in selected:
                    if lang in languages:
                        languages.remove(lang)
                message = "Selected languages deleted"
            else:
                message = "No language selected"

        elif action == 'clear' and is_admin:
            languages.clear()
            message = "All languages cleared"

        elif action == 'sort':
            languages.sort()
            message = "Languages sorted"

        else:
            message = "Unauthorized action"

    return render_template(
        "favorites.html",
        languages=languages,
        message=message,
        is_admin=is_admin
    )

# ---------------- START APP ----------------
if __name__ == '__main__':
    app.run(debug=True)
