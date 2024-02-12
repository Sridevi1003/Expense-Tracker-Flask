from flask import Flask, render_template, request, redirect, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
import sqlite3 as db

app = Flask(__name__)
app.config['SECRET_KEY'] = '@123456789'  # Change this to a secret key for production use


# Define a function to check user authentication
def authenticate_user(username, password):
    connection = db.connect("expenseTracker.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    connection.close()
    return user


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = authenticate_user(username, password)
        if user:
            session['username'] = user[1]  # Storing username in session
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')


# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    flash('You have been logged out', 'success')
    return redirect('/')


# ExpenseForm definition
class ExpenseForm(FlaskForm):
    date = StringField('Date', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    expense = IntegerField('Expense', validators=[DataRequired()])


# Initialize database
def init():
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    query = '''
    create table if not exists expenses (
        date string,
        name string,
        title string,
        expense number
        )
    '''
    curr.execute(query)
    connectionObjn.commit()


# Index route
@app.route('/')
def index():
    init()
    form = ExpenseForm()
    return render_template('index.html', form=form)


# Submit route
@app.route('/submit', methods=['POST'])
def submit():
    form = ExpenseForm(request.form)
    if form.validate_on_submit():
        values = [form.date.data, form.name.data, form.title.data, form.expense.data]
        connectionObjn = db.connect("expenseTracker.db")
        curr = connectionObjn.cursor()
        query = '''
        INSERT INTO expenses VALUES (?, ?, ?, ?)
        '''
        curr.execute(query, values)
        connectionObjn.commit()
    return redirect('/')


# View expenses route
@app.route('/view')
def view():
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    query = '''
    SELECT * FROM expenses
    '''
    total = '''
    SELECT sum(expense) FROM expenses
    '''
    curr.execute(query)
    rows = curr.fetchall()
    curr.execute(total)
    amount = curr.fetchall()[0]
    return render_template('view.html', rows=rows, amount=amount)


if __name__ == '__main__':
    app.run(debug=True)
