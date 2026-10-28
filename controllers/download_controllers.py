from flask import jsonify, send_from_directory 

UPLOAD_FOLDER = 'uploads'
 
class DownloadController:
    @staticmethod
    def download_file(filename):
        return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

        except FileNotFoundError:
            return jsonify({'error': 'File not found'}), 404
            
    