SELECT regierungsbezirk, SUM(einwohner_w), SUM(einwohner_m)
FROM Gemeinde
GROUP BY regierungsbezirk