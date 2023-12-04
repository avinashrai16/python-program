from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Set a secret key for the session
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return '<h1>Welcome to the Flask Sessions Example!</h1> <h3><a href = "/login" >login</a></h3>'


# Visit http://127.0.0.1:5000/login to log in with a username.
# After logging in, you can visit http://127.0.0.1:5000/greet to see a personalized greeting with the username stored in the session.
# The "Logout" link allows you to clear the session and log out.

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username from the form
        username = request.form['username']

        # Store the username in the session
        session['username'] = username

        return redirect(url_for('greet'))

    return render_template('login.html')

@app.route('/greet')
def greet():
    # Retrieve the username from the session
    username = session.get('username', 'Guest')

    # Render a template with the personalized greeting
    return render_template('greet_session.html', username=username)

@app.route('/logout')
def logout():
    # Clear the session to log the user out
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
