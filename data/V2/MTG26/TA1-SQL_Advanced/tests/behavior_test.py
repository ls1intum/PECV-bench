import unittest
from sql import BaseAccess as Ba
from sql import Helper as He


class TestSQLQueries(unittest.TestCase):

    def test_a01_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe01.sql"))
        except Exception as e:
            self.fail(e)


    def test_a02_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe02.sql"))
        except Exception as e:
            self.fail(e)

    def test_a03_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe03.sql"))
        except Exception as e:
            self.fail(e)

    def test_a04_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe04.sql"))
        except Exception as e:
            self.fail(e)

    def test_a05_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe05.sql"))
        except Exception as e:
            self.fail(e)

    def test_a06_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe06.sql"))
        except Exception as e:
            self.fail(e)

    def test_a07_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe07.sql"))
        except Exception as e:
            self.fail(e)

    def test_a08_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe08.sql"))
        except Exception as e:
            self.fail(e)

    def test_a09_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe09.sql"))
        except Exception as e:
            self.fail(e)

    def test_a10_KEIN_FEHLER__SQL_Ergebnis_anzeigen(self):
        try:
            self.fail(Ba.runAndGetStringTable_fromFile("assignment/aufgabe10.sql"))
        except Exception as e:
            self.fail(e)

    def test_a01_checkEquality(self):
        res = He.checkEquality("assignment/aufgabe01.sql", "mock/a01.sql")
        if res != "":
            self.fail(res)

    def test_a02_checkEquality(self):
        res = He.checkEquality("assignment/aufgabe02.sql", "mock/a02.sql")
        if res != "":
            self.fail(res)

    def test_a03_checkEquality(self):
        res = He.checkEquality("assignment/aufgabe03.sql", "mock/a03.sql")
        if res != "":
            self.fail(res)

    def test_a04_checkEquality(self):
        res = He.checkEquality("assignment/aufgabe04.sql", "mock/a04.sql")
        if res != "":
            self.fail(res)

    def test_a05_checkEquality(self):
        res = He.checkEquality("assignment/aufgabe05.sql", "mock/a05.sql")
        if res != "":
            self.fail(res)

    def test_a06_checkEquality(self):
        res = He.checkEquality("assignment/aufgabe06.sql", "mock/a06.sql")
        if res != "":
            self.fail(res)

    def test_a07_checkEquality(self):
        res = He.checkEquality("assignment/aufgabe07.sql", "mock/a07.sql")
        if res != "":
            self.fail(res)

    def test_a08_checkEquality(self):
        res = He.checkEquality("assignment/aufgabe08.sql", "mock/a08.sql")
        if res != "":
            self.fail(res)

    def test_a09_checkEquality(self):
        res = He.checkEquality("assignment/aufgabe09.sql", "mock/a09.sql")
        if res != "":
            self.fail(res)

    def test_a10_checkEquality(self):
        res = He.checkEquality("assignment/aufgabe10.sql", "mock/a10.sql")
        if res != "":
            self.fail(res)

