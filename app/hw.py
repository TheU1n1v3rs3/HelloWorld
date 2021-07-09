from flask import Flask

app= Flask(__name__)

@app.route('/')
def hwi():
    return "<h1>Hello to Welt!!</h1>"
