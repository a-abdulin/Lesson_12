import logging

from flask import Flask, request, render_template, send_from_directory

# Импорт блюпринтов
from loader.views import loader_blueprint
from main.views import main_blueprint

logging.basicConfig(filename="basic.log")

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


app.register_blueprint(main_blueprint)

app.register_blueprint(loader_blueprint)

# @app.route("/uploads/<path:path>")
# def static_dir(path):
#     return send_from_directory("uploads", path)

#
# @app.route("/post", methods=["GET", "POST"])
# def page_post_form():
#     pass
#
#
# @app.route("/post", methods=["POST"])
# def page_post_upload():
#     pass
#


app.run(port=8000)
