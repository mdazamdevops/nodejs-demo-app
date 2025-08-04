from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todos")
    todos = c.fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

# ➕ Add Task
@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM todos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
