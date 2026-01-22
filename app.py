# Importerer Flask og nødvendige funksjoner
from flask import Flask, render_template, request, redirect, url_for
# Importerer Mood-klassen
from models.mood import Mood 
# Importerer database-funksjoner
from database import create_table, save_mood_entry, get_all_moods 

# Lager Flask-applikasjonen og kobler til databasen
app = Flask(__name__)
create_table() # Sørger for at tabellen finnes før vi begynner

# Hovedrute for visning og lagring av humørdata
@app.route("/", methods=["GET", "POST"])
def index():
    # Tar imot brukerens valg fra skjemaet og lagrer i databasen
    if request.method == "POST":
        mood = request.form["mood"]
        energy = request.form["energy"]
        note = request.form["note"]

        new_entry = Mood(mood, energy, note)
        save_mood_entry(new_entry)

        # Redirect etter POST for å unngå dobbel lagring ved refresh
        return redirect(url_for("index", saved="true"))

    rows = get_all_moods()
    entry_saved = request.args.get("saved") == "true"

    return render_template("index.html", moods=rows, saved=entry_saved)

# Kjører Flask-serveren lokalt for testing og visning
if __name__ == "__main__":
    app.run(debug=False)
