from flask import Flask
from flask import request
from emailSend import emailSend

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

if __name__ == "__main__":
    app.run(port = 80)
