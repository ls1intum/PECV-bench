SELECT Freizeitpark.name as Park_name, Gemeinde.name as Gemeinde_name, Freizeitpark.strasse
FROM Freizeitpark, Gemeinde
WHERE Gemeinde.schluessel = Freizeitpark.gemeindeschluessel
