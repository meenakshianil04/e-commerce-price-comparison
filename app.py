from flask import Flask, render_template, request
from scraper import compare_prices

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    product = ""

    if request.method == "POST":
        product = request.form["product"]
        results = compare_prices(product)

    return render_template("index.html", results=results, product=product)

if __name__ == "__main__":
    app.run(debug=True)
