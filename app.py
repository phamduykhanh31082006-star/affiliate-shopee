from flask import Flask, render_template, request
from openpyxl import Workbook, load_workbook
import os
from datetime import datetime

app = Flask(__name__)

EXCEL_FILE = "data.xlsx"

def save_to_excel(data):
    if not os.path.exists(EXCEL_FILE):
        wb = Workbook()
        ws = wb.active
        ws.append([
            "Thời gian",
            "Họ tên",
            "Số điện thoại",
            "Email",
            "Link Shopee / MXH"
        ])
        wb.save(EXCEL_FILE)

    wb = load_workbook(EXCEL_FILE)
    ws = wb.active
    ws.append(data)
    wb.save(EXCEL_FILE)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    link = request.form["link"]

    time_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    save_to_excel([time_now, name, phone, email, link])

    return render_template("success.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
