# Erstellen eines Textcorpus
Bevor eine Inahaltanalyse bzw. eine Themenmodellierung durchgeführt werden kann, müssen die einzelnen Artikel zunächst in einem Textcorpus, also einer Textsammlung zusammengefasst werden[^1]. 
 
Wie läuft das in Python ab, wie sieht der Aufbau aus (List of List), Links hierzu


Skript Links hierzu

```
#DEFINITIONS

def remove_umlaut(string):
    """
    Removes umlauts from strings and replaces them with the letter+e convention
    :param string: string to remove umlauts from
    :return: unumlauted string
    """
    u = 'ü'.encode()
    U = 'Ü'.encode()
    a = 'ä'.encode()
    A = 'Ä'.encode()
    o = 'ö'.encode()
    O = 'Ö'.encode()
    ss = 'ß'.encode()

    string = string.encode()
    string = string.replace(u, b'ue')
    string = string.replace(U, b'Ue')
    string = string.replace(a, b'ae')
    string = string.replace(A, b'Ae')
    string = string.replace(o, b'oe')
    string = string.replace(O, b'Oe')
    string = string.replace(ss, b'ss')

    string = string.decode('utf-8')
    return string


def currency(text):
    """
    Removes the currency symbols from the text
    :param text: text as string
    :retrun: manipulated text as string
    """

    tempVar = text # local variable

    tempVar = tempVar.replace('$', '')
    tempVar = tempVar.replace('€', '')
    tempVar = tempVar.replace('¥', '')
    tempVar = tempVar.replace('₹', '')
    tempVar = tempVar.replace('£', '')

    return tempVar

def umlauts(text):
    """
    Replace umlauts for a given text

    :param word: text as string
    :return: manipulated text as str
    """

    tempVar = word # local variable

    # Using str.replace()

    tempVar = tempVar.replace('ä', 'ae')
    tempVar = tempVar.replace('ö', 'oe')
    tempVar = tempVar.replace('ü', 'ue')
    tempVar = tempVar.replace('Ä', 'Ae')
    tempVar = tempVar.replace('Ö', 'Oe')
    tempVar = tempVar.replace('Ü', 'Ue')
    tempVar = tempVar.replace('ß', 'ss')

    return tempVar



def lemmatizer(text):
    """
    Lemmetize words using spacy
    :param: text as string
    :return: lemmetized text as string
    """
    sent = []
    doc = model_de(text)
    for word in doc:
        sent.append(word.lemma_)
    return " ".join(sent)



import re, csv, os
#Repeat for all Files in Dircetory
directory = r'C:\Users\admin\Documents\Dissertation\Diversity of News\Files\\bild\Clean'
corpus =[]

for filename in os.listdir(directory):
    article_list =[]
    print(filename)
    if filename.endswith(".txt"):
        print(os.path.join(directory, filename))
        filename_dir = os.path.join(directory, filename)

        with open(filename_dir, 'r', encoding="utf8") as f:
            article = f.read()
            print(article)


            #Remove Umlaute

            new_text = remove_umlaut(article)
            new_text = ' '.join((new_text.strip('\n').split()))
            #print(new_text)

            #Remove Special Characters

            from string import punctuation
            remove_pun = str.maketrans('', '', punctuation)
            text_wo_pun = new_text.translate(remove_pun) # we are using native string functions as they are fast
            #print(text_wo_pun)

            #Remove Digits

            from string import digits
            remove_digits = str.maketrans('', '', digits)
            text_wo_num = text_wo_pun.translate(remove_digits)
            #print(text_wo_num)


            #Remove Currencies

            text_after_currency_removal = currency(text_wo_num)
            #print(text_after_currency_removal)


            #Remove StopWords

            import os, re, sys
            from nltk.corpus import stopwords
            german_stop_words = stopwords.words('german')
            german_stop_words[len(german_stop_words)-6]
            german_stop_words_to_use = []   # List to hold words after conversion
            for word in german_stop_words:
                german_stop_words_to_use.append(umlauts(word))

            text_wo_stop_words = [word for word in text_after_currency_removal.split() if word.lower() not in german_stop_words_to_use]
            text_wo_stop_words = ' '.join(text_wo_stop_words)
            #print(text_wo_stop_words)


            #Lemmetizer - Spacy
            #CMD python -m spacy download de_core_news_sm
            import spacy
            model_de = spacy.load("de_core_news_sm")
            text_after_lema_spacy = lemmatizer(text_wo_stop_words.lower())
            #print(text_after_lema_spacy)


            #Create List of Words
            #Split
            text_data = text_after_lema_spacy.split()
            #No Split
            text_data_no_split = str(text_after_lema_spacy)

            print(text_data_no_split)

            with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/bild/Corpus/Test_no_split.csv', 'a', newline='') as file:
                writer =csv.writer(file)
                writer.writerow(text_data_no_split)
            corpus.append(text_data_no_split)
            print(corpus)
```
























[^1]: Eine Einführung zum Thema Korpusaufbau und Erstellung findet sich z.B. in [Hirschmann (2019)](https://link.springer.com/book/10.1007%2F978-3-476-05493-7).
