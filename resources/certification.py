from flask_restful import Resource
from flask import send_from_directory


class Certification(Resource):
    @classmethod
    def get(cls):
        return send_from_directory('static', 'certification')
