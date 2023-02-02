from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map


class ShippingForm(FlaskForm):
  sender = StringField('Sender', validators=[DataRequired()])
  recipient = StringField('Recipient',validators=[DataRequired()])
  origin = SelectField('Origin', choices=[*map.keys()], validators=[DataRequired()])
  destination = SelectField('Destination', choices=[*map.keys()], validators=[DataRequired()])
  express = BooleanField('Express', validators=[DataRequired()])
  submit = SubmitField('Submit')
  cancel = SubmitField('Cancel')
