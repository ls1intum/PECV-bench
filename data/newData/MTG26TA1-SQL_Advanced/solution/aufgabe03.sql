SELECT Schwimmbad.name, Schwimmbad.art as Art, Gemeinde.name, Gemeinde.einwohner_m, Gemeinde.einwohner_w
FROM Schwimmbad, Gemeinde
WHERE Gemeinde.schluessel = Schwimmbad.gemeindeschluessel
