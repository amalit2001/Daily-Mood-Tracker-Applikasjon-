# Importerer Flask og nødvendige funksjoner
from flask import Flask, render_template, request 
# Importerer Mood-klassen
from models.mood import Mood 
# Importerer database-funksjoner
from database import create_table, insert_mood, get_all_moods 

app = Flask(__name__) # Oppretter Flask-applikasjonen
create_table() # Sikrer at databasen er klar før applikasjonen brukes

# Hovedrute for visning og lagring av humørdata
@app.route("/", methods=["GET", "POST"]) 
def index():
    saved = False 

    # Håndterer skjema-innsending
    if request.method == "POST":
        mood = request.form["mood"]
        energy = request.form["energy"]
        note = request.form["note"]

        new_entry = Mood(mood, energy, note)
        insert_mood(new_entry)
 
        saved = True
        
    rows = get_all_moods()
    return render_template("index.html", moods=rows, saved=saved)

# Starter Flask-applikasjonen
if __name__ == "__main__":
    app.run(debug=True)
