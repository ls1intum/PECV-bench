SELECT gemeindeschluessel,COUNT(*) as Anzahl
FROM Wanderweg_zu_Gemeinde
GROUP BY gemeindeschluessel
ORDER BY Anzahl DESC