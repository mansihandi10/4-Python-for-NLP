# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 09:19:29 2024

@author: Hp
"""

from nltk import ngrams
#extraction n-grams with the help of nltk
list(ngrams("The Cute Little boy is playing with kitten".split(),2))
list(ngrams("The Cute Little boy is playing with kitten".split(),3))

from textblob import TextBlob
blob=TextBlob("The Cute Little boy is playing with kitten")
blob.ngrams(n=2)
blob.ngrams(n=3)

#Tokenization using Textblob
sentence="sharat twitted ,Wittnessing 68th republic day India from Rajpath , \new Delhi ,Mesmorizing performance by Indian Army !"
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence)

#Tokenize using TextBob
from textblob import TextBlob
blob=TextBlob(sentence)
blob.words

#Tweek Tokenizer

from nltk.tokenize import TweetTokenizer
tweer_tokenizer=TweetTokenizer()
tweer_tokenizer.tokenize(sentence)
##################################################

from nltk.tokenize import MWETokenizer
sentence
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence.split())
mwe_tokenizer.tokenize(sentence.replace('!',' ').split())
