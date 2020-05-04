
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "OfUJnnclWc7iAWap1qsr"

import api.service
