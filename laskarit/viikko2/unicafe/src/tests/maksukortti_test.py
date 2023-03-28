import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alkusaldo_toimii(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.10 euroa")

    def test_lataus_toimii(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.20 euroa")

    def test_saldo_vahenee(self):
        out = self.maksukortti.ota_rahaa(10)
        self.assertEqual(out, True)

    def test_saldo_ei_mene_negatiiviseks(self):
        out = self.maksukortti.ota_rahaa(20)
        self.assertEqual(out, False)