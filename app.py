from flask import Flask,render_template,request
import numpy as np
import pickle

app = Flask(__name__)

with open('H:\Student_Performance\data\StudentsPerformance.csv','rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        pass