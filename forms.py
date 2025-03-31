from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class StaffForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    role = StringField('Role')
    department = StringField('Department')
    submit = SubmitField('Submit')