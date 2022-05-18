# Vaatimusmäärittely

## Sovelluksen tarkoitus

Connect Four on kahden pelaajan lauatapeli, jossa pelaajat valitsevat värin ja sen jälkeen tiputtavat vuorollaan värillisiä pelimerkkejä 
seitsemän kolumnin ja kuuden rivin pystysuoraan ruudukkoon. Merkit tippuvat suoraan alas varaten sarakkeen alimman mahdollisen vapaana olevan ruudun.
Pelin tavoitteena on saada ensimmäisenä vaakasuoraan, pystysuoraan tai diagonaalille neljä peräkkäistä omaa pelimerkkiä.

## Käyttäjät

Sovellusta voi käyttää vieraana ja jokainen pelaaja voi tallentaa voittonsa nimimerkin alle. 

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- [x] Peliä voi pelata vieraana, jolloin pelien tulokset eivät jää tietokantaan muistiin.
- [x] Aloitusnäkymästä pelaaja voi valita haluaako hän,
  - [x] Aloittaa pelin pelaamisen painamalla enteriä
  - [x] Lukea ohjeet
  - [x] Katsoa TOP10-listaa 
 - [x] Pelinäkymässä pelaaja voi,
  - [x] Pelata peliä esim. jonkun kaverin kanssa samalla koneella
 - [x] Pelin tullessa loppuun (voittamalla tai tasapelillä)
  - [x] Pelaaja voi tallentaa uuden voiton tietokantaan
    - [x] Jos nimimerkillä on jo voittoja, voittojen määrää kasvatetaan yhdellä
    - [x] Jos nimimerkillä ei ole vielä voittoja, luodaan uusi nimimerkki ja tallennetaan sille yksi voitto.

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Lisätään sovellukseen käyttäjäryhmiä, kuten vieraat ja kirjautuneet käyttäjät
- Lisätään sovellukseen ylläpitäjiä, jotka voivat mm. poistaa muita käyttäjiä
- Mahdollisuus valita isompi tai pienempi ruudukko
- Algoritmi toteuttamaan vastapuolen pelaajaa
