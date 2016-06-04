"""Base configuration and configuration helper functions.

Defaults are appropriate for production use.
"""
import logging

LOGLEVEL = logging.INFO

#: List of parameters which should not be logged. This should list any
#: configuration parameters which include secrets, such as SECRET_KEY,
#: or the database connection string which may have a password.
DO_NOT_LOG_VARS = [
    'SECRET_KEY',
    'MAIL_PASSWORD',
]
MAIL_TITLE = 'PGP Message'
