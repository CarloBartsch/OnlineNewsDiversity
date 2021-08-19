


list_1 = ['schnefall','glaette','rutschen','fahrer','kommen']
list_2 = ['sagen','geben','unfaellen','betreffen','gesamt']
list_3 = ['ereignen','schleudern','ebenfalls','geraten','meist']

list_of_lists =[]
list_of_lists.append(list_1)
list_of_lists.append(list_2)
list_of_lists.append(list_3)
print(list_of_lists)

text_data = list_of_lists


from gensim import corpora

dictionary = corpora.Dictionary(text_data)
corpus = [dictionary.doc2bow(text) for text in text_data]

import pickle
pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')

import gensim
NUM_TOPICS = 5
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
ldamodel.save('model5.gensim')
topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)


