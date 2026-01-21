from datetime import date

class Mood:  # Representerer en humørregistrering
    def __init__(self, mood_value, energy_level, note_text):
        self._mood = mood_value
        self._energy = energy_level
        self._note = note_text
        self._date = date.today()

    # Metoder for å hente data fra objektet
    def get_mood(self):
        return self._mood

    def get_energy(self):
        return self._energy
    
    def get_note(self):
        return self._note
    
    def has_note(self):
        return bool(self._note)

    def get_date(self):
        return self._date

    def __str__(self):
        return (
           f"Dato: {self._date}, "
           f"Humør: {self._mood}, "
           f"Energi: {self._energy}"
      )
