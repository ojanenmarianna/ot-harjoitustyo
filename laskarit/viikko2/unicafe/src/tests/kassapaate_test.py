import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(100)

    def test_rahamaara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_myynnit_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_myynnit_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_jos_kateinen_riittaa_edulliseen_kassan_rahamara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_jos_kateinen_riittaa_maukkaaseen_kassan_rahamaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_jos_kateinen_riittaa_edullisesti_syotyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_jos_kateinen_riittaa_maukkasti_syotyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_jos_kateinen_riittaa_edulliseen_palautettava_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_jos_kateinen_riittaa_maukkaaseen_palautettava_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_jos_kateinen_ei_riita_edulliseen_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_jos_kateinen_ei_riita_maukkaaseen_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_jos_kateinen_ei_riita_edulliseen_syotyjen_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_jos_kateinen_ei_riita_maukkaasti_syotyjen_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_jos_kateinen_ei_riita_edulliseen_rahat_palautetaan_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_jos_kateinen_ei_riita_maukkaaseen_rahat_palautetaan_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
    
    def test_jos_kortilla_rahaa_edullinen_lounas_veloitetaan_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 140)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_jos_kortilla_rahaa_maukas_lounas_veloitetaan_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_jos_kortilla_rahaa_edullisten_lounaiden_maara_kasvaa(self):
        self.maksukortti.lataa_rahaa(140)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_jos_kortilla_rahaa_edullinen_vahennetaan_oikein(self):
        self.maksukortti.lataa_rahaa(140)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 0)

    def test_jos_kortilla_rahaa_maukas_vahennetaan_oikein(self):
        self.maksukortti.lataa_rahaa(300)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 0)

    def test_jos_kortilla_rahaa_maukkaiden_lounaiden_maara_kasvaa(self):
        self.maksukortti.lataa_rahaa(300)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_jos_kortilla_syodaan_edullisesti_kassa_ei_muutu(self):
        self.maksukortti.lataa_rahaa(140)
        self.kassapaate.syo_edullisesti_kortilla
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_jos_kortilla_syodaan_maukkaasti_kassa_ei_muutu(self):
        self.maksukortti.lataa_rahaa(300)
        self.kassapaate.syo_maukkaasti_kortilla
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_jos_kortilla_ei_rahaa_edullisen_ostaminen_palauttaa_false(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)

    def test_jos_kortilla_ei_rahaa_maukkaan_ostaminen_palauttaa_false(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_jos_kortilla_ei_rahaa_edullinen_ei_muuta_kortin_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)

    def test_jos_kortilla_ei_rahaa_maukas_ei_muuta_kortin_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)

    def test_jos_kortilla_ei_rahaa_edullisten_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_jos_kortilla_ei_rahaa_maukkaiden_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_jos_kortilla_ei_rahaa__edullista_ostettaessa_kassan_summa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_jos_kortilla_ei_rahaa_maukasta_ostettaessa_kassan_summa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kasvattaa_kortin_rahamaaraa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_lataa_rahaa_ei_voi_vahentaa_kortin_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 100)