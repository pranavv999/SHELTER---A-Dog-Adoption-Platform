import os
import secrets
from PIL import Image
from shelter import bcrypt
from shelter import app


def password_hash(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')


def check_password(password_from_db, password_from_form):
    return bcrypt.check_password_hash(password_from_db, password_from_form)


def save_picture(form_picture):
    random_name = secrets.token_hex(8)
    oldext = os.path.splitext(form_picture.filename)[1]
    new_name = random_name + oldext
    picture_path = os.path.join(app.root_path, 'static/img/dog_img', new_name)

    # Resizing Image
    op_size = (500, 500)
    img = Image.open(form_picture)
    img = img.resize(op_size)
    img.save(picture_path)

    return new_name
