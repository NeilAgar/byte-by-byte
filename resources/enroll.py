from flask_restful import Resource
from flask import redirect


class EnrollRedirect(Resource):
    @classmethod
    def get(cls):
        return redirect("https://forms.gle/EjDw3b5nBbHCBDF88", code=302)


class AlternateEnrollRedirect(Resource):
    @classmethod
    def get(cls):
        return redirect("/enroll", code=302)
