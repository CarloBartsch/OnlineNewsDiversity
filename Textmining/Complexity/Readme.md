# Lesbarkeitsskript

An dieser Stelle folgt eine kurze Erläuterung des Skriptes zur Ermittlung des FRE-Index.
Falls noch nicht geschehen, so müssen die importierten Module, wie bereits beim Scaping-Skript, zuvor in der Kommandozeile, über ["pip install"](https://docs.python.org/3/installing/index.html), z.B. "pip install [textstat](https://pypi.org/project/textstat/)", installiert werden.

#pip istall textstat
#pip install readability

#Import
import textstat
import os, csv, re
import glob
import docx2txt
import textract
import pandas as pd
textstat.set_lang('de')

#Path and Folders(zdf_nachrichten anspassen!!!)
folder = ['bild','br','dlf','dw','faz','focus','zdf_nachrichten','mdr','ndr','ntv','pro7','rtl','spiegel','stern','swr','sz','tagesschau','taz','tonline','wdr','welt','zeit']

#folder =['bild','dlf','dw','focus','zdf_nachrichten','spiegel','t-online']
with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Textmining/Complexity/all_complexity_test.csv','w',encoding='utf8',errors='ignore', newline='') as word_file:
        word_writer = csv.writer(word_file,delimiter=',')

        word_writer.writerow(['Name','Article','Flesch Reading Ease'])
        for items in folder:
            print(items)


            entries = os.listdir('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/'+items+'/Clean')








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
