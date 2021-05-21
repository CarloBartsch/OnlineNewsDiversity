import re, csv, os
directory = r'C:\Users\admin\Documents\Dissertation\Diversity of News\Files\\sz\Test'

for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".txt"):
        print(os.path.join(directory, filename))
        filename_dir = os.path.join(directory, filename)

        with open(filename_dir, 'r', encoding="utf8") as f:
            article = f.read()
            #print(article)
            regex = re.compile('\d+\.\s[A-z]+\s\d{4},\s\d+:\d{2}\sUhr')
            datetime = regex.findall(article)
            #print(datetime)
            date = datetime[0]
            print(date)


            with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/sz/redundant_words.csv', newline='', encoding='latin') as e:
                redundantWords = csv.reader(e)
                regex_before = re.compile('.+'+date)
                article = regex_before.sub("",article)
                regex_after = re.compile('© .+')
                article = regex_after.sub("",article)
                for row in redundantWords:


                    print(','.join(row))

                    regex = re.compile('|'.join(map(re.escape, row)))

                    article = regex.sub("", article)


            article = article.strip()
            article = " ".join(article.split())
            print(article)
            with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/sz/Clean/'+filename,'w', encoding="utf-8") as e:
                e.write(article)
    else:
        continue

