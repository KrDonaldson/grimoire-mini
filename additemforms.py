from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddItemForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    details = StringField('Details', validators = [DataRequired()])
    submit_button = SubmitField()