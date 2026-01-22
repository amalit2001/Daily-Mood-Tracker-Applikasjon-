Prosjektdokumentasjon – Daily Mood Tracker

1. Beskrivelse av løsningen

Daily Mood Tracker er en liten webbasert applikasjon laget i Python med Flask, der brukeren kan loggføre eget humør, energinivå og korte refleksjoner fra hverdagen.
Alle registreringer lagres lokalt i en enkel SQL-database og kan hentes frem senere.

Applikasjonen er laget som et personlig verktøy for økt bevissthet rundt egen trivsel og hverdag. Den er ikke ment som et medisinsk eller helsefaglig verktøy, men som et lavterskel refleksjonsverktøy.

Målgruppe:
Applikasjonen er ment for personer som ønsker å reflektere over egen hverdag på en strukturert, men enkel måte.

Problemet løsningen adresserer:
I en travel hverdag er det lett å miste oversikt over egen trivsel.
Applikasjonen gir brukeren et ukomplisert, men strukturert system for dette uten krav til teknisk forkunnskap.

2. Krav
2.1 Funksjonelle krav

Applikasjonen skal:

- La brukeren registrere daglig humør (glad, rolig, stresset, trist)

- La brukeren velge energinivå (1–5)

- Gi mulighet for å skrive et kort refleksjons-notat

- Lagre registreringene permanent

- Vise tidligere registrerte logger

- Gi tydelig tilbakemelding når en registrering er lagret

2.2 Krav til brukervennlighet og enkelhet

- Applikasjonen skal være lett å bruke uten forklaring

- Brukergrensesnittet skal være ryddig og oversiktlig

- Det skal være få valg

- Skjemaelementer skal være tydelig merket

- Designet skal ha rolige farger og god kontrast


3. Systemstruktur
3.1 Overordnet arkitektur

Applikasjonen er strukturert slik at hver del av systemet har sitt eget ansvar:

Frontend: HTML (Jinja-maler) og CSS

Backend: Flask (Python)

Datamodell: Objektorientert klasse (Mood)

Datalagring: SQLite via egen database-modul

3.2 Mappestruktur
daily-mood-tracker/
│
├── models/
│   └── mood.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── .gitinore
├── app.py
├── database.py
│
├── README.md
└── reflection.md

3.3 Klasser og ansvar

Mood (klasse)
Representerer én enkel humørregistrering og inneholder tilhørende data.

Attributter:

mood

energy

note

datetime

Klassen er brukt for å samle data som naturlig hører sammen, og benytter innkapsling for å strukturere informasjonen.

database.py
Har ansvar for:

- Opprettelse av database og tabell

- Lagring av humørdata

- Henting av lagrede registreringer

app.py
Har ansvar for:

- Håndtere brukerinput via Flask-ruter

- Kobler database, frontend og datamodell

- Sender data videre til visning i HTML

3.4 Enkel UML-inspirert skisse
+----------------+
|     Mood       |
+----------------+
| mood           |
| energy         |
| note           |
| datetime       |
+----------------+

Mood - brukes av app.py  
app.py - kommuniserer med database.py

4. Arbeidsprosess

Jeg startet prosjektet med å avklare hva løsningen skulle gjøre og hvem den var ment for. Deretter ble prosjektstrukturen godt planlagt for å sikre ryddig kode og god oversikt.

Utviklingen ble gjennomført stegvis:

1. Bekrefte at Flask-applikasjonen kjørte korrekt

2. Lage enkel HTML-visning

3. Implementere skjema for brukerinput

4. Bruke objektorientert programmering for å strukturere data

5. Vise registreringer i brukergrensesnittet

6. Gå fra midlertidig lagring i minne til permanent lagring i SQLite-database

7. Forbedre brukeropplevelse med visuell tilbakemelding

Denne tilnærmingen gjorde det enklere å teste underveis og rette feil tidlig.

5. Sikkerhet, GDPR og universell utforming
5.1 Sikkerhet

Applikasjonen kjører lokalt og har ingen brukerpålogging eller nettverkstilkobling. Dette reduserer angrepsflaten betydelig. I et større system ville det vært nødvendig med tiltak som kryptering, tilgangskontroll og validering av input av data.

5.2 GDPR og personvern

Applikasjonen behandler ikke direkte identifiserbare personopplysninger som navn,  fødselsnummer eller e-post. Humørdata kan likevel anses som personlig informasjon. I et mer profesjonelt system bør brukeren informeres tydelig om datalagring, og data bør beskyttes bedre.

5.3 Universell utforming

Løsningen er laget med fokus på enkelhet og tilgjengelighet:

- Tydelige labels på alle input-felt

- God kontrast mellom bakgrunn og tekst

- Ryddig layout og store klikkflater 

Videre forbedringer kunne vært å ha bedre støtte for skjermlesere og tastaturnavigasjon.

6. Bruk av ressurser og AI

Under arbeidet er dokumentasjon og AI-verktøy brukt som støtte i planleggings- og utviklingsfasen. Løsningen er tilpasset, forstått og videreutviklet av meg, og jeg kan forklare alle deler av koden og arkitekturen.

7. Oppsummering

Gjennom prosjektet har jeg vist forståelse for både grunnleggende og objektorientert programmering, samt hvordan god struktur og tydelig systemoppbygging bidrar til oversiktlig og vedlikeholdbar kode. Fokus har vært på enkelhet, forståelse og kvalitet, heller enn teknisk kompleksitet. Løsningen kan videreutvikles med funksjoner som brukerprofiler, grafisk visning av humør over tid eller tilpasning for mobilbruk.