from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# SQLite database configuration
DATABASE = 'items.db'

# Function to connect to the database
def connect_db():
    return sqlite3.connect(DATABASE)

# Route to display all items
@app.route('/')
def show_items():
    with connect_db() as db:
        cursor = db.execute('SELECT id, name FROM items ORDER BY id DESC')
        items = cursor.fetchall()
    return render_template('show_items.html', items=items)

# Route to add a new item
@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form['name']
    with connect_db() as db:
        db.execute('INSERT INTO items (name) VALUES (?)', [item_name])
        db.commit()
    return redirect(url_for('show_items'))

# Route to delete an item
@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    with connect_db() as db:
        db.execute('DELETE FROM items WHERE id = ?', [item_id])
        db.commit()
    return redirect(url_for('show_items'))

if __name__ == '__main__':
    app.run(debug=True)
