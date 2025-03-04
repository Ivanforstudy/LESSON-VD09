from flask import Flask, render_template, redirect, url_for, flash
from app.forms import RegistrationForm, LoginForm  # Убедитесь, что путь правильный
from app.models import User  # Импортируйте User, если он используется
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Или другой URI
db = SQLAlchemy(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Здесь должна быть логика сохранения пользователя
        flash('Регистрация прошла успешно!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Здесь должна быть логика аутентификации
        flash('Вы вошли в систему!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

