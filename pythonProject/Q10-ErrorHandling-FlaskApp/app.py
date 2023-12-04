from flask import Flask, render_template

app = Flask(__name__)

# Define a route that will result in a 404 error
@app.route('/not_found')
def not_found():
    # Force a 404 error by trying to access a non-existing page
    return render_template('not_found.html'), 404

# Define a route that will result in a 500 error
@app.route('/internal_server_error')
def internal_server_error():
    # Force a 500 error by raising an exception
    raise Exception("This is a simulated internal server error")

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_server_error_handler(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
