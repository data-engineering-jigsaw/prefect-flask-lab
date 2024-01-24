from flask import Flask

from db import cursor, find_all
from src.track import Track


def create_app():
    app = Flask(__name__)

    @app.route('/tracks')
    def tracks():
        tracks = find_all(Track, cursor)
        return [track.__dict__ for track in tracks]

    return app