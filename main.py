from enum import unique
from flask import Flask, render_template, redirect, request, url_for, session
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms .validators import InputRequired, Length, ValidationError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://moringa:1234@localhost/register"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SECRET KEY'] = "1234code"
app.secret_key = "1234code"
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})


Submit = SubmitField("Register")


def validate_username(self, username):
    existing_user_name = User.query.filter_by(username=username.data).first()
    if existing_user_name:
        raise ValidationError(
            "That username already exists.Please choose a different one")


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})


Submit = SubmitField("Login")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.secret_key = "1234code"
    app.run(debug=True)
