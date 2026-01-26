SELECT Radweg_zu_Gemeinde.radweg_id
FROM Radweg_zu_Gemeinde, Gemeinde
WHERE Gemeinde.schluessel = Radweg_zu_Gemeinde.gemeindeschluessel
  AND (Gemeinde.regierungsbezirk = "Oberfranken" OR Gemeinde.regierungsbezirk="Unterfranken")