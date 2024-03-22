from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        message = request.form['message']
        save_message(message)
        return redirect(url_for('index'))

def save_message(message):
    connection = sqlite3.connect('messages.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO messages (content) VALUES (?)', (message,))
    connection.commit()
    connection.close()

if __name__ == '__main__':
    app.run(debug=True)

