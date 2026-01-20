Prosjektdokumentasjon

Daily Mood Tracker

1. Beskrivelse av løsningen

Daily Mood Tracker er en enkel webapplikasjon utviklet i Python og Flask som lar brukeren registrere daglig humør, energinivå og korte refleksjoner. Registreringene lagres lokalt i en SQLite-database og kan vises i ettertid.

Applikasjonen er laget som et personlig verktøy for økt bevissthet rundt egen trivsel og hverdag. Den er ikke ment som et medisinsk eller helsefaglig verktøy, men som et lavterskel refleksjonsverktøy.

Målgruppe:
Privatpersoner som ønsker et enkelt og oversiktlig digitalt verktøy for å følge eget humør og energinivå over tid.

Problemet løsningen adresserer:
Mange mangler en enkel måte å reflektere over egen hverdag på. Applikasjonen gir brukeren et strukturert, men ukomplisert system for dette uten krav til teknisk forkunnskap.

2. Krav
2.1 Funksjonelle krav

Applikasjonen skal:

la brukeren registrere daglig humør

la brukeren velge energinivå (1–5)

gi mulighet for å skrive et kort notat

lagre registreringene permanent

vise tidligere registrerte logger

gi tydelig tilbakemelding når en registrering er lagret

2.2 Krav til brukervennlighet og enkelhet

Applikasjonen skal være enkel å bruke uten forklaring

Brukergrensesnittet skal være oversiktlig og ryddig

Det skal være få valg per side

Skjemaelementer skal være tydelig merket

Designet skal ha god kontrast og rolige farger

3. Systemstruktur
3.1 Overordnet arkitektur

Applikasjonen er bygget med tydelig separasjon av ansvar:

Frontend: HTML (Jinja templates) og CSS

Backend: Flask (Python)

Datamodell: Objektorientert klasse (Mood)

Datalagring: SQLite via egen database-modul

3.2 Mappestruktur
daily-mood-tracker/
│
├── app.py
├── database.py
├── models/
│   └── mood.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── README.md
└── reflection.md

3.3 Klasser og ansvar

Mood (klasse)
Representerer én humørregistrering.

Attributter:

mood

energy

note

date

Klassen bruker innkapsling ved at data lagres som private attributter og hentes via metoder.

database.py
Har ansvar for:

opprettelse av database og tabell

lagring av humørdata

henting av lagrede registreringer

app.py

håndterer brukerinput via Flask-ruter

kobler frontend, datamodell og database

sender data videre til visning i HTML

3.4 Enkel UML-inspirert skisse
+----------------+
|     Mood       |
+----------------+
| mood           |
| energy         |
| note           |
| date           |
+----------------+

Mood → brukes av → app.py  
app.py → kommuniserer med → database.py

4. Arbeidsprosess

Arbeidet startet med å definere formål, målgruppe og funksjonalitet før koding. Deretter ble prosjektstrukturen planlagt for å sikre ryddig kode og god oversikt.

Utviklingen ble gjennomført stegvis:

Bekrefte at Flask-applikasjonen kjørte korrekt

Lage enkel HTML-visning

Implementere skjema for brukerinput

Bruke objektorientert programmering for å strukturere data

Vise registreringer i brukergrensesnittet

Gå fra midlertidig lagring i minne til permanent lagring i SQLite-database

Forbedre brukeropplevelse med visuell tilbakemelding

Denne tilnærmingen gjorde det enklere å teste underveis og rette feil tidlig.

5. Sikkerhet, GDPR og universell utforming
5.1 Sikkerhet

Applikasjonen kjører lokalt og har ingen brukerpålogging eller nettverkstilkobling. Dette reduserer angrepsflaten betydelig. I et større system ville tiltak som tilgangskontroll, validering av input og kryptering av data vært nødvendig.

5.2 GDPR og personvern

Applikasjonen behandler ikke direkte identifiserbare personopplysninger som navn, e-post eller fødselsnummer. Humørdata kan likevel anses som personlig informasjon. I et mer profesjonelt system burde brukeren informeres tydelig om datalagring, og data burde beskyttes bedre.

5.3 Universell utforming

Løsningen er laget med fokus på enkelhet og tilgjengelighet:

tydelige labels på alle input-felt

god kontrast mellom tekst og bakgrunn

store klikkflater og ryddig layout

Videre forbedringer kunne inkludert bedre støtte for tastaturnavigasjon og skjermlesere.

6. Bruk av ressurser og AI

Under arbeidet er dokumentasjon og AI-verktøy brukt som støtte i planleggings- og utviklingsfasen. Løsningen er tilpasset, forstått og videreutviklet av meg, og jeg kan forklare alle deler av koden og arkitekturen.

7. Oppsummering

Prosjektet viser grunnleggende og objektorientert programmering, strukturert kode, tydelig systemforståelse og faglig refleksjon. Fokus har vært på kvalitet, enkelhet og forståelse fremfor teknisk kompleksitet.