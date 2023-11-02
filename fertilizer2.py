from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open("classifier.pkl","rb"))

app = Flask(__name__)


@app.route("/")
def man():
    return render_template("index.html")

@app.route('/fertilizer')
def ferti():
    return render_template("fertilizer.html")


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
     pred = model.predict(arr)
     data = request.form   
    return render_template("fertilizer.html", data=pred[0])

if __name__== "__main__":
    app.run(debug=True,port=8001)