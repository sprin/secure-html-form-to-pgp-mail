from flask import redirect, send_from_directory
from flask_mail import Message
from . import forms

def index():
        """GET - sends the static contact HTML.

        It is better to configure the web server to send the contact HTML
        directly, rather than let Flask handle it.
        """
        return send_from_directory('../static', 'contact.html')

def handle_contact_form(mail, title, recipient):
    """Wrapper function for POST handler to inject configuration parameters.

    Allows us to avoid references to the app or config object here.
    """
    def inner():
        """Process the contact form, validating the CSRF token. Send the email
        if valid.
        """
        form = forms.ContactForm()
        if form.validate_on_submit():
            msg = Message(title, recipients=[recipient])
            msg.body = form.content.data
            mail.send(msg)
            return 'OK'
    return inner

def csrf_token():
    # Create dummy form to generate CSRF token
    form = forms.ContactForm()
    return form.csrf_token._value()
