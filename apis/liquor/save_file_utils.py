#파일(이미지) 저장 함수
import os
import uuid
from flask import abort, flash
from werkzeug.utils import secure_filename
from glob import glob
from config import ALLOWED_EXTENSIONS, COCKTAIL_THUMBNAIL_FOLDER, UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def naming_file(filename):
    u=uuid.uuid4()
    new_filename = str(u) + "." + filename.rsplit('.', 1)[1].lower()
    return new_filename
    
def save_image(image_file, is_search=True):
    img = image_file['file']
    
    if img.filename == '':
        flash('No selected file')
        return abort(500,'No selected file')

    if img and allowed_file(img.filename):
        filename = naming_file(secure_filename(img.filename))
        
        if is_search:
            image_path = os.path.join(UPLOAD_FOLDER, filename)
       
        else: #cocktail 레시피 등록
            image_path = os.path.join(COCKTAIL_THUMBNAIL_FOLDER, filename)
        img.save(image_path)
        
        return image_path

# file_path = 'C:/liquor/project-template/apis/liquor/지빠귀'
# file_names = os.listdir(file_path)
# print(file_names)

# for name in file_names:
#     src = os.path.join(file_path, name)
#     u = uuid.uuid4()
#     dst=str(u)+'.jpg'
#     dst = os.path.join(file_path, dst)
#     os.rename(src,dst)