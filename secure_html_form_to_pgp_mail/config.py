"""Base configuration and configuration helper functions.

Defaults are appropriate for production use.
"""
import logging

LOGLEVEL = logging.INFO

#: List of parameters which should not be logged. This should list any
#: configuration parameters which include secrets, such as SECRET_KEY.
DO_NOT_LOG_VARS = [
    'SECRET_KEY',
    'MAIL_PASSWORD',
]

#: Default title of emails sent by backend.
MAIL_TITLE = 'PGP Message'
