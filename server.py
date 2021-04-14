from flask import Flask
from flask import request
from emailSend import emailSend
import datetime


import sys
sys.path.append('tax-filler')
from fillPdfData import fillPDFData

app = Flask(__name__)

@app.route('/user/<user_id>/form/<form_id>', methods = ['GET', 'POST'])
def form(user_id, form_id):
    fillPdf = fillPDFData()
    fillPdf.exec(request.json, "8843")

    email = emailSend("8843", request.json["email"])
    email.exec()

    print(request.json)
    return {
        "test" : "key",
        "dict" : "d"
    }

@app.route('/due', methods = ['GET', 'POST'])
def due():
    today = datetime.date.today()
    future = datetime.date(2021,5,17)
    diff = (future - today).days

    return {
        "days": diff
    }

if __name__ == "__main__":
    app.run(port = 3000)
