from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Flask URL Parameters Example!'


# http://127.0.0.1:5000/greet?name=avinash  this will display as per the name parameter i.e. avinash in this case
# http://127.0.0.1:5000/greet # this will display default i.e. guest
@app.route('/greet', methods=['GET'])
def greet():
    # Get the 'name' parameter from the URL
    name = request.args.get('name', 'Guest')

    # Render a template with the personalized greeting
    return render_template('greet.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
