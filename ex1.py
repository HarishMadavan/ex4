# app.py
from flask import Flask

# Welcome
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my web application!'

if __name__ == '__main__':
    app.run(debug=True)
