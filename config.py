from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet

db = SQLAlchemy()
photo_test = UploadSet('PHOTO')
