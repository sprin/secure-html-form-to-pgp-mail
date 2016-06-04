from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class ContactForm(Form):
    content = TextAreaField('content', validators=[DataRequired()])
