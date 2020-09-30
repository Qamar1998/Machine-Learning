# Import Libraries
from flask import Flask, render_template,request,jsonify
import numpy as np
import pandas as pd
import pickle
import argparse


# Create flask object
app = Flask('MyApp')

#Prepare model pickle file
def prepare_pickle_file():

   # Instantiate the ArgumentParser object as parser
   parser = argparse.ArgumentParser(description='Process pickle file.')
   parser.add_argument('-path' , dest= 'lm_path' , type=str,
                    help='Get lm pickle file')
   args = parser.parse_args()
   pickle_file_path = args.lm_path
   return pickle_file_path 



# Predection function
def predict(model, data):
    x = np.array(model.iloc[:,0:6])
    y= np.array(model.iloc[:,6:])
    print("the x dim is " ,x.ndim)
    parameters = x.flatten() 
    intercept = y.flatten() 
    price = 0
    for index,feature in enumerate(data):
        price += float(feature) * float(parameters[index])
    print(price)
    price+= intercept
    return price

# Create web page
@app.route('/')
def home():
    return render_template("House_Price_prediction.html")

@app.route('/predict' , methods=['GET', 'POST'])
def add():

      
  if request.method == 'POST':

        json_req = request.json
        for i in range(6):
            features.append(json_req['features'])
        features = np.asarray(features, dtype=float).reshape(1,6)
        p_price = str(model.predict(features))
        return jsonify(p_price)
    
  else:
        
    #get features from get url
    x1 = request.args.get('x1')
    x2 = request.args.get('x2')
    x3 = request.args.get('x3')
    x4 = request.args.get('x4')
    x5 = request.args.get('x5')
    x6 = request.args.get('x6')
    arr = np.array([x1,x2,x3,x4,x5,x6])
    p_price = predict(model , arr)
    return str(p_price)

# 4. run in main
if __name__ == "__main__":
   # Loading a model pickled file
   model = pickle.load(open(prepare_pickle_file(), 'rb'))
   app.run(debug=True)