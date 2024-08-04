from flask import render_template, request
from todolist import app
from todolist.forms import LoginForm


@app.route('/')
def return_main_page():
    return render_template('main_page.html')


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
