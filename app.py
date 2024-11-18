from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            # Reading the inputs given by the user
            relative_compactness = float(request.form['relative_compactness'])
            surface_area = float(request.form['surface_area'])
            wall_area = float(request.form['wall_area'])
            roof_area = float(request.form['roof_area'])
            overall_height = float(request.form['overall_height'])
            orientation = int(request.form['orientation'])
            glazing_area = float(request.form['glazing_area'])
            glazing_area_distribution = int(request.form['glazing_area_distribution'])

# Prepare the data as a NumPy array
            data = [relative_compactness, surface_area, wall_area, roof_area, overall_height, orientation, glazing_area, glazing_area_distribution]
            data = np.array(data).reshape(1, 8)  # Reshape it to match the model input shape
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            # print('The Exception message is: ',e)
            error=e
            return error

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)