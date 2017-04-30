from flask_wtf import FlaskForm
from wtforms import BooleanField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired

class AddWeight(FlaskForm):
    ballot_entry = TextAreaField('Name', validators=[DataRequired()])
    delete_first_column = IntegerField('Weight', default=0, validators=[DataRequired()])
    item_type = SelectField(choices=[('Trailer', 'Trailer'), ('Component', 'Component')])