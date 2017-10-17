import os
from flask import Flask, render_template, redirect, request, url_for, jsonify, session
from instance.config import app_config

app = Flask(__name__)

app.config.from_object(app_config[os.getenv('CONFIG')])

