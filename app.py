from flask import Flask,request,render_template,jsonify
from flask_cors import CORS,cross_origin
import os
from src.tumorClassification.utils.common import decodeImage
from src.tumorClassification.pipeline.prediction import PredictionPipeline
from src.tumorClassification.database.db_operation import DatabaseHandler


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app=Flask(__name__)
CORS(app)

class ClientApp():
    def __init__(self):
        self.filename="inputImage.jpg"
        self.classifier=PredictionPipeline(self.filename)

@app.route("/",methods=["GET"])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # os.system("dvc repro")
    return "Training done successfully!"


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()

    db_handler = DatabaseHandler()
    db_handler.insert_prediction("path_to_image", result)
    db_handler.close_connection()

    return jsonify(result)

if __name__ == "__main__":
    
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)  