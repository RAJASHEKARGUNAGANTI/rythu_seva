from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("fertilizer_prediction_model.sav")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/fertilizer')
def fertilizer():
    return render_template("fertilizer.html")    

@app.route('/predict_fertilizer', methods=['POST'])
def result():
    # s_length = float(request.form['sepal_length'])
    # s_width = float(request.form['sepal_width'])
    # p_length = float(request.form['petal_length'])
    # p_width = float(request.form['petal_width'])
    c_nitrogen = float(request.form['nitrogen'])
    c_phosphorous = float(request.form['phosphorous'])
    c_pottasium = float(request.form['pottasium'])
    c_cropname = str(request.form['cropname'])
    # c_soil= str(request.form['soil'])
    # c_Maize= c_Sugarcane= c_Cotton= c_Tobacco= c_paddy= c_Barley= c_Wheat= c_Millets=0
    # if(c_cropname == "rice"):
    #     c_rice =1

    # pred = model.predict([[c_nitrogen, c_phosp    horous, c_pottasium, c_cropname]])
    print(c_nitrogen, c_phosphorous, c_pottasium, c_cropname)
    
    return render_template("fertilizer.html", result = 0)
   
    
    
    

if __name__ == '__main__':
    app.run()
