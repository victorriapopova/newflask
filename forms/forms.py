# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, SubmitField
from wtforms.validators import DataRequired, URL

class AddHeadphoneForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    description = TextAreaField('Описание')
    price = FloatField('Цена', validators=[DataRequired()])
    image_url = StringField('URL изображения', validators=[DataRequired(), URL()])
    submit = SubmitField('Добавить')
