import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kassan_raha(self):
        self.assertEqual(self.kassa.kassassa_rahaa == 100000 and self.kassa.edulliset == 0 and
                    self.kassa.maukkaat == 0, True)

    def test_edullinen_osto(self):
        out = self.kassa.syo_edullisesti_kateisella(220)
        self.assertEqual(
        self.kassa.kassassa_rahaa == 100000 
        and out == 220 and self.kassa.edulliset == 0
        and self.kassa.maukkaat == 0, True)

    def test_edullinen_osto_2(self):
        out = self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.kassassa_rahaa == 100240 
        and out == 10 and self.kassa.edulliset == 1
        and self.kassa.maukkaat == 0, True)

    def test_maukas_osto(self):
        out = self.kassa.syo_maukkaasti_kateisella(220)
        self.assertEqual(self.kassa.kassassa_rahaa == 100000 
        and out == 220 and self.kassa.edulliset == 0
        and self.kassa.maukkaat == 0, True)

    def test_maukas_osto_2(self):
        out = self.kassa.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassa.kassassa_rahaa == 100400 
        and out == 10 and self.kassa.edulliset == 0
        and self.kassa.maukkaat == 1, True)

    def test_edullinen_kortilla(self):
        kortti = Maksukortti(220)
        out = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa == 100000 
        and out == False and self.kassa.edulliset == 0
        and self.kassa.maukkaat == 0 and str(kortti) == "Kortilla on rahaa 2.20 euroa", True)

    def test_edullinen_kortilla2(self):
        kortti = Maksukortti(240)
        out = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa == 100000 
        and out == True and self.kassa.edulliset == 1
        and self.kassa.maukkaat == 0 and str(kortti) == "Kortilla on rahaa 0.00 euroa", True)

    def test_maukas_kortilla(self):
        kortti = Maksukortti(390)
        out = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa == 100000 and out == False 
        and self.kassa.edulliset == 0
        and self.kassa.maukkaat == 0 and str(kortti) == "Kortilla on rahaa 3.90 euroa", True)

    def test_maukas_kortilla2(self):
        kortti = Maksukortti(410)
        out = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa == 100000 and out == True 
        and self.kassa.edulliset == 0
        and self.kassa.maukkaat == 1 and str(kortti) == "Kortilla on rahaa 0.10 euroa", True)

    def test_lataa_korttia(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, 50)
        self.assertEqual(self.kassa.kassassa_rahaa == 100050 
        and str(kortti) == "Kortilla on rahaa 0.50 euroa", True)

    def test_lataa_korttia2(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, -50)
        self.assertEqual(self.kassa.kassassa_rahaa == 100000 
        and str(kortti) == "Kortilla on rahaa 0.00 euroa", True)