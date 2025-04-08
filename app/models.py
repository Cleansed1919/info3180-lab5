from . import db
from datetime import datetime, timezone

class Movies(db.Model):
    __tablename__='movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(127))
    description =  db.Column(db.Text)
    poster = db.Column(db.String(127))
    created_at =  db.Column(db.DateTime, default=datetime.now(timezone.utc))