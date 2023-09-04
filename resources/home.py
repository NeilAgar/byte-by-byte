from flask_restful import Resource
from flask import make_response, render_template, request, url_for, redirect
from flask_mail import Message

from extensions import mail, is_spam


class HomePage(Resource):
    @classmethod
    def get(cls):
        print(dict(request.headers))
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("home_page.html"), 200, headers, )

    @classmethod
    def post(cls):
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        if not is_spam(name, email):
            msg = Message("Byte By Byte Website Question",
                          recipients=["neiliscool67@gmail.com", "aditagarwal76@gmail.com", "help@byte-by-byte.org",
                                      "aditneil@outlook.com"])

            msg.body = f"""
    Name: {name}
    Email: {email}

    {message}
    """

            mail.send(msg)

        return redirect(url_for("homepage"))
