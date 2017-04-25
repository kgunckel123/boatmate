from flask_wtf import FlaskForm
from wtforms import BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class BoatInputForm(FlaskForm):
    pontoon_neither = IntegerField(label='Pontoon Neither', default=0)
    pontoon_neither = IntegerField(label='Pontoon Neither', default=0)
    pontoon_neither = IntegerField(label='Pontoon Neither', default=0)
    pontoon_neither = IntegerField(label='Pontoon Neither', default=0)




    ballot_entry = TextAreaField('Ballots', validators=[DataRequired()])
    delete_first_column = BooleanField('delete_first_column', default=False)
    delete_first_row = BooleanField('delete_first_row', default=False)

