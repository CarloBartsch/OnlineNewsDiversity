import re, csv, os
directory = r'C:\Users\admin\Documents\Dissertation\Diversity of News\Files\rtl'

for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".txt"):
        print(os.path.join(directory, filename))
        filename_dir = os.path.join(directory, filename)

        with open(filename_dir, 'r', encoding="utf8") as f:
            article = f.read()
            #print(article)
            article = article.strip()
            article = " ".join(article.split())
            #print(article)
            #regex = re.compile('\d+\.\d+\.\d{4}.\d{2}:\d{2}.Uhr')
            #datetime = regex.findall(article)
            #print(datetime)
            #if datetime:

                #date = datetime[0]
                #print(datetime)
            size = len(article)
            # Slice string to remove last 3 characters from string
            article = article[:size - 310]


            with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/rtl/redundant_words.csv', newline='') as e:
                    redundantWords = csv.reader(e)
                    regex_before = re.compile('.+RTL.de >')
                    article = regex_before.sub("",article)
                    regex_after = re.compile('RTL.de.+')
                    article = regex_after.sub("",article)
                    regex_after = re.compile('(dpa).+')
                    article = regex_after.sub("",article)
                    #regex_after = re.compile('Mehr Nachrichten aus der Region.+')
                    #article = regex_after.sub("",article)
                    for row in redundantWords:


                        print(','.join(row))

                        regex = re.compile('|'.join(map(re.escape, row)))

                        article = regex.sub("", article)

            article = article.strip()
            article = " ".join(article.split())
            #print(article)
            with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/rtl/Clean/'+filename,'w', encoding="utf-8") as e:
                e.write(article)

            #else:
                #continue
    else:
        continue

