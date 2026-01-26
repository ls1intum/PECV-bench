SELECT Zoo.name, Gemeinde.name, Gemeinde.regierungsbezirk, Zoo.url
FROM Zoo, Gemeinde
WHERE Zoo.gemeindeschluessel = Gemeinde.schluessel