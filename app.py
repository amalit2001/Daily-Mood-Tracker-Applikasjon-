from models.mood import Mood
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mood = request.form["mood"]
        energy = request.form["energy"]
        note = request.form["note"]

        new_entry = Mood(mood, energy, note)
        mood_entries.append(new_entry)

        print("Ny registrering:")
        print(new_entry)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
