from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class SpiderForm(FlaskForm):
    scientific_name = StringField('Scientific Name', validators=[DataRequired()])
    characteristic_1 = StringField('Characteristic 1', validators=[DataRequired()])
    characteristic_2 = StringField('Characteristic 2', validators=[DataRequired()])
    characteristic_3 = StringField('Characteristic 3', validators=[DataRequired()])
    submit = SubmitField('Submit')