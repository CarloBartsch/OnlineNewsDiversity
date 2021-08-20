#Selenium
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#from selenium.webdriver.common.keys import Keys
PATH = "C:\DRIVERS\chromedriver.exe"
driver = webdriver.Chrome(PATH)

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
print(str(d2))
d3 = today.strftime("%Y%m%d")
print(d3)

driver.get('https://secure.mypass.de/sso/web/login?service=https%3A%2F%2Fwww.welt.de%2F')
driver.find_element_by_xpath('/html/body/div/div/form/div[1]/div/div[1]/div/input').send_keys('carlo.bartsch@hsu-hh.de')

driver.find_element_by_xpath('/html/body/div/div/form/div[1]/div/div[2]/div/input').send_keys('hsu_2021!')

driver.find_element_by_xpath('/html/body/div/div/form/button/span[1]').click()


WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[id^='sp_message_iframe']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[3]/div[2]/button"))).click()
time.sleep(5)
driver.switch_to.default_content()
driver.switch_to.active_element
pages = ['','politik/','wirtschaft/']
for element in pages:

    try:
        data=[]
        with open('C:/Users/Carlo Bartsch/Documents/Diversity of News/Helpfiles Skript/welt/welt_linklist_login.csv',encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                        data.append(row)

    except:
        with open('C:/Users/Carlo Bartsch/Documents/Diversity of News/Helpfiles Skript/welt/welt_linklist_login.csv','w', newline='',encoding='utf-8') as f:
                    writer = csv.writer(f,delimiter=',')
                    writer.writerow(['ID','Headline','Date','Link'])
        data=[]

    driver.get('https://www.welt.de/'+element)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    body = soup.find('body')
    running_number = 1
    print(data)
    href_column = [x[2] for x in data]
    for link in body.find_all('a'):
                    href = link.get('href')                    
                    listToCheck = ['reise','sport','/gesundheit/','/kultur/','/videos/','/icon/','/gutscheine','/podcasts/','/weinshop','/services/','/aaps/','/spiele/','/mediathek/','/sponsored/','/Advertorials/']
                    whole_link = 'https://www.welt.de/' + str(href)
                    print(whole_link)
                    name = link.text
                    name = replaceMultiple(name,["'",'[',']','.',':','?','!','"','/',',','.','-','“','„','«','»'],"")
                    print(name)
                    identifier = str(d3)+str(running_number)
                    row_contents =[identifier,name,d2,href]
                    row_contents_error =[identifier,name,'error',href]
                    if href in href_column:
                        print('old')

                    else:
                        print('new')
                            #zu Liste hinzufügen
                        try:

                            with open(r'C:/Users/Carlo Bartsch/Documents/Diversity of News/Helpfiles Skript/welt/welt_linklist_login.csv','a',newline='',encoding="utf-8") as f:
                                        writer = csv.writer(f)
                                        writer.writerow(row_contents)
                        except:
                            with open(r'C:/Users/Carlo Bartsch/Documents/Diversity of News/Helpfiles Skript/welt/welt_linklist_login.csv','a',newline='',encoding="utf-8") as f:
                                        writer = csv.writer(f)
                                        writer.writerow(row_contents_error)
                        if any(ext in href for ext in listToCheck):
                        #if video or podcast or icon or gutscheine in href:
                            pass
                        else:
                            try:
                                driver.get(whole_link)
                                html_id = driver.page_source
                                print(text_from_html(html_id))
                                article = text_from_html(html_id)
                                with open('C:/Users/Carlo Bartsch/Documents/Diversity of News/Files/welt/Login/'+identifier+'.txt','w', encoding="utf-8") as e:
                                    e.write(article)
                                    running_number = running_number +1

                            except Exception as e:
                                print(e)
                                try:
                                    with open(r'C:/Users/Carlo Bartsch/Documents/Diversity of News/Helpfiles Skript/welt/welt_error_login.csv','a',newline='',encoding="utf-8") as file_error:
                                        writer_error = csv.writer(file_error)
                                        writer_error.writerow(name,d2,href,'no')
                                except:
                                    with open('C:/Users/Carlo Bartsch/Documents/Diversity of News/Helpfiles Skript/welt/welt_error_login.csv','w', newline='',encoding='utf-8') as file_error:
                                        writer_error = csv.writer(file_error,delimiter=',')
                                        writer_error.writerow(['Headline','Date','Link','Download'])
                                        writer_error.writerow([name,d2,href,'no'])
                                continue
driver.close()

