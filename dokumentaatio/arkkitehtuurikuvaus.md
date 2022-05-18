# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa vastaavaa kerrosrakennette kuin referenssisovelluskin.

Pakkaus *ui* käsittelee pelin käyttöliittymää eli pelin sisäisen toiminnan ja käyttäjän välistä vuorovaikutusta, *services* pelin sovelluslogiikkaa ja *repositories* tietojen pysyväistallennusta. Lisäksi on pakkaukset *assets* ja *images*, jotka sisältävät Pygamen käytön kannalta oleelliset kuvat sekä *assetit*.

## Käyttöliittymä

Käyttöliittymällä on 5 näkymää:
* Aloitusnäyttö
* Pelisäännöt
* Top10-tuloslista
* Pelinäyttö
* Uuden tuloksen tallentaminen / pelin lopetusnäyttö
