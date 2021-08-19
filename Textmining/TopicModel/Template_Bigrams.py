#Source Bigrams https://towardsdatascience.com/text-analysis-basics-in-python-443282942ec5

from csv import reader
# read csv file as a list of lists
with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/bild/Corpus/Test_no_split.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    print(list_of_rows)
    res = str(list_of_rows)[1:-1]



#import pandas as pd
#df = pd.read_csv('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/bild/Corpus/Test_no_split.csv', error_bad_lines=False)



#List as Pandas Dataframe
corpus = list_of_rows
import pandas as pd
df = pd.DataFrame(corpus)
df.columns = ['reviews']

from sklearn.feature_extraction.text import CountVectorizer
c_vec = CountVectorizer(ngram_range=(2,3))
# matrix of ngrams
ngrams = c_vec.fit_transform(df['reviews'])
# count frequency of ngrams
count_values = ngrams.toarray().sum(axis=0)
# list of ngrams
vocab = c_vec.vocabulary_
df_ngram = pd.DataFrame(sorted([(count_values[i],k) for k,i in vocab.items()], reverse=True)
            ).rename(columns={0: 'frequency', 1:'bigram/trigram'})
print(df_ngram)
