# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:20:42 2024

@author: maansiii__10
"""
sentence2="I visited MY from IND on 14-02-19"
normalized_sentence=sentence2.replace("My","Malaysia").replace("IND","India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)

########################################
from autocorrect import Speller 
spell=Speller(lang='en')
spell("English")
#####################################
#Suppose we want to correct the whole sentence 
import nltk 
nltk.download('punkt')
from nltk import word_tokenize
sentence3="Ntural language processin deals within the aart of extract"
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word)for word in sentence3])
print(corrected_sentence)

###############################
#Stemming 
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programed")
stemmer.stem("Jumping")
stemmer.stem("Jumped")

##########################
#lematizer
#lematizer looks into dictionary words
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("programs")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")

###################################
#chunking 
nltk.download("maxent_ne_chunker")
nltk.download('words')
sentence4="we are Learning NLp in python by sanjivaniAI"
#first we will tokenization
nltk.download("averaged_perceptron_tagger")
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]

from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are learning Nlp .do you know where")
sent
################################
#HE WANT to bank and checked account it was almost 0
#looking this he want to river bank and was crying 
from nltk.wsd import lesk
sentence1="keep your saving in the bank"
print(lesk(word_tokenize(sentence1),'bank'))
# Synset('savings_bank.n.02')
sentence2="It is so risky to drive over the banks of river"
print(lesk(word_tokenize(sentence2),'bank'))
#Synset('bank.v.07')