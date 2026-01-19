# Daily-Mood-Tracker-Applikasjon
En enkel webapplikasjon som lar brukeren loggføre og spore daglig humør og energinivå, samt skrive korte refleksjoner.

## 1. Beskrivelse av løsningen
Daily Mood Tracker er en enkel webapplikasjon som lar brukeren loggføre daglig humør og energinivå, samt skrive korte refleksjoner.  
Applikasjonen er laget som et personlig verktøy for økt bevissthet rundt egen trivsel og velvære.

Løsningen er utviklet med fokus på ryddig struktur, enkel funksjonalitet og et rolig visuelt uttrykk.

## 2. Målgruppe
Applikasjonen er laget for privatpersoner som ønsker et enkelt digitalt verktøy for refleksjon rundt egen hverdag og velvære.  
Den er ikke ment som et medisinsk eller helsefaglig verktøy.

## 3. Funksjonelle krav
Applikasjonen skal:
- la brukeren legge til en dagslogg
- gi brukeren mulighet til å velge humør
- gi brukeren mulighet til å velge energinivå
- la brukeren skrive en kort refleksjon
- vise tidligere registrerte logger
- gi brukeren mulighet til å slette en logg

## 4. Krav til brukervennlighet og enkelhet
- Applikasjonen skal være enkel å bruke uten forklaring
- Brukergrensesnittet skal være oversiktlig og ryddig
- Det skal være få valg per side
- Designet skal ha god kontrast og tydelige tekstfelt
- Navigasjonen skal være enkel og logisk

## 5. Systemstruktur

### Teknologier
- Backend: Python og Flask
- Database: SQLite
- Frontend: HTML (Jinja templates) og CSS

### Klasser og ansvar

**MoodEntry**
- Representerer én dagslogg
- Inneholder:
  - id
  - dato
  - humør
  - energinivå
  - notat

**Database**
- Har ansvar for lagring, henting og sletting av loggdata
- Skiller datatilgang fra resten av applikasjonen

**app.py**
- Inneholder Flask-ruter
- Kobler frontend og backend

## 6. Arbeidsprosess
Arbeidet startet med å definere formål, målgruppe og funksjonalitet før koding.  
Deretter ble systemstrukturen planlagt ved å identifisere nødvendige klasser og ansvar.

Utviklingen ble gjennomført stegvis:
1. Oppsett av GitHub-repository og prosjektstruktur
2. Planlegging av datamodell
3. Implementering av grunnleggende funksjonalitet
4. Utforming av brukergrensesnitt
5. Faglig refleksjon rundt sikkerhet, personvern og universell utforming

## 7. Planlegging
Før utvikling ble det laget en enkel skisse av brukergrensesnittet for å planlegge struktur og flyt i applikasjonen.

7. Faglig refleksjon rundt sikkerhet, personvern og universell utforming

