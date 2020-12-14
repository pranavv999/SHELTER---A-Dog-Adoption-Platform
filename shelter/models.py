from datetime import datetime
from shelter import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_number = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(60), nullable=False)

    ads = db.relationship('Advertisement', backref='owner',)

    def __repr__(self):
        return f"User({self.name}, {self.surname}, {self.email})"


class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breed_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime,
                            nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Advertisement({self.breed_name},\
{self.image_file}, {self.date_posted})"
