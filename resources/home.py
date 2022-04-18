from flask_restful import Resource
from flask import make_response, render_template


class HomePage(Resource):
    @classmethod
    def get(cls):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("home_page.html"), 200, headers,)
