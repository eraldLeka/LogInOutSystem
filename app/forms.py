from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[ 
        DataRequired(),
        Length(min=5, max=25, message='Username must be between 5 and 25 characters.')
    ])
    password = PasswordField('Password', validators=[ 
        DataRequired(),
        Length(min=8, message='Password must be at least 8 characters long.')
    ])
    confirm = PasswordField('Confirm your password', validators=[ 
        DataRequired(),
        EqualTo('password', message='Passwords do not match.')
    ])
    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user = User.query.filter_by(username=username.data).first()
        if existing_user:
            raise ValidationError("This username already exists. Choose another!")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
