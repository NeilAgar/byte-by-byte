from flask_mail import Mail

from default_config import spam_names, spam_domains, spam_emails

mail = Mail()

def is_spam(name, email):
    return False
