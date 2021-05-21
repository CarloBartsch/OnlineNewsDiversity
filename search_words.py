import re, csv, os
directory = r'C:\Users\admin\Documents\Dissertation\Diversity of News\Files\ntv'
count = 1
for filename in os.listdir(directory):
    #print(filename)
    if filename.endswith(".txt"):
        #print(os.path.join(directory, filename))
        filename_dir = os.path.join(directory, filename)

        with open(filename_dir, 'r', encoding="utf8") as f:
            article = f.read()
            #print(article)




            #with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Helpfiles Skript/zdf_nachrichten/search_word_cleaning.csv', newline='') as e:
                #redundantWords = csv.reader(e)

                #for row in redundantWords:

        match = re.search('Quelle:', article)
        if match:
             count = count +1
             #print(count)
        else:
            print(filename)
            continue

print('Final:' + str(count))
           #print(','.join(row))

                    #regex = re.compile('|'.join(map(re.escape, row)))

                    #article = regex.sub("", article)
                    #article = article.strip()
                    #print(article)


            #with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/zdf_nachrichten/Clean/'+filename,'w', encoding="utf-8") as e:
                #e.write(article)
    #else:
        #continue
