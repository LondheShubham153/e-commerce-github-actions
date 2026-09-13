from flask import Flask, render_template

app = Flask(__name__)

DB_USER = "admin"
DB_PASSWORD = "SuperSecretPassword123!" 

def connect_db():
    print(f"Connecting to database as {DB_USER}...")
    # Connection logic here
    
def login(app_secret):
    print("logging in with password",app_secret)


@app.route('/')
def home():
    API_KEY = "xhdasjd5524==ere"
    login(API_KEY)
    return render_template('index.html')