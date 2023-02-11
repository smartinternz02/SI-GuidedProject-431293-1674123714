

from flask import Flask, jsonify, make_response, request, abort, render_template
import pandas as pd

import pickle

model = pickle.load(open( "sales_demand_ forecasting.pkl", "rb"))
app = Flask(__name__)





@app.route('/')
def home():
    return render_template('index.html')

@app.route("/y_predict", methods=['POST', 'GET'])
def y_predict():
    x = [[float(x) for x in request.form.values()]]
    
    print(x)
    
    cols=["day_1","day_2","day_3","day_4"]
    
    print(x)
    pred = model.predict(x)
    
    print(pred[0])
    return render_template('result.html', prediction_text=pred[0])


if __name__ == "__main__":
  app.run()