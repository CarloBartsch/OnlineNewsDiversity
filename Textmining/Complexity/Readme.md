# Lesbarkeitsskript

An dieser Stelle folgt eine kurze Erläuterung des Skriptes zur Ermittlung des FRE-Index.
```
#Import
import textstat
import os, csv, re
import glob
import docx2txt
import textract
import pandas as pd
textstat.set_lang('de')
```
Importieren der einzelnen Module. Falls noch nicht geschehen, so müssen die zu importierenden Module, wie bereits beim Scaping-Skript, zuvor in der Kommandozeile, über ["pip install"](https://docs.python.org/3/installing/index.html), z.B. "pip install [textstat](https://pypi.org/project/textstat/)", installiert werden.
```
#Path and Folders(zdf_nachrichten anspassen!!!)
folder = ['bild','br','dlf','dw','faz','focus','zdf_nachrichten','mdr','ndr','ntv','pro7','rtl','spiegel','stern','swr','sz','tagesschau','taz','tonline','wdr','welt','zeit']
```
Festlegen der einzelnen Ordner, in denen die Artikel analysiert werden sollen. 
```
with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Textmining/Complexity/all_complexity_test.csv','w',encoding='utf8',errors='ignore', newline='') as word_file:
        word_writer = csv.writer(word_file,delimiter=',')
        word_writer.writerow(['Name','Article','Flesch Reading Ease'])
        for items in folder:
            print(items)
            entries = os.listdir('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/'+items+'/Clean')
```
Erstellen eines CSV-Files mit der Struktur: Name, Artikel, FRE.
```
            for line in entries:
                    path = 'C:/Users/admin/Documents/Dissertation/Diversity of News/Files/'+items+'/Clean/'+ line
                    print(path)
                    try:
                        text = str(textract.process(path),encoding='utf8',errors='ignore')
                        Flesch = str(textstat.flesch_reading_ease(text))
                        print('Flesch Reading Ease:' + str(Flesch))
                        word_writer.writerow([items,line,Flesch])
                    except Exception as error:
                        print(error)
```
Schleife, welche jeden Artikel Artikel analysiert und Name, Website und der FRE-Index im CSV speichert. Sollte ein Artikel nicht gelesen werden können, z.B. fehlerhafte Speicherung oder falsches Dateiformat, so wird dieser Artikel als "error" im CSV abgespeichert. Aus der Anzhal der Errors kann später die Fehlerquote berechnet werden. 
