SELECT Zoo.name, Zoo.url as Internetadresse, Gemeinde.name, Gemeinde.regierungsbezirk
FROM Zoo, Gemeinde
WHERE Zoo.gemeindeschluessel = Gemeinde.schluessel