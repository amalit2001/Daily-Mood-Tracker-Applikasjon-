from datetime import date

class Mood:
    def __init__(self, mood, energy, note):
        self._mood = mood
        self._energy = energy
        self._note = note
        self._date = date.today()

    # Getters
    def get_mood(self):
        return self._mood

    def get_energy(self):
        return self._energy

    def get_note(self):
        return self._note

    def get_date(self):
        return self._date

    def __str__(self):
        return f"{self._date} – {self._mood} (Energi: {self._energy})"
