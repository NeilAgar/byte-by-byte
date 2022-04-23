from flask_restful import Resource
from flask import make_response, render_template, redirect


class Announcements(Resource):
    @classmethod
    def get(cls):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("announcements.html"), 200, headers,)


class AnnouncementsRedirect(Resource):
    @classmethod
    def get(cls):
        return redirect("/announcements", code=302)
