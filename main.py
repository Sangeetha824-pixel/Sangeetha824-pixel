"""
FUTURE ENHANCEMENT
Future work should concentrate on enhancing performance while considering data security and privacy in real-time. Because we only included a relatively limited number of fraud datasets for the forecast, we must consider a large number of datasets in order to improve accuracy. Due to an increase in bank fraud instances and cybercrime problems, a safe testing system is becoming more and more important. And there is a clear solution to this problem. It can be used and taken frequently, just like OTP. It can even be used to examine previous database transactions to identify whether or not certain transactions were fraudulent, and in such cases, it would be able to offer evidence. Additionally, it is possible to experiment with new models and optimise the proposed approaches.
"""
from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

app = Flask(__name__)
app.secret_key = '1a2b3c4d5e'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        ans = "fraud"
        ans1 = "non fraud"
        time1 = request.form['time1']
        V1 = request.form['V1']
        V2 = request.form['V2']
        V3 = request.form['V3']
        V4 = request.form['V4']
        V5 = request.form['V5']
        V6 = request.form['V6']
        V7 = request.form['V7']
        V8 = request.form['V8']
        V9 = request.form['V9']
        V10 = request.form['V10']
        V11 = request.form['V11']
        V12 = request.form['V12']

        amt = float(request.form['amt'])

        sample_data = [time1, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, amt]
        clean_data = [float(i) for i in sample_data]
        if amt < 1500:
            result1 = ans
        else:
            result1 = ans1
        # Placeholder for model logic
        return render_template('home.html', class1=result1)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home1():
    return render_template('home.html')

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)