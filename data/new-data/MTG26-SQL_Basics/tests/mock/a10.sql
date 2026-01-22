SELECT COUNT(*) as Anzahl,gemeindeschluessel
FROM Wanderweg_zu_Gemeinde
GROUP BY gemeindeschluessel
ORDER BY Anzahl DESC