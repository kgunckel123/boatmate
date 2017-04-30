from flask_wtf import FlaskForm
from wtforms import BooleanField, TextAreaField
from wtforms.validators import DataRequired

class AddWeight(FlaskForm):
    ballot_entry = TextAreaField('Name', validators=[DataRequired()])
    delete_first_column = BooleanField('delete_first_column', default=False)
    delete_first_row = BooleanField('delete_first_row', default=False)