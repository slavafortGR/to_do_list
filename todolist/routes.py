from todolist.models import User, Task, Week
from flask import render_template, request, session, redirect, url_for, flash
from todolist import app
from todolist.forms import LoginForm
from werkzeug.security import check_password_hash


@app.route('/')
def return_main_page():
    return render_template('main_page.html')

@app.route('/home_page', methods=['GET'])
def return_home_page():
    user_id = session.get('user_id')
    week_id= session.get('week_id')
    if user_id:
        user = User.query.filter_by(id=user_id).first()
        week = Week.query.filter_by(owner=user_id).first()
        tasks = Task.query_by(belong=week_id, active=True).all()

        return render_template('home_page.html', user=user, week=week, tasks=tasks)
    else:
        return redirect(url_for('login_user_get'))


@app.route('/login', methods=['GET'])
def login_user_get():
    login_form = LoginForm(request.form)
    return render_template('login_register.html', login_tab=True, login_form=login_form)


@app.route('/login', methods=['POST'])
def login_user_post():
    login_form = LoginForm(request.form)

    if login_form.validate_on_submit():
        nick_name = login_form.nick_name.data
        password = login_form.password.data

        user = User.query.filter_by(nick_name=nick_name).first()
        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details and try again.", "danger")
            return redirect(url_for('login_user_get'))
        else:
            session['user_id'] = user.id
            return redirect(url_for("return_home_page"))

    flash("Invalid input. Please check your details and try again.", "danger")
    return redirect(url_for("login_user_get"))
