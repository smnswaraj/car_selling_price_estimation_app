
from types import MethodType
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('car_price_prediction_model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('input.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        present_price          = request.form['present_price']
        kms_driven             = request.form['kms_driven']
        Owner                  = request.form['owner']
        no_of_years            = request.form['no_of_years']
        fuel_type             = request.form['fuel_type']
        cng = 0
        petrol = 0
        diesel = 0;
        if( fuel_type == 0):
            cng = 1;
        elif (fuel_type == 1):
            petrol = 1;
        elif (fuel_type == 2):
            diesel = 1;

        seller_type_individual = request.form['seller_type_individual']
        dealer = 0;
        individual = 0
        if (seller_type_individual == 0):
            dealer = 1
        elif (seller_type_individual == 1):
            individual = 1

        transmission = request.form['transmission']
        manual = 0
        automatic = 0
        if (transmission == 0):
            manual = 1
        elif (transmission == 1):
            automatic = 1

        arr = np.array([[present_price, kms_driven, Owner, no_of_years, cng, petrol, diesel,dealer, individual, automatic, manual]])
        val1 = pd.DataFrame(data=arr, index=None, columns=None)
        result = model.predict(val1)
        return render_template('result.html', data=round(result[0],3))

if __name__=="__main__" :
    app.run(debug=True)