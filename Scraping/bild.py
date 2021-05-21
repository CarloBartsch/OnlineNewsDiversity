###IMPORT

import requests, re, csv, os
from bs4 import BeautifulSoup
from datetime import date
import locale
import threading
#import urllib2

from csv import writer
from datetime import datetime
from contextlib import contextmanager
import datetime


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
website = requests.get('https://www.bild.de/home/newsticker/news/alle-news-54190636.bild.html').text
html = BeautifulSoup(website,'lxml')
body = html.find('body')

try:
    data=[]
    with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/bild/bild_linklist.csv',encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                    data.append(row)

except:
    with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/bild/bild_linklist.csv','w', newline='',encoding='utf-8') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow(['Headline','Date','Link'])
    data=[]

print(data)
href_column = [x[2] for x in data]
for link in body.find_all('a'):
                href = link.get('href')
                header = link.get('data-tb-kicker')
                title = link.get('data-tb-title')
                whole_link = 'https://www.bild.de' + str(href)
                print(whole_link)
                print(header)
                print(title)
                if header is None:
                    continue
                else:
                    header = replaceMultiple(header,["'",'[',']','.',':','?','!','"','/',',','.'],"")
                    title = replaceMultiple(title,["'",'[',']','.',':','?','!','"','/',',','.'],"")
                    name = header + title
                    row_contents =[name,d2,href]
                    row_contents_error =['error',d2,'error']
                    if href in href_column:
                        print('old')

                    else:
                        print('new')
                            #zu Liste hinzufügen
                        try:
                            with open(r'C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/bild/bild_linklist.csv','a',newline='',encoding="utf-8") as f:
                                    writer = csv.writer(f)
                                    writer.writerow(row_contents)
                        except:
                            with open(r'C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/bild/bild_linklist.csv','a',newline='',encoding="utf-8") as f:
                                    writer = csv.writer(f)
                                    writer.writerow(row_contents_error)
                        try:
                            html = urllib.request.urlopen(whole_link).read()
                            print(text_from_html(html))
                            article = text_from_html(html)
                            with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/bild/%s.txt' % name,'w', encoding="utf-8") as e:
                                e.write(article)


                        except:
                            try:
                                with open(r'C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/bild/bild_error.csv','a',newline='',encoding="utf-8") as file_error:
                                    writer_error = csv.writer(file_error)
                                    writer_error.writerow(name,d2,href,'no')
                            except:
                                with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/bild/bild_error.csv','w', newline='',encoding='utf-8') as file_error:
                                    writer_error = csv.writer(file_error,delimiter=',')
                                    writer_error.writerow(['Headline','Date','Link','Download'])
                                    writer_error.writerow([name,d2,href,'no'])
                            continue

