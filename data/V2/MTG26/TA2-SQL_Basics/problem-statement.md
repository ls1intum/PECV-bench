### Tabellenschema

Alle Abfragen beziehen sich auf folgende Datenbank (auch [hier](https://www.dbiu.de/bayern/) zu finden; Achtung: Datensätze können leicht abweichen):

<!---![Klassendiagramm_dbiu-bayern.drawio.svg](/api/core/files/markdown/Markdown_2024-11-10T13-52-29-793_05deab6a.svg)--->

![image.png](/api/core/files/markdown/Markdown_2025-09-13T18-05-51-900_8553f729.png)


### Automatische Überprüfung der Korrektheit

Für jede Aufgabe wird überprüft, ob die korrekten Spalten  und Tabellen ausgewählt werden und wenn ja, ob deine Abgabe äquivalent zur Musterlösung ist.

Die Aufgaben sind jeweils korrekt gelöst, wenn `Aufgabe X` grün ist (3 von 3 bestanden). Die Zeile darunter (`Ergebnistabelle`) wird immer rot bleiben (0 von 1 bestanden). Hier werden die ersten zehn Ergebniszeilen und wie viele weitere es gibt, angezeigt. 

Eine korrekt gelöste Aufgabe sieht z.B. so aus: 

![image.png](/api/core/files/markdown/Markdown_2025-01-17T21-11-52-308_5437573c.png)


### Fortschritt

@startuml
skinparam minClassWidth 10
skinparam nodesep 10
skinparam ranksep 10

rectangle "Aufgabe 01" #testsColor(test_a01_checkEquality)  {
    rectangle "SELECT" as S01  #testsColor(test_a01_SPALTEN) 
    rectangle "FROM" as T01 #testsColor(test_a01_TABELLEN) 
    rectangle "WHERE" as B01 #testsColor(test_a01_BEDINGUNG) 
    rectangle "ORDER BY" as SO01 #testsColor(test_a01_SORTIERUNG) 
    rectangle "GROUP BY" as G01 #testsColor(test_a01_GRUPPIERUNG) 
}
rectangle "Aufgabe 02" #testsColor(test_a02_checkEquality)  {
    rectangle "SELECT" as S02  #testsColor(test_a02_SPALTEN)
    rectangle "FROM" as T02 #testsColor(test_a02_TABELLEN) 
    rectangle "WHERE" as B02 #testsColor(test_a02_BEDINGUNG) 
    rectangle "ORDER BY" as SO02 #testsColor(test_a02_SORTIERUNG) 
    rectangle "GROUP BY" as G02 #testsColor(test_a02_GRUPPIERUNG) 
}
rectangle "Aufgabe 03" #testsColor(test_a03_checkEquality)  {
    rectangle "SELECT" as S03  #testsColor(test_a03_SPALTEN)
    rectangle "FROM" as T03 #testsColor(test_a03_TABELLEN) 
    rectangle "WHERE" as B03 #testsColor(test_a03_BEDINGUNG) 
    rectangle "ORDER BY" as SO03 #testsColor(test_a03_SORTIERUNG) 
    rectangle "GROUP BY" as G03 #testsColor(test_a03_GRUPPIERUNG) 
}
rectangle "Aufgabe 04" #testsColor(test_a04_checkEquality)  {
    rectangle "SELECT" as S04 #testsColor(test_a04_SPALTEN) 
    rectangle "FROM" as T04 #testsColor(test_a04_TABELLEN) 
    rectangle "WHERE" as B04 #testsColor(test_a04_BEDINGUNG) 
    rectangle "ORDER BY" as SO04 #testsColor(test_a04_SORTIERUNG) 
    rectangle "GROUP BY" as G04 #testsColor(test_a04_GRUPPIERUNG) 
}
rectangle "Aufgabe 05" #testsColor(test_a05_checkEquality)  {
    rectangle "SELECT" as S05  #testsColor(test_a05_SPALTEN)
    rectangle "FROM" as T05 #testsColor(test_a05_TABELLEN) 
    rectangle "WHERE" as B05 #testsColor(test_a05_BEDINGUNG) 
    rectangle "ORDER BY" as SO05 #testsColor(test_a05_SORTIERUNG) 
    rectangle "GROUP BY" as G05 #testsColor(test_a05_GRUPPIERUNG)
}
rectangle "Aufgabe 06" #testsColor(test_a06_checkEquality)  {
    rectangle "SELECT" as S06 #testsColor(test_a06_SPALTEN)
    rectangle "FROM" as T06 #testsColor(test_a06_TABELLEN)  
    rectangle "WHERE" as B06 #testsColor(test_a06_BEDINGUNG) 
    rectangle "ORDER BY" as SO06 #testsColor(test_a06_SORTIERUNG) 
    rectangle "GROUP BY" as G06 #testsColor(test_a06_GRUPPIERUNG) 
}
rectangle "Aufgabe 07" #testsColor(test_a07_checkEquality)  {
    rectangle "SELECT" as S07  #testsColor(test_a07_SPALTEN)
    rectangle "FROM" as T07 #testsColor(test_a07_TABELLEN) 
    rectangle "WHERE" as B07 #testsColor(test_a07_BEDINGUNG) 
    rectangle "ORDER BY" as SO07 #testsColor(test_a07_SORTIERUNG) 
    rectangle "GROUP BY" as G07 #testsColor(test_a07_GRUPPIERUNG) 
    
}
rectangle "Aufgabe 08" #testsColor(test_a08_checkEquality)  {
    rectangle "SELECT" as S08  #testsColor(test_a08_SPALTEN)
    rectangle "FROM" as T08 #testsColor(test_a08_TABELLEN) 
    rectangle "WHERE" as B08 #testsColor(test_a08_BEDINGUNG) 
    rectangle "ORDER BY" as SO08 #testsColor(test_a08_SORTIERUNG) 
    rectangle "GROUP BY" as G08 #testsColor(test_a08_GRUPPIERUNG) 
}
rectangle "Aufgabe 09" #testsColor(test_a09_checkEquality)  {
    rectangle "SELECT" as S09  #testsColor(test_a09_SPALTEN)
    rectangle "FROM" as T09 #testsColor(test_a09_TABELLEN) 
    rectangle "WHERE" as B09 #testsColor(test_a09_BEDINGUNG) 
    rectangle "ORDER BY" as SO09 #testsColor(test_a09_SORTIERUNG) 
    rectangle "GROUP BY" as G09 #testsColor(test_a09_GRUPPIERUNG) 
}
rectangle "Aufgabe 10" #testsColor(test_a10_checkEquality)  {
    rectangle "SELECT" as S10  #testsColor(test_a10_SPALTEN)
    rectangle "FROM" as T10 #testsColor(test_a10_TABELLEN) 
    rectangle "WHERE" as B10 #testsColor(test_a10_BEDINGUNG) 
    rectangle "ORDER BY" as SO10 #testsColor(test_a10_SORTIERUNG) 
    rectangle "GROUP BY" as G10 #testsColor(test_a10_GRUPPIERUNG) 
}
@enduml

