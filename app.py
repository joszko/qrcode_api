from flask import Flask
from flask_restful import Api

from resources.qr_resource import CreateQRCodes, DecodeQRCodes

app = Flask(__name__)
api = Api(app)

api.add_resource(CreateQRCodes, "/create/<string:text>")
api.add_resource(DecodeQRCodes, "/decode")

if __name__ == '__main__':
    app.run(debug=True)
