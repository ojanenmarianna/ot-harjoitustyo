# Connect Four

Connect Four on vuoropeli, jossa pelaajan on tarkoitus saada neljä pelimerkkiä peräkkäin joko riviin, jonoon tai diagonaaliin.
Sovellus toteutetaan Helsingin yliopiston kurssilla Ohjelmistotekniikka 2022.

## Huomio Python versiosta

Sovelluksen toiminta on testattu käyttäen Pythonin versiota `3.8`. Vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.

## Dokumentaatio

[Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

[Changelog](./dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

## Komentorivitoiminnot

1. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

2. Testit voi suorittaa komennolla
```bash
poetry run invoke test
```

3. Koodin laatutarkistuksen voi suorittaa komennolla

```bash
poetry run invoke lint
```

