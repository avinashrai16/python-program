from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/")
def show_form():
    return render_template("index.html")
@app.route("/productList")
def show_product_list():
    return render_template("products.html")

@app.route("/serviceList")
def show_service_list():
    return render_template("services.html")
@app.route("/back")
def go_back():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
