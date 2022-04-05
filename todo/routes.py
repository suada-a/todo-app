from todo import app
from flask import render_template, redirect, url_for
from todo.models import Task
from todo.forms import *
from todo import db

@app.route('/', methods=['GET'])
@app.route('/home')
def home_page():
    add_task_form = AddTaskForm()
    edit_task_form = EditTaskForm()
    complete_task_form = CompleteTaskForm()
    delete_task_form = DeleteTaskForm()
    
    tasks = Task.query.all()
    return render_template('index.html', add_task_form=add_task_form, edit_task_form=edit_task_form,
    complete_task_form=complete_task_form, delete_task_form=delete_task_form, tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    add_task_form = AddTaskForm()
    edit_task_form = EditTaskForm()
    complete_task_form = CompleteTaskForm()
    delete_task_form = DeleteTaskForm()

    if add_task_form.validate_on_submit():
        new_task = Task(description=add_task_form.description.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home_page'))
    
    return render_template('index.html', add_task_form=add_task_form, edit_task_form=edit_task_form,
    complete_task_form=complete_task_form, delete_task_form=delete_task_form)

@app.route('/edit', methods=['POST'])
def edit():
    add_task_form = AddTaskForm()
    edit_task_form = EditTaskForm()
    complete_task_form = CompleteTaskForm()
    delete_task_form = DeleteTaskForm()

    if edit_task_form.validate_on_submit():
        new_description = edit_task_form.description.data
        current_task_id = edit_task_form.task_id.data
        current_task = Task.query.get(current_task_id)
        current_task.description = new_description
        db.session.commit()

        return redirect(url_for('home_page')) 
    
    return render_template('index.html', add_task_form=add_task_form, edit_task_form=edit_task_form,
    complete_task_form=complete_task_form, delete_task_form=delete_task_form)

@app.route('/complete', methods=['POST'])
def complete():
    add_task_form = AddTaskForm()
    edit_task_form = EditTaskForm()
    complete_task_form = CompleteTaskForm()
    delete_task_form = DeleteTaskForm()

    if complete_task_form.validate_on_submit():
        current_task_id = complete_task_form.task_id.data
        current_task = Task.query.get(current_task_id)
        current_task.complete = True
        db.session.commit()

        tasks = Task.query.all()
        return render_template('index.html', add_task_form=add_task_form, edit_task_form=edit_task_form,
        complete_task_form=complete_task_form, delete_task_form=delete_task_form, tasks=tasks)

    return redirect(url_for('home_page'))

@app.route('/delete', methods=['POST'])
def delete():
    add_task_form = AddTaskForm()
    edit_task_form = EditTaskForm()
    complete_task_form = CompleteTaskForm()
    delete_task_form = DeleteTaskForm()

    if delete_task_form.validate_on_submit():
        current_task_id = edit_task_form.task_id.data
        current_task = Task.query.get(current_task_id)
        db.session.delete(current_task)
        db.session.commit()

        return redirect(url_for('home_page'))
    
    return render_template('index.html', add_task_form=add_task_form, edit_task_form=edit_task_form,
    complete_task_form=complete_task_form, delete_task_form=delete_task_form)

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/login')
def login_page():
    return render_template('login.html')