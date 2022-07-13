from flask_wtf import FlaskForm

class LoginForm(FlaskForm):

    employee_number = StringField("Employee number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])