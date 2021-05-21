#ReadIn Corpus
#Import for ReadIn
from csv import reader
# read csv file as a list of lists
with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/Spiegel/Corpus/Test.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    corpus = list(csv_reader)
    #print(list_of_rows)
    corpus_str = str(corpus)[1:-1]

#print(corpus_str)
#print(corpus)


#Import for HDP
import pandas as pd
from pandas import option_context
import numpy as np
import string
import re
import sys

from sklearn.datasets import  fetch_20newsgroups

import matplotlib.pyplot as plt

import tomotopy as tp

'''
min_cf=5 words that appeared in at least 5 documents; rm_top=7 excluding the 7 most frequent words;
gamma=1  alpha=0.1  I assume documents share many topics while individual documents only talk about few topics
initial_k=10 initial number of topics;

'''
term_weight = tp.TermWeight.ONE
hdp = tp.HDPModel(tw=term_weight, min_cf=5, rm_top=7, gamma=1,
                  alpha=0.1, initial_k=20, seed=99999)

# Add docs to train
for vec in corpus:
    hdp.add_doc(vec)

# Initiate sampling burn-in  (i.e. discard N first iterations)
hdp.burn_in = 100
hdp.train(0)
print('Num docs:', len(hdp.docs), ', Vocab size:', hdp.num_vocabs,
      ', Num words:', hdp.num_words)
print('Removed top words:', hdp.removed_top_words)

# Train model
for i in range(0, 10000, 500):
    hdp.train(100) # 100 iterations at a time
    print('Iteration: {}\tLog-likelihood: {}\tNum. of topics: {}'.format(i, hdp.ll_per_word, hdp.live_k))


#Definition
def get_hdp_topics(hdp, top_n=10):
    '''Wrapper function to extract topics from trained tomotopy HDP model

    ** Inputs **
    hdp:obj -> HDPModel trained model
    top_n: int -> top n words in topic based on frequencies

    ** Returns **
    topics: dict -> per topic, an arrays with top words and associated frequencies
    '''

    # Get most important topics by # of times they were assigned (i.e. counts)
    sorted_topics = [k for k, v in sorted(enumerate(hdp.get_count_by_topics()), key=lambda x:x[1], reverse=True)]

    topics=dict()

    # For topics found, extract only those that are still assigned
    for k in sorted_topics:
        if not hdp.is_live_topic(k): continue # remove un-assigned topics at the end (i.e. not alive)
        topic_wp =[]
        for word, prob in hdp.get_topic_words(k, top_n=top_n):
            topic_wp.append((word, prob))

        topics[k] = topic_wp # store topic word/frequency array

    return topics

topics = get_hdp_topics(hdp, top_n=10) # changing top_n changes no. of words displayed
#print(topics[1])

test_doc =corpus[2]
doc_inst =hdp.make_doc(test_doc)
topic_dist, ll = hdp.infer(doc_inst)

topic_idx = np.array(topic_dist).argmax()
print(topic_idx)

which_words =hdp.get_topic_words(topic_idx)
print(which_words)
