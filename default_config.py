import os

SECRET_KEY = os.environ["APP_SECRET_KEY"]

MAIL_DEBUG = True
MAIL_SERVER = "smtp.sendgrid.net"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = "apikey"
MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
MAIL_DEFAULT_SENDER = "bytebybyte.npo@gmail.com"
MAIL_MAX_EMAILS = None
MAIL_ASCII_ATTACHMENTS = False

spam_names = ["HenryPhiBe", "CrytoPhiBePhiBe"]
spam_domains = [""]
spam_emails = [""]