import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# show individual activity
def get_activity(activity_id):
    conn = get_db_connection()
    activity = conn.execute('SELECT * FROM activities WHERE id = ?',
                        (activity_id,)).fetchone()
    conn.close()
    if activity is None:
        abort(404)
    return activity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    conn = get_db_connection()
    activities = conn.execute('SELECT * FROM activities').fetchall()
    conn.close()
    return render_template('index.html', activities=activities)

@app.route('/<int:activity_id>')
def activity(activity_id):
    activity = get_activity(activity_id)
    return render_template('activity.html', activity=activity)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO activities (title, description) VALUES (?, ?)',
                         (title, description))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    activity = get_activity(id)

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE activities SET title = ?, description = ?'
                         ' WHERE id = ?',
                         (title, description, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', activity=activity)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    activity = get_activity(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM activities WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(activity['title']))
    return redirect(url_for('index'))