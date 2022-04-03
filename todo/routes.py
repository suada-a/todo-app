from todo import app
from flask import render_template, redirect, url_for
from todo.models import Task
from todo.forms import AddTaskForm
from todo import db

@app.route('/', methods=['POST', 'GET'])
@app.route('/home')
def home_page():
    add_task_form = AddTaskForm()
    if add_task_form.validate_on_submit():
        new_task = Task(description=add_task_form.description.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home_page'))

    tasks = Task.query.all()
    return render_template('index.html', add_task_form=add_task_form, tasks=tasks)

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/login')
def login_page():
    return render_template('login.html')