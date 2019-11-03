from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import werkzeug
import os
from werkzeug.datastructures import FileStorage
import numpy as np
import pandas as pd
import joblib

#from transformation import Columns, Debug
import sklearn
import dill

app = Flask(__name__)
api = Api(app)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')

def log_data():
    return


class Home(Resource):
    def get(self):
        return "I'm alive!"
    
class Predict(Resource):    
    def post(self):  
        
        data = request.json
        data_t = pd.DataFrame(data, index=[0])
        output = model.predict(data_t).tolist()
        print(output)
         
        return {"output": output}
    
    def get(self):
        return {'task': 'Hello world'}, 201


api.add_resource(Home, '/')
api.add_resource(Predict, '/predict')

if __name__ =='__main__':
    import os
    print(os.listdir("."))
    
    with open('pipeline_2.pkl', 'rb') as file:
        model = dill.load(file)
         
    app.run(host='0.0.0.0', debug=True)