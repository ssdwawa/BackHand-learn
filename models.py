from  flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import  pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/richText'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Content(db.Model):
    __tableName__ = "content"
    id = db.Column(db.Integer, primary_key=True)
    Content = db.Column(db.String())
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Content %r>' % self.id

if __name__ == "__main__":
    db.create_all()