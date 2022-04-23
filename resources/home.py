from flask_restful import Resource
from flask import make_response, render_template, request, url_for, redirect


class HomePage(Resource):
    @classmethod
    def get(cls):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("home_page.html"), 200, headers,)

    @classmethod
    def post(cls):
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # return {"name": name, "email": email, "message": message}
        return redirect(url_for("homepage"))
