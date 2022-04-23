import os

SECRET_KEY = os.environ["APP_SECRET_KEY"]

MAIL_DEBUG = True
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "bytebybyte.npo@gmail.com"
MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
MAIL_DEFAULT_SENDER = "bytebybyte.npo@gmail.com"
MAIL_MAX_EMAILS = None
MAIL_ASCII_ATTACHMENTS = False
