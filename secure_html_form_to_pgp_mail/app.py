"""Factory function for the WSGI application object.
"""
import os

import flask
from flask_wtf.csrf import CsrfProtect
from flask_mail import Mail

from . import config
from . import views

def app_factory():
    """Factory function for the WSGI application object.

    Reads config, initializes Flask extensions that are part of the core,
    loads pg-config drivers and extensions, and configures core views.
    """
    # Flask application
    app = flask.Flask('flask-html-form-to-gpg')
    app.root_path = os.path.abspath(os.path.dirname(__file__))

    # Load default config value
    app.config.from_object(config)

    # Load custom config from user-defined file
    custom_settings = os.environ.get('SETTINGS_FILE',
                                     './local_settings.py')
    if custom_settings and os.path.isfile(custom_settings):
        app.config.from_pyfile(custom_settings)

    CsrfProtect(app)
    mail = Mail(app)

    app.route('/', methods=['GET'])(views.index)
    app.route('/post', methods=['POST'])(views.handle_contact_form(
        mail, app.config['MAIL_TITLE'], app.config['MAIL_RECIPIENT']))
    app.route('/csrf_token', methods=['GET'])(views.csrf_token)

    return app
