from flask import Flask, render_template, request
import joblib
import pickle
import numpy as np

app = Flask(__name__)

model = joblib.load("crop_recommendation.sav")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/crop')
def crop():
    return render_template("crop.html")

@app.route('/crop_recommend', methods=['POST'])
def result():
    print(request.form)
    c_nitrogen = float(request.form['nitrogen'])
    c_phosphorous = float(request.form['phosphorous'])
    c_pottasium = float(request.form['pottasium'])
    c_ph = float(request.form['ph'])
    c_rainfall = float(request.form['rainfall'])
    c_temparature = float(request.form['temparature'])
    c_humidity = float(request.form['humidity'])
    print(c_nitrogen, c_phosphorous, c_pottasium, c_ph, c_rainfall, c_temparature, c_humidity)
    pred = model.predict([[c_nitrogen, c_phosphorous, c_pottasium, c_ph, c_rainfall, c_temparature, c_humidity]])
    print("prediction: {}".format(pred))
    
    return render_template("crop.html", result = pred[0])
   
@app.route('/fertilizer')
def ferti():
    return render_template("fertilizer.html")


model2 = pickle.load(open("classifier.pkl","rb"))


@app.route('/predict', methods=["POST","GET"])
def fertiPred():
    if request.method == "POST":
     data1 = request.form["a"]
     data2 = request.form["b"]
     data3 = request.form["c"]
     data4 = request.form["d"]
     data5 = request.form["e"]
     data6 = request.form["f"]
     data7 = request.form["g"]
     data8 = request.form["h"]
     arr = np.array([[data1,data2,data3,data4,data5,data6,data7,data8]])
     pred = model2.predict(arr)
     data = request.form   
    return render_template("fertilizer.html", data=pred[0])

@app.route('/techFarming')
def techfarming():
    return render_template("/techFarming.html")
@app.route('/home')
def index():
    return render_template("index.html")
    

if __name__ == '__main__':
    app.run()
