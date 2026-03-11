Alle Abfragen beziehen sich auf folgende Datenbank (auch [hier](https://www.dbiu.de/bayern/) zu finden; Achtung: Datensätze können leicht abweichen):

![Klassendiagramm_dbiu-bayern.drawio.svg](/api/core/files/markdown/Markdown_2024-11-10T13-52-29-793_05deab6a.svg)

Die Aufgaben sind jeweils korrekt gelöst, wenn `Aufgabe X` grün ist (1 von 1 bestanden). Die Zeile darunter (`Ergebnistabelle`) wird immer rot bleiben (0 von 1 bestanden). Hier werden die ersten drei Ergebniszeilen und wie viele weitere es gibt, angezeigt. Eine korrekt gelöste Aufgabe sieht z.B. so aus:

![image.png](/api/core/files/markdown/Markdown_2024-11-10T14-10-48-551_e92054a6.png)

### Musterlösung: 

[https://0187.drive.bycs.de/s/hHQEGULfDPqMRxi](https://0187.drive.bycs.de/s/hHQEGULfDPqMRxi)

### Aufgaben: 
Gib immer genau die geforderten Daten aus und nicht mehr. Sortiere nicht, wenn du nicht dazu aufgefordert wirst.

[task][Aufgabe 01](test_a01_checkEquality)
[task][Ergebnistabelle](test_a01_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Verändere die SQL-Abfrage so, dass die Namen und Internetadressen (=url) aller Zoos und der Name und Regierungsbezirk der jeweiligen Gemeinde ausgegeben wird.


[task][Aufgabe 02](test_a02_checkEquality)
[task][Ergebnistabelle](test_a02_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Verändere die SQL-Abfrage so, dass die der Namen und Straßen aller Freizeitparks und die Namen der jeweils zugehörigen Gemeinde ausgegeben wird. 

[task][Aufgabe 03](test_a03_checkEquality)
[task][Ergebnistabelle](test_a03_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die Namen und Art aller Schwimmbäder und den Namen und alle Einwohnerzahlen der zugehörigen Gemeinden ausgibt.

[task][Aufgabe 04](test_a04_checkEquality)
[task][Ergebnistabelle](test_a04_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die die Anzahl an Schwimmbädern in Gemeinden mit <ins>mehr</ins> als 1000 weiblichen Einwohnerinnen ausgibt.

*Tipp: Hier brauchst du mehrere verknüpfte Bedingungen*

[task][Aufgabe 05](test_a05_checkEquality)
[task][Ergebnistabelle](test_a05_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die die Namen aller Gemeinde in Oberbayern oder Niederbayern, zu denen ein Wanderweg führt, ausgibt. Dopplungen dürfen auftreten und sollte nicht entfernt werden!

*Tipp: Hier brauchst du wieder mehrere verknüpfte Bedingungen. Überlege bei der Verknüpfung von Bedingungen, ob du Klammern setzen musst!*

### Zusatzübung für Zuhause
[task][Aufgabe 06](test_a06_checkEquality)
[task][Ergebnistabelle](test_a06_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die aus den Tabellen Gemeinde und Wanderweg_zu_Gemeinde die Anzahl der Wanderwege, die zu Gemeinden mit mehr als 500 000 männlichen Einwohnern führen, ausgibt.

[task][Aufgabe 07](test_a07_checkEquality)
[task][Ergebnistabelle](test_a07_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die eine Liste mit den Namen aller Gemeinden, die ein `"Freibad"` haben, und die Namen der jeweiligen Freibäder ausgibt. 

[task][Aufgabe 08](test_a08_checkEquality)
[task][Ergebnistabelle](test_a08_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die die Anzahl an Radwegen, die an Gemeinden im PLZ-Bereich **größer** als 96400 angrenzen, ausgibt.


[task][Aufgabe 09](test_a09_checkEquality)
[task][Ergebnistabelle](test_a09_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die die Namen aller Zoos in einer Gemeinde namens `"Erlangen"` ausgibt.

[task][Aufgabe 10](test_a10_checkEquality)
[task][Ergebnistabelle](test_a10_KEIN_FEHLER__SQL_Ergebnis_anzeigen)
Schreibe eine SQL-Abfrage, die die IDs aller Radwege, die zu Gemeinden in Oberfranken oder Unterfranken führen, ausgibt. Dopplungen sollen nicht entfernt werden.