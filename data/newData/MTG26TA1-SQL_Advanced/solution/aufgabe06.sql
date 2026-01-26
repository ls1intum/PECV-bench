SELECT *
FROM Gemeinde, Wanderweg_zu_Gemeinde
WHERE Gemeinde.schluessel = Wanderweg_zu_Gemeinde.gemeindeschluessel
  AND einwohner_m > 500000