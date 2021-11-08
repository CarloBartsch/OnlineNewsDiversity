## Cleaning
Nachdem die Artikel gedownloadet wurden, müssen diese zunächst bereinigt bzw. auf den eigentlichen Text des Artikels reduziert werden, da andernfalls Werbeanzeigen, Nutzungsbedingungen, Impressum, usw. enthalten sind. Das genaue Vorgehen wird wieder beispielhaft anhand eines Skriptes dokumentiert.
```
import re, csv, os
```
Importieren der notwendigen Module
```
directory = 'C:/Users/Carlo Bartsch/Documents/Diversity of News/Files/focus'
```
Definieren des jeweiligen Verzeichnisses, welches die Artikel einer Website enthält.
```
```
for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".txt"):
        print(os.path.join(directory, filename))
        filename_dir = os.path.join(directory, filename)

        with open(filename_dir, 'r', encoding="utf8") as f:
            article = f.read()
            print(article)
```
Schleife die nacheinander jede Textdatei öffnet, sollte die Datei keine Textdatei (.txt) sein, dann wird fortgefahren (siehe "continue" am Textende).
```

            with open('C:/Users/Carlo Bartsch/Documents/Diversity of News/Helpfiles Skript/focus/redundant_words.csv', newline='') as e:
                redundantWords = csv.reader(e)
```
Öffnen eines CSV-Files (redundant_words), welche eine Liste überflüssiger Worte beinhaltet.
```
                regex_after = re.compile('Login.+Heft-Abo & ePaper')
                article = regex_after.sub("",article)
                regex_after = re.compile('(?<=Vielen Dank).+\s+(\S+).+\s+(\S+).+\s+(\S+).+\s+(\S+).+\s+(\S+).+\s+(\S+)')
                article = regex_after.sub("",article)
```
Definieren bestimmter Textabschnitte, welche den Anfang und das Ende des Artikels definieren. Alles andere wird gelöscht.
```
                for row in redundantWords:


                    print(','.join(row))

                    regex = re.compile('|'.join(map(re.escape, row)))

                    article = regex.sub("", article)
```
Sollten dann noch überflüssig Abschnitte bzw. Worte enthalten sein, dann werden mittels des CSV-Files die redundaten Wörter gelöscht.
```
            article = article.strip()
            article = " ".join(article.split())
            print(article)
```
Formatierung des Artikels, z.B. überflüssige Freizeichen werden gelöscht. 
```
            with open('C:/Users/Carlo Bartsch/Documents/Diversity of News/Files/focus/Clean/'+filename,'w', encoding="utf-8") as e:
                e.write(article)
```
Abspeichern des bereinigten Artikels in einem neuen Verzeichnis (Clean).
```
    else:
        continue

```
