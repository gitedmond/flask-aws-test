from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'i finally got aws eb to work'