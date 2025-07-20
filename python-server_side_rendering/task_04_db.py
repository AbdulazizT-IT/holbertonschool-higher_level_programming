from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

def read_sqlite_file(product_id=None):
    try:
        conn = sqlite3.connect("products.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if product_id:
            cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except Exception as e:
        return {"error": str(e)}

@app.route('/products')
def products():
    source = request.args.get("source")
    id_param = request.args.get("id")

    # تحقق من صلاحية source
    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source", products=None)

    # جلب البيانات من المصدر المناسب
    product_list = []
    if source == "json":
        product_list = read_json_file()
    elif source == "csv":
        product_list = read_csv_file()
    elif source == "sql":
        product_list = read_sqlite_file(id_param)
        if not product_list:  # <= هذا الشرط يكتشف أن ID غير موجود
            return render_template("product_display.html", error="Product not found", products=None)

    # في حال وجود خطأ من قاعدة البيانات
    if isinstance(product_list, dict) and "error" in product_list:
        return render_template("product_display.html", error=product_list["error"], products=None)

    # فلترة ID (إن لم تكن SQL فعلًا)
    if id_param and source != "sql":
        try:
            product_id = int(id_param)
            filtered = [p for p in product_list if p["id"] == product_id]
            if not filtered:
                return render_template("product_display.html", error="Product not found", products=None)
            return render_template("product_display.html", products=filtered)
        except ValueError:
            return render_template("product_display.html", error="Invalid ID", products=None)

    return render_template("product_display.html", products=product_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
