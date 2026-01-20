from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mood = request.form["mood"]
        energy = request.form["energy"]
        note = request.form["note"]

        print("Humør:", mood)
        print("Energi:", energy)
        print("Notat:", note)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
