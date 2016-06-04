import sys
from setuptools import setup

PYPY = hasattr(sys, 'pypy_version_info')

requires = [
    'flask>=0.10, <1.0',
    'Flask-WTF>=0.12',
]

setup(
    name='secure-html-form-to-pgp-mail',
    version='1.0b1',

    description='Send mail with verifiable client-side PGP via HTML form',
    license='MIT',

    author='Steffen Prince',
    author_email='steffen@sprin.io',

    url='https://github.com/sprin/secure-html-form-to-pgp-mail',
    download_url='https://github.com/sprin/secure-html-form-to-pgp-mail',

    classifiers=['Development Status :: 4 - Beta',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Intended Audience :: Developers',
                 'Environment :: Web Environment',
                 'Framework :: Flask',
                 ],

    platforms=['Any'],

    provides=['secure-html-form-to-pgp-mail'],
    zip_safe=False,

    install_requires=requires,
)
