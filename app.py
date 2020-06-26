from flask import Flask, render_template, abort, flash, url_for
from config import Production
from flask_bootstrap import Bootstrap
from form import MailForm
from flask_mail import Mail, Message
from email_validator import validate_email, EmailSyntaxError


app = Flask(__name__)
app.config.from_object(Production)


bootstrap = Bootstrap(app)
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MailForm()

    if form.validate_on_submit():
        mail_from = None

        if not form.mail_from.data:
            mail_from = ('Anonymous Mail', 'anonymousmail@no-reply.com')

        try: 
            validate_email(form.mail_from.data)
            mail_from = form.mail_from.data
        except EmailSyntaxError:
            mail_from = (form.mail_from.data, 'anonymousmail@no-reply.com')

        msg = Message(
            subject=form.subject.data, 
            recipients=[form.to.data],
            sender=mail_from,
            body=form.text.data
        )

        try:
            mail.send(msg)
            flash('Email has been sent successfully.', 'success')

            # to make form fields empty
            for field in form:
                field.data = ''

            return render_template('index.html', form=form)
        except: # in case of having any error while sending email
            abort(500)

    return render_template('index.html', form=form)



@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='favicon.ico')



@app.errorhandler(500)
def err_500(er):
    return render_template('500.html'), 500




if __name__ == '__main__':
    app.run()