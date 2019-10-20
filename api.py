from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import werkzeug
import os
from werkzeug.datastructures import FileStorage

UPLOAD_FOLDER = '/Users/stephencarmody/Documents/Career/side_projects/ml_api/img'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')

class Quotes(Resource):
    def get(self):
        return {
            'ataturk': {
                'quote': ['Yurtta sulh, cihanda sulh.', 'Egemenlik verilmez, alınır.', 'Hayatta en hakiki mürşit ilimdir.']
            },
            'linus': {
                'quote': ['Talk is cheap. Show me the code.']
            }

        }

class Mirror(Resource):
    def get(self):
        args = parser.parse_args()
        user_query = args['query']
        
        return user_query

class UploadImage(Resource):
    def post(self):
        parser.add_argument('image', type=FileStorage, location='files')
        args = parser.parse_args()
        stream = args['image'].stream

        imageFile = args['image']
        imageFile.save(os.path.join('img', "your_file_name.jpg"))

        return {'status' : True}

api.add_resource(Quotes, '/')
api.add_resource(Mirror, '/mirror')
api.add_resource(UploadImage, '/image')


if __name__ =='__main__':
    app.run(debug=True)