from flask import Flask, render_template, request
import os
from predictor import predict_disease, irrigation_advisor

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    soil = float(request.form["soil"])
    temp = float(request.form["temp"])
    humidity = float(request.form["humidity"])

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    disease = predict_disease(filepath)

    irrigation = irrigation_advisor(
        soil,
        temp,
        humidity
    )

    return render_template(
        "result.html",
        image=filepath,
        disease=disease,
        irrigation=irrigation
    )

if __name__ == "__main__":
    app.run(debug=True)
