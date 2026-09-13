from flask import Flask, render_template

app = Flask(__name__)

def login(app_secret):
    print("logging in with password",app_secret)


@app.route('/')
def home():
    API_KEY = "xhdasjd5524==ere"
    login(API_KEY)
    return render_template('index.html')