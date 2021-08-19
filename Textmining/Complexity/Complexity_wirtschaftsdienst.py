#Source: https://towardsdatascience.com/using-data-science-skills-now-text-readability-analysis-c4c4641f5875
#Source 2: count_words Script

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
#folder =['bild','br','dlf','dw','faz','focus','zdf_nachrichten','mdr','ndr','ntv','pro7','rtl','spiegel','stern','swr','sz','tagesschau','taz','tonline','wdr','welt','zeit']
folder =['Wirtschaftsdienst']
with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Textmining/Complexity/wd_complexity.csv','w',encoding='utf8',errors='ignore', newline='') as word_file:
        word_writer = csv.writer(word_file,delimiter=',')

        word_writer.writerow(['Name','Article','Flesch Reading Ease'])
        for items in folder:
            print(items)


            entries = os.listdir('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/'+items)








            for line in entries:

                    path = 'C:/Users/admin/Documents/Dissertation/Diversity of News/Files/'+items+'/'+ line
                    print(path)
                    try:
                        text = str(textract.process(path),encoding='utf8',errors='ignore')
                        Flesch = str(textstat.flesch_reading_ease(text))
                        print('Flesch Reading Ease:' + str(Flesch))

                        word_writer.writerow([items,line,Flesch])
                    except Exception as error:
                        print(error)

