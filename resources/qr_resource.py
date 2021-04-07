import werkzeug
from flask_restful import Resource, reqparse, marshal_with, fields
from flask import send_from_directory
from qrcodes import create_qrcode, decode_qrcode
import os

UPLOAD_FOLDER = './static'


class CreateQRCodes(Resource):

    def get(self, text):
        create_qrcode(text)
        return send_from_directory("./static", "response.png", as_attachment=True), 200


class DecodeQRCodes(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')

    def post(self):
        data = DecodeQRCodes.parser.parse_args()

        file = data['file']
        filename = werkzeug.utils.secure_filename(file.filename)

        return {"message": decode_qrcode(os.path.join(UPLOAD_FOLDER, filename))}, 200
