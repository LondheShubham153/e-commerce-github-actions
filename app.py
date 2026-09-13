from flask import Flask, render_template

app = Flask(__name__)

def login(app_secret):
    print("logging in with password",app_secret)


@app.route('/')
def home():
    app_secret = "xhdasjd5524==ere"
    login(app_secret)
    return render_template('index.html')