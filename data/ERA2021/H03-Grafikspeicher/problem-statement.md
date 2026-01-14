
[task][Erfolgreiches Kompilieren](Compile)
*Die Aufgabe muss kompilieren um korrigiert und bewertet zu werden!*


##<span class="red">Achtung:</span>

Um das mitgelieferte Template verwenden zu können müssen Sie an zusätzlichen mit <span class="red">TODO</span> gekennzeichneten Stellen den Code verändern. Was genau dort zu tun ist wird hier und im Template beschrieben.

Verändern Sie im Template nur die mit <span class="red">TODO</span> gekennzeichneten Bereiche.

Wie das Template verwendet werden kann wird in den Kommentaren im Code beschrieben (Achtung: Die Verwendung unter SASM kann sich zu der normalen mit NASM unterscheiden).


## Hausaufgabe 3: Zugriff auf Grafikspeicher

Grafikkarten mit 8 Bit pro Farbintensität (Rot/Grün/Blau, d. h. true color) benötigen mindestens 24 Bit pro Pixel.
Diese werden inzwischen fast immer, wie in dieser Aufgabe auch, auf 32 Bit aufgerundet.

### Teilaufgabe a)
Mit welcher Formel kann man allgemein die Speicheradresse eines bestimmten RGB-
Bildpunkts (x, y) aus den Werten Bildschirmspeicherstart, Breite und Höhe berechnen? Die (Zeilen-)Pixel sollen hierbei konsekutiv im Arbeitsspeicher entlang der x Koordinate
liegen.
Setzen Sie diese beim ersten TODO im Code für X ein. 
Zusätzlich müssen Sie im dritten TODO nun Assembler-Code einfügen um aus den gegebenen Werten x (in EAX), y (in EBX), beginnend mit 0 und der Auflösung aus b) (1920 × 1080) die Speicherposition (Ergebnis nach ESI) zu berechen.
Schreiben Sie dann den Wert des Pixels nach ecx (mov ecx, [esi]). ecx muss natürlich nicht gesichert werden.
Achten Sie darauf Register, welche Sie verändern, davor zu sichern.

### Teilaufgabe b)
Der Start des Bildschirmspeichers mit der Auflösung 1920 × 1080 stehe an der Speicherstelle display\_start. Die Pixelkoordinaten x und y werden in den Registern eax und
ebx übergeben, der zu setzende RGB-Wert im Register ecx. Schreiben Sie das Unterprogramm set\_pixel, das das Pixel auf den Farbwert setzt. Außer dem Register eax dürfen
keine anderen Registerinhalte verändert werden. Der Wertebereich von x und y soll nicht
überprüft werden.

Versuchen Sie so wenig wie möglich Multiplikationen zu verwenden, indem Sie von der
indirekten Adressierung Gebrauch machen.