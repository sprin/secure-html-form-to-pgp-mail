import logging

from secure_html_form_to_pgp_mail.app import app_factory

app = app_factory()

# Set up logging

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(app.config['LOGLEVEL'])

# Log configuration parameters
app.logger.info('Configuration parameters:\n{}'.format(
    '\n'.join([k + '=' + str(v) for k, v in
               sorted(app.config.items())
               if k not in app.config['DO_NOT_LOG_VARS']])))

# Make `application` alias for uwsgi/pypy
# See https://github.com/unbit/uwsgi/issues/900
application = app
