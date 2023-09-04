from flask_restful import Resource
from flask import make_response, render_template, redirect


class ImportantLinks(Resource):
    @classmethod
    def get(cls):
        # headers = {"Content-Type": "text/html"}
        # return make_response(render_template("important_links.html"), 200, headers,)

        return redirect("/", code=302)


class ImportantLinksRedirect(Resource):
    @classmethod
    def get(cls):
        return redirect("/important_links", code=302)
