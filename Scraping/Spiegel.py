###IMPORT

import requests, re, csv, os
from bs4 import BeautifulSoup
from datetime import date
import locale
import threading
#import urllib2


from datetime import datetime
from contextlib import contextmanager
import datetime

from csv import writer
from bs4.element import Comment
import urllib.request
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



### DATE

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

# Let's set a non-US locale
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

today = date.today()

print("Today's date:", today)

d2 = today.strftime("%e. %B %Y")
#print("d2 =", d2)
print(str(d2))


#HTML
website = requests.get('https://www.spiegel.de/schlagzeilen/').text
html = BeautifulSoup(website,'lxml')
body = html.find('body')


try:
    data=[]
    with open(r'C:\Users\admin\Documents\Dissertation\Diversity of News\Helpfiles Skript\spiegel.de\sp_linklist.csv',newline='',encoding="utf-8") as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    data.append(row)

except Exception as e :
    print(e)
    with open(r'C:\Users\admin\Documents\Dissertation\Diversity of News\Helpfiles Skript\spiegel.de\sp_linklist.csv','w',newline='',encoding="utf-8") as f:
                writer = csv.writer(f ,delimiter=',')
                writer.writerow(['Headline','Date','Link'])
    data=[]
    #with open(r'C:\Users\admin\Documents\Dissertation\Diversity of News\Helpfiles Skript\spiegel.de\sp_linklist.csv',newline='',encoding="latin-1") as f:
                #reader = csv.reader(f, delimiter=',')
                #for row in reader:
                    #data.append(row)
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
                        name = replaceMultiple(name,["'",'[',']','.',':','?','!','"','/',',','.'],"")
                        print(href)
                        print(name)

                        row_contents =[name,d2,href]
                        row_contents_error =['error',d2,'error']
                        if href in href_column:
                            print('old')

                        else:
                            print('new')
                            #zu Liste hinzufügen
                            try:
                                with open(r'C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/spiegel.de/sp_linklist.csv','a',newline='',encoding="utf-8") as f:
                                    writer = csv.writer(f)
                                    writer.writerow(row_contents)
                                    print('worked')
                            except:
                                with open(r'C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/spiegel.de/sp_linklist.csv','a',newline='',encoding="utf-8") as f:
                                    writer = csv.writer(f)
                                    writer.writerow(row_contents_error)
                                    print('error')
                            try:
                                html = urllib.request.urlopen(href).read()
                                print(text_from_html(html))
                                article = text_from_html(html)
                                with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/Spiegel/%s.txt' % str(name),'w', encoding="utf-8") as e:
                                    e.write(article)


                            except:
                                try:
                                    with open(r'C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/spiegel.de/sp_error.csv','a',newline='',encoding="utf-8") as file_error:
                                        writer_error = csv.writer(file_error)
                                        writer_error.writerow(name,d2,href,'no')
                                except:
                                    with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/spiegel.de/sp_error.csv','w', newline='',encoding='utf-8') as file_error:
                                        writer_error = csv.writer(file_error,delimiter=',')
                                        writer_error.writerow(['Headline','Date','Link','Download'])
                                        writer_error.writerow([name,d2,href,'no'])
                                continue



try:
    data_author=[]
    with open(r'C:\Users\admin\Documents\Dissertation\Diversity of News\Helpfiles Skript\spiegel.de\sp_linklist_author.csv',newline='',encoding="latin-1") as file_author:
                reader_author = csv.reader(file_author, delimiter=',')
                for row_author in reader_author:
                    data_author.append(row_author)

except:
    with open(r'C:\Users\admin\Documents\Dissertation\Diversity of News\Helpfiles Skript\spiegel.de\sp_linklist_author.csv','w',newline='',encoding="utf-8") as file_author:
                writer_author = csv.writer(file_author,delimiter=',')
                writer_author.writerow(['Headline','Date','Author'])
    data_author=[]

headline = [x[0] for x in data_author]

for link in body.find_all('a'):


        plus = link.text

        plus = plus.strip()
        plus = os.linesep.join([s for s in plus.splitlines() if s])
        name = plus.partition('\n')[0]
        plus = plus.partition('\n')[2]

        row_contents_author =[name,d2,plus]
        row_contents_author_error =['error',d2,'error']
        if name in headline:
            print('old')
        else:
            print('new')
            #zu Liste hinzufügen
            try:
                with open(r'C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/spiegel.de/sp_linklist_author.csv','a',newline='',encoding="utf-8") as f:
                                    writer = csv.writer(f)
                                    writer.writerow(row_contents_author)
            except UnicodeError:
                with open(r'C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/spiegel.de/sp_linklist_author.csv','a',newline='',encoding="utf-8") as f:
                                    writer = csv.writer(f)
                                    writer.writerow(row_contents_author_error)


try:
    data_plus=[]
    with open(r'C:\Users\admin\Documents\Dissertation\Diversity of News\Helpfiles Skript\spiegel.de\sp_linklist_plus.csv',newline='',encoding="utf-8") as file_plus:
            reader_plus = csv.reader(file_plus, delimiter=',')
            for row_plus in reader_plus:
                data_plus.append(row_plus)
except:
    with open(r'C:\Users\admin\Documents\Dissertation\Diversity of News\Helpfiles Skript\spiegel.de\sp_linklist_plus.csv','w',newline='',encoding="utf-8") as file_plus:
            writer_plus = csv.writer(file_plus,delimiter=',')
            writer_plus.writerow(['Name','Date','Content'])
    data_plus=[]

headline = [x[0] for x in data_plus]
for link in body.find_all('a'):
        plus = link.text
        plus = plus.strip()
        plus = os.linesep.join([s for s in plus.splitlines() if s])
        name = plus.partition('\n')[0]

        for span in link.find_all(id="M/SPlus-Flag"):

            regex = re.compile(r'SPlus')
            span = regex.findall(str(span))
            print(span)
            row_contents_plus =[name,d2,span]
            row_contents_plus_error =['error',d2,'error']
            if name in headline:
                print('old')
            else:
                print('new')
                try:
                    #zu Liste hinzufügen
                    with open(r'C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/spiegel.de/sp_linklist_plus.csv','a',newline='',encoding="utf-8") as f:
                                    writer = csv.writer(f)
                                    writer.writerow(row_contents_plus)
                except UnicodeError:
                    with open(r'C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/spiegel.de/sp_linklist_plus.csv','a',newline='',encoding="utf-8") as f:
                                    writer = csv.writer(f)
                                    writer.writerow(row_contents_plus_error)

