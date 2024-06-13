from flask_restful import Resource
from flask import make_response, render_template, redirect


class WeekSetup(Resource):
    @classmethod
    def get(cls):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("weeksetup.html"), 200, headers)


class WeekSetupRedirect(Resource):
    @classmethod
    def get(cls):
        return redirect("/week_setup", code=302)
