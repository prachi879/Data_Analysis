from flask import Flask,render_template,request
#import jsonify
import requests
import pickle
import numpy as np
import sklearn

from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('file_customer.pkl','rb'))
model2 = pickle.load(open('file_manufacture.pkl','rb'))
import os

PEOPLE_FOLDER = os.path.join('static', 'img')

@app.route('/',methods=['GET'])
def Home():
  return render_template('index.html')
@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')
@app.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/form',methods=['GET'])
def form():
  return render_template('form.html')
@app.route('/form2',methods=['GET'])
def form2():
  return render_template('form2.html')

@app.route('/predict',methods = ['POST'])
def predict():
    Fuel_Type_Diesel =0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        current_Price = float(request.form['current_Price'])
        total_kms = int(request.form['total_kms'])
        Owner = int(request.form['Owner'])
        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        Seller_Type = request.form['Seller_Type']
        Transmission = request.form['Transmission']
        if(Fuel_Type_Petrol == 'Petrol'):
            Fuel_Type_Diesel = 0
            Fuel_Type_Petrol = 1

        elif(Fuel_Type_Diesel=='Diesel'):
            Fuel_Type_Diesel = 1
            Fuel_Type_Petrol = 0

        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0

        Year = 2022 - Year

        if(Seller_Type=='Individual'):
            Seller_Type =1
        else:
            Seller_Type = 0

        if(Transmission == 'Manual'):
            Transmission = 1
        else:
            Transmission = 0

        prediction = model.predict([[current_Price,total_kms,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type,Transmission]])
        output = round(prediction[0],2)

        if output<0:
            return render_template('form.html',prediction_text='Sorry! You cannot sell this car  Rs.{}'.format(output))
        else:
            return render_template('form.html', prediction_text='You can sell this car at Rs.{} lakhs'.format(output))

    else:
        return render_template('form.html')
@app.route('/predict2',methods=['POST'])
def predict2():
    Fuel_Type_Diesel = 0
    Fuel_Type_Gas = 0
    dohc = 0
    rotor = 0
    ohcf = 0
    dohcv = 0
    l = 0
    ohc = 0
    ohcv = 0
    Aspiration = 0
    Aspiration = 0
    hardtop = 0
    hatchback = 0
    sedan = 0
    wagon = 0
    convertible = 0
    Medium = 0
    Highend = 0
    Budget = 0
    Budget = 0
    rwd = 0
    fwd = 0
    fowd = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    eight = 0
    twelve = 0


    if request.method == 'POST':
        car_length = float(request.form['car_length'])
        car_width = float(request.form['car_width'])
        horse_power = int(request.form['horse_power'])
        bore_ratio = float(request.form['bore_ratio'])
        engine_size = int(request.form['engine_size'])
        curb_weight = int(request.form['curb_weight'])
        wheel_base = float(request.form['wheel_base'])
        Aspiration = request.form['Aspiration']
        Fuel_Type = request.form['Fuel_Type']
        car_body_type = request.form['car_body_type']
        drive_wheel = request.form['drive_wheel']
        engine_type = request.form['engine_type']
        engine_no = request.form['engine_no']
        car_range = request.form['car_range']
        citympg = int(request.form['citympg'])
        highwaympg = int(request.form['highwaympg'])
        fueleconomy = (0.55 * citympg) + (0.45 * highwaympg)

        if(Fuel_Type == 'Gas'):
            Fuel_Type_Diesel = 0
            Fuel_Type_Gas = 1
        elif(Fuel_Type =='Diesel'):
            Fuel_Type_Diesel = 1
            Fuel_Type_Gas = 0
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0


        if(Aspiration == 'turbo'):
            Aspiration = 1
        else:
            Aspiration = 0


        if(engine_type == 'dohc'):
            dohc = 1
        elif(engine_type == 'ohcv'):
            ohcv = 1
        elif(engine_type == 'ohc'):
            ohc = 1
        elif(engine_type == 'rotor'):
            rotor = 1
        elif(engine_type == 'ohcf'):
            ohcf = 1
        elif(engine_type == 'dohcv'):
            dohcv = 1
        elif(engine_type == 'l'):
            l = 1

        if(car_body_type == 'hardtop'):
            hardtop = 1
        elif(car_body_type == 'hatchback'):
            hatchback = 1
        elif(car_body_type == 'sedan'):
            sedan = 1
        elif(car_body_type == 'wagon'):
            wagon = 1
        elif(car_body_type == 'convertible'):
            convertible = 1

        if(drive_wheel == 'rwd'):
            rwd = 1
        elif(drive_wheel == 'fwd'):
            fwd = 1
        elif(drive_wheel == '4wd'):
            fowd = 1


        if(engine_no == 'two'):
            two = 1
        elif(engine_no == 'three'):
            three = 1
        elif(engine_no == 'four'):
            four = 1
        elif(engine_no == 'five'):
            five = 1
        elif(engine_no == 'six'):
            six = 1
        elif(engine_no == 'eight'):
            eight = 1
        elif(engine_no == 'twelve'):
            twelve = 1

        if(car_range == 'Medium'):
            Medium = 1
        elif(car_range == 'Highend'):
            Highend = 1
        elif(car_range == 'Budget'):
            Budget = 1


        prediction = model2.predict([[wheel_base,curb_weight,engine_size,bore_ratio,horse_power,fueleconomy,car_length,car_width,Fuel_Type_Gas,Aspiration,hardtop,hatchback,sedan,wagon,fwd,rwd,dohcv,l,ohc,ohcf,ohcv,rotor,five,four,six,three,twelve,two,Medium,Highend]])
        output = round(prediction[0],2)

        if output<0:
            return render_template('form2.html',prediction_text='Sorry! You cannot sell this car')
        else:
            return render_template('form2.html', prediction_text='You can sell this car at Rs.{}'.format(output))

    else:
        return render_template('form2.html')


if __name__ == '__main__':
    app.run(debug=True)
