from flask import Flask
from config import db, photo_test
from apis import api
from flask_migrate import Migrate
from flask_uploads import configure_uploads, IMAGES
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/richText'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['UPLOADED_PHOTO_DEST'] = os.path.dirname(os.path.abspath(__file__)) + '/file_uploads'
    app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES
    api.init_app(app)
    db.init_app(app)
    configure_uploads(app, photo_test)
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    migrate = Migrate(app, db)
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
