from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secret key for production

# Initialize Flask-Assignment-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Simple in-memory user database for demonstration purposes
users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}

# User class for Flask-Assignment-Login
class User(UserMixin):
    pass

# Function to load a user from the user database
@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user

# Routes
@app.route('/')
@login_required
def home():
    return f'Hello, {current_user.id}! <a href="/logout">Logout</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User()
            user.id = username
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
