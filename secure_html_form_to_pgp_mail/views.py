from flask import redirect, send_from_directory
from flask_mail import Message
from .forms import ContactForm
from . import _compat

def index(mail, title, recipient):
    def inner():
        form = ContactForm()
        if form.validate_on_submit():
            print(form.content.data)
            msg = Message(title, recipients=[recipient])
            msg.body = form.content.data
            print(msg)
            mail.send(msg)
            return redirect('/')
        return send_from_directory('../static', 'contact.html')
    return inner

def csrf_token():
    # Create dummy form to generate CSRF token
    form = ContactForm()
    return _compat.to_unicode(form.csrf_token._value())
