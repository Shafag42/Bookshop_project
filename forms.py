from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length
class BookComments(FlaskForm):
    full_name = StringField(label='Tam Adınız', validators=[DataRequired()])
    comment = TextAreaField(label='Şərhiniz', validators=[DataRequired(), Length(min = 10, message=('Your message is short!'))])
class RegisterForm(FlaskForm):
    first_name = StringField(label='Adınız: ', validators=[DataRequired(), Length(min = 3, max = 30)])
    last_name = StringField(label='Soydınız: ', validators=[DataRequired(), Length(min = 3, max = 30)])
    email = EmailField(label="Elektron Ünvanınız: ", validators=[DataRequired(), Length(min = 3, max = 30)])
    username = StringField(label="İstifadəçi adınız: ", validators=[DataRequired(), Length(min = 3, max = 30)])
    password = PasswordField(label="Şifrəniz: ", validators=[DataRequired(), Length(min = 8, max = 30)])
class LoginForm(FlaskForm):
    username = StringField(label="İstifadəçi adınız: ", validators=[DataRequired(), Length(min = 3, max = 30)])
    password = PasswordField(label="Şifrəniz: ", validators=[DataRequired(), Length(min = 8, max = 30)])