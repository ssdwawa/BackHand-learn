
from datetime import datetime
from config import db


class Content(db.Model):
    __tableName__ = "content"
    id = db.Column(db.Integer, primary_key=True)
    Content = db.Column(db.String())
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Content %r>' % self.id