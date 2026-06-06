from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        attendance = float(request.form["attendance"])
        study = float(request.form["study"])
        assignment = float(request.form["assignment"])
        internal = float(request.form["internal"])

        result = model.predict([
            [attendance, study, assignment, internal]
        ])

        prediction = round(result[0], 2)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)