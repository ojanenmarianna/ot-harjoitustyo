# Käyttöohje

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

## Komentorivitoiminnot


1. Alusta tietokanta sovelluksen käyttöä varten komennolla:

```bash
poetry run invoke build
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

3. Testit voi suorittaa komennolla
```bash
poetry run invoke test
```

4. Koodin laatutarkistuksen voi suorittaa komennolla

```bash
poetry run invoke lint
```

## Sovelluksen käyttäminen

Käynnistyksen jälkeen pelin voi alottaa painamalla enteriä. 
Pelaaja 1 käyttää punaisia pelimerkkejä ja pelaaja 2 keltaisia.
