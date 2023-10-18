from flask import Flask,request,render_template,jsonify
from flask_cors import CORS,cross_origin
from src.tumorClassification.utils.common import decodeImage
from src.tumorClassification.pipeline.prediction import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app=Flask(__name__)
CORS(app)

class Clientapp():
    def __init__(self):
        self.