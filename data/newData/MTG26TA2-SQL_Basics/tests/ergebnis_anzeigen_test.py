import unittest
import os

# ensure to always use the latest version of sql_testing_tools
os.system('pip install -U sql_testing_tools')

# import sql_testing_tools
import sql_testing_tools.BaseAccess as Ba
import sql_testing_tools.Helper as He


class TestErgebnistabellenAnzeigen(unittest.TestCase):

    # Datenbank auswählen 
    # Quelle: www.dbiu.de (SQL-Frontend) bzw. www.datenbanken-im-unterricht.de (Katalog und Rohdaten)
    
    # Derzeit verfügbar (Klassendiagramme, automatisch aktualisierte Liste):
    # https://github.com/ValentinHerrmann/dbiu_databases 

    # Stand 04.02.2025 verfügbar:
    #  1 - dbiu.bahn
    #  2 - dbiu.bayern
    #  3 - dbiu.bundestag
    #  4 - dbiu.bundestag_einfach
    #  5 - dbiu.film_fernsehen
    #  6 - dbiu.haushaltsausstattung
    #  7 - dbiu.straftaten
    #  8 - dbiu.straftaten_einfach
    #  9 - dbiu.kunstsammlung
    # 10 - dbiu.ladepunkte
    # 11 - dbiu.laenderspiele
    # 12 - dbiu.lebensmittel
    # 13 - dbiu.schulstatistik
    # 14 - dbiu.studierende
    # 15 - dbiu.unfallstatistik
    # 16 - dbiu.videospiele_einfach
    # 17 - dbiu.videospiele
    # 18 - dbiu.wetterdaten


    # Auswahl einer Datenbank mit Name oder Nummer (unbedingt in beiden test.py Dateien!)
    Ba.setDBName("dbiu.bayern")  
    # oder: Ba.setDBName(2) 

    # Einstellungen für Ausgabe der Ergebnistabelle
    anzahlZeilen = 10
    maxLineLength = 100

    #########################################
    #########################################

    def test_a01_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe01.sql", self.anzahlZeilen, self.maxLineLength))
        except Exception as e:
            self.fail(e)


    def test_a02_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe02.sql", self.anzahlZeilen, self.maxLineLength))
        except Exception as e:
            self.fail(e)

    def test_a03_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe03.sql", self.anzahlZeilen, self.maxLineLength))
        except Exception as e:
            self.fail(e)

    def test_a04_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe04.sql", self.anzahlZeilen, self.maxLineLength))
        except Exception as e:
            self.fail(e)

    def test_a05_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe05.sql", self.anzahlZeilen, self.maxLineLength))
        except Exception as e:
            self.fail(e)

    def test_a06_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe06.sql", self.anzahlZeilen, self.maxLineLength))
        except Exception as e:
            self.fail(e)

    def test_a07_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe07.sql", self.anzahlZeilen, self.maxLineLength))
        except Exception as e:
            self.fail(e)

    def test_a08_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe08.sql", self.anzahlZeilen, self.maxLineLength))
        except Exception as e:
            self.fail(e)

    def test_a09_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe09.sql", self.anzahlZeilen, self.maxLineLength))
        except Exception as e:
            self.fail(e)

    def test_a10_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe10.sql", self.anzahlZeilen, self.maxLineLength))
        except Exception as e:
            self.fail(e)
            

    #########################################
    #########################################