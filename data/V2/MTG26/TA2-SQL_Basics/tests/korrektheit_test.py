import unittest
import os

# ensure to always use the latest version of sql_testing_tools
os.system('pip install -U sql_testing_tools')

# import sql_testing_tools
import sql_testing_tools.BaseAccess as Ba
import sql_testing_tools.Helper as He


class TestSQLQueries(unittest.TestCase):

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


    #########################################
    #########################################
    
    def test_a01_SPALTEN(self):
        nr = '01'
        res = He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a01_TABELLEN(self):
        nr = '01'
        res = He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a01_BEDINGUNG(self):
        nr = '01'
        res = He.checkCondition("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a01_SORTIERUNG(self):
        nr = '01'
        res = He.checkOrder("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a01_GRUPPIERUNG(self):
        nr = '01'
        res = He.checkGroup("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a01_checkEquality(self):
        nr = '01'
        if He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "" or He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "":
            self.fail("\n\nDie Abgabe stimmt nicht mit der Musterlösung überein.")
        res = He.checkEquality("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    #########################################
    #########################################
    
    def test_a02_SPALTEN(self):
        nr = '02'
        res = He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a02_TABELLEN(self):
        nr = '02'
        res = He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a02_BEDINGUNG(self):
        nr = '02'
        res = He.checkCondition("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a02_SORTIERUNG(self):
        nr = '02'
        res = He.checkOrder("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a02_GRUPPIERUNG(self):
        nr = '02'
        res = He.checkGroup("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a02_checkEquality(self):
        nr = '02'
        if He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "" or He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "":
            self.fail("\n\nDie Abgabe stimmt nicht mit der Musterlösung überein.")
        res = He.checkEquality("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    #########################################
    #########################################
    
    def test_a03_SPALTEN(self):
        nr = '03'
        res = He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a03_TABELLEN(self):
        nr = '03'
        res = He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a03_BEDINGUNG(self):
        nr = '03'
        res = He.checkCondition("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a03_SORTIERUNG(self):
        nr = '03'
        res = He.checkOrder("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a03_GRUPPIERUNG(self):
        nr = '03'
        res = He.checkGroup("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a03_checkEquality(self):
        nr = '03'
        if He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "" or He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "":
            self.fail("\n\nDie Abgabe stimmt nicht mit der Musterlösung überein.")
        res = He.checkEquality("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    #########################################
    #########################################
    
    def test_a04_SPALTEN(self):
        nr = '04'
        res = He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a04_TABELLEN(self):
        nr = '04'
        res = He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a04_BEDINGUNG(self):
        nr = '04'
        res = He.checkCondition("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a04_SORTIERUNG(self):
        nr = '04'
        res = He.checkOrder("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a04_GRUPPIERUNG(self):
        nr = '04'
        res = He.checkGroup("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a04_checkEquality(self):
        nr = '04'
        if He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "" or He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "":
            self.fail("\n\nDie Abgabe stimmt nicht mit der Musterlösung überein.")
        res = He.checkEquality("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    #########################################
    #########################################
    
    def test_a05_SPALTEN(self):
        nr = '05'
        res = He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a05_TABELLEN(self):
        nr = '05'
        res = He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a05_BEDINGUNG(self):
        nr = '05'
        res = He.checkCondition("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a05_SORTIERUNG(self):
        nr = '05'
        res = He.checkOrder("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a05_GRUPPIERUNG(self):
        nr = '05'
        res = He.checkGroup("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a05_checkEquality(self):
        nr = '05'
        if He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "" or He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "":
            self.fail("\n\nDie Abgabe stimmt nicht mit der Musterlösung überein.")
        res = He.checkEquality("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    #########################################
    #########################################
    
    def test_a06_SPALTEN(self):
        nr = '06'
        res = He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a06_TABELLEN(self):
        nr = '06'
        res = He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a06_BEDINGUNG(self):
        nr = '06'
        res = He.checkCondition("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a06_SORTIERUNG(self):
        nr = '06'
        res = He.checkOrder("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a06_GRUPPIERUNG(self):
        nr = '06'
        res = He.checkGroup("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a06_checkEquality(self):
        nr = '06'
        if He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "" or He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "":
            self.fail("\n\nDie Abgabe stimmt nicht mit der Musterlösung überein.")
        res = He.checkEquality("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    #########################################
    #########################################
    
    def test_a07_SPALTEN(self):
        nr = '07'
        res = He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a07_TABELLEN(self):
        nr = '07'
        res = He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a07_BEDINGUNG(self):
        nr = '07'
        res = He.checkCondition("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a07_SORTIERUNG(self):
        nr = '07'
        res = He.checkOrder("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a07_GRUPPIERUNG(self):
        nr = '07'
        res = He.checkGroup("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a07_checkEquality(self):
        nr = '07'
        if He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "" or He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "":
            self.fail("\n\nDie Abgabe stimmt nicht mit der Musterlösung überein.")
        res = He.checkEquality("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    #########################################
    #########################################
    
    def test_a08_SPALTEN(self):
        nr = '08'
        res = He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a08_TABELLEN(self):
        nr = '08'
        res = He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a08_BEDINGUNG(self):
        nr = '08'
        res = He.checkCondition("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a08_SORTIERUNG(self):
        nr = '08'
        res = He.checkOrder("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a08_GRUPPIERUNG(self):
        nr = '08'
        res = He.checkGroup("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a08_checkEquality(self):
        nr = '08'
        if He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "" or He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "":
            self.fail("\n\nDie Abgabe stimmt nicht mit der Musterlösung überein.")
        res = He.checkEquality("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    #########################################
    #########################################
    
    def test_a09_SPALTEN(self):
        nr = '09'
        res = He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a09_TABELLEN(self):
        nr = '09'
        res = He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a09_BEDINGUNG(self):
        nr = '09'
        res = He.checkCondition("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a09_SORTIERUNG(self):
        nr = '09'
        res = He.checkOrder("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a09_GRUPPIERUNG(self):
        nr = '09'
        res = He.checkGroup("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a09_checkEquality(self):
        nr = '09'
        if He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "" or He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "":
            self.fail("\n\nDie Abgabe stimmt nicht mit der Musterlösung überein.")
        res = He.checkEquality("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    #########################################
    #########################################
    
    def test_a10_SPALTEN(self):
        nr = '10'
        res = He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a10_TABELLEN(self):
        nr = '10'
        res = He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a10_BEDINGUNG(self):
        nr = '10'
        res = He.checkCondition("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a10_SORTIERUNG(self):
        nr = '10'
        res = He.checkOrder("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a10_GRUPPIERUNG(self):
        nr = '10'
        res = He.checkGroup("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

    def test_a10_checkEquality(self):
        nr = '10'
        if He.checkColumns("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "" or He.checkTables("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql") != "":
            self.fail("\n\nDie Abgabe stimmt nicht mit der Musterlösung überein.")
        res = He.checkEquality("assignment/aufgabe"+nr+".sql", "mock/a"+nr+".sql")
        if res != "":
            self.fail(res)

