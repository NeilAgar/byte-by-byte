from flask_restful import Resource
from flask import make_response, render_template, request, url_for, redirect
from flask_mail import Message

from extensions import mail, is_spam


class HomePage(Resource):
    @classmethod
    def get(cls):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("home_page.html"), 200, headers, )

    @classmethod
    def post(cls):
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        if not is_spam(name, email):
            msg = Message("Byte By Byte Website Question",
                          recipients=["neil_agarwal@outlook.com", "aditagarwal76@gmail.com", "bytebybyte.npo@gmail.com"])

            msg.body = f"""
    Name: {name}
    Email: {email}

    {message}
    """

            mail.send(msg)

        return redirect(url_for("homepage"))
