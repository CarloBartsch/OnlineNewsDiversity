import re, csv, os
#Repeat for all Files in Dircetory
directory = r'C:\Users\admin\Documents\Dissertation\Diversity of News\Files\\bild\Preprocessed'

corpus =[]
with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/bild/Corpus/Test.csv', 'w', newline='') as file:
                writer =csv.writer(file)

for filename in os.listdir(directory):
    article =[]
    print(filename)
    if filename.endswith(".csv"):
        print(os.path.join(directory, filename))
        filename_dir = os.path.join(directory, filename)

        with open(filename_dir, 'r', newline='') as f:
            for line in csv.reader(f):
                print(line)
                article.extend(line)
            print(article)
            '''
            with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/bild/Corpus/Test.csv', 'a', newline='') as file:
                writer =csv.writer(file)
                writer.writerow(corpus)
            print(article)
            corpus.append(article)
            print(corpus)


    else:
        continue
            '''

