from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertiesForm(FlaskForm):
    propertyTitle = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    bedrooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    propertyType = SelectField(u'Property Type', choices=[('House'), ('Apartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Only Images Allowed!')])