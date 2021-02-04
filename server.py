from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/user/<user_id>/form/<form_id>', methods = ['GET', 'POST'])
def form(user_id, form_id):
    print(request.json)
    return "xyz"

if __name__ == "__main__":
    app.run(port = 80)
