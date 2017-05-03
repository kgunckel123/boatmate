from flask_wtf import FlaskForm
from wtforms import BooleanField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired

class AddWeight(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    weight = IntegerField('Weight', default=0, validators=[DataRequired()])
    item_type = SelectField(choices=[('Trailer', 'Trailer'), ('Component', 'Component')])