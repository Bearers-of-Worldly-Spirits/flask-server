from flask import Flask
from flask import request
from emailSend import emailSend

import sys
sys.path.append('tax-filler')
from fillPdfData import fillPDFData

app = Flask(__name__)

@app.route('/user/<user_id>/form/<form_id>', methods = ['GET', 'POST'])
def form(user_id, form_id):

    raw_dict = {
        "state": "CA",
        "days2018": 343,
        "phone": 8082567179,
        "email": "dev@josharnold.me",
        "days2020": 365,
        "zipCode": 95616,
        "dob": -39565320,
        "ssn": 111-111-111,
        "apt": 123,
        "countryOfCitizenship": "New Zealand",
        "passportNumber": "ABC123",
        "visa": "F1",
        "city": "Davis",
        "days2019": 350,
        "filedBefore": 1,
        "name": "Josh Arnold"
    }

    fillPdf = fillPDFData()
    fillPdf.exec(raw_dict, "8843")

    email = emailSend("8843")
    email.exec()

    print(request.json)
    return {
        "test" : "key",
        "dict" : "d"
    }

if __name__ == "__main__":
    app.run(port = 8080)
