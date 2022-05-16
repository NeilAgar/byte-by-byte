from dotenv import load_dotenv
from flask import Flask, render_template
from flask_restful import Api

load_dotenv(".env", verbose=True)

from extensions import mail
from resources.home import HomePage
from resources.links import ImportantLinks, ImportantLinksRedirect
from resources.announcements import Announcements, AnnouncementsRedirect
from resources.enroll import EnrollRedirect, AlternateEnrollRedirect


app = Flask(__name__)

app.config.from_object("default_config")

api = Api(app)
mail.init_app(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def unknown_error(e):
    return render_template('500.html'), 500


api.add_resource(HomePage, "/")
api.add_resource(ImportantLinks, "/important_links")
api.add_resource(ImportantLinksRedirect, "/important_links/")
api.add_resource(Announcements, "/announcements")
api.add_resource(AnnouncementsRedirect, "/announcements/")
api.add_resource(EnrollRedirect, "/enroll")
api.add_resource(AlternateEnrollRedirect, "/enroll/")

if __name__ == "__main__":
    app.run(debug=False, port=5001)
