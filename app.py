import json
import pickle

from flask import Flask,request,app,jsonify,url_for, render_template
import pandas as pd
import numpy as np

@app.route ('/')
def home():
    return render_template('home.html')

@app.route('predict_api', methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,1))
    output=clf.predict(data)
    print(output[0])
    return jsonify(output[0])

if name=='__main__':
    app.run(debug=True)