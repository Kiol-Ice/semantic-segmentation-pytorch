import os
import json
from flask import Blueprint, render_template, current_app, session

download_bp = Blueprint("download_bp", __name__)


download_bp.add_url_rule(
    "/<name>", endpoint="download_file", build_only=True
)

@download_bp.route('/<name>')
def download_file(name):
    full_filename = os.path.join(current_app.config['RESULT_FOLDER'], name)
    
    prediction = ''
    if session.get('prediction') != None:
        prediction = json.loads(session['prediction'])
    
    return render_template('download.html', image=name, img_path=full_filename, prediction=prediction)