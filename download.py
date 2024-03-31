from flask import send_from_directory, current_app, Blueprint

download_bp = Blueprint("download_bp", __name__)


download_bp.add_url_rule(
    "/image_to_seg/<name>", endpoint="download_file", build_only=True
)

@download_bp.route('/image_to_seg/<name>')
def download_file(name):
    print(current_app.config["UPLOAD_FOLDER"])
    return send_from_directory("./image_to_seg", name)