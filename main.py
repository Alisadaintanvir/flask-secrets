from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'the night is scary'


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
