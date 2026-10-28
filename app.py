from flask import flask
from database.db import init_db
from route.upload_route import upload_bp
from route.download_route import download_bp

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

init_db()

app.register_blueprint(upload_bp, url_prefix='/upload')
app.register_blueprint(download_bp, url_prefix='/download')

if __name__ == '__main__':
    app.run(debug=True)