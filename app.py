#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


# In[2]:


app = Flask(__name__)
model = pickle.load(open('modelLR.pkl', 'rb'))

# In[3]:


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    float_features = int_features[7:11]
    int_features = [int(x)for x in int_features[0:7]]
    for x in float_features:
    	int_features.insert(5+float_features.index(x),x)
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    if(output == 1):
    	result = 'Congrats! You have high chances of loan approval'
    elif(output==0):
    	result = 'Sorry! You have low chances of loan approval'
    return render_template('prediction.html', prediction_text=format(result))
       

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)


# In[ ]:




