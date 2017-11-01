import os
from flask import Flask, render_template, redirect, request, url_for, session
from instance.config import app_config

IMAGE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/static/uploaded_images"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_PATH

app.config.from_object(app_config[os.getenv('CONFIG')])
