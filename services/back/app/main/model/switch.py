from .. import db
from datetime import datetime

class Switch(db.Model):
    __tablename__ = "backup_sw"

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(50), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now)
    file_path = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(), nullable=False)

    def __init__(self, ip, model, serial, created_on, file_path, content):
        self.name = ip
        self.model = model
        self.serial = serial
        self.created_on = created_on
        self.file_path = file_path
        self.content = content

    def __repr__(self):
        return f"<Switch {self.model}>"