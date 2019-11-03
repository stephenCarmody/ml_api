from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import werkzeug
import os
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
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
    
    def post(self):
        parser.add_argument('quote', type=str)
        args = parser.parse_args()

        return {
            'status': True,
            'quote': '{} added. Good'.format(args['quote'])
        }
    
class Quotes2(Resource):
    def get(self):
        return {
            'ataturk': {
                'quote': ['Yurtta sulh, cihanda sulh.', 'Egemenlik verilmez, alınır.', 'Hayatta en hakiki mürşit ilimdir.']
            },
            'linus': {
                'quote': ['Talk is cheap. Show me the code.']
            }

        }
    
    
class Predict(Resource):    
#     def post(self):
#         print('test')
#         args = parser.parse_args()
#         user_query = args['query']
        
#         return {'status' : True}
    
    def get(self):
        return {'task': 'Hello world'}, 201


api.add_resource(Quotes, '/')
api.add_resource(Quotes2, '/test')
api.add_resource(Predict, '/predict')

if __name__ =='__main__':
    app.run(debug=True)