import os
from flask import flash, request, redirect, url_for, Blueprint, current_app
from werkzeug.utils import secure_filename
from outil_segmentation import segmentation

ALLOWED_EXTENSIONS = {'jpg'}

segmentation_bp = Blueprint("segmentation_bp", __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@segmentation_bp.route('/seg', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            img_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(img_path)
            
            segmentation(img_path)
            
            return redirect(url_for('download_bp.download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''