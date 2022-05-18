# Käyttöohje

## Asennus

1. Ennen ohjelman käynnistämistä, senna riippuvuudet komennolla:

```bash
poetry install
```
2. Sen jälkeen alusta tietokanta sovelluksen käyttöä varten komennolla:

```bash
poetry run invoke build
```

3. Nyt ohjelman voi käynnistää komennolla:

```bash
poetry run invoke start
```


## Sovelluksen käyttäminen

Käynnistyksen jälkeen pelin voi alottaa painamalla enteriä. Aloitusnäkymästä voi myös siirtyä lukemaan pelin säännöt painamalla näppäintä 1 tai katsomaan TOP10-listaa näppäimellä 2. Näistä pääsee takaisin painamalla yläkulmassa olevaa rastia.

Pelaaja 1 käyttää punaisia pelimerkkejä ja pelaaja 2 keltaisia. 

Pelin päättyessä jomman kumman pelaajan voittoon, pelaaja voi tallentaa voittonsa syöttämällä nimimerkin näppäimistön kautta. Eteenpäin pääsee painamalla enteriä.

Jos peli päättyy tasapeliin, siitä tulee näkyviin ilmoitus, josta pääsee eteenpäin painamalla enteriä.
