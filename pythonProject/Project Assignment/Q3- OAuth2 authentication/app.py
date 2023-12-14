from flask import Flask, redirect, url_for, session,request
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key='610763299201-qhguhv62spdrh4dfqc7q52jc51fu97nk.apps.googleusercontent.com',
    consumer_secret='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',
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
)

# Redirect URI should be specified in your Google Developer Console

@app.route('/')
def index():
    return 'Welcome to OAuth with Google using Flask! <a href="/login">Login with Google</a>'

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return 'Logged out'

@app.route('/login/authorized')
def authorized():
    response = google.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )

    session['google_token'] = (response['access_token'], '')
    user_info = google.get('userinfo')

    # Here you can use user_info to get user details
    return 'Logged in as: ' + user_info.data['email']

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

if __name__ == '__main__':
    app.run(debug=True)
