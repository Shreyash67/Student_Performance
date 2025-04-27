from flask import Flask,render_template,request
import numpy as np
import pickle

app = Flask(__name__)

with open('H:\Student_Performance\my_model\Logistic_model.pkl','rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            math_score = float(request.form['math_score'])
            reading_score = float(request.form['reading_score'])
            writing_score = float(request.form['writing_score'])

            input_data = np.array([[math_score,reading_score,writing_score]])
            result = model.predict(input_data)

            if result[0]==1:
                prediction = "Pass"
            else:
                prediction = "Fail"

            return render_template('index.html',result = f"Predict Student Pass Or Fail: {prediction}")
        except Exception as e:
            return render_template('index.html',result=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)