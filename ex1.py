# app.py
from flask import Flask

#Welcome 
app = Flask(_name_)

@app.route('/')
def welcome():
    return 'Welcome to my web application!'

if _name_ == '_main_':
    app.run(debug=True)
