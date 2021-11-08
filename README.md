# Online News Diversity
## Einleitung
Die verschiedenen Scraping-Files enthalten jeweils den Code zum scrapen einer Online-Nachrichten-Seite. Das Untersuchungsziel liegt hierbei auf einer Gegenüberstellung von Öffentlich-rechtlichem-Rundfunk (ÖRR) und privaten Medienanstalten, jedoch lassen sich die Daten auch für andere Zwecke, z.B. Berechnung eines Media Bias benutzen. Für jedes Medium liegen demnach mehrere tausend Nachrichtenartikel und zusätzliche Metadaten vor. Die genaue vorgehensweise zur Datenerhebung und -aufbereitung wird später im Unterpunkt Scraping-Skript beschrieben. Zusammengenommen ergibt sich eine Datensammlung von 18 Medien über einen Zeitraum von mehreren Monaten. (hier genauer) 

Mit Hilfe der einzelnen Artikel lassen sich mittels Textmining vrschiedene Analysen durchführen und Kennzahlen berechnen. Hierzu zählen Sentiment-Analyse, Topic-Modelling, Komplexitätsanalyse sowie Kennzhalen über Textlänge, Artikelanzahl, Rubriken, Veröffentlichungsdatum. 
Dien einzelnen Schritte vom Download der Daten bis zur Erstellung des fertigen Datensatzes sehen dabei wie folgt aus:
1.Download --> 2. Aufbereitung --> 3. Erstellung eines Corpus --> 4. Textmining

Ein genauerer Überblick findet sich hier: https://github.com/CarloBartsch/OnlineNewsDiversity/blob/main/Vortrag%20zum%20Expose.pdf

## Scraping
Anhand des Scraping-Skriptes der Spiegel-Website, werden exemplarisch die einzelnen Punkte des Skriptes erklärt. Sämtliche Skripte basieren auf der gleichen Vorlage und weichen nur aufgrund des unterschiedlichen Aufbaus der einzelenn Websites ab. Die Skripte sind in Python geschrieben. Eine genauere Anleitung zu Download, Installtion und Einrichtung von Python ist unter folgenden Links zu finden: 

https://www.python.org/downloads/

https://wiki.python.org/moin/BeginnersGuide/Download

https://docs.python.org/3/using/windows.html

https://realpython.com/installing-python/

https://www.youtube.com/watch?v=YYXdXT2l-Gg
Hinweis: Sämtliche "print()" Befehle dienen lediglich der Überprüfung und Suche von Bugs, sind jedoch für die eigentliche Scraping-Funktionalität des Skriptes redundant, weshalb im Folgenden nicht genauer auf die print-Befehle eingegangen wird. Kommentar sind durch ein # zu erkennen und dienen lediglich der Beschreibung einzelner Funktionen und Abschnitte des Skriptes.
````
import requests, re, csv, os
from bs4 import BeautifulSoup
from datetime import date
import locale
import threading

from datetime import datetime
from contextlib import contextmanager
import datetime

from csv import writer
from bs4.element import Comment
import urllib.request
import lovely_logger as log
````
Importieren der einzelnen Module. Sollten die Module nicht in Python enthalten sein, so müssen dies zuvor installiert werden. Hierzu in der Windowsconsole "pip install modul-name" eingeben. z.B. "pip install BeautifulSoup". Mehr hierzu unter:
https://packaging.python.org/tutorials/installing-packages/

```
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

@contextmanager
def setlocale(name):
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)

def replaceMultiple(mainString, toBeReplaces, newString):
                    # Iterate over the strings to be replaced
                        for elem in toBeReplaces :
                    # Check if string is in the main string
                            if elem in mainString :
                    # Replace the string
                                mainString = mainString.replace(elem, newString)

                        return  mainString

```
Definition einiger benutzerdifinierter Funktionen, die im späteren Verlauf benutzt werden. Zur genauen Beschreibung der einzelnen Funktionen siehe hier:
https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/
https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
```
# Let's set a non-US locale
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

today = date.today()

print("Today's date:", today)

d2 = today.strftime("%e. %B %Y")
#print("d2 =", d2)
print(str(d2))
d3 = today.strftime("%Y%m%d")
print(d3)
d4 = now.strftime("%Y%m%d%H%M%S")
print(d4)
```
Ermittlung des jeweiligen Downloaddatums und der Datumsfromatierung, z.B. d2 = 20211104 (Jahr, Monat, Tag) und d4 = 20211104104029 (Jahr, Monat, Tag, Stunden, Minuten, Sekunden). Beide Datumswerte werden später zur Berechnung einer laufenden Nummer und als Metadaten benutzt.
```
#Logging


log.init('C:/Users/Carlo Bartsch/Documents/Diversity of News/Helpfiles Skript/bild/Logs/'+d4+'.log')

log.debug('here are the in-scope variables right now: %s', dir())
log.info('%s v1.2 HAS STARTED', __file__)
log.warning('here is a warning message')
log.error('generally you would use error for handled exceptions which prevent further execution')
log.critical('generally you would use critical for uncaught exceptions')
```
Erstellen und speichern eines Log-Files zur Fehlerbehebung





