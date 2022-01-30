from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__)

# Set up configuration
app.config.from_object(DevConfig)