# from flask import Flask
from flask import Flask, request, render_template
app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')


def hello_world():
    return 'Hello, World!\n This looks great within 5 minutes'

if _name_ == '_main_':
    app.run()
