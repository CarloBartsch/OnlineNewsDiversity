import re, csv, os
directory = r'C:\Users\admin\Documents\Dissertation\Diversity of News\Files\focus\Test'

for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".txt"):
        print(os.path.join(directory, filename))
        filename_dir = os.path.join(directory, filename)

        with open(filename_dir, 'r', encoding="utf8") as f:
            article = f.read()
            print(article)




            with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/focus/redundant_words.csv', newline='') as e:
                redundantWords = csv.reader(e)
                regex_after = re.compile('Login.+Heft-Abo & ePaper')
                article = regex_after.sub("",article)
                regex_after = re.compile('(?<=Vielen Dank).+\s+(\S+).+\s+(\S+).+\s+(\S+).+\s+(\S+).+\s+(\S+).+\s+(\S+)')
                article = regex_after.sub("",article)
                for row in redundantWords:


                    print(','.join(row))

                    regex = re.compile('|'.join(map(re.escape, row)))

                    article = regex.sub("", article)

            article = article.strip()
            article = " ".join(article.split())
            print(article)
            with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/focus/Clean/'+filename,'w', encoding="utf-8") as e:
                e.write(article)
    else:
        continue
