from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, bcrypt  # Импортируем app, db и bcrypt
from app.models import User
from app.forms import LoginForm, RegistrationForm

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            # Здесь вы можете добавить логику для создания пользователя
            flash('Регистрация прошла успешно!', 'success')
            return redirect(url_for('login'))
        return render_template('register.html', form=form)

    return render_template("register.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Неверно введены данные аккаунта', 'danger')

    return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/click')
@login_required
def click():
    current_user.clicks += 1
    db.session.commit()
    flash('Вы кликнули!', 'info')
    return redirect(url_for('index'))



