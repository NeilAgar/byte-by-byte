from flask import Flask, jsonify, render_template
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources.home import HomePage


app = Flask(__name__)
api = Api(app)

jwt = JWTManager(app)

app.config.from_object("config")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(403)
def page_forbidden(e):
    return render_template('403.html'), 403


@app.errorhandler(401)
def page_forbidden(e):
    return render_template('401.html'), 401


@app.errorhandler(500)
def unknown_error(e):
    return render_template('500.html'), 500


api.add_resource(HomePage, "/")

if __name__ == "__main__":
    app.run(debug=False)
