from flask import render_template
from todolist import app


@app.route('/')
def return_main_page():
    return render_template('main_page.html')
