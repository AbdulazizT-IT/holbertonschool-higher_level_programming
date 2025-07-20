from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file():
    with open("products.json", "r") as f:
        return json.load(f)

def read_csv_file():
    products = []
    with open("products.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = {
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            }
            products.append(product)
    return products

@app.route('/products')
def products():
    source = request.args.get("source")
    id_param = request.args.get("id")

    if source not in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source", products=None)

    # Load data
    if source == "json":
        product_list = read_json_file()
    else:
        product_list = read_csv_file()

    # Filter by ID if provided
    if id_param:
        try:
            product_id = int(id_param)
            filtered = [p for p in product_list if p["id"] == product_id]
            if not filtered:
                return render_template("product_display.html", error="Product not found", products=None)
            return render_template("product_display.html", products=filtered)
        except ValueError:
            return render_template("product_display.html", error="Invalid ID", products=None)

    return render_template("product_display.html", products=product_list)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
