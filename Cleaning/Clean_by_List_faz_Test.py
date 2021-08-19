import re, csv, os
directory = r'C:\Users\admin\Documents\Dissertation\Diversity of News\Files\faz\Test'

for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".txt"):
        print(os.path.join(directory, filename))
        filename_dir = os.path.join(directory, filename)

        with open(filename_dir, 'r', encoding="utf8") as f:
            article = f.read()
            print(article)
            article = article.strip()
            article = " ".join(article.split())
            print(article)
            regex = re.compile('\d+\.\d+\.\d{4}')
            datetime = regex.findall(article)
            print(datetime)



            with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/faz/redundant_words.csv', newline='') as e:
                    redundantWords = csv.reader(e)
                    #regex_before_head = re.compile('.+"headline":')
                    #article_headline = regex_before_head.sub("",article)
                    #regex_after_head = re.compile('"publisher".+')
                    #rticle_headline = regex_after_head.sub("",article_headline)
                    #regex_before = re.compile('.+"description":')
                    #article_description = regex_before.sub("",article)
                    #regex_after = re.compile('"articleBody".+')
                    #article_description = regex_after.sub("",article_description)
                    regex_before_main = re.compile('.+"articleBody":')
                    article_main = regex_before_main.sub("",article)
                    regex_after_main = re.compile('"datePublished".+')
                    article_main = regex_after_main.sub("",article_main)
                    article = article_main
                    for row in redundantWords:


                        print(','.join(row))

                        regex = re.compile('|'.join(map(re.escape, row)))

                        article = regex.sub("", article)

            article = article.strip()
            article = " ".join(article.split())
            print(article)
            with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/faz/Clean/'+filename,'w', encoding="utf-8") as e:
                e.write(article)


    else:
        continue

