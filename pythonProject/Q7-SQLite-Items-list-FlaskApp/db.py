from flask import Flask
import sqlite3

app = Flask(__name__)

DATABASE = 'items.db'
def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    with connect_db() as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

init_db()