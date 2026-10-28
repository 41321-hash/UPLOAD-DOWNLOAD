from flaski import Blueprint
from
upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    return UploadController.upload_file()
    