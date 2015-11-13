from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from portal import app, db, lm
from forms import LoginForm
from models import User, ROLE_EXT_USER, ROLE_ADMIN, ROLE_CLAN_LEAD, ROLE_CLAN_MEMBER, ROLE_MODERATOR, ROLE_OFFICER, ROLE_RAID_LEADER

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title = 'Home', user = current_user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sign In', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = current_user