# Vaatimusmäärittely

## Sovelluksen tarkoitus

Connect Four on kahden pelaajan lauatapeli, jossa pelaajat valitsevat värin ja sen jälkeen tiputtavat vuorollaan värillisiä pelimerkkejä 
seitsemän kolumnin ja kuuden rivin pystysuoraan ruudukkoon. Merkit tippuvat suoraan alas varaten sarakkeen alimman mahdollisen vapaana olevan ruudun.
Pelin tavoitteena on saada ensimmäisenä vaakasuoraan, pystysuoraan tai diagonaalille neljä peräkkäistä omaa pelimerkkiä.

## Käyttäjät
Sovellusta voi käyttää joko vieraana tai normaalina käyttäjänä.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- [x] Peliä voi pelata vieraana, jolloin pelien tulokset eivät jää tietokantaan muistiin.
- Käyttäjä voi luoda uuden tunnuksen
  - Käyttäjätunnuksen tulee olla uniikki ja pituudeltaan vähintään 3 merkkiä
- Käyttäjä voi kirjautua sisään
  - Tunnuksen tulee olla olemassa ja salasanan tulee täsmätä järjestelmään tallennettua salasanaa
  - Jos käyttäjää ei ole olemassa, tai salasana ei täsmää, järjestelmä ilmoittaa tästä

### Kirjautumisen jälkeen

- Käyttäjä voi pelata peliä
- Käyttäjä voi tarkastella omia aiempia pisteitään
- Käyttäjä voi kirjautua ulos

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Luodaan TOP10-lista, jolle pääsevät vain kirjautuneet käyttäjät
- Lisätään sovellukseen ylläpitäjiä, jotka voivat mm. poistaa muita käyttäjiä
- Mahdollisuus valita isompi tai pienempi ruudukko
- Algoritmi toteuttamaan vastapuolen pelaajaa
