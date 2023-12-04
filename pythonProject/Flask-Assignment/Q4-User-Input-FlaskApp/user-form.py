from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def load_user_form():
    return render_template("user-input.html")

@app.route("/greetings")
def greet_user():
    first_name = request.args.get('firstName')
    last_name = request.args.get('lastName')
    return f"Hello {first_name} {last_name} ! Thanks for the input."

if __name__ == "__main__":
    app.run(host="0.0.0.0")
