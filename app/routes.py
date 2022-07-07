from app import app
from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm


@app.route('/')
@app.route("/index")
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Nice day in Portland'
        },
        {
            'author': {'username': 'Jane'},
            'body': 'Nice day in Kingston'
        },
        {
            'author': {'username': 'Jack'},
            'body': 'Nice day in Luxemburg'
        },
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login by user {} successful. Account remembered: {}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)