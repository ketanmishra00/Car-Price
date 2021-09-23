
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Random.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        fueltype=int(request.form['fueltype'])
        doornumber = int(request.form['doornumber'])
        carbody=int(request.form['carbody'])
        Size = float(request.form['Size'])
        enginetype=float(request.form['enginetype'])
        cylindernumber=int(request.form['cylindernumber'])
        enginesize = int(request.form['enginesize']) 
        horsepower=int(request.form['horsepower'])
        peakrpm = int(request.form['peakrpm'])
        mpg = int(request.form['mpg'])
         
        prediction=model.predict([[Size,enginetype,enginesize,cylindernumber,horsepower,fueltype,peakrpm,mpg,doornumber,carbody]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot buy this car")
        else:
            return render_template('index.html',prediction_text="The price of the car in lakhs is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
