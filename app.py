from flask import Flask, render_template, request #Importerer Flask og nødvendige funksjoner
from models.mood import Mood # Importerer Mood-klassen
from database import create_table, insert_mood, get_all_moods # Importerer database-funksjoner

app = Flask(__name__) #Oppretter Flask-applikasjonen
create_table() #Oppretter database og tabell ved oppstart

@app.route("/", methods=["GET", "POST"]) 
def index():
    saved = False 

    if request.method == "POST":
        mood = request.form["mood"]
        energy = request.form["energy"]
        note = request.form["note"]

        new_entry = Mood(mood, energy, note)
        insert_mood(new_entry)
 
        saved = True
        
    rows = get_all_moods()
    return render_template("index.html", moods=rows, saved=saved)

#Viser lagrede humørdata
if __name__ == "__main__":
    app.run(debug=True)
