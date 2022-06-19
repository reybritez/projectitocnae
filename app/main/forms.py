from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Accepts a nickname and a room."""
    name = StringField('Nombre', validators=[DataRequired()])
    room = SelectField(u'Sala', choices=[('Primero Primera BATAN', '1ro 1ra BATAN'), ('Segundo Segunda BTC', '2do 2da BTC'), ('Tercero Tercera BTI', '3ro 3ra BTI')], validators=[DataRequired()])
   
    submit = SubmitField('Ingresa al chat')