```
website = requests.get('https://www.spiegel.de/').text
html = BeautifulSoup(website,'lxml')
body = html.find('body')
```
Abfrage der Website im HTML-Format. "Body" repräsentiert dabei den Inhalt einer Website aber nicht deren Layout, welche im "header" beschrieben werden. Sowohl "body" als auch "header" sind einzigartig und können daher gezielt abgefragt werden. Mehr hierzu unter: 
https://developer.mozilla.org/de/docs/Learn/Getting_started_with_the_web/HTML_basics
```
try:
    data=[]
    with open(r'C:\Users\Carlo Bartsch\Documents\Diversity of News\Helpfiles Skript\spiegel\h_sp_linklist.csv',newline='') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    data.append(row)

except Exception as e :
    print(e)
    with open(r'C:\Users\Carlo Bartsch\Documents\Diversity of News\Helpfiles Skript\spiegel\h_sp_linklist.csv','w',newline='') as f:
                writer = csv.writer(f ,delimiter=',')
                writer.writerow(['ID','Headline','Date','Link'])
    data=[]
```
Zunächst versucht das Skript auf ein bestehendes CSV-Files zuzugreifen, sollte bereits ein CSV bestehen, dann werden anschließend sämtliche Links zu den einzelnen Nachrichtenartikeln in diesem File gespeichert. Wenn es sich um den ersten Durchlauf des Skriptes handelt und dementsprechend noch kein CV existiert, dann wird ein neues CSV erstellt und anschließend zur Speicherung der Downloadlinkslinks benutzt. Neben dem Link enthält das CSV-File eine laufende Nummer zu jedem Artikel (ID), die Schlagzeile (Headline) und das Datum (Date). 

```                    
running_number = 1
```
Start der laufenden Nummer zur Nummerierung der einzelnen Artikel
```
print(data)
href_column = [x[2] for x in data]

for link in body.find_all('a'):

                plus = link.text
                plus = plus.strip()
                plus = os.linesep.join([s for s in plus.splitlines() if s])
                plus = plus.partition('\n')[0]
                print(plus)
                sub = 'Icon:'
                if sub in plus:
                    plus = plus
                else:
                    plus =''


                for span in link.find_all("span",{"class":"align-middle mr-6"}):


                        href = link.get('href')
                        name = str(span.text)
                        name = name.strip()
                        name = os.linesep.join([s for s in name.splitlines() if s])
                        name = replaceMultiple(name,["'",'[',']','.',':','?','!','"','/',',','.','-','“','„','«','»'],"")
                        #name = name.replace('ß','ss')
                        #name = name.replace('–','')
                        print(href)
                        print(name)
```
Loop zur Abfrage der einzelnen Downloaddinks (href) und der Schlagzeilen (name), sowie entfernen von Sonderzeichen, Satzzeichen usw..
```
                        identifier = str(d4)+str(running_number)
```
Erstellen einer eindeutigen Nummer (ID) aus Datum, Uhrzeit (d3) und der laufenden Nummer. 
```
                        row_contents =[identifier,name,d2,href]
                        row_contents_error =[identifier,name,'error',href]
```
"row_contents" ergeben später die einzelnen Zeilen pro Artikel des CSV-Files.
```
                        if href in href_column:
                            print('old')

                        else:
                            print('new')
                            #zu Liste hinzufügen
```
Falls ein Link bereits im CSV enthalten ist (neuer Link = alter Link), dann wird der Artikel übersprungen, andernfalls wird der Artikel gedownloadet.
```
                            try:
                                with open(r'C:/Users/Carlo Bartsch/Documents/Diversity of News/Helpfiles Skript/spiegel/h_sp_linklist.csv','a',newline='',encoding="utf-8") as f:
                                    writer = csv.writer(f)
                                    writer.writerow(row_contents)
                                    print('worked')
                            except Exception as e:
                                with open(r'C:/Users/Carlo Bartsch/Documents/Diversity of News/Helpfiles Skript/spiegel/h_sp_linklist.csv','a',newline='',encoding="utf-8") as f:
                                    writer = csv.writer(f)
                                    writer.writerow(row_contents_error)
                                    print('error')

                            try:
                                html = urllib.request.urlopen(href).read()
                                print(text_from_html(html))
                                article = text_from_html(html)
                                with open('C:/Users/Carlo Bartsch/Documents/Diversity of News/Files/spiegel/Homepage/'+identifier+'.txt','w', encoding="utf-8") as e:
                                    e.write(article)
                                    running_number = running_number +1

                            except:
                                try:
                                    with open(r'C:/Users/Carlo Bartsch/Documents/Diversity of News/Helpfiles Skript/spiegel/sp_error.csv','a',newline='',encoding="utf-8") as file_error:
                                        writer_error = csv.writer(file_error)
                                        writer_error.writerow(name,d2,href,'no')
                                except:
                                    with open('C:/Users/Carlo Bartsch/Documents/Diversity of News/Helpfiles Skript/spiegel/sp_error.csv','w', newline='',encoding="utf-8") as file_error:
                                        writer_error = csv.writer(file_error,delimiter=',')
                                        writer_error.writerow(['Headline','Date','Link','Download'])
                                        writer_error.writerow([name,d2,href,'no'])
                                continue
```
