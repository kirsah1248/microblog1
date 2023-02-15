from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, OtherForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/songs')
def songs():
    return render_template('songs.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Logged in")
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/other_form', methods=['GET', 'POST'])
def other_form():
    form = OtherForm()
    if form.validate_on_submit():
        flash("Grades Entered")
        return redirect(url_for('index'))
    return render_template('other_form.html', title='Enter Grades', form=form)
