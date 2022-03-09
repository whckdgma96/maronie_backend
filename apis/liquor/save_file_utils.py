#파일(이미지) 저장 함수
import os
import uuid
from flask import abort, flash
from werkzeug.utils import secure_filename
from config import ALLOWED_EXTENSIONS, COCKTAIL_THUMBNAIL_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def naming_file(filename):
    u=uuid.uuid4()
    new_filename = str(u) + "." + filename.rsplit('.', 1)[1].lower()
    return new_filename
    
def save_image(thumbnail):
    if thumbnail.filename == '':
        flash('No selected file')
        return abort(500,'No selected file')

    if thumbnail and allowed_file(thumbnail.filename):
        filename = naming_file(secure_filename(thumbnail.filename))
        image_path = os.path.join(COCKTAIL_THUMBNAIL_FOLDER, filename)
        thumbnail.save(image_path)
        return image_path