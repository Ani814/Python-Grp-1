from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, TextAreaField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, NumberRange


class RegisterForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password", message="Passwords must match.")]
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class JobForm(FlaskForm):
    title = StringField("Job Title", validators=[DataRequired(), Length(max=150)])
    short_description = StringField("Short Description", validators=[DataRequired(), Length(max=300)])
    full_description = TextAreaField("Full Description", validators=[DataRequired()])
    company = StringField("Company", validators=[DataRequired(), Length(max=150)])
    salary = FloatField("Salary (GEL)", validators=[Optional(), NumberRange(min=0)])
    location = StringField("Location", validators=[DataRequired(), Length(max=150)])
    category = SelectField("Category", validators=[DataRequired()])
    submit = SubmitField("Save Job")


class ProfileForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture = FileField("Profile Picture", validators=[Optional(), FileAllowed(["jpg", "jpeg", "png", "gif"])])
    submit = SubmitField("Update Profile")
