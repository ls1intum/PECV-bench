SELECT Freizeitpark.name, Freizeitpark.strasse, Gemeinde.name
FROM Freizeitpark, Gemeinde
WHERE Gemeinde.schluessel = Freizeitpark.gemeindeschluessel
