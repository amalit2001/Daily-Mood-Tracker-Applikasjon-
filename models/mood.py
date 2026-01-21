from datetime import datetime

class Mood:  # Representerer en humørregistrering
    def __init__(self, mood_value, energy_level, note_text):
        self._mood = mood_value
        self._energy = energy_level
        self._note = note_text
        self._datetime = datetime.now() # Lagrer dato og tid for registreringen

    # Metoder for å hente data fra objektet
    def get_mood(self):
        return self._mood

    def get_energy(self):
        return self._energy
    
    def get_note(self):
        return self._note
    
    def has_note(self):
        return bool(self._note)

    def get_datetime(self):
        return self._datetime

    def __str__(self):
         # Formaterer som: "2026-01-21 14:35 – Glad (Energi: 4)
        return (
           f"Dato: {self._datetime.strftime('%Y-%m-%d %H:%M')}, "
           f"Humør: {self._mood}, "
           f"Energi: {self._energy}"
      )
