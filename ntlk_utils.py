import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())

# a= "How long does shipping take?"
# print(a)
# a= tokenize(a)
# print(a)

# stemmed_words= [stem(w) for w in a]
# print(stemmed_words)



# def bag_of_words(tokenized_sentence, words):
#     sentence_words = [stem(word) for word in tokenized_sentence]
#     bag = np.zeros(len(words), dtype=np.float32)
#     for idx, w in enumerate(words):
#         if w in sentence_words: 
#             bag[idx] = 1

#     return 


 