### Aufgaben: 
Gib immer genau die geforderten Daten aus und nicht mehr. Sortiere nicht und benenne keine mit Spalten mit AS, wenn du nicht dazu aufgefordert wirst. Die Aufgaben werden jeweils in der entsprechenden Datei bearbeitet.

Falls du bei Gruppierung und Aggregatfunktionen Schwierigkeiten hast, hilft dir dieses Video **(bitte Kopfhörer verwenden!)**: [bycs.link/simpleclub-group-sort-aggregat](https://bycs.link/simpleclub-group-sort-aggregat)

[task][Aufgabe 01](test_a01_checkEquality,test_a01_SPALTEN,test_a01_TABELLEN,test_a01_BEDINGUNG,test_a01_SORTIERUNG,test_a01_GRUPPIERUNG)
[task][Ergebnistabelle](test_a01_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Vervollständige die SQL-Abfrage so, dass sie ID, Name, Art und URL aller Freibäder ausgibt.


[task][Aufgabe 02](test_a02_checkEquality,test_a02_SPALTEN,test_a02_TABELLEN,test_a02_BEDINGUNG,test_a02_SORTIERUNG,test_a02_GRUPPIERUNG)
[task][Ergebnistabelle](test_a02_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die ausgibt, wie viele Gemeinden es im Regierungsbezirk `Oberbayern` gibt.


[task][Aufgabe 03](test_a03_checkEquality,test_a03_SPALTEN,test_a03_TABELLEN,test_a03_BEDINGUNG,test_a03_SORTIERUNG,test_a03_GRUPPIERUNG)
[task][Ergebnistabelle](test_a03_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die Name, Straße und URL (also die Internetadresse) alle Zoos in der Gemeinde mit Schluessel `09162000` ausgibt.

[task][Aufgabe 04](test_a04_checkEquality,test_a04_SPALTEN,test_a04_TABELLEN,test_a04_BEDINGUNG,test_a04_SORTIERUNG,test_a04_GRUPPIERUNG)
[task][Ergebnistabelle](test_a04_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die die Summe aller weiblichen Einwohnerinnen und die Summe aller männlichen Einwohner gruppiert nach Regierungsbezirk und den Namen des jeweiligen Regierungsbezirks ausgibt.

[task][Aufgabe 05](test_a05_checkEquality,test_a05_SPALTEN,test_a05_TABELLEN,test_a05_BEDINGUNG,test_a05_SORTIERUNG,test_a05_GRUPPIERUNG)
[task][Ergebnistabelle](test_a05_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die die durchschnittliche Fläche der Gemeinde eines Kreises (=Landkreis) und den Namen und Regierungsbezirk des jeweiligen Landkreises anzeigt. Sortiere die Ausgabe nach Name des Landkreises.

*Achtung: Du kannst bei der Verwendung von Gruppierung nur Spalten, nach denen gruppiert wird und solche, die mit Aggregatfunktionen zusammengefasst werden, anzeigen! Überlege, wie du dieses Problem hier lösen kannst.* 


[task][Aufgabe 06](test_a06_checkEquality,test_a06_SPALTEN,test_a06_TABELLEN,test_a06_BEDINGUNG,test_a06_SORTIERUNG,test_a06_GRUPPIERUNG)
[task][Ergebnistabelle](test_a06_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die die Namen und Einwohnerzahlen aller Gemeinde, die mehr als 100.000 männliche und mehr als 100.000 weibliche Einwohner:innen haben, ausgibt.


[task][Aufgabe 07](test_a07_checkEquality,test_a07_SPALTEN,test_a07_TABELLEN,test_a07_BEDINGUNG,test_a07_SORTIERUNG,test_a07_GRUPPIERUNG)
[task][Ergebnistabelle](test_a07_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die die Namen und Einwohnerzahlen aller Gemeinde, die mehr als 75.000 männliche oder mehr als 75.000 weibliche Einwohner:innen haben, ausgibt.


[task][Aufgabe 08](test_a08_checkEquality,test_a08_SPALTEN,test_a08_TABELLEN,test_a08_BEDINGUNG,test_a08_SORTIERUNG,test_a08_GRUPPIERUNG)
[task][Ergebnistabelle](test_a08_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die Name, Landkreis, Fläche und die Einwohnerzahlen aller Gemeinden ausgibt, die jeweils mehr als 50.000 männliche und weibliche Einwohner:innen oder eine Fläche größer als 100 km² hat.


[task][Aufgabe 09](test_a09_checkEquality,test_a09_SPALTEN,test_a09_TABELLEN,test_a09_BEDINGUNG,test_a09_SORTIERUNG,test_a09_GRUPPIERUNG)
[task][Ergebnistabelle](test_a09_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die die durchschnittlichen männlichen und weiblichen Einwohnerzahlen aller Gemeinde mit mehr als 100 km² Fläche pro Landkreis und den Namen des jeweiligen Landkreises ausgibt.


[task][Aufgabe 10](test_a10_checkEquality,test_a10_SPALTEN,test_a10_TABELLEN,test_a10_BEDINGUNG,test_a10_SORTIERUNG,test_a10_GRUPPIERUNG)
[task][Ergebnistabelle](test_a10_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die die Anzahl von Wanderwegen, die zu einer Gemeinde führen in einer Spalte `Anzahl` und den jeweiligen Gemeindeschlüssel absteigend nach Anzahl sortiert, ausgibt.

