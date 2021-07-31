from flask import Flask
import ctypes

app= Flask(__name__)

@app.route('/')
def hwi():
    ctypes.windll.user32.LockWorkStation()
    return "<h1>Hello to Welt!!</h1>"
