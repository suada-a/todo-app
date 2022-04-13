from todo import app
from flask import render_template, redirect, url_for, flash, request
from todo.models import Task, User
from todo.forms import *
from todo import db
from flask_login import login_required, login_user, logout_user, current_user

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home_page():
    add_task_form = AddTaskForm()
    edit_task_form = EditTaskForm()
    complete_task_form = CompleteTaskForm()
    delete_task_form = DeleteTaskForm()
    
    tasks = Task.query.filter_by(user_id = current_user.get_id())

    return render_template('index.html', add_task_form=add_task_form, edit_task_form=edit_task_form,
    complete_task_form=complete_task_form, delete_task_form=delete_task_form, tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    add_task_form = AddTaskForm()
    edit_task_form = EditTaskForm()
    complete_task_form = CompleteTaskForm()
    delete_task_form = DeleteTaskForm()

    if add_task_form.validate_on_submit():
        new_task = Task(user_id=current_user.get_id(), description=add_task_form.description.data)
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

@app.route('/complete', methods=['GET', 'POST'])
def complete():
    add_task_form = AddTaskForm()
    edit_task_form = EditTaskForm()
    complete_task_form = CompleteTaskForm()
    delete_task_form = DeleteTaskForm()

    if request.method == 'POST':
        if complete_task_form.validate_on_submit():
            current_task_id = complete_task_form.task_id.data
            current_task = Task.query.get(current_task_id)
            current_task.complete = True
            db.session.commit()
            return redirect(url_for('home_page'))
            
    if request.method == 'GET':
        tasks = Task.query.all()
        return render_template('index.html', add_task_form=add_task_form, edit_task_form=edit_task_form,
        complete_task_form=complete_task_form, delete_task_form=delete_task_form, tasks=tasks)

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

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        email_address=form.email_address.data,
                        password=form.password.data)

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash(f'Welcome {new_user.username}!', category='success')
        return redirect(url_for('home_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating the account: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        entered_user = User.query.filter_by(username=form.username.data).first()

        if entered_user and entered_user.check_password(entered_password=form.password.data):
            login_user(entered_user)
            flash('Successfully logged in', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Invalid username or password. Try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been successfully logged out', category='info')
    return redirect(url_for('login_page'))
