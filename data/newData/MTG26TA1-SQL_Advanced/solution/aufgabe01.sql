SELECT Zoo.name, Gemeinde.name, Gemeinde.regierungsbezirk, Zoo.url as Internetadresse
FROM Zoo, Gemeinde
WHERE Zoo.gemeindeschluessel = Gemeinde.schluessel