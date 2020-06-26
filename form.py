from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class MailForm(FlaskForm):
    to         = StringField('To', validators=[DataRequired(), Email()])
    mail_from  = StringField('From')
    subject    = StringField('Subject')
    text       = TextAreaField('Message', validators=[DataRequired()], render_kw={'rows': 5})
    recaptcha  = RecaptchaField()
    send       = SubmitField('Send')
