# Flask Project for beginners - Let's make a full website from scratch!

from flask import Flask
from views import views

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")


if __name__ == "__main__":
	app.run(debug=True, port=5173